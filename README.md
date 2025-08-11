# Proyecto Academia
![Django](https://img.shields.io/badge/Django-092E20?style=plastic&logo=django&logoColor=white)
![Django REST Framework](https://img.shields.io/badge/Django%20REST-A30000?style=plastic&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=plastic&logo=python&logoColor=white)
![Swagger](https://img.shields.io/badge/Swagger-85EA2D?style=plastic&logo=swagger&logoColor=black)
![ReDoc](https://img.shields.io/badge/ReDoc-E0234A?style=plastic&logo=redoc&logoColor=white)


Este es el backend de la plataforma de cursos online "Academia". Está desarrollado con Django y Django REST Framework, y está diseñado para ser consumido por un frontend de Next.js.

## Características

*   **API RESTful:** Proporciona endpoints para gestionar usuarios, cursos y categorías.
*   **Autenticación:** (Próximamente) Se implementará un sistema de autenticación basado en tokens.
*   **Documentación de la API:** La API está documentada con Swagger y ReDoc.

## Empezando

Sigue estas instrucciones para configurar y ejecutar el proyecto en tu entorno local.

### Prerrequisitos

*   Python 3.12
*   pip
*   venv

### Instalación

1.  **Clona el repositorio:**

    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd academia
    ```

2.  **Crea y activa un entorno virtual:**

    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3.  **Instala las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplica las migraciones de la base de datos:**

    ```bash
    python manage.py migrate
    ```

5.  **Crea un superusuario para acceder al panel de administración:**

    ```bash
    python manage.py createsuperuser
    ```

### Ejecución

Para iniciar el servidor de desarrollo, ejecuta el siguiente comando:

```bash
python manage.py runserver
```

El backend estará disponible en `http://127.0.0.1:8000`.

## Endpoints de la API

La documentación completa de la API está disponible en las siguientes URLs una vez que el servidor está en marcha:

*   **Swagger UI:** `http://127.0.0.1:8000/swagger/`
*   **ReDoc:** `http://127.0.0.1:8000/redoc/`

### Endpoints principales

*   `GET /api/users/`: Lista todos los usuarios.
*   `GET, POST /api/cursos/`: Lista o crea nuevos cursos.
*   `GET, PUT, PATCH, DELETE /api/cursos/{id}/`: Obtiene, actualiza o elimina un curso específico.
*   `GET, POST /api/categorias/`: Lista o crea nuevas categorías.
*   `GET, PUT, PATCH, DELETE /api/categorias/{id}/`: Obtiene, actualiza o elimina una categoría específica.

## Panel de Administración

Puedes acceder al panel de administración de Django en `http://127.0.0.1:8000/admin/` para gestionar los datos directamente.
