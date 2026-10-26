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

def LLAMA(translate=(0.0, 0.0, 0.0), rotate=(0, 0.0, 1.0, 0.0), scale=(1.0, 1.0, 1.0), name="animal", visible=True):
    if not visible:
        return

    glPushMatrix()
    glTranslatef(*translate)
    glRotatef(*rotate)
    glScalef(*scale)

    # CUERPO 
    mesh.sphere(color=paleta("PAJA"), translate=(0.0, 1.95, 0.0), scale=(1.30, 0.62, 0.55), name="Torso")
    mesh.sphere(color=paleta("PAJA"), translate=(-0.85, 2.0, 0.0), scale=(0.62, 0.62, 0.52), name="Pecho")
    mesh.sphere(color=paleta("PAJA"), translate=(0.85, 2.0, 0.0), scale=(0.65, 0.66, 0.56), name="Anca")
    mesh.sphere(color=paleta("BEIGE"), translate=(0.0, 1.55, 0.0), scale=(1.00, 0.35, 0.45), name="Panza")

    # COLA
    mesh.sphere(color=paleta("NEGRO"), translate=(1.50, 2.25, 0.0), scale=(0.14, 0.22, 0.12), name="Cola")

    # PATA DELANTERA IZQUIERDA
    mesh.sphere(color=paleta("NARANJA"), translate=(-0.7, 1.8, -0.45), rotate=(5,1,0,0), scale=(0.32, 0.55, 0.26), name="DI Hombro") 
    mesh.cone(color=paleta("AZUL"), translate=(-0.7, 1.3, -0.5), rotate=(90,1,0,0), scale=(0.24, 0.21, 0.40), name="DI Tubo 1")
    mesh.sphere(color=paleta("BEIGE"), translate=(-0.7, 1.40, -0.5), scale=(0.26, 0.46, 0.22), name="DI Rodilla")
    mesh.cone(color=paleta("AZUL"), translate=(-0.7, 0.75, -0.5), rotate=(90,1,0,0), scale=(0.14, 0.14, 0.50), name="DI Tubo 2")
    mesh.sphere(color=paleta("BEIGE"), translate=(-0.7, 0.75, -0.5), scale=(0.15, 0.15, 0.15), name="DI Tobillo")
    mesh.sphere(color=paleta("MADERA"), translate=(-0.7, 0.1, -0.5), scale=(0.18, 0.12, 0.20), name="DI Pie Esferico")

    # PATA DELANTERA DERECHA
    mesh.sphere(color=paleta("NARANJA"), translate=(-0.7, 1.8, 0.45), rotate=(-5,1,0,0), scale=(0.32, 0.55, 0.26), name="DD Hombro")
    mesh.cone(color=paleta("AZUL"), translate=(-0.7, 1.3, 0.5), rotate=(90,1,0,0), scale=(0.24, 0.21, 0.40), name="DD Tubo 1")
    mesh.sphere(color=paleta("BEIGE"), translate=(-0.7, 1.40, 0.5), scale=(0.26, 0.46, 0.22), name="DD Rodilla")
    mesh.cone(color=paleta("AZUL"), translate=(-0.7, 0.77, 0.5), rotate=(90,1,0,0), scale=(0.14, 0.14, 0.50), name="DD Tubo 2")
    mesh.sphere(color=paleta("BEIGE"), translate=(-0.7, 0.75, 0.5), scale=(0.15, 0.15, 0.15), name="DD Tobillo")
    mesh.sphere(color=paleta("MADERA"), translate=(-0.7, 0.1, 0.5), scale=(0.18, 0.12, 0.20), name="DD Pie Esferico")

    # PATA TRASERA IZQUIERDA
    mesh.sphere(color=paleta("NARANJA"), translate=(0.9, 1.8, 0.35), rotate=(345,0,0,1), scale=(0.42, 0.75, 0.28), name="TI Muslo Esponjoso")
    mesh.cone(color=paleta("AZUL"), translate=(0.9, 1.3, 0.35), rotate=(90,1,0,0), scale=(0.38, 0.23, 0.40), name="TI Tubo 1")
    mesh.sphere(color=paleta("BEIGE"), translate=(0.9, 1.40, 0.35), scale=(0.40, 0.40, 0.24), name="TI Rodilla")
    mesh.cone(color=paleta("AZUL"), translate=(0.9, 0.60, 0.35), rotate=(90,1,0,0), scale=(0.15, 0.10, 0.30), name="TI Tubo 2")
    mesh.sphere(color=paleta("BEIGE"), translate=(0.9, 0.65, 0.35), scale=(0.15, 0.15, 0.10), name="TI Tobillo")
    mesh.sphere(color=paleta("MADERA"), translate=(0.9, 0.1, 0.35), scale=(0.18, 0.12, 0.20), name="TI Pie Esferico")

    # PATA TRASERA DERECHA
    mesh.sphere(color=paleta("NARANJA"), translate=(0.9, 1.8, -0.35), rotate=(345,0,0,1), scale=(0.42, 0.75, 0.28), name="TD Muslo Esponjoso")
    mesh.cone(color=paleta("AZUL"), translate=(0.9, 1.3, -0.35), rotate=(90,1,0,0), scale=(0.38, 0.23, 0.40), name="TD Tubo 1")
    mesh.sphere(color=paleta("BEIGE"), translate=(0.9, 1.40, -0.35), scale=(0.40, 0.40, 0.24), name="TD Rodilla")
    mesh.cone(color=paleta("AZUL"), translate=(0.9, 0.60, -0.35), rotate=(90,1,0,0), scale=(0.15, 0.10, 0.30), name="TD Tubo 2")
    mesh.sphere(color=paleta("BEIGE"), translate=(0.9, 0.65, -0.35), scale=(0.15, 0.15, 0.10), name="TD Tobillo")
    mesh.sphere(color=paleta("MADERA"), translate=(0.9, 0.1, -0.35), scale=(0.18, 0.12, 0.20), name="TD Pie Esferico")
    glPopMatrix()

def month(): #Mesa
    meshQuad.tube(name="Mesa", radio_base=.8, radio_tope=1, altura=.2,rotate=convert.degrees(-90,0,0), translate=(-3.5, 1.3, 0), tapas=True, color=paleta("MADERA"))
    meshQuad.tube(name="Soporte", radio_base=.1, radio_tope=.3, altura=1.3, rotate=convert.degrees(-90,0,0), translate=(-3.5,0,0), color=paleta("MADERA"))
    #Tason
    meshQuad.tube(name="Tazon", radio_base=0.4, radio_tope=.7, altura=0.2, rotate=convert.degrees(-90,0,0),translate=(-3.3, 1.5, 0), color=paleta("BLANCO"))
    meshQuad.disk(name="Agua", radio_exterior=.6, rotate=convert.degrees(-90,0,0),translate=(-3.3, 1.65,0), color=paleta("AZUL"))

def drawingScene():
    light.sun()
    #   Sistemas generales
    sysScene.ejes(visibleMallas=True, visibleEjes=True)
    #   Aqui se dibuja todo lo que no se va animar 
    mesh.plane(scale=(20,1,10),color=paleta("VERDE"))
    LLAMA()
    month()
    #   Animación: dibuja el fotograma que toca en este momento
    lineasGuia()
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

def drawEjemple():
    cantidad = 10   # Número de segmentos.
    largo = 0.3     # Largo de cada segmento (todos iguales).
    giro = 10       # Grados que se dobla cada segmento (negativo hacia abajo, ver abajo).
    x, y = 0.0, 1.0  # Punto donde empieza la tela.
    for i in range(cantidad):
        a = -giro * i  # Ángulo de este segmento (el signo menos la curva hacia abajo).
        dx = largo * math.cos(math.radians(a))  # Cuánto avanza en X.
        dy = largo * math.sin(math.radians(a))  # Cuánto avanza en Y.
        mesh.plane(name="Tela " + str(i), ancho=largo, largo=2.0, rotate=convert.degrees(0, 0, a), translate=(x + dx / 2, y + dy / 2, 0))  # Se coloca en el punto medio del segmento.
        mesh.plane(name="Tela " + str(i), ancho=largo, largo=2.0, rotate=convert.degrees(0, 0, a * -1), translate=((x + dx / 2) *-1, y + dy / 2, 0))  # Se coloca en el punto medio del segmento.
        x += dx  # El siguiente empieza donde termina este.
        y += dy


 
class fotogramas:
    # Animación: el cuello sigue a la cabeza con una ligera curva y la cabeza baja con el hocico a 45°. f0 = inicio, f12 = final.
    def f0():
        #Cuello
        cuello0(translate=(-0.0, 0.0, 0.0), rotate=(-0.0, 0.0, 0.0))
        cuello1(translate=(-0.0, 0.0, 0.0), rotate=(-0.0, 0.0, 0.0))
        cuello2(translate=(-0.0, 0.0, 0.0), rotate=(-0.0, 0.0, 0.0))
        cuello3(translate=(-0.0, 0.0, 0.0), rotate=(-0.0, 0.0, 0.0))
        #Cabeza
        cabeza()
    def f1():  # 1/12 del recorrido
        #Cuello
        cuello0(translate=(-0.028, -0.01, 0.0), rotate=(0.0, 0.0, 5.605))
        cuello1(translate=(-0.058, -0.049, 0.0), rotate=(0.0, 0.0, 7.101))
        cuello2(translate=(-0.104, -0.093, 0.0), rotate=(0.0, 0.0, 8.193))
        cuello3(translate=(-0.146, -0.135, 0.0), rotate=(0.0, 0.0, 2.991))
        #Cabeza
        cabeza(translate=(-0.123, -0.152, 0.0), hocico=3.75)
    def f2():  # 2/12 del recorrido
        #Cuello
        cuello0(translate=(-0.055, -0.02, 0.0), rotate=(0.0, 0.0, 9.626))
        cuello1(translate=(-0.104, -0.09, 0.0), rotate=(0.0, 0.0, 11.968))
        cuello2(translate=(-0.171, -0.168, 0.0), rotate=(0.0, 0.0, 13.899))
        cuello3(translate=(-0.238, -0.246, 0.0), rotate=(0.0, 0.0, 9.499))
        #Cabeza
        cabeza(translate=(-0.245, -0.303, 0.0), hocico=7.5)
    def f3():  # 3/12 del recorrido
        #Cuello
        cuello0(translate=(-0.082, -0.03, 0.0), rotate=(0.0, 0.0, 14.231))
        cuello1(translate=(-0.151, -0.131, 0.0), rotate=(0.0, 0.0, 17.419))
        cuello2(translate=(-0.24, -0.242, 0.0), rotate=(0.0, 0.0, 20.19))
        cuello3(translate=(-0.332, -0.356, 0.0), rotate=(0.0, 0.0, 16.591))
        #Cabeza
        cabeza(translate=(-0.367, -0.455, 0.0), hocico=11.25)
    def f4():  # 4/12 del recorrido
        #Cuello
        cuello0(translate=(-0.11, -0.04, 0.0), rotate=(0.0, 0.0, 19.341))
        cuello1(translate=(-0.199, -0.17, 0.0), rotate=(0.0, 0.0, 23.375))
        cuello2(translate=(-0.312, -0.315, 0.0), rotate=(0.0, 0.0, 26.986))
        cuello3(translate=(-0.428, -0.465, 0.0), rotate=(0.0, 0.0, 24.189))
        #Cabeza
        cabeza(translate=(-0.49, -0.607, 0.0), hocico=15.0)
    def f5():  # 5/12 del recorrido
        #Cuello
        cuello0(translate=(-0.137, -0.05, 0.0), rotate=(0.0, 0.0, 24.814))
        cuello1(translate=(-0.249, -0.208, 0.0), rotate=(0.0, 0.0, 29.694))
        cuello2(translate=(-0.385, -0.386, 0.0), rotate=(0.0, 0.0, 34.145))
        cuello3(translate=(-0.525, -0.573, 0.0), rotate=(0.0, 0.0, 32.149))
        #Cabeza
        cabeza(translate=(-0.613, -0.758, 0.0), hocico=18.75)
    def f6():  # 6/12 del recorrido
        #Cuello
        cuello0(translate=(-0.165, -0.06, 0.0), rotate=(0.0, 0.0, 30.444))
        cuello1(translate=(-0.3, -0.245, 0.0), rotate=(0.0, 0.0, 36.17))
        cuello2(translate=(-0.461, -0.456, 0.0), rotate=(0.0, 0.0, 41.461))
        cuello3(translate=(-0.624, -0.679, 0.0), rotate=(0.0, 0.0, 40.267))
        #Cabeza
        cabeza(translate=(-0.735, -0.91, 0.0), hocico=22.5)
    def f7():  # 7/12 del recorrido
        #Cuello
        cuello0(translate=(-0.192, -0.07, 0.0), rotate=(0.0, 0.0, 36.002))
        cuello1(translate=(-0.353, -0.281, 0.0), rotate=(0.0, 0.0, 42.574))
        cuello2(translate=(-0.539, -0.525, 0.0), rotate=(0.0, 0.0, 48.704))
        cuello3(translate=(-0.724, -0.785, 0.0), rotate=(0.0, 0.0, 48.311))
        #Cabeza
        cabeza(translate=(-0.858, -1.062, 0.0), hocico=26.25)
    def f8():  # 8/12 del recorrido
        #Cuello
        cuello0(translate=(-0.22, -0.08, 0.0), rotate=(0.0, 0.0, 41.268))
        cuello1(translate=(-0.407, -0.316, 0.0), rotate=(0.0, 0.0, 48.685))
        cuello2(translate=(-0.618, -0.592, 0.0), rotate=(0.0, 0.0, 55.656))
        cuello3(translate=(-0.826, -0.89, 0.0), rotate=(0.0, 0.0, 56.065))
        #Cabeza
        cabeza(translate=(-0.98, -1.213, 0.0), hocico=30.0)
    def f9():  # 9/12 del recorrido
        #Cuello
        cuello0(translate=(-0.247, -0.09, 0.0), rotate=(0.0, 0.0, 46.073))
        cuello1(translate=(-0.462, -0.35, 0.0), rotate=(0.0, 0.0, 54.337))
        cuello2(translate=(-0.7, -0.657, 0.0), rotate=(0.0, 0.0, 62.147))
        cuello3(translate=(-0.93, -0.993, 0.0), rotate=(0.0, 0.0, 63.357))
        #Cabeza
        cabeza(translate=(-1.102, -1.365, 0.0), hocico=33.75)
    def f10():  # 10/12 del recorrido
        #Cuello
        cuello0(translate=(-0.275, -0.1, 0.0), rotate=(0.0, 0.0, 50.316))
        cuello1(translate=(-0.519, -0.382, 0.0), rotate=(0.0, 0.0, 59.426))
        cuello2(translate=(-0.784, -0.721, 0.0), rotate=(0.0, 0.0, 68.076))
        cuello3(translate=(-1.036, -1.096, 0.0), rotate=(0.0, 0.0, 70.088))
        #Cabeza
        cabeza(translate=(-1.225, -1.517, 0.0), hocico=37.5)
    def f11():  # 11/12 del recorrido
        #Cuello
        cuello0(translate=(-0.303, -0.11, 0.0), rotate=(0.0, 0.0, 53.958))
        cuello1(translate=(-0.578, -0.414, 0.0), rotate=(0.0, 0.0, 63.914))
        cuello2(translate=(-0.87, -0.784, 0.0), rotate=(0.0, 0.0, 73.404))
        cuello3(translate=(-1.143, -1.198, 0.0), rotate=(0.0, 0.0, 76.217))
        #Cabeza
        cabeza(translate=(-1.347, -1.668, 0.0), hocico=41.25)
    def f12():  # Final
        #Cuello
        cuello0(translate=(-0.33, -0.12, 0.0), rotate=(0.0, 0.0, 57.009))
        cuello1(translate=(-0.637, -0.444, 0.0), rotate=(0.0, 0.0, 67.81))
        cuello2(translate=(-0.958, -0.845, 0.0), rotate=(0.0, 0.0, 78.141))
        cuello3(translate=(-1.253, -1.299, 0.0), rotate=(0.0, 0.0, 81.755))
        #Cabeza
        cabeza(translate=(-1.47, -1.82, 0.0), hocico=45.0)
 




def cuello0(rotate=(0, 0, 0), translate=(0, 0, 0)):  # Ambos en orden (x, arriba, fondo).
    mesh.sphere(color=paleta("BEIGE"), translate=(-1.15 + translate[0], 2.40 + translate[1], 0.0 + translate[2]), rotate=convert.degrees(*rotate), scale=(0.42, 0.45, 0.36), name="Cuello 1")

def cuello1(rotate=(0, 0, 0), translate=(0, 0, 0)):
    mesh.sphere(color=paleta("BEIGE"), translate=(-1.28 + translate[0], 2.80 + translate[1], 0.0 + translate[2]), rotate=convert.degrees(*rotate), scale=(0.36, 0.42, 0.31), name="Cuello 2")

def cuello2(rotate=(0, 0, 0), translate=(0, 0, 0)):
    mesh.sphere(color=paleta("BEIGE"), translate=(-1.40 + translate[0], 3.20 + translate[1], 0.0 + translate[2]), rotate=convert.degrees(*rotate), scale=(0.31, 0.42, 0.27), name="Cuello 3")

def cuello3(rotate=(0, 0, 0), translate=(0, 0, 0)):
    mesh.sphere(color=paleta("BEIGE"), translate=(-1.52 + translate[0], 3.58 + translate[1], 0.0 + translate[2]), rotate=convert.degrees(*rotate), scale=(0.27, 0.40, 0.24), name="Cuello 4")

def cabeza(rotate=(0,0,0), translate=(0,0,0), hocico=0):  # hocico = grados que baja el hocico (0 = recto, 45 = mirando abajo). Toda la cabeza (ojos y orejas) gira con él.
    a = math.radians(hocico)  # Ángulo en radianes.
    def girar(dx, dy):  # Gira un punto (relativo al centro de la cabeza) alrededor del centro de la cabeza.
        return (dx * math.cos(a) - dy * math.sin(a), dx * math.sin(a) + dy * math.cos(a))  # Posición ya girada.
    cx, cy, cz = -1.72 + translate[0], 3.95 + translate[1], 0.0 + translate[2]  # Centro de la cabeza.
    def parte(dx, dy, dz):  # Posición final de una parte, a partir de cuánto se separa del centro de la cabeza.
        gx, gy = girar(dx, dy)  # La separa girada junto con la cabeza.
        return (cx + gx, cy + gy, cz + dz)  # Suma el centro de la cabeza.
    giro = convert.degrees(0, 0, hocico)  # Giro de la cabeza (en Z).
    giro_oreja = convert.degrees(270, 0, hocico)  # Oreja: su giro propio (270 en X) y luego el de la cabeza.
    # CABEZA
    mesh.sphere(color=paleta("CAFE"),   translate=(cx, cy, cz),        rotate=giro,       scale=(0.34, 0.26, 0.22), name="Cabeza")
    mesh.sphere(color=paleta("BEIGE"),  translate=parte(-0.30, -0.10, 0.0),  rotate=giro, scale=(0.20, 0.15, 0.16), name="Hocico")
    mesh.sphere(color=paleta("NEGRO"),  translate=parte(-0.48, -0.07, 0.0),  rotate=giro, scale=(0.05, 0.05, 0.07), name="Nariz")
    mesh.sphere(color=paleta("NEGRO"),  translate=parte(-0.18, 0.10, 0.17),  scale=(0.045, 0.045, 0.045), name="Ojo izq")
    mesh.sphere(color=paleta("NEGRO"),  translate=parte(-0.18, 0.10, -0.17), scale=(0.045, 0.045, 0.045), name="Ojo der")
    mesh.cone(color=paleta("CAFE"),     translate=parte(0.14, 0.17, 0.13),   rotate=giro_oreja, scale=(0.07, 0.05, 0.34), name="Oreja izq")
    mesh.cone(color=paleta("CAFE"),     translate=parte(0.14, 0.17, -0.13),  rotate=giro_oreja, scale=(0.07, 0.05, 0.34), name="Oreja der")



def lineasGuia():
    #Guias
    mesh.cube(scale=(5, 0.02, 0.02), rotate=convert.degrees(0, 0, 55), translate=(-2.8, 3, 0), color=paleta("AZUL"))
    #Fotograma
    mesh.cube(scale=(5, 0.1, 0.01), translate=(-3, 5, 0))
    mesh.cube(scale=(0.1, 0.5, 0.02), translate=(-0.5, 5, 0), color=paleta("ROJO"))
    mesh.cube(scale=(0.1, 0.5, 0.02), translate=(-1, 5, 0), color=paleta("ROJO"))
    mesh.cube(scale=(0.1, 0.5, 0.02), translate=(-1.5, 5, 0), color=paleta("ROJO"))
    mesh.cube(scale=(0.1, 0.5, 0.02), translate=(-2.5, 5, 0), color=paleta("ROJO"))
    mesh.cube(scale=(0.1, 0.5, 0.02), translate=(-3.5, 5, 0), color=paleta("ROJO"))
    mesh.cube(scale=(0.1, 0.5, 0.02), translate=(-4.5, 5, 0), color=paleta("ROJO"))
    mesh.cube(scale=(0.1, 0.5, 0.02), translate=(-5, 5, 0), color=paleta("ROJO"))
    mesh.cube(scale=(0.1, 0.5, 0.02), translate=(-5.5, 5, 0), color=paleta("ROJO"))