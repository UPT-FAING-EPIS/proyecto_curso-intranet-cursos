[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/7qywsEwv)
# API REST Cursos 

## Descripción
Este es un proyecto de API REST para la entidad Curso, que permite realizar operaciones CRUD (Crear, Leer y Actualizar ) en una base de datos

## Paquetes necesarios

| Package | Version |
|---------|---------|
| asgiref | 3.6.0   |
| Django  | 4.2     |
| mysqlclient | 2.1.1 |
| pip     | 23.1.1  |
| PyMySQL | 1.0.3   |
| setuptools | 67.6.1 |
| sqlparse | 0.4.4   |
| tzdata  | 2023.3  |
| wheel   | 0.40.0  |

## URLs

### `GET /`
Obtiene una lista de todos los cursos.

### `GET /<str:CodigoCurso>`
Obtiene los datos de los cursos en específico.

### `POST /`
Crea un nuevo curso.

### `PUT /<str:CodigoCurso>`
Actualiza los datos de los cursos existente.

## Vistas

### APICursosViews

Vista que maneja las operaciones CRUD para la entidad Curso.

#### Métodos

## GET

Obtiene una lista de todos los Cursos o los datos de un Curso específico si se proporciona el Codigo del Curso como parámetro en la URL.

Parámetros:
- `CodigoCurso` (str): Codigo del Curso.

Respuestas:
- 200 OK: Si se proporciona el Codigo del Curso, devuelve uno o mas datos de ese curso en formato JSON.
- 404 Not Found: Si se proporciona un Codigo del Curso que no existe.

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
  "Cursos": [
    {
      "CodigoCurso": "EG-181",
      "NombreCurso": "COMUNICACIÓN I",
      "THCurso": 5,
      "PreRequisitoCurso": "Ninguno",
      "CicloCurso": "I",
      "CodigoProfesor_id": 1,
      "FkEstado_id": 1
    },
    {
      "CodigoCurso": "EG-182",
      "NombreCurso": "MATEMATICA BASICA",
      "THCurso": 6,
      "PreRequisitoCurso": "Ninguno",
      "CicloCurso": "I",
      "CodigoProfesor_id": 2,
      "FkEstado_id": 1
    },
    ]
}
```

Ejemplo de petición con ID de Curso en específico:

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
  "Cursos": {
    "CodigoCurso": "SI-085",
    "NombreCurso": "TALLER DE EMPRENDIMIENTO Y LIDERAZGO",
    "THCurso": 4,
    "PreRequisitoCurso": "Ninguno",
    "CicloCurso": "X",
    "CodigoProfesor_id": 8,
    "FkEstado_id": 1
  }
}
```

Continuando la documentación:

## POST

El método `POST` crea un nuevo Curso con los datos proporcionados en el cuerpo de la solicitud. 

##### Parámetros

Los siguientes parámetros deben ser proporcionados en el cuerpo de la solicitud en formato JSON:

- `CodigoCurso` (string): Codigo del curso
- `NombreCurso` (string): Nombre del curso.
- `THCurso` (int): Horas Totales del curso
- `PreRequisitoCurso` (string): Prerequisito para llevar el curso.
- `CodigoProfesor` (int): Codigo del profesor.
- `FkEstado` (int): Estado del Curso.

##### Ejemplo de solicitud

```
POST / HTTP/1.1
Host: example.com
Content-Type: application/json
Content-Length: 102
{
      "CodigoCurso": "SI-1001",
      "NombreCurso": "DDD",
      "THCurso": 4,
      "PreRequisitoCurso": "Ninguno",
      "CicloCurso": "Electivo",
      "CodigoProfesor": 2,
      "FkEstado_id": 1
}
```

##### Respuesta

- `200 OK`: Si se crea el curso correctamente.

##### Ejemplo de respuesta

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 19
{
    "message": "Success"
}
```
## PUT
El método `PUT` se utiliza para actualizar los datos de un Curso existente en la base de datos.

### Parámetros

- `CodigoCurso` (str): El Codigo del Curso que se desea actualizar.

En el cuerpo de la solicitud se deben proporcionar los siguientes parámetros:

- `NombreCurso` (string): Nombre del curso.
- `THCurso` (int): Horas Totales del curso
- `PreRequisitoCurso` (string): Prerequisito para llevar el curso.
- `CodigoProfesor` (int): Codigo del profesor.
- `FkEstado` (int): Estado del Curso.

### Respuestas

- `200 OK`: Si se actualizan los datos del Curso correctamente.
- `404 Not Found`: Si el Curso con el Codigo proporcionado no existe.

### Ejemplo

A continuación se presenta un ejemplo de solicitud `PUT` para actualizar los datos de un Curso:

```
PUT /APICursos/SI-SI-085 HTTP/1.1
Host: example.com
Content-Type: application/json
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxx
{
    "CodigoCurso": "SI-085",
    "NombreCurso": "TALLER DE EMPRENDIMIENTO Y LIDERAZGO",
    "THCurso": 4,
    "PreRequisitoCurso": "Ninguno",
    "CicloCurso": "X",
    "CodigoProfesor_id": 8,
    "FkEstado_id": 1
}
```
