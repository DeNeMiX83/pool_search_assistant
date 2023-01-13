from typing import Protocol
import pandas as pd

from app.core.pool.entities import PoolEntity

class PoolAnalysisProtocol(Protocol):

    def __init__(self, metadata: pd.DataFrame) -> None:
        super().__init__()

    def get_recommended_pools(self, pool_analysis: str) -> list[PoolEntity]:
        raise NotImplementedError