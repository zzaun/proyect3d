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
nFotograma = 0
def drawingScene():
    #   Informacion:
    global nFotograma
    print("--FOTOGRAMA: [" + str(nFotograma) + "]")
    nFotograma += 1
    #   Sistemas generales
    light.sun()
    sysScene.ejes(visibleMallas=True, visibleEjes=True)
    #   Aqui se dibuja todo lo que no se va animar
    #   Aqui se dibuja los fotogramas
    

def backgraungScene():
    # Aqui se dibuja todo lo que no se va a
    pass




def drawEjemple():  # Dibuja la banca y llama al resto de la escena.
    # Ejemplos:
    # wire.cube(translate=(0,2,0))
    wire.dodecahedron(translate=(0,2,0))
    mesh.plane(scale=(4,1,4))
