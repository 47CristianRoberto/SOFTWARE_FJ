
# Importamos las herramientas necesarias para crear clases abstractas.
from abc import ABC, abstractmethod
import re


# Esta clase representa una entidad general del sistema.
# Al ser abstracta, sirve como base para crear otras clases.
class Entidad(ABC):

    def __init__(self, identificador):
        if not identificador or not str(identificador).strip():
            raise ValueError("El identificador es obligatorio.")

        self._identificador = str(identificador).strip()

    # Este metodo debe ser implementado por las clases que hereden de Entidad.
    @abstractmethod
    def mostrar_informacion(self):
        pass


# La clase Cliente hereda de Entidad y representa
# a las personas que utilizan los servicios de Software FJ.
class Cliente(Entidad):

    def __init__(self, identificador, nombre, documento, correo, telefono):

        # Inicializamos los datos heredados de la clase Entidad.
        super().__init__(identificador)

        # Guardamos los datos personales utilizando atributos privados.
        self.__nombre = self.validar_nombre(nombre)
        self.__documento = self.validar_documento(documento)
        self.__correo = self.validar_correo(correo)
        self.__telefono = self.validar_telefono(telefono)

    # Validamos que el nombre tenga un formato correcto.
    @staticmethod
    def validar_nombre(nombre):

        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del cliente es obligatorio.")

        nombre = " ".join(nombre.strip().split())

        # Permitimos letras, espacios, tildes y algunos signos.
        if not all(
            caracter.isalpha() or caracter in " -'"
            for caracter in nombre
        ):
            raise ValueError("El nombre contiene caracteres no permitidos.")

        if len(nombre) < 3:
            raise ValueError("El nombre debe tener al menos 3 caracteres.")

        return nombre

    # Revisamos que el documento tenga un formato valido.
    @staticmethod
    def validar_documento(documento):

        if not isinstance(documento, str) or not documento.strip():
            raise ValueError("El documento del cliente es obligatorio.")

        documento = documento.strip()

        if not re.fullmatch(r"[A-Za-z0-9-]{5,20}", documento):
            raise ValueError("El documento debe tener entre 5 y 20 caracteres.")

        return documento

    # Comprobamos que el correo tenga una estructura correcta.
    @staticmethod
    def validar_correo(correo):

        if not isinstance(correo, str) or not correo.strip():
            raise ValueError("El correo electronico es obligatorio.")

        correo = correo.strip().lower()

        patron = r"^[\w.+-]+@[\w-]+\.[A-Za-z]{2,}$"

        if not re.fullmatch(patron, correo):
            raise ValueError("El correo electronico no es valido.")

        return correo

    # Validamos que el telefono contenga entre 7 y 15 digitos.
    @staticmethod
    def validar_telefono(telefono):

        if not isinstance(telefono, str) or not telefono.strip():
            raise ValueError("El telefono del cliente es obligatorio.")

        telefono = telefono.strip()

        if not re.fullmatch(r"\+?[0-9]{7,15}", telefono):
            raise ValueError("El telefono debe contener entre 7 y 15 digitos.")

        return telefono

    # Consultamos el identificador sin modificarlo directamente.
    @property
    def identificador(self):
        return self._identificador

    # Consultamos el nombre del cliente.
    @property
    def nombre(self):
        return self.__nombre

    # Consultamos el documento del cliente.
    @property
    def documento(self):
        return self.__documento

    # Consultamos el correo electronico.
    @property
    def correo(self):
        return self.__correo

    # Consultamos el telefono del cliente.
    @property
    def telefono(self):
        return self.__telefono

    # Permitimos actualizar el correo, manteniendo su validacion.
    @correo.setter
    def correo(self, nuevo_correo):
        self.__correo = self.validar_correo(nuevo_correo)

    # Permitimos actualizar el telefono, comprobando que sea valido.
    @telefono.setter
    def telefono(self, nuevo_telefono):
        self.__telefono = self.validar_telefono(nuevo_telefono)

    # Implementamos el metodo abstracto de la clase Entidad.
    def mostrar_informacion(self):
        return (
            f"Identificador: {self.identificador}\n"
            f"Nombre: {self.nombre}\n"
            f"Documento: {self.documento}\n"
            f"Correo: {self.correo}\n"
            f"Telefono: {self.telefono}"
        )
