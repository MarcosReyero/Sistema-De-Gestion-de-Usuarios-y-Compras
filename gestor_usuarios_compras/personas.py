import hashlib

class Cliente:
    """Clase para modelar un cliente en una página de compras."""

    def __init__(self, nombre: str, email: str, direccion: str, telefono: str) -> None:
        self.__nombre = nombre
        self.__email = email
        self.__direccion = direccion
        self.__telefono = telefono

    def __str__(self) -> str:
        return f"Cliente: {self.__nombre}, Email: {self.__email}, Dirección: {self.__direccion}, Teléfono: {self.__telefono}"

    def get_nombre(self) -> str:
        return self.__nombre

    def get_email(self) -> str:
        return self.__email

    def get_direccion(self) -> str:
        return self.__direccion

    def get_telefono(self) -> str:
        return self.__telefono

class Usuario(Cliente):
    """Clase para modelar un usuario que hereda de Cliente."""

    def __init__(self, nombre: str, email: str, direccion: str, telefono: str, usuario: str, password: str) -> None:
        super().__init__(nombre, email, direccion, telefono)
        self.__usuario = usuario
        self.__password_hash = self.hash_password(password)

    def __str__(self) -> str:
        return f"Usuario: {self.__usuario}, {super().__str__()}"

    def get_usuario(self) -> str:
        return self.__usuario

    def check_password(self, password: str) -> bool:
        """Verifica si la contraseña proporcionada coincide con la contraseña almacenada."""
        return self.__password_hash == self.hash_password(password)

    def hash_password(self, password: str) -> str:
        """Genera un hash SHA-256 para la contraseña proporcionada."""
        return hashlib.sha256(password.encode()).hexdigest()
