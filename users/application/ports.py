# Interfaces (puertos) para los repositorios y servicios.
from abc import ABC, abstractmethod
from users.domain.entities import User

class UserRepositoryPort(ABC):
    """Puerto para desacoplar el acceso a datos del dominio."""
    @abstractmethod
    def create(self, user: User) -> User:
        pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> User:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> User:
        pass

    @abstractmethod
    def update(self, user: User) -> User:
        pass

    @abstractmethod
    def delete(self, user_id: int) -> None:
        pass

    @abstractmethod
    def list(self) -> list:
        pass
