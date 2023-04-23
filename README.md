
# API REST Profesor

## Descripción
Este es un proyecto de API REST para la entidad Profesor, que permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) en una base de datos.

## Instalación
Para poder utilizar esta API, se necesita tener Python 3.x y Django 3.x instalados. Para instalar Django, se puede utilizar el siguiente comando en la línea de comandos:

```
pip install django
```

## URLs

### `GET /`
Obtiene una lista de todos los profesores.

### `GET /<int:CodigoDocente>`
Obtiene los datos de un profesor específico.

### `POST /`
Crea un nuevo profesor.

### `PUT /<int:CodigoDocente>`
Actualiza los datos de un profesor existente.

## Vistas

### APIProfesorViews

Vista que maneja las operaciones CRUD para la entidad Profesor.

#### Métodos

##### `GET`

Obtiene una lista de todos los profesores o los datos de un profesor específico si se proporciona el ID del profesor como parámetro en la URL.

Parámetros:
- `CodigoDocente` (int): ID del profesor.

Respuestas:
- 200 OK: Si se proporciona el ID del profesor, devuelve los datos de ese profesor en formato JSON.
- 404 Not Found: Si se proporciona un ID de profesor que no existe.
- 200 OK: Si no se proporciona ningún ID de profesor, devuelve una lista de todos los profesores en formato JSON.

Ejemplo de petición:

```
GET / HTTP/1.1
Host: example.com
Content-Type: application/json
```

Respuesta:

```
HTTP/1.1 200 OK
Content-Type: application/json

{
    "Profesores": [
        {
            "CodigoDocente": 1,
            "NombreDocente": "Juan",
            "ApellidoDocente": "Pérez",
            "EmailDocente": "juan.perez@example.com",
            "NumeroDocente": "1234567890",
            "DireccionDocente": "Calle 123"
        },
        {
            "CodigoDocente": 2,
            "NombreDocente": "María",
            "ApellidoDocente": "González",
            "EmailDocente": "maria.gonzalez@example.com",
            "NumeroDocente": "0987654321",
            "DireccionDocente": "Avenida 456"
        }
    ]
}
```

Ejemplo de petición con ID de profesor específico:

```
GET /1 HTTP/1.1
Host: example.com
Content-Type: application/json
```

Respuesta:

```
HTTP/1.1 200 OK
Content-Type: application/json

{
    "Profesores": {
        "CodigoDocente": 1,
        "NombreDocente": "Juan",
        "ApellidoDocente": "Pérez",
        "EmailDocente": "juan.perez@example.com",
        "NumeroDocente": "1234567890",
        "DireccionDocente": "Calle 123"
    }
}
```

Continuando la documentación:

#### POST

El método `POST` crea un nuevo profesor con los datos proporcionados en el cuerpo de la solicitud. 

##### Parámetros

Los siguientes parámetros deben ser proporcionados en el cuerpo de la solicitud en formato JSON:

- `NombreDocente` (string): Nombre del profesor.
- `ApellidoDocente` (string): Apellido del profesor.
- `EmailDocente` (string): Email del profesor.
- `NumeroDocente` (string): Número de teléfono del profesor.
- `DireccionDocente` (string): Dirección del profesor.

##### Ejemplo de solicitud

```
POST / HTTP/1.1
Host: example.com
Content-Type: application/json
Content-Length: 102

{
    "NombreDocente": "Juan",
    "ApellidoDocente": "Perez",
    "EmailDocente": "juan.perez@example.com",
    "NumeroDocente": "123456789",
    "DireccionDocente": "Calle 123, Ciudad"
}
```

##### Respuesta

- `200 OK`: Si se crea el profesor correctamente.

##### Ejemplo de respuesta

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 19

{
    "message": "Success"
}
```
#### PUT
El método `PUT` se utiliza para actualizar los datos de un profesor existente en la base de datos.

### Parámetros

- `CodigoDocente` (int): El ID del profesor que se desea actualizar.

En el cuerpo de la solicitud se deben proporcionar los siguientes parámetros:

- `NombreDocente` (string): El nuevo nombre del profesor.
- `ApellidoDocente` (string): El nuevo apellido del profesor.
- `EmailDocente` (string): El nuevo email del profesor.
- `NumeroDocente` (string): El nuevo número de teléfono del profesor.
- `DireccionDocente` (string): La nueva dirección del profesor.

### Respuestas

- `200 OK`: Si se actualizan los datos del profesor correctamente.
- `404 Not Found`: Si el profesor con el ID proporcionado no existe.

### Ejemplo

A continuación se presenta un ejemplo de solicitud `PUT` para actualizar los datos de un profesor:

```
PUT /api/profesores/1 HTTP/1.1
Host: example.com
Content-Type: application/json
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxx

{
    "NombreDocente": "Juan",
    "ApellidoDocente": "Pérez",
    "EmailDocente": "juan.perez@example.com",
    "NumeroDocente": "1234567890",
    "DireccionDocente": "Calle 123"
}
```
