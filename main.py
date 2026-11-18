
# Importamos las clases necesarias.
from entidades import Cliente
from servicios import ReservaSala
from reservas import Reserva
from gestor import GestorSistema


print("PRUEBA 6: BUSQUEDA Y CONTROL DE DUPLICADOS")
print("------------------------------------------")

try:

    # Creamos el gestor principal.
    gestor = GestorSistema()

    # Creamos un cliente.
    cliente = Cliente(
        "CLI006",
        "Maria Fernanda",
        "78945612",
        "maria@gmail.com",
        "3159876543"
    )

    # Registramos el cliente.
    print("\n1. REGISTRO DE CLIENTE")
    print(gestor.agregar_cliente(cliente))

    # Creamos un servicio.
    sala = ReservaSala(
        "Reserva de sala",
        50000,
        20,
        "Sala de reuniones"
    )

    # Registramos el servicio.
    print("\n2. REGISTRO DE SERVICIO")
    print(gestor.agregar_servicio(sala))

    # Creamos una reserva.
    reserva = Reserva(
        "RES006",
        cliente,
        sala,
        2
    )

    # Registramos la reserva.
    print("\n3. REGISTRO DE RESERVA")
    print(gestor.agregar_reserva(reserva))

    # Buscamos el cliente por su documento.
    print("\n4. BUSQUEDA DE CLIENTE")

    resultado_cliente = gestor.buscar_cliente("78945612")

    if resultado_cliente:
        print("Cliente encontrado:", resultado_cliente.nombre)
    else:
        print("Cliente no encontrado.")

    # Buscamos el servicio por su nombre.
    print("\n5. BUSQUEDA DE SERVICIO")

    resultado_servicio = gestor.buscar_servicio("Reserva de sala")

    if resultado_servicio:
        print("Servicio encontrado:", resultado_servicio.nombre)
    else:
        print("Servicio no encontrado.")

    # Buscamos la reserva por su codigo.
    print("\n6. BUSQUEDA DE RESERVA")

    resultado_reserva = gestor.buscar_reserva("RES006")

    if resultado_reserva:
        print("Reserva encontrada:", resultado_reserva.codigo)
    else:
        print("Reserva no encontrada.")

    # Intentamos registrar nuevamente el mismo cliente.
    print("\n7. PRUEBA DE CLIENTE DUPLICADO")

    try:
        gestor.agregar_cliente(cliente)

    except ValueError as error:
        print("Duplicado controlado:", error)

    # Intentamos registrar nuevamente la misma reserva.
    print("\n8. PRUEBA DE RESERVA DUPLICADA")

    try:
        gestor.agregar_reserva(reserva)

    except ValueError as error:
        print("Duplicado controlado:", error)

    # Intentamos registrar nuevamente el mismo servicio.
    print("\n9. PRUEBA DE SERVICIO DUPLICADO")

    try:
        gestor.agregar_servicio(sala)

    except ValueError as error:
        print("Duplicado controlado:", error)

    # Mostramos el resumen final.
    print("\n10. RESUMEN DEL SISTEMA")
    print("----------------------")
    print(gestor.mostrar_resumen())

except Exception as error:

    print("Se presento un error:", error)

else:

    print("\nPrueba finalizada correctamente.")