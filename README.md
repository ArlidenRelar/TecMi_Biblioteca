# Biblioteca colaborativa

Aplicación web educativa desarrollada con Python y Flask para practicar el flujo de trabajo colaborativo de Git y GitHub.

## Funciones

- Consultar un catálogo de libros.
- Agregar títulos y autores.
- Registrar préstamos y devoluciones.
- Practicar ramas, commits, Pull Requests y revisión de código.

## Requisitos

- Python 3.10 o posterior.
- Git.
- Una cuenta de GitHub.
- CMD en Windows o Terminal en macOS.

## Ejecutar en Windows (CMD)

```bat
py -m venv .venv
.venv\Scripts\activate
py -m pip install -r requirements.txt
py app.py
```

Si el comando `py` no existe, prueba `python` en su lugar.

## Ejecutar en macOS (Terminal)

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 app.py
```

Abre http://127.0.0.1:5000 en el navegador. Para detener el servidor, vuelve a la terminal y pulsa `Ctrl+C`.

## Flujo colaborativo recomendado

1. Crear un repositorio en GitHub y añadir colaboradores.
2. Cada persona clona el repositorio.
3. Cada persona crea una rama con su nombre o función.
4. Hace cambios pequeños y commits descriptivos.
5. Sube la rama a GitHub y abre un Pull Request hacia `main`.
6. Otro compañero revisa el código.
7. El equipo aprueba e integra el Pull Request.
8. Todos actualizan su copia local con `git pull`.

## Limitación de esta versión

Los libros se almacenan en una lista de Python en memoria. No hay base de datos y los cambios desaparecen al detener la aplicación. La aplicación Flask no puede ejecutarse directamente en GitHub Pages, que sirve contenido estático.
