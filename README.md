# SOFTWARE_FJ
### Sistema de gestión de servicios y reservas

## 1. Descripción del proyecto

SOFTWARE_FJ es un sistema desarrollado en Python que permite gestionar clientes, servicios y reservas mediante programación orientada a objetos.

El proyecto incorpora validaciones, manejo de excepciones y registro de eventos para controlar las operaciones realizadas en el sistema.

## 2. Objetivo

Desarrollar un sistema que permita organizar y administrar la información de clientes, servicios y reservas, aplicando los principios de la programación orientada a objetos y herramientas para el control de errores.

## 3. Tecnologías utilizadas

- Python.
- Programación orientada a objetos (POO).
- Manejo de excepciones.
- Módulo Logging para el registro de eventos.
- Git y GitHub para el control de versiones y almacenamiento del proyecto.

## 4. Estructura del proyecto

| Archivo | Descripción |
|---|---|
| `main.py` | Ejecuta las operaciones principales y las pruebas de búsqueda y control de duplicados. |
| `entidades.py` | Contiene las clases relacionadas con las entidades del sistema. |
| `servicios.py` | Define los servicios y sus métodos de cálculo. |
| `reservas.py` | Gestiona la creación, confirmación, cancelación y procesamiento de reservas. |
| `excepciones.py` | Contiene las excepciones personalizadas. |
| `gestor.py` | Administra clientes, servicios y reservas. |
| `logs.py` | Configura el registro de eventos y errores. |
| `pruebas_excepciones.py` | Comprueba el funcionamiento del manejo de excepciones. |
| `pruebas_reservas.py` | Realiza pruebas de validación y control de reservas. |
| `.gitignore` | Define los archivos que Git debe excluir del repositorio. |

## 5. Funcionalidades principales

- Registro y administración de clientes.
- Registro y administración de servicios.
- Creación y búsqueda de reservas.
- Validación de datos.
- Control de registros duplicados.
- Confirmación y cancelación de reservas.
- Cálculo del costo de los servicios.
- Manejo de excepciones personalizadas.
- Registro de eventos mediante archivos de log.

## 6. Requisitos

- Tener Python instalado.
- Contar con Visual Studio Code o un editor compatible.

## 7. Ejecución del proyecto

Para ejecutar el programa principal, abrir una terminal en la carpeta del proyecto y escribir:

```bash
python main.py
```

Para ejecutar las pruebas de excepciones:

```bash
python pruebas_excepciones.py
```

Para ejecutar las pruebas de reservas:

```bash
python pruebas_reservas.py
```


## 8. Autores

- Cristian Andres Roberto
- Danna Julieth Salcedo Corso

Proyecto académico desarrollado en Python.


## 9. Repositorio

[SOFTWARE_FJ en GitHub](https://github.com/47CristianRoberto/SOFTWARE_FJ)
