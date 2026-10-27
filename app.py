from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Datos de ejemplo en memoria. Se reinician al detener la aplicación.
libros = [
    {"id": 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "prestado": False},
    {"id": 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry", "prestado": True},
    {"id": 3, "titulo": "Python para principiantes", "autor": "Equipo docente", "prestado": False},
]


@app.get("/")
def inicio():
    return render_template("index.html", libros=libros)


@app.post("/agregar")
def agregar():
    titulo = request.form.get("titulo", "").strip()
    autor = request.form.get("autor", "").strip()

    if titulo and autor:
        nuevo_id = max((libro["id"] for libro in libros), default=0) + 1
        libros.append({
            "id": nuevo_id,
            "titulo": titulo,
            "autor": autor,
            "prestado": False,
        })

    return redirect(url_for("inicio"))


@app.post("/cambiar_estado/<int:libro_id>")
def cambiar_estado(libro_id):
    for libro in libros:
        if libro["id"] == libro_id:
            libro["prestado"] = not libro["prestado"]
            break

    return redirect(url_for("inicio"))


if __name__ == "__main__":
    app.run(debug=True)
