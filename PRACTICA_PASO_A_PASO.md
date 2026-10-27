# Práctica guiada: construcción y lanzamiento colaborativo de una Web App

**Duración:** 90 minutos  
**Proyecto:** Biblioteca colaborativa con Python y Flask  
**Herramientas:** GitHub, Git y CMD de Windows o Terminal de macOS

## Objetivo

Trabajar en equipo con un repositorio compartido. Cada integrante desarrolla una parte en una rama propia, registra cambios con commits, abre un Pull Request y revisa el código de otra persona antes de integrarlo a `main`.

## Antes de comenzar

- Todos los integrantes deben tener una cuenta de GitHub.
- Instalar Git y Python 3.10 o posterior.
- Una persona será responsable de crear el repositorio.
- Cada integrante debe conocer su nombre de usuario de GitHub.

Comprueba las herramientas:

**Windows CMD**
```bat
git --version
py --version
```
Si `py` no funciona, prueba:
```bat
python --version
```

**macOS Terminal**
```bash
git --version
python3 --version
```

Si Git no está instalado, en macOS se puede instalar mediante las herramientas de línea de comandos de Xcode ejecutando `xcode-select --install`. En Windows, instala Git for Windows y abre una nueva ventana de CMD.

---

# Fase 1. Configurar el repositorio (15 minutos)

## A. Crear el repositorio en GitHub

1. Entra a https://github.com e inicia sesión.
2. Pulsa **New repository**.
3. Nombre sugerido: `biblioteca-colaborativa`.
4. Selecciona **Public** o **Private**, según indique el docente.
5. Marca **Add a README file**.
6. Pulsa **Create repository**.
7. En el repositorio, entra a **Settings → Collaborators** (puede aparecer como Collaborators and teams).
8. Pulsa **Add people** e invita a tus compañeros por su usuario de GitHub.
9. Cada compañero debe aceptar la invitación.

> Si el repositorio ya contiene un README, no vuelvas a inicializar otro repositorio local desde cero. Se clonará el repositorio existente.

## B. Configurar nombre y correo de Git

Cada alumno ejecuta estos comandos una sola vez por equipo de trabajo. Usa el correo asociado a GitHub o una dirección `noreply` configurada en GitHub.

**Windows CMD y macOS Terminal**
```bash
git config --global user.name "Nombre Apellido"
git config --global user.email "correo@example.com"
```

Comprueba la configuración:
```bash
git config --global --list
```

## C. Clonar el repositorio

En GitHub, pulsa el botón verde **Code**, selecciona HTTPS y copia la URL. Sustituye la URL de ejemplo por la URL real de tu repositorio.

**Windows CMD**
```bat
cd %USERPROFILE%\Documents
git clone https://github.com/USUARIO/biblioteca-colaborativa.git
cd biblioteca-colaborativa
dir
```

**macOS Terminal**
```bash
cd ~/Documents
git clone https://github.com/USUARIO/biblioteca-colaborativa.git
cd biblioteca-colaborativa
ls -la
```

Si la carpeta Documents no existe o prefieres otra ubicación, entra en una carpeta que sí exista. No ejecutes `git clone` dentro de otra copia del mismo repositorio.

## D. Copiar los archivos de la práctica

Descarga y descomprime el paquete entregado por el docente. Copia `app.py`, `requirements.txt`, `.gitignore`, `README.md` y la carpeta `templates` dentro de la carpeta clonada.

Si GitHub creó un README, puedes reemplazarlo por el README de esta práctica. Después revisa el estado:

```bash
git status
```

Agrega y registra el proyecto base:

```bash
git add .
git commit -m "Agrega la estructura inicial de la biblioteca"
git push origin main
```

Si `git push` indica que hay cambios remotos que no tienes, ejecuta primero `git pull --rebase origin main` y resuelve cualquier conflicto antes de volver a subir.

---

# Fase 2. Crear ramas individuales (15 minutos)

Cada alumno trabaja en una rama propia. No deben editar directamente `main`.

Ejemplos de nombres:
- `feature/formulario-libros`
- `feature/estado-prestamos`
- `docs/mejora-readme`

Cada integrante usa un nombre distinto y crea su rama desde la versión actual de `main`.

**Windows CMD y macOS Terminal**
```bash
git switch main
git pull origin main
git switch -c feature/mi-funcionalidad
git branch
```

Reemplaza `feature/mi-funcionalidad` por el nombre de tu rama. El asterisco `*` debe aparecer junto a la rama nueva.

Para ver la rama actual:
```bash
git branch --show-current
```

## Reparto de trabajo sugerido

- **Integrante A — formulario:** mejora el formulario para agregar libros y sus mensajes de validación.
- **Integrante B — catálogo:** mejora la presentación de los libros y sus estados.
- **Integrante C — documentación:** completa el README con instalación, uso y limitaciones.
- **Integrante D — pruebas/revisión:** prueba los casos principales y revisa los Pull Requests. Si son menos personas, combina roles.

Cada cambio debe ser pequeño y estar relacionado con el objetivo de la rama. Si varios alumnos editan simultáneamente las mismas líneas de un archivo, puede haber conflictos.

---

# Fase 3. Desarrollar y hacer commits (35 minutos)

## A. Ejecutar primero la aplicación base

Crea un entorno virtual e instala las dependencias.

**Windows CMD**
```bat
py -m venv .venv
.venv\Scripts\activate
py -m pip install -r requirements.txt
py app.py
```

Si `py` no existe, usa `python` en los comandos correspondientes.

**macOS Terminal**
```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 app.py
```

Abre `http://127.0.0.1:5000` en el navegador. Prueba agregar un libro, prestarlo y devolverlo. Detén el servidor con `Ctrl+C`.

## B. Realizar el cambio asignado

Cada integrante modifica los archivos correspondientes a su tarea. Antes de editar, confirma la rama:

```bash
git branch --show-current
git status
```

Después de editar, revisa qué cambió:
```bash
git diff
```

Agrega solamente los archivos que correspondan a tu tarea. Por ejemplo:
```bash
git add templates/index.html
git commit -m "Mejora la presentación del catálogo"
```

Si modificaste otros archivos, agrega sus rutas con `git add archivo`. También puedes usar `git add .` si revisaste todos los cambios y estás seguro de que son correctos.

Consulta el historial:
```bash
git log --oneline -5
```

**Un commit debe representar un cambio pequeño y entendible.** Evita mensajes como `cambios`, `final` o `arreglos`.

## C. Subir la rama

```bash
git push -u origin feature/mi-funcionalidad
```

Sustituye el nombre por tu rama real. La primera vez, `-u` enlaza tu rama local con la remota. Si Git solicita autenticación por HTTPS, sigue el flujo de inicio de sesión del navegador o usa un método de autenticación configurado en GitHub; la contraseña normal de la cuenta no funciona como contraseña de Git por HTTPS.

---

# Fase 4. Pull Request y revisión de código (15 minutos)

## A. Abrir un Pull Request

1. En GitHub, abre el repositorio.
2. Pulsa **Compare & pull request** si aparece, o entra a **Pull requests → New pull request**.
3. Base: `main`.
4. Compare: tu rama `feature/...`.
5. Escribe un título claro, por ejemplo: `Mejora la presentación del catálogo`.
6. En la descripción explica qué cambiaste y cómo lo probaste.
7. Asigna como revisor a un compañero.
8. Pulsa **Create pull request**.

## B. Revisar el Pull Request de un compañero

El revisor debe:
1. Leer la descripción del cambio.
2. Revisar la pestaña **Files changed**.
3. Comprobar que el cambio sea pertinente y legible.
4. Señalar errores o proponer mejoras concretas.
5. Si todo está bien, seleccionar **Review changes → Approve** (si tiene permisos) o dejar un comentario de aprobación.

Si se solicitan cambios, el autor corrige los archivos en su rama y realiza otro commit. Al hacer `git push`, el Pull Request se actualiza automáticamente.

## C. Integrar los cambios

Después de la revisión, el responsable del repositorio pulsa **Merge pull request** y confirma. Para una práctica introductoria, puede utilizarse **Squash and merge** si está habilitado, pero el equipo debe usar el mismo criterio durante la actividad.

No se debe integrar un Pull Request que tenga errores conocidos sin discutirlos con el equipo.

---

# Fase 5. Actualizar e iniciar la aplicación (10 minutos)

Una vez integrado el Pull Request, cada integrante actualiza su copia local.

Primero cambia a `main`:
```bash
git switch main
git pull origin main
```

Activa el entorno virtual si no está activo e inicia la aplicación:

**Windows CMD**
```bat
.venv\Scripts\activate
py app.py
```

**macOS Terminal**
```bash
source .venv/bin/activate
python3 app.py
```

Abre `http://127.0.0.1:5000` y verifica que la aplicación funcione. Si no se ha instalado Flask en esa computadora, ejecuta `pip install -r requirements.txt` con el entorno virtual activado.

## Cierre de la práctica: evidencia que debe entregar el equipo

1. URL del repositorio GitHub.
2. Captura o enlace a las ramas creadas.
3. Al menos un commit descriptivo por integrante.
4. Al menos un Pull Request revisado por un compañero.
5. Evidencia de que el Pull Request fue integrado a `main`.
6. Captura de la aplicación funcionando en el navegador.
7. Breve reflexión: ¿qué aportó la revisión de código y qué problema encontraron?

## Problemas comunes

### `git` no se reconoce
Git no está instalado o la terminal no se ha reiniciado después de instalarlo. Instala Git y abre una terminal nueva.

### `Author identity unknown`
Configura `git config --global user.name` y `git config --global user.email`, y repite el commit.

### `src refspec main does not match any`
Puede que todavía no exista ningún commit o que la rama tenga otro nombre. Ejecuta `git status` y `git branch`. Crea el primer commit y comprueba el nombre de la rama.

### `Updates were rejected`
El repositorio remoto contiene cambios que no están en tu copia. Guarda o confirma tus cambios y ejecuta `git pull --rebase origin main` cuando estés trabajando en `main`. Si hay conflictos, resuélvelos antes de continuar.

### Conflicto al integrar
GitHub puede marcar conflictos si dos personas cambiaron las mismas líneas. El autor del Pull Request y el responsable del repositorio deben resolverlos y probar la aplicación antes de integrar.

### Flask no se encuentra
Activa el entorno virtual e instala las dependencias:
```bash
python -m pip install -r requirements.txt
```
En macOS puedes usar `python3 -m pip install -r requirements.txt`.

### ¿Por qué no se publica en GitHub Pages?
GitHub Pages publica HTML, CSS y JavaScript estáticos; no ejecuta una aplicación Flask. Para esta práctica se ejecuta localmente. Un despliegue público requeriría un servicio que admita aplicaciones Python.
