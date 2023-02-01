import pandas as pd
from dataclasses import asdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from app.core.pool.protocols.pool_analysis import PoolAnalysis
from app.core.pool import entities


class PoolAnalysisImp(PoolAnalysis):
    def __init__(self, metadata: pd.DataFrame) -> None:
        self.metadata = metadata

    def get_recommended_pools_id(
        self, pool_analysis: entities.Pool
    ) -> list[int]:
        pools = []
        if pool_analysis:
            self.clean_up_data()
            self.create_df_with_glued_columns()
            self.calculate_vectors_by_pool(pool_analysis)
            pools = self.get_n_top_recommended_pools(3)
        return pools

    def clean_up_data(self) -> None:
        self.metadata = self.metadata.dropna()
        self.data_for_analysis = self.metadata
        self.data_for_analysis = self.data_for_analysis.drop(
            "global_id", axis=1
        )
        self.data_for_analysis = self.data_for_analysis.drop(
            "ObjectName", axis=1
        )

    def create_df_with_glued_columns(self) -> None:
        self.metadata_glued_columns = pd.DataFrame(
            columns=["glued_columns"],
            index=self.data_for_analysis.index,
            data=""
        )

        for column in self.data_for_analysis.columns:
            self.metadata_glued_columns["glued_columns"] += (
                column + ": " + self.data_for_analysis[column] + " "
            )

    def calculate_vectors_by_pool(self, pool_analysis: entities.Pool) -> None:
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(
            self.metadata_glued_columns["glued_columns"]
        )

        like = self.pool_to_str(pool_analysis)

        new_entry = vectorizer.transform([like])
        cosine_similarities = cosine_similarity(new_entry, vectors).flatten()

        self.metadata["cos_similarities"] = cosine_similarities

        self.metadata = self.metadata.sort_values(
            by=["cos_similarities"], ascending=[0]
        )

    def get_n_top_recommended_pools(self, n: int) -> list[int]:
        return [pool_id for pool_id in self.metadata[1:1 + n]["global_id"]]

    def pool_to_str(self, pool: entities.Pool) -> str:
        return " ".join(map(lambda x: f"{x[0]}: {x[1]}", asdict(pool).items()))
