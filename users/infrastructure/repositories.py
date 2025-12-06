# Adaptador que implementa el puerto del repositorio usando Django ORM.
from users.application.ports import UserRepositoryPort
from users.domain.entities import User
from users.infrastructure.models import UserModel

class DjangoUserRepository(UserRepositoryPort):
    """Implementa el puerto del repositorio usando el ORM de Django."""
    def create(self, user: User) -> User:
        obj = UserModel.objects.create(
            nombre=user.nombre,
            apellido=user.apellido,
            email=user.email,
            telefono=user.telefono,
            password_hash=user.password_hash
        )
        return User(obj.id, obj.nombre, obj.apellido, obj.email, obj.telefono, obj.password_hash)

    def get_by_id(self, user_id: int) -> User:
        try:
            obj = UserModel.objects.get(id=user_id)
            return User(obj.id, obj.nombre, obj.apellido, obj.email, obj.telefono, obj.password_hash)
        except UserModel.DoesNotExist:
            return None

    def get_by_email(self, email: str) -> User:
        try:
            obj = UserModel.objects.get(email=email)
            return User(obj.id, obj.nombre, obj.apellido, obj.email, obj.telefono, obj.password_hash)
        except UserModel.DoesNotExist:
            return None

    def update(self, user: User) -> User:
        obj = UserModel.objects.get(id=user.id)
        obj.nombre = user.nombre
        obj.apellido = user.apellido
        obj.telefono = user.telefono
        obj.save()
        return User(obj.id, obj.nombre, obj.apellido, obj.email, obj.telefono, obj.password_hash)

    def delete(self, user_id: int) -> None:
        UserModel.objects.filter(id=user_id).delete()

    def list(self) -> list:
        return [
            User(obj.id, obj.nombre, obj.apellido, obj.email, obj.telefono, obj.password_hash)
            for obj in UserModel.objects.all()
        ]
