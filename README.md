# PROYECTO 3D. LLAMITA

Este proyecto busca crear una llamita usando las librerías PyOpenGL (`.GL`, `.GLU`, `.GLUT`), NumPy, Pygame, entre otras. Todo se dibuja armando figuras simples (cubos, esferas, cilindros, etc.) con transformaciones, sin cargar modelos externos.

## Requisitos

- Python 3.12
- freeglut instalado en el sistema (en Fedora):

```bash
sudo dnf install freeglut freeglut-devel mesa-libGLU
```

## Instalación

Desde la carpeta del proyecto:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install PyOpenGL numpy pygame
```

## Ejecutar

```bash
python main.py
```

`main.py` fija `PYOPENGL_PLATFORM=x11` para evitar el error de contexto de GLUT en Wayland.

## Controles

- **Arrastrar con el ratón:** gira la cámara alrededor de la escena.
- **Rueda del ratón:** acerca y aleja la cámara.

## Cómo funciona

- **`main.py`:** abre la ventana (`runWinodws()`), maneja la cámara y el ratón, y limita el dibujo a `fps` fotogramas por segundo (12 por defecto, se cambia en la configuración del archivo).
- **`scene.py`:** aquí se dibuja la escena. `main.py` llama a `scene.drawingScene()` en cada fotograma.
- **Recarga automática:** mientras el programa corre, al guardar cualquier `.py` de la carpeta se vuelven a leer los archivos y la escena se actualiza sin cerrar la ventana. Los cambios en `main.py` sí requieren volver a ejecutar.
- **Ventana redimensionable:** la perspectiva se recalcula con la proporción real, así que los modelos no se deforman al cambiar el tamaño.

## Meshs

Todas las figuras comparten los mismos parámetros de posición y aspecto:

| Parámetro | Qué hace |
|---|---|
| `color` | Color `(R, G, B)` con valores de 0 a 1. Se puede usar `paleta("ROJO")` o `paleta(3)`. |
| `translate` | Posición `(x, y, z)`. |
| `rotate` | Giro `(ángulo, x, y, z)`: ángulo en grados y eje de giro. Se puede obtener con `convert.degrees(x, y, z)`. |
| `scale` | Escala `(x, y, z)`; permite estirar o aplastar la figura. |
| `name` | Nombre de la figura. |
| `visible` | Si es `False`, la figura no se dibuja. |

### Clase `mesh` (figuras de GLUT)

`cube`, `teapot`, `sphere`, `cone`, `torus`, `cylinder`, `plane`, `tetrahedron`, `octahedron`, `dodecahedron` e `icosahedron`.

```python
mesh.cube(size=1.0, color=paleta("ROJO"), translate=(0, 1, 0))
mesh.cylinder(radio=0.1, altura=2.0, rotate=convert.degrees(-90, 0, 0))  # Cilindro parado
```

Los cuatro poliedros no reciben tamaño; se cambian con `scale`. El cilindro nace acostado sobre el eje Z, por eso se gira -90° en X para pararlo.

### Clase `meshQuad` (figuras de GLU, moldeables)

`tube` (cilindro con dos radios, cono si el radio del tope es 0, con `tapas` opcionales), `disk`, `partialDisk` y `sphere`. Además de los parámetros comunes, aceptan:

| Parámetro | Valores |
|---|---|
| `estilo` | `"solido"`, `"alambre"`, `"puntos"`, `"silueta"` |
| `normales` | `"suaves"` (lisa) o `"planas"` (facetada) |
| `textura` | `True` genera coordenadas de textura |
| `adentro` | `True` voltea las normales hacia adentro |

```python
meshQuad.tube(radio_base=0.25, radio_tope=0.15, altura=0.8, rotate=convert.degrees(-90, 0, 0))
meshQuad.sphere(radio=0.6, scale=(1.0, 0.6, 1.0), normales="planas")  # Esfera aplastada y facetada
```

## Otras utilidades

- **`light.sun(color, ambient, direction, visible)`:** luz solar direccional. Se llama en cada fotograma, después de las transformaciones de cámara y antes de dibujar las figuras.
- **`convert.degrees(x, y, z)`:** convierte giros en grados sobre cada eje a la forma `(ángulo, x, y, z)` que entiende OpenGL.
- **`paleta(color)`:** devuelve un color por nombre (`"ROJO"`), por id (`3`) o deja pasar una tupla.
- **`audio.backgroundMusic(path, volumen)`:** música de fondo en bucle infinito con Pygame. Se llama una sola vez al iniciar.

## Repositorio de GitHub

Repositorio: https://github.com/zzaun/proyect3d.git

### Quick setup — si ya has hecho esto antes

```bash
git clone https://github.com/zzaun/proyect3d.git
```

### …o crear un repositorio nuevo desde la línea de comandos

```bash
echo "# proyect3d" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/zzaun/proyect3d.git
git push -u origin main
```

### …o subir un repositorio existente desde la línea de comandos

```bash
git remote add origin https://github.com/zzaun/proyect3d.git
git branch -M main
git push -u origin main
```

## Para que no vuelva a pasar

Haz commit antes de hacer pull, o usa `git pull --rebase` con el árbol de trabajo limpio. Los conflictos del autostash aparecen justo cuando haces pull con cambios sin commitear.