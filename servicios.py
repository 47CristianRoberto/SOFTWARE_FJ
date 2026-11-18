
# Importamos las herramientas para trabajar con clases abstractas.
from abc import ABC, abstractmethod


# Esta clase representa la estructura general de los servicios
# que ofrece la empresa Software FJ.
class Servicio(ABC):

    def __init__(self, nombre, tarifa_base):

        # Comprobamos que el nombre del servicio no este vacio.
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del servicio es obligatorio.")

        # La tarifa debe ser un numero mayor que cero.
        if isinstance(tarifa_base, bool) or not isinstance(
            tarifa_base, (int, float)
        ) or tarifa_base <= 0:
            raise ValueError("La tarifa debe ser mayor que cero.")

        self.nombre = nombre.strip()
        self.tarifa_base = float(tarifa_base)

    # Este metodo obliga a cada servicio a validar sus propios datos.
    @abstractmethod
    def validar_parametros(self):
        pass

    # Cada servicio debe tener su propia descripcion.
    @abstractmethod
    def describir(self):
        pass

    # Cada servicio debe implementar su propio calculo de costos.
    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        pass

    # Validamos la duracion, los impuestos y los descuentos.
    def validar_calculo(self, duracion, impuesto, descuento):

        if isinstance(duracion, bool) or not isinstance(
            duracion, (int, float)
        ) or duracion <= 0:
            raise ValueError("La duracion debe ser mayor que cero.")

        if isinstance(impuesto, bool) or not isinstance(
            impuesto, (int, float)
        ) or not 0 <= impuesto <= 100:
            raise ValueError("El impuesto debe estar entre 0 y 100.")

        if isinstance(descuento, bool) or not isinstance(
            descuento, (int, float)
        ) or not 0 <= descuento <= 100:
            raise ValueError("El descuento debe estar entre 0 y 100.")

    # Este metodo realiza el calculo general del costo.
    # Primero aplica el descuento y despues el impuesto.
    def calcular_total(self, duracion, impuesto=0, descuento=0):

        self.validar_calculo(duracion, impuesto, descuento)

        subtotal = self.tarifa_base * duracion

        valor_descuento = subtotal * (descuento / 100)

        subtotal_con_descuento = subtotal - valor_descuento

        valor_impuesto = subtotal_con_descuento * (impuesto / 100)

        total = subtotal_con_descuento + valor_impuesto

        return round(total, 2)


# Esta clase representa el servicio de reserva de salas.
# Hereda las caracteristicas generales de Servicio.
class ReservaSala(Servicio):

    def __init__(self, nombre, tarifa_base, capacidad, tipo_sala):

        super().__init__(nombre, tarifa_base)

        self.capacidad = capacidad
        self.tipo_sala = tipo_sala

        # Verificamos que los datos de la sala sean correctos.
        self.validar_parametros()

    # Comprobamos que la capacidad y el tipo de sala sean validos.
    def validar_parametros(self):

        if isinstance(self.capacidad, bool) or not isinstance(
            self.capacidad, int
        ) or self.capacidad <= 0:
            raise ValueError("La capacidad debe ser un numero entero positivo.")

        if not isinstance(self.tipo_sala, str) or not self.tipo_sala.strip():
            raise ValueError("Debe indicar el tipo de sala.")

    # Mostramos las caracteristicas de la sala.
    def describir(self):
        return (
            f"Servicio: {self.nombre} | "
            f"Tipo de sala: {self.tipo_sala} | "
            f"Capacidad: {self.capacidad} personas | "
            f"Tarifa por hora: ${self.tarifa_base:,.2f}"
        )

    # Calculamos el costo de la reserva de la sala.
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        return self.calcular_total(duracion, impuesto, descuento)


# Esta clase representa el alquiler de equipos.
class AlquilerEquipo(Servicio):

    def __init__(self, nombre, tarifa_base, equipo, cantidad):

        super().__init__(nombre, tarifa_base)

        self.equipo = equipo
        self.cantidad = cantidad

        # Revisamos que la informacion del equipo sea correcta.
        self.validar_parametros()

    # Validamos el nombre del equipo y la cantidad solicitada.
    def validar_parametros(self):

        if not isinstance(self.equipo, str) or not self.equipo.strip():
            raise ValueError("Debe indicar el nombre del equipo.")

        if isinstance(self.cantidad, bool) or not isinstance(
            self.cantidad, int
        ) or self.cantidad <= 0:
            raise ValueError("La cantidad debe ser un numero entero positivo.")

    # Presentamos la informacion del equipo disponible para alquiler.
    def describir(self):
        return (
            f"Servicio: {self.nombre} | "
            f"Equipo: {self.equipo} | "
            f"Cantidad: {self.cantidad} | "
            f"Tarifa por unidad y hora: ${self.tarifa_base:,.2f}"
        )

    # Calculamos el costo teniendo en cuenta la cantidad de equipos.
    def calcular_costo(self, duracion, impuesto=0, descuento=0):

        self.validar_calculo(duracion, impuesto, descuento)

        subtotal = self.tarifa_base * duracion * self.cantidad

        valor_descuento = subtotal * (descuento / 100)

        subtotal_con_descuento = subtotal - valor_descuento

        valor_impuesto = subtotal_con_descuento * (impuesto / 100)

        total = subtotal_con_descuento + valor_impuesto

        return round(total, 2)


# Esta clase representa el servicio de asesorias especializadas.
class AsesoriaEspecializada(Servicio):

    def __init__(self, nombre, tarifa_base, especialidad, asesor):

        super().__init__(nombre, tarifa_base)

        self.especialidad = especialidad
        self.asesor = asesor

        # Comprobamos que la especialidad y el asesor esten registrados.
        self.validar_parametros()

    # Validamos la informacion de la asesoria.
    def validar_parametros(self):

        if not isinstance(self.especialidad, str) or not self.especialidad.strip():
            raise ValueError("Debe indicar la especialidad de la asesoria.")

        if not isinstance(self.asesor, str) or not self.asesor.strip():
            raise ValueError("Debe indicar el nombre del asesor.")

    # Mostramos la informacion de la asesoria especializada.
    def describir(self):
        return (
            f"Servicio: {self.nombre} | "
            f"Especialidad: {self.especialidad} | "
            f"Asesor: {self.asesor} | "
            f"Tarifa por hora: ${self.tarifa_base:,.2f}"
        )

    # Calculamos el costo de la asesoria segun su duracion.
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        return self.calcular_total(duracion, impuesto, descuento)
