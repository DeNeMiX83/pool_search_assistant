import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from app.core.pool.usecase.protocols.pool_analysis import PoolAnalysisProtocol
from app.core.pool.entities.pool import PoolEntity

class PoolAnalysisImp(PoolAnalysisProtocol):
    def __init__(self, metadata: pd.DataFrame) -> None:
        super().__init__()
        self.metadata = metadata

    def get_recommended_pools(self, pool_analysis: PoolEntity) -> list[PoolEntity]:
        self.clean_up_data()
        self.create_df_with_glued_columns()
        self.calculate_vectors_by_pool(pool_analysis)

    def clean_up_data(self) -> None:
        self.metadata = self.metadata.dropna()
        self.data_for_analysis = self.metadata
        self.data_for_analysis = self.data_for_analysis.drop('global_id', axis=1)
        self.data_for_analysis = self.data_for_analysis.drop('ObjectName', axis=1)

    def create_df_with_glued_columns(self) -> None:
        self.metadata_glued_columns = pd.DataFrame(columns=['glued_columns'], index=self.data_for_analysis.index, data='')

        for column in self.data_for_analysis.columns:
            self.metadata_glued_columns['glued_columns'] += column + ': ' + self.data_for_analysis[column] + ' '

    def calculate_vectors_by_pool(self, pool_analysis: PoolEntity) -> None:
        vectorizer = TfidfVectorizer()
        vectors = self.vectorizer.fit_transform(self.metadata_glued_columns['glued_columns'])

        like = self.pool_to_str(pool_analysis)

        new_entry = vectorizer.transform([like])
        cosine_similarities = cosine_similarity(new_entry, vectors).flatten()

        metadata['cos_similarities'] = cosine_similarities

        metadata = metadata.sort_values(by=['cos_similarities'], ascending=[0])

    def get_n_top_recommended_pools(self, n: int) -> list[PoolEntity]:
        return [
            self.pool_str_to_pool(pool_str) 
            for pool_str in self.metadata.head(1, n + 1).to_dict('records')
        ]

    def pool_to_str(self, pool: PoolEntity) -> str:
        return " ".join(
            map(
                lambda x: f"{x[0]}: {x[1]}",
                pool.dict().items()
            )
        )

    def pool_str_to_pool(self, pool: str) -> PoolEntity:
        return PoolEntity(
            **dict(
                map(
                    lambda x: x.split(": "),
                    pool.split(" ")
                )
            )
        )