# Entidad de Usuario pura, desacoplada de Django ORM.
class User:
    def __init__(self, id, nombre, apellido, email, telefono, password_hash):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.password_hash = password_hash

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.email})"
