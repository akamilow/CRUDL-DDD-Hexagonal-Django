# Excepciones de dominio para reglas de negocio y errores específicos.
class UserAlreadyExists(Exception):
    """Se lanza cuando se intenta crear un usuario con un email ya existente."""
    pass

class UserNotFound(Exception):
    """Se lanza cuando no se encuentra un usuario por ID o email."""
    pass

class InvalidCredentials(Exception):
    """Se lanza cuando las credenciales de login son incorrectas."""
    pass
