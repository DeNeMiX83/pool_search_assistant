from abc import ABC, abstractmethod

class UseCase(ABC):
    def __init__(self):
        ...

    @abstractmethod
    def execute(self) -> None: 
        raise NotImplementedError