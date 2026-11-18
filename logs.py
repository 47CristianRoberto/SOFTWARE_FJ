
# Importamos la herramienta que permite guardar registros del programa.
import logging
from pathlib import Path


# Definimos la ubicacion del archivo donde guardaremos los registros.
RUTA_LOG = Path(__file__).resolve().parent / "registro.log"


# Configuramos el sistema de registros.
logging.basicConfig(
    filename=RUTA_LOG,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
    encoding="utf-8",
    force=True
)


# Obtenemos el encargado de escribir los registros.
logger = logging.getLogger("SoftwareFJ")


# Esta funcion guarda los eventos importantes del sistema.
def registrar_evento(mensaje):
    logger.info(mensaje)


# Esta funcion guarda los errores que se presentan durante la ejecucion.
def registrar_error(mensaje):
    logger.error(mensaje)


# Esta funcion permite guardar errores con informacion detallada.
def registrar_error_detallado(mensaje):
    logger.exception(mensaje)


