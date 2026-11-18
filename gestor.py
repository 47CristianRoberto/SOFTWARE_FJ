
# Importamos la funcion para guardar los eventos del sistema.
from logs import registrar_evento


# Clase encargada de administrar la informacion del sistema.
class GestorSistema:

    def __init__(self):

        # Listas donde se almacenan los datos.
        self.clientes = []
        self.servicios = []
        self.reservas = []

        registrar_evento(
            "El gestor del sistema fue inicializado."
        )

    # Metodo para agregar un cliente.
    def agregar_cliente(self, cliente):

        # Verificamos que el cliente no este duplicado.
        for actual in self.clientes:

            if actual.documento == cliente.documento:
                raise ValueError(
                    "Ya existe un cliente con ese documento."
                )

        self.clientes.append(cliente)

        registrar_evento(
            f"Cliente {cliente.nombre} registrado correctamente."
        )

        return "Cliente registrado correctamente."

    # Metodo para agregar un servicio.
    def agregar_servicio(self, servicio):

        # Comprobamos que el servicio no este duplicado.
        for actual in self.servicios:

            if actual.nombre == servicio.nombre:
                raise ValueError(
                    "Ya existe un servicio con ese nombre."
                )

        self.servicios.append(servicio)

        registrar_evento(
            f"Servicio {servicio.nombre} registrado correctamente."
        )

        return "Servicio registrado correctamente."

    # Metodo para agregar una reserva.
    def agregar_reserva(self, reserva):

        # Comprobamos que el codigo de reserva sea unico.
        for actual in self.reservas:

            if actual.codigo == reserva.codigo:
                raise ValueError(
                    "Ya existe una reserva con ese codigo."
                )

        self.reservas.append(reserva)

        registrar_evento(
            f"Reserva {reserva.codigo} registrada correctamente."
        )

        return "Reserva registrada correctamente."

    # Metodo para buscar un cliente por documento.
    def buscar_cliente(self, documento):

        for cliente in self.clientes:

            if cliente.documento == documento:
                return cliente

        return None

    # Metodo para buscar un servicio por nombre.
    def buscar_servicio(self, nombre):

        for servicio in self.servicios:

            if servicio.nombre.lower() == nombre.lower():
                return servicio

        return None

    # Metodo para buscar una reserva por codigo.
    def buscar_reserva(self, codigo):

        for reserva in self.reservas:

            if reserva.codigo == codigo:
                return reserva

        return None

    # Metodo para consultar los clientes.
    def listar_clientes(self):

        return self.clientes

    # Metodo para consultar los servicios.
    def listar_servicios(self):

        return self.servicios

    # Metodo para consultar las reservas.
    def listar_reservas(self):

        return self.reservas

    # Metodo para mostrar un resumen del sistema.
    def mostrar_resumen(self):

        return (
            f"Total de clientes: {len(self.clientes)}\n"
            f"Total de servicios: {len(self.servicios)}\n"
            f"Total de reservas: {len(self.reservas)}"
        )
