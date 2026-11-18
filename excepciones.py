
# En este archivo creamos los errores propios del sistema Software FJ.
# Asi podemos identificar mejor los problemas que ocurren al gestionar reservas.


# Error general para las operaciones relacionadas con reservas.
class ErrorReserva(Exception):
    pass


# Se utiliza cuando se intenta realizar una operacion
# con una reserva que no esta confirmada.
class ReservaNoConfirmadaError(ErrorReserva):
    pass


# Se utiliza cuando se intenta trabajar con una reserva cancelada.
class ReservaCanceladaError(ErrorReserva):
    pass


# Se utiliza cuando los datos de una reserva no son correctos.
class DatosReservaError(ErrorReserva):
    pass
