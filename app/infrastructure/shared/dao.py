from typing import Protocol


class DAOProtocol(Protocol):
    
    def commit(self) -> None:
        raise NotImplementedError


class ReadDAOProtocol(DAOProtocol):

    def get(self, pool_id: int) -> dict:
        raise NotImplementedError

    def get_all(self) -> list:
        raise NotImplementedError


class WriteDAOProtocol(DAOProtocol):
    
    def create(self, data: dict) -> None:
        raise NotImplementedError

    def update(self, data: dict) -> None:
        raise NotImplementedError

    def delete(self, data: dict) -> None:
        raise NotImplementedError
    