# Casos de uso (servicios de aplicación) que orquestan la lógica de negocio.
from users.domain.entities import User
from users.domain.exceptions import UserAlreadyExists, UserNotFound, InvalidCredentials
from users.application.ports import UserRepositoryPort
import hashlib

class RegisterUserUseCase:
    """Caso de uso para registrar un usuario. Desacopla la lógica del framework."""
    def __init__(self, repo: UserRepositoryPort):
        self.repo = repo

    def execute(self, nombre, apellido, email, telefono, password):
        if self.repo.get_by_email(email):
            raise UserAlreadyExists()
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        user = User(id=None, nombre=nombre, apellido=apellido, email=email, telefono=telefono, password_hash=password_hash)
        return self.repo.create(user)

class GetUserProfileUseCase:
    def __init__(self, repo: UserRepositoryPort):
        self.repo = repo

    def execute(self, user_id):
        user = self.repo.get_by_id(user_id)
        if not user:
            raise UserNotFound()
        return user

class UpdateUserUseCase:
    def __init__(self, repo: UserRepositoryPort):
        self.repo = repo

    def execute(self, user_id, nombre, apellido, telefono):
        user = self.repo.get_by_id(user_id)
        if not user:
            raise UserNotFound()
        user.nombre = nombre
        user.apellido = apellido
        user.telefono = telefono
        return self.repo.update(user)

class DeleteUserUseCase:
    def __init__(self, repo: UserRepositoryPort):
        self.repo = repo

    def execute(self, user_id):
        user = self.repo.get_by_id(user_id)
        if not user:
            raise UserNotFound()
        self.repo.delete(user_id)

class ListUsersUseCase:
    def __init__(self, repo: UserRepositoryPort):
        self.repo = repo

    def execute(self):
        return self.repo.list()

class LoginUseCase:
    def __init__(self, repo: UserRepositoryPort):
        self.repo = repo

    def execute(self, email, password):
        user = self.repo.get_by_email(email)
        if not user:
            raise InvalidCredentials()
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        if user.password_hash != password_hash:
            raise InvalidCredentials()
        # Token simple (NO JWT, solo para demo)
        token = hashlib.sha256((email + password).encode()).hexdigest()
        return {"token": token, "message": "Login exitoso"}
