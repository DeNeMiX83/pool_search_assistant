from typing import Protocol
import pandas as pd
from app.core.pool.entities.pool import Pool

class PoolAnalysis(Protocol):

    def __init__(self, metadata: pd.DataFrame) -> None:
        super().__init__()

    def get_recommended_pools(self, pool_analysis: Pool) -> list[Pool]:
        raise NotImplementedError