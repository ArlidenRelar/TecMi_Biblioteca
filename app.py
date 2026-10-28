#Modificación hecha por Mariana Yamile, Alexa del Carmen y Fedro Rojas

from flask import Flask, render_template

app = Flask(__name__)

# Datos de ejemplo para tu biblioteca
LIBROS = [
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "disponible": True},
    {"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "disponible": False},
   # Modificación adicional por Diego Mondragón
    {{"titulo": "Clean Code", "autor": "Robert C. Martin", "disponible": True},
 {"titulo": "El principito", "autor": "Antoine de Saint-Exupéry", "disponible": True}
]

@app.route('/')
def home():
    # Pasa el nombre de la biblioteca y el catálogo de libros a la plantilla
    return render_template('index.html', titulo_pagina="Mi Biblioteca Virtual", libros=LIBROS)

@app.route('/acerca')
def acerca():
    return "<h1>Acerca de TecMi Biblioteca</h1><p>Sistema de gestión de libros del proyecto.</p>"

if __name__ == '__main__':
    app.run(debug=True)
