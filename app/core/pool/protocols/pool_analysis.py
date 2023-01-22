from typing import Protocol
import pandas as pd
from app.core.pool import entities


class PoolAnalysis(Protocol):
    def __init__(self, metadata: pd.DataFrame) -> None:
        super().__init__()

    def get_recommended_pools_id(
        self, pool_analysis: entities.Pool
    ) -> list[int]:
        raise NotImplementedError
