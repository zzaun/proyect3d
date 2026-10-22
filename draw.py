# meshs son los glutSolidMesh pero con parámetros extra
from meshs import *

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

def drawing():
    light.sun()
    ejes(visibleMallas=True, visibleEjes=True)
    drawEjemple()


def ejes(visibleMallas = True, visibleEjes = True):
    auxScale = 0.005
    tamaño = 20
    if visibleEjes:
        mesh.cylinder(name="ejeX", radio=auxScale, scale=(1,1,50), translate=(0,0,-50), color=(1,0,0))
        mesh.cylinder(name="ejeY", radio=auxScale, rotate=(-90, 0,90,0), scale=(1,1,50), translate=(50,0,0), color=(0,1,0))
        mesh.cylinder(name="ejeZ", radio=auxScale, rotate=(-90, 90,0,0), altura=100, translate=(0,-50,0), color=(0,0,1))
    #Mall
    salto = 0
    auxScale = 0.0015
    if visibleMallas:
        for i in range(100):
            mesh.cube(name="ejeX"+str(i), scale=(tamaño,auxScale,auxScale), translate=(0,0,-10 +salto),color=(0.8,0,0))
            mesh.cube(name="ejeY"+str(i), scale=(auxScale,auxScale,tamaño), translate=(-10 +salto,0,0),color=(0,0,0.8))
            salto += .2

# ---------------------------------------------------------------------------
# 1) Agrega estos colores AL FINAL de tu diccionario COLORES (así los ids
#    anteriores no cambian):
#
#    "NARANJA":        (1.0, 0.5, 0.05),
#    "CAFE":           (0.35, 0.18, 0.08),
#    "BEIGE":          (0.95, 0.75, 0.55),
#    "AMARILLO_VERDE": (0.7, 0.85, 0.15),
#    "VERDE_OSCURO":   (0.08, 0.3, 0.15),
#    "JEANS":          (0.2, 0.45, 0.75),
#    "PAJA":           (0.85, 0.7, 0.3),
#    "MADERA":         (0.5, 0.3, 0.12),
#    "ROSA":           (1.0, 0.45, 0.55),
#
# 2) En main(), junto a glClearColor, usa el fondo naranja de la imagen:
#
#    glClearColor(1.0, 0.27, 0.0, 1.0)
#
# 3) Reemplaza tu función banca() por todo lo de abajo. drawing() no cambia.
# ---------------------------------------------------------------------------

# def sumar(a, b):  # Suma dos posiciones (x, y, z); sirve para mover un personaje completo.
#     return (a[0] + b[0], a[1] + b[1], a[2] + b[2])  # Regresa la nueva posición.

def drawEjemple():  # Dibuja la banca y llama al resto de la escena.
    # Ejemplos:
    # wire.cube(translate=(0,2,0))
    wire.dodecahedron(translate=(0,2,0))
    mesh.plane(scale=(4,1,4))

