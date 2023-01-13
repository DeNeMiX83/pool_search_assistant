from abc import ABC, abstractmethod

class UseCase(ABC):
    def __init__(self):
        ...

    @abstractmethod
    def handle(self) -> None: 
        raise NotImplementedError