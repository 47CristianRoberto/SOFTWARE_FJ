
# Importamos las funciones para guardar los registros.
from logs import registrar_evento, registrar_error


# PRUEBA 1: Uso de try, except y else.
def probar_try_except_else():

    print("\nPRUEBA 1: TRY, EXCEPT Y ELSE")
    print("--------------------------------")

    try:
        resultado = 100 / 2

    except ZeroDivisionError as error:
        print("Se presento un error:", error)
        registrar_error(f"Error en la operacion: {error}")

    else:
        print("Operacion realizada correctamente.")
        print("Resultado:", resultado)
        registrar_evento("Prueba try-except-else realizada.")

    finally:
        print("Finalizacion de la primera prueba.")


# PRUEBA 2: Uso de try, except y finally.
def probar_try_except_finally():

    print("\nPRUEBA 2: TRY, EXCEPT Y FINALLY")
    print("--------------------------------")

    try:
        numero = int("texto")

    except ValueError as error:
        print("No fue posible convertir el dato.")
        print("Motivo:", error)
        registrar_error(
            f"Error de conversion de datos: {error}"
        )

    finally:
        print("La operacion ha finalizado.")
        registrar_evento(
            "Finalizo la prueba try-except-finally."
        )


# Funcion que permite validar la duracion de una reserva.
def validar_duracion(valor):

    try:
        duracion = float(valor)

    except (ValueError, TypeError) as error:

        # Conservamos la causa original del error.
        raise ValueError(
            "La duracion debe ser un valor numerico."
        ) from error

    if duracion <= 0:
        raise ValueError(
            "La duracion debe ser mayor que cero."
        )

    return duracion


# PRUEBA 3: Encadenamiento de excepciones.
def probar_encadenamiento():

    print("\nPRUEBA 3: ENCADENAMIENTO DE EXCEPCIONES")
    print("-----------------------------------------")

    try:
        validar_duracion("dos")

    except ValueError as error:

        print("Se detecto un error:", error)

        if error.__cause__:
            print("Causa original:", error.__cause__)

        registrar_error(
            f"Error de validacion de duracion: {error}"
        )


# Funcion principal para ejecutar todas las pruebas.
def ejecutar_pruebas():

    print("SISTEMA SOFTWARE FJ")
    print("PRUEBAS DE MANEJO DE EXCEPCIONES")
    print("================================")

    probar_try_except_else()

    probar_try_except_finally()

    probar_encadenamiento()

    print("\nTodas las pruebas finalizaron.")
    registrar_evento(
        "Se completaron las pruebas avanzadas de excepciones."
    )


# Ejecutamos las pruebas al iniciar este archivo.
if __name__ == "__main__":
    ejecutar_pruebas()
