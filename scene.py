# meshs son los glutSolidMesh pero con parámetros extra
from tools import *

'''
    Cube        =   Cubo
    Cylinder    =   Cilindro
    Plane       =   Plano
    Teapot      =   Tetera
    Sphere      =   Esfera
    Cone        =   Cono
    Torus       =   Dona
    Tetrahedrion    =   Piramidre
    Octahedron      =   Diamante
    Dodecahedron    =   Esfera PS2  o Una papa
    Icosahedron     =   Esfera PS1  o Un huevo a baja resolucion
'''

def paleta(color=0):
    COLORES = {
        "GRIS":   (0.5, 0.5, 0.5),
        "NEGRO":  (0.1, 0.1, 0.1),
        "BLANCO": (0.9, 0.9, 0.9),
        "ROJO":   (0.7, 0.1, 0.1),
        "VERDE":  (0.1, 0.7, 0.1),
        "AZUL":   (0.1, 0.1, 0.7),
        "MORADO": (0.5, 0.1, 0.5),
        "NARANJA":(1.0, 0.5, 0.05),
        "CAFE":   (0.35, 0.18, 0.08),
        "BEIGE":  (0.95, 0.75, 0.55),
        "AMARILLO_VERDE": (0.7, 0.85, 0.15),
        "VERDE_OSCURO":   (0.08, 0.3, 0.15),
        "JEANS":  (0.2, 0.45, 0.75),
        "PAJA":   (0.85, 0.7, 0.3),
        "MADERA": (0.5, 0.3, 0.12),
        "ROSA":   (1.0, 0.45, 0.55),
    }
    # Acepta un nombre ("ROJO", "rojo"), un id (3) o una tupla (1, 0, 0)
    if isinstance(color, str):
        return COLORES.get(color.upper(), COLORES["GRIS"])

    if isinstance(color, int):
        valores = list(COLORES.values())
        if 0 <= color < len(valores):
            return valores[color]
        return COLORES["GRIS"]

    return color    # si ya es una tupla de color, se regresa tal cual

def drawingScene():
    #   Sistemas generales
    sysScene.ejes(visibleMallas=True, visibleEjes=True)
    #   Aqui se dibuja todo lo que no se va animar
    mesh.plane()
    #   Animación: dibuja el fotograma que toca en este momento
    drawAnimation()

# ---------------------------------------------------------------------------
#   ANIMACIÓN POR FOTOGRAMAS
#   Cada def fN de la clase "fotogramas" es un fotograma. En cada cuadro de la
#   ventana se dibuja uno, en orden: f0, f1, f2... Agrega o borra los que
#   necesites (f13, f14...): se detectan solos. La velocidad la define "fps"
#   en main.py (12 fps = 12 fotogramas por segundo).
# ---------------------------------------------------------------------------
nFotograma = 0  # Número de fotograma que sigue.
loop = True  # True = repite la animación; False = se queda en el último fotograma.

def drawAnimation():  # Dibuja un fotograma cada vez que se llama (una vez por cuadro).
    global nFotograma  # Permite modificar el contador.
    nombres = sorted((n for n in vars(fotogramas) if n[0] == "f" and n[1:].isdigit()), key=lambda n: int(n[1:]))  # Busca f0, f1, f2... y los ordena por número.
    if not nombres:  # Si no hay ningún fotograma.
        return  # No hace nada.
    n = nFotograma % len(nombres) if loop else min(nFotograma, len(nombres) - 1)  # Fotograma a dibujar (vuelve a 0 o se queda en el último).
    print("--FOTOGRAMA: [" + str(n) + "]")  # Informa cuál se está dibujando.
    getattr(fotogramas, nombres[n])()  # Ejecuta ese fotograma (la escena ya se limpió, solo se dibuja lo de este).
    nFotograma += 1  # Pasa al siguiente.

def drawEjemple():  # Dibuja la banca y llama al resto de la escena.
    # Ejemplos:
    # wire.cube(translate=(0,2,0))
    meshWire.dodecahedron(translate=(0,2,0))
    mesh.plane(scale=(4,1,4))

class fotogramas:
    # Ejemplo: una esfera que avanza 0.5 en X por fotograma (bórralo y dibuja lo tuyo).
    def f0():
        mesh.sphere(radio=0.3, translate=(-3.0, 0.3, 0), color=paleta("ROJO"))
        audio.sound(path="golpe-en-la-cara.mp3")
    def f1():
        mesh.sphere(radio=0.3, translate=(-2.5, 0.3, 0), color=paleta("ROJO"))
    def f2():
        mesh.sphere(radio=0.3, translate=(-2.0, 0.3, 0), color=paleta("AZUL"))
    def f3():
        mesh.sphere(radio=0.3, translate=(-1.5, 0.3, 0), color=paleta("AZUL"))
    def f4():
        mesh.sphere(radio=0.3, translate=(-1.0, 0.3, 0), color=paleta("ROJO"))
    def f5():
        mesh.sphere(radio=0.3, translate=(-0.5, 0.3, 0), color=paleta("ROJO"))
    def f6():
        mesh.sphere(radio=0.3, translate=(0.0, 0.3, 0), color=paleta("AZUL"))
    def f7():
        mesh.sphere(radio=0.3, translate=(0.5, 0.3, 0), color=paleta("AZUL"))
    def f8():
        mesh.sphere(radio=0.3, translate=(1.0, 0.3, 0), color=paleta("ROJO"))
    def f9():
        mesh.sphere(radio=0.3, translate=(1.5, 0.3, 0), color=paleta("ROJO"))
    def f10():
        mesh.sphere(radio=0.3, translate=(2.0, 0.3, 0), color=paleta("AZUL"))
    def f11():
        mesh.sphere(radio=0.3, translate=(2.5, 0.3, 0), color=paleta("AZUL"))
    def f12():
        mesh.sphere(radio=0.3, translate=(3.0, 0.3, 0), color=paleta("ROJO"))