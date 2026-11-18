
# Importamos las clases necesarias.
from entidades import Cliente
from servicios import ReservaSala
from reservas import Reserva

# Importamos nuestras excepciones personalizadas.
from excepciones import (
    DatosReservaError,
    ReservaNoConfirmadaError,
    ReservaCanceladaError
)


print("SISTEMA SOFTWARE_FJ")
print("PRUEBAS DE VALIDACION DE RESERVAS")
print("=================================")


# Creamos un cliente para las pruebas.
cliente = Cliente(
    "CLI007",
    "Andres Gomez",
    "45678912",
    "andres@gmail.com",
    "3101234567"
)

# Creamos un servicio.
sala = ReservaSala(
    "Reserva de sala",
    50000,
    20,
    "Sala de reuniones"
)


# PRUEBA 1: Validar una duracion incorrecta.
print("\nPRUEBA 1: VALIDACION DE DATOS")
print("--------------------------------")

try:
    reserva_invalida = Reserva(
        "RES007",
        cliente,
        sala,
        0
    )

except DatosReservaError as error:
    print("Error controlado:", error)


# PRUEBA 2: Intentar procesar una reserva pendiente.
print("\nPRUEBA 2: PROCESAR RESERVA PENDIENTE")
print("------------------------------------")

reserva1 = Reserva(
    "RES008",
    cliente,
    sala,
    2
)

try:
    reserva1.procesar_reserva()

except ReservaNoConfirmadaError as error:
    print("Operacion controlada:", error)


# PRUEBA 3: Confirmar una reserva correctamente.
print("\nPRUEBA 3: CONFIRMAR RESERVA")
print("----------------------------")

try:
    print(reserva1.confirmar())

except Exception as error:
    print("Error:", error)


# PRUEBA 4: Procesar una reserva confirmada.
print("\nPRUEBA 4: PROCESAR RESERVA CONFIRMADA")
print("-------------------------------------")

try:
    costo = reserva1.procesar_reserva()
    print(f"Costo calculado: ${costo:,.2f}")

except Exception as error:
    print("Error:", error)


# PRUEBA 5: Intentar confirmar una reserva cancelada.
print("\nPRUEBA 5: CONFIRMAR RESERVA CANCELADA")
print("-------------------------------------")

reserva2 = Reserva(
    "RES009",
    cliente,
    sala,
    2
)

try:
    print(reserva2.cancelar())
    reserva2.confirmar()

except ReservaCanceladaError as error:
    print("Operacion controlada:", error)


# PRUEBA 6: Intentar procesar una reserva cancelada.
print("\nPRUEBA 6: PROCESAR RESERVA CANCELADA")
print("------------------------------------")

try:
    reserva2.procesar_reserva()

except ReservaCanceladaError as error:
    print("Operacion controlada:", error)


print("\nRESUMEN DE LAS PRUEBAS")
print("----------------------")
print("Se finalizaron las pruebas de validacion.")
print("Verifique que las operaciones incorrectas")
print("fueron controladas por el sistema.")

print("\nPruebas finalizadas.")
