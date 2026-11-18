
# Importamos las clases necesarias para gestionar las reservas.
from entidades import Cliente
from servicios import Servicio

# Importamos las excepciones personalizadas.
from excepciones import (
    ErrorReserva,
    ReservaNoConfirmadaError,
    ReservaCanceladaError,
    DatosReservaError
)

# Importamos la funcion para registrar eventos.
from logs import registrar_evento


# Esta clase permite relacionar clientes con los servicios.
class Reserva:

    def __init__(self, codigo, cliente, servicio, duracion):

        # Validamos el codigo de la reserva.
        if not isinstance(codigo, str) or not codigo.strip():
            raise DatosReservaError("El codigo es obligatorio.")

        # Verificamos que exista un cliente valido.
        if not isinstance(cliente, Cliente):
            raise DatosReservaError(
                "Debe seleccionar un cliente valido."
            )

        # Comprobamos que el servicio sea correcto.
        if not isinstance(servicio, Servicio):
            raise DatosReservaError(
                "Debe seleccionar un servicio valido."
            )

        # Validamos la duracion de la reserva.
        if isinstance(duracion, bool) or not isinstance(
            duracion, (int, float)
        ) or duracion <= 0:
            raise DatosReservaError(
                "La duracion debe ser mayor que cero."
            )

        self.codigo = codigo.strip()
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"
        self.costo_total = None

        # Registramos la creacion de la reserva.
        registrar_evento(
            f"Reserva {self.codigo} creada para "
            f"el cliente {self.cliente.nombre}."
        )

    # Permite confirmar una reserva.
    def confirmar(self):

        if self.estado == "Cancelada":
            raise ReservaCanceladaError(
                "No se puede confirmar una reserva cancelada."
            )

        if self.estado == "Confirmada":
            raise ErrorReserva(
                "La reserva ya esta confirmada."
            )

        self.estado = "Confirmada"

        registrar_evento(
            f"Reserva {self.codigo} confirmada correctamente."
        )

        return (
            f"La reserva {self.codigo} "
            "fue confirmada correctamente."
        )

    # Permite cancelar una reserva.
    def cancelar(self):

        if self.estado == "Cancelada":
            raise ReservaCanceladaError(
                "La reserva ya se encuentra cancelada."
            )

        self.estado = "Cancelada"
        self.costo_total = None

        registrar_evento(
            f"Reserva {self.codigo} cancelada correctamente."
        )

        return (
            f"La reserva {self.codigo} "
            "fue cancelada correctamente."
        )

    # Procesa la reserva y calcula su costo.
    def procesar_reserva(self, impuesto=0, descuento=0):

        if self.estado == "Cancelada":
            raise ReservaCanceladaError(
                "No se puede procesar una reserva cancelada."
            )

        if self.estado != "Confirmada":
            raise ReservaNoConfirmadaError(
                "Primero debe confirmar la reserva."
            )

        # Calculamos el costo utilizando el servicio seleccionado.
        self.costo_total = self.servicio.calcular_costo(
            self.duracion,
            impuesto,
            descuento
        )

        registrar_evento(
            f"Reserva {self.codigo} procesada. "
            f"Costo total: ${self.costo_total:,.2f}"
        )

        return self.costo_total

    # Muestra toda la informacion de la reserva.
    def mostrar_informacion(self):

        if self.costo_total is None:
            costo = "Pendiente de calculo"
        else:
            costo = f"${self.costo_total:,.2f}"

        return (
            f"Codigo de reserva: {self.codigo}\n"
            f"Cliente: {self.cliente.nombre}\n"
            f"Documento: {self.cliente.documento}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Duracion: {self.duracion} horas\n"
            f"Estado: {self.estado}\n"
            f"Costo total: {costo}"
        )
