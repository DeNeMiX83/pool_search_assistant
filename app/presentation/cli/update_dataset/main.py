import os

import requests
import urllib3
import ssl
from pprint import pprint
import re

import csv
from sqlalchemy import create_engine

import pandas as pd

from app.settings import MosApiSettings, PostgresSettings

class CustomHttpAdapter(requests.adapters.HTTPAdapter):
    '''Transport adapter" that allows us to use custom ssl_context.'''

    def __init__(self, ssl_context=None, **kwargs):
        self.ssl_context = ssl_context
        super().__init__(**kwargs)

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = urllib3.poolmanager.PoolManager(
            num_pools=connections, maxsize=maxsize,
            block=block, ssl_context=self.ssl_context)


def get_legacy_session():
    ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ctx.options |= 0x4

    session = requests.Session()
    session.mount('https://', CustomHttpAdapter(ctx))

    return session

def clear_redundant_data_in_json(data: list) -> list:
    for item in data:
        for value in ["DimensionsWinter", "UsagePeriodWinter", "PhotoWinter", "WorkingHoursWinter", "NameWinter", 
            "Email", "WebSite", "HelpPhone", "HelpPhoneExtension", "ClarificationOfWorkingHoursWinter", "EquipmentRentalComments", "TechServiceComments", 
            "Seats", "PaidComments"]:
            if value in item:
                del item[value]


def main():
    settings_mos_api = MosApiSettings()
    settings_postgres = PostgresSettings()

    session = get_legacy_session()

    base_url = settings_mos_api.get_mos_api_dataset_url()
    postges_url = settings_postgres.dsn().replace("+asyncpg", "")

    raw_data_path = 'app/resources/raw_data.csv'

    print('-' * 50)
    print('Start updating dataset...')
    print(f'Base url: {base_url}')
    print('-' * 50)

    print()

    print('-' * 50)
    print(f'Create file ({raw_data_path})')
    print('-' * 50)

    print()

    print('-' * 50)
    print(f'Download dataset to ({raw_data_path})')
    print()

    count = session.get(
        url=f'{base_url}/count',
        params={
            'api_key': settings_mos_api.mos_api_key,
        }
    ).json()

    delimiter = 100

    print(f'Count rows: {count}')
    print(f'Delimiter: {delimiter}')
    print()
    for i in range(0, count, delimiter):
        raw_data = session.get(
            url=f'{base_url}/rows?$top={i+delimiter}&$skip={i}',
            params={
                'api_key': settings_mos_api.mos_api_key,
            }
        ).json()

        data = list()
        for item in raw_data:
            data.append(item['Cells'])

        if i == 0:
            with open(raw_data_path, 'w') as f:
                csv_writer = csv.writer(f)
                header = data[0].keys()
                csv_writer.writerow(header)

        with open(raw_data_path, 'a') as f:
            csv_writer = csv.writer(f)

            for item in data:
                csv_writer.writerow(item.values())
            
        print(f'Processed {min(i+delimiter, count)} rows')

    print()
    print('Finish downloading dataset')
    print('-' * 50)
    print()

    data_path = 'app/resources/data.csv'
    print('-' * 50)
    print(f'Create file ({data_path})')
    print('-' * 50)
    print('')

    print('-' * 50)
    print(f'Select the necessary data for analysis')
    print()

    print(f'Open file with raw data ({raw_data_path})')
    data = pd.read_csv(raw_data_path, low_memory=False)
    print()

    print('Remove redundant columns')
    redundant_columns = [
        "DimensionsWinter", "UsagePeriodWinter", "PhotoWinter", 
        "WorkingHoursWinter", "NameWinter", "Email", "WebSite", 
        "HelpPhone", "HelpPhoneExtension", "ClarificationOfWorkingHoursWinter",
        "EquipmentRentalComments", "TechServiceComments", "Seats", 
        "PaidComments"
    ]
    # print('Redundant columns:', end=' ')
    # pprint(redundant_columns)
    data = data.drop(redundant_columns, axis=1)
    print('Finish removing redundant columns')
    print()

    print('Remove duplicates')
    data = data.drop_duplicates()
    print('Finish removing duplicates')
    print()

    print(f'Save data to file ({data_path})')
    data.to_csv(data_path, index=False)
    print('Finish saving data')
    print()

    print('Finish selecting the necessary data for analysis')
    print('-' * 50)
    print()

    print('-' * 50)
    print('Create connection to database...')
    engine = create_engine(postges_url)
    print('Connection created')
    print('-' * 50)
    print()

    print('-' * 50)
    print('Select the necessary data for database')
    print()

    print(f'Open file with raw data ({raw_data_path})')
    data = pd.read_csv(raw_data_path, low_memory=False)
    print()

    print('Remove redundant columns')
    redundant_columns = [
        "ClarificationOfWorkingHoursWinter", "DimensionsWinter", 
        "EquipmentRentalComments", "HelpPhoneExtension", "Lighting", "NameWinter", 
        "PaidComments", "PhotoWinter", "Seats", "ServicesWinter", "SurfaceTypeWinter",
        "TechServiceComments", "UsagePeriodWinter", "WorkingHoursWinter", "geoData",
    ]

    # print('Redundant columns:', end=' ')
    # pprint(redundant_columns)
    data = data.drop(redundant_columns, axis=1)
    print('Finish removing redundant columns')
    print()

    print('Remove duplicates')
    data = data.drop_duplicates()
    print('Finish removing duplicates')
    print()

    print('Rename columns')
    new_names = []
    for column in list(data):
        new_names.append(re.sub(r"(?<!^)(?=[A-Z])", "_", column).lower())

    data.columns = new_names
    data.rename(
        columns={
            'adm_area': 'administrative_area',
            'disability_friendly': 'how_suitable_for_disabled',
            'help_phone': 'phone_number',
            'paid': 'is_paid',
            'object_name': 'name',
            'has_toilet': 'has_toilets',
            'global_id': 'id',
        }, 
        inplace=True)
    
    print('Finish renaming columns')
    print()

    print('Convert data types')
    data = data.replace("да", True)
    data = data.replace("нет", False)
    data = data.replace("платно", True)
    data = data.replace("бесплатно", False)
    print('Finish converting data types')
    print()

    print('Start loading data to table pools')
    data.to_sql(
        'pools', 
        engine, 
        if_exists="replace",
        index=False,
        )
    print('Finish loading data')
    print()

    print('Finish selecting the necessary data for database')
    print('-' * 50)




        


if __name__ == '__main__':
    main()