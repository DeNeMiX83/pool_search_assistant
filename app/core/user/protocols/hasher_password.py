from typing import Protocol


class HasherPassword(Protocol):
    def hash(self, password: str) -> str:
        ...