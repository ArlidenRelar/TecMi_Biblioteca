from flask import Flask, render_template, request, redirect, url_for, flash
from typing import List, Dict, Any

app = Flask(__name__)
# Se requiere una clave secreta para usar sesiones y mensajes flash
app.secret_key = "clave_secreta_super_segura" 

# Tipado de datos para mejorar la legibilidad y el autocompletado en el IDE
libros: List[Dict[str, Any]] = [
    {"id": 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "prestado": False},
    {"id": 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry", "prestado": True},
    {"id": 3, "titulo": "Python para principiantes", "autor": "Equipo docente", "prestado": False},
]

@app.get("/")
def inicio() -> str:
    # Ordenar los libros por ID inverso para que los más nuevos salgan arriba (opcional)
    libros_ordenados = sorted(libros, key=lambda x: x["id"], reverse=True)
    return render_template("index.html", libros=libros_ordenados)

@app.post("/agregar")
def agregar():
    titulo = request.form.get("titulo", "").strip()
    autor = request.form.get("autor", "").strip()

    # Validación temprana (Early Return) para evitar condicionales anidados
    if not titulo or not autor:
        flash("Error: El título y el autor son obligatorios.", "error")
        return redirect(url_for("inicio"))

    nuevo_id = max((libro["id"] for libro in libros), default=0) + 1
    libros.append({
        "id": nuevo_id,
        "titulo": titulo,
        "autor": autor,
        "prestado": False,
    })
    
    flash(f"Libro '{titulo}' agregado con éxito.", "success")
    return redirect(url_for("inicio"))

@app.post("/cambiar_estado/<int:libro_id>")
def cambiar_estado(libro_id: int):
    # Búsqueda más eficiente y "pitónica" usando next() en lugar de un ciclo for tradicional
    libro = next((l for l in libros if l["id"] == libro_id), None)
    
    if libro:
        libro["prestado"] = not libro["prestado"]
        estado = "prestado" if libro["prestado"] else "disponible"
        flash(f"El libro '{libro['titulo']}' ahora está {estado}.", "info")
    else:
        flash("Error: Libro no encontrado.", "error")

    return redirect(url_for("inicio"))

@app.post("/eliminar/<int:libro_id>")
def eliminar(libro_id: int):
    global libros
    # Filtrar la lista excluyendo el libro a eliminar
    libros_previos = len(libros)
    libros = [l for l in libros if l["id"] != libro_id]
    
    if len(libros) < libros_previos:
        flash("Libro eliminado correctamente.", "success")
    else:
        flash("Error: Libro no encontrado.", "error")
        
    return redirect(url_for("inicio"))

if __name__ == "__main__":
    app.run(debug=True)
