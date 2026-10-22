# Liberias de apollo
import numpy as np

# Librerías gráficas
from OpenGL.GL import *  # Funciones principales de OpenGL (color, matrices, transformaciones).
from OpenGL.GLU import *  # Funciones de utilidad de OpenGL (perspectiva, cuádricas).
from OpenGL.GLUT import *  # Funciones de GLUT (ventana y figuras sólidas como glutSolidCube).


class mesh:
    @staticmethod  # Indica que la función no necesita "self"; se llama directo desde la clase.
    def cube(size=1.0, color=(0.5, 0.5, 0.5), translate=(0.0, 0.0, 0.0), rotate=(0, 0.0, 1.0, 0.0), scale=(1.0, 1.0, 1.0), name = "cube", visible = True):  # Dibuja un cubo; size = lado, color = (R,G,B), translate = (x,y,z), rotate = (ángulo,x,y,z), scale = (x,y,z), name = nombre, visible = si se dibuja.
        if not visible:  # Revisa si la figura está marcada como no visible.
            return  # Sale de la función sin dibujar nada.
        glColor3f(*color)  # Asigna el color; el * separa la tupla en 3 números (R, G, B).
        glPushMatrix()  # Guarda la posición, giro y escala actuales.
        glTranslatef(*translate)  # Mueve la figura a la posición (x, y, z).
        glRotatef(*rotate)  # Gira la figura: primer valor es el ángulo, los otros 3 son el eje.
        glScalef(*scale)  # Cambia el tamaño en x, y, z (permite estirar o aplastar la figura).
        glutSolidCube(size)  # Dibuja el cubo sólido con el lado indicado.
        glPopMatrix()  # Restaura lo guardado, para que no afecte a las demás figuras.
        print(name)  # Imprime el nombre de la figura en la terminal.
    
    @staticmethod  # La función se llama directo desde la clase, sin "self".
    def cylinder(radio=1.0, altura=2.0, slices=32, stacks=1, color=(0.5, 0.5, 0.5), translate=(0.0, 0.0, 0.0), rotate=(0, 0.0, 1.0, 0.0), scale=(1.0, 1.0, 1.0), name = "cylinder", visible = True):  # Dibuja un cilindro; radio = grosor, altura = largo, slices = lados, stacks = divisiones a lo largo.
        if not visible:  # Revisa si la figura está marcada como no visible.
            return  # Sale de la función sin dibujar nada.
        glColor3f(*color)  # Asigna el color (R, G, B).
        glPushMatrix()  # Guarda la posición, giro y escala actuales.
        glTranslatef(*translate)  # Mueve la figura a la posición (x, y, z).
        glRotatef(*rotate)  # Gira la figura: (ángulo, x, y, z).
        glScalef(*scale)  # Cambia el tamaño en x, y, z.
        glutSolidCylinder(radio, altura, slices, stacks)  # Dibuja el cilindro sólido con tapas (nace acostado sobre Z).
        glPopMatrix()  # Restaura lo guardado, para que no afecte a las demás figuras.
        print(name)  # Imprime el nombre de la figura en la terminal.

    @staticmethod  # La función se llama directo desde la clase, sin "self".
    def plane(ancho=1.0, largo=1.0, color=(0.5, 0.5, 0.5), translate=(0.0, 0.0, 0.0), rotate=(0, 0.0, 1.0, 0.0), scale=(1.0, 1.0, 1.0), name = "plane", visible = True):  # Dibuja un plano horizontal (como un piso); ancho = medida en X, largo = medida en Z.
        if not visible:  # Revisa si la figura está marcada como no visible.
            return  # Sale de la función sin dibujar nada.
        glColor3f(*color)  # Asigna el color (R, G, B).
        glPushMatrix()  # Guarda la posición, giro y escala actuales.
        glTranslatef(*translate)  # Mueve la figura a la posición (x, y, z).
        glRotatef(*rotate)  # Gira la figura: (ángulo, x, y, z).
        glScalef(*scale)  # Cambia el tamaño en x, y, z.
        glBegin(GL_QUADS)  # Empieza a dibujar un cuadrilátero con 4 vértices.
        glNormal3f(0.0, 1.0, 0.0)  # La cara mira hacia arriba (+Y); la luz lo necesita para iluminarla.
        glTexCoord2f(0.0, 0.0); glVertex3f(-ancho / 2, 0.0, -largo / 2)  # Esquina de atrás a la izquierda (con su coordenada de textura).
        glTexCoord2f(1.0, 0.0); glVertex3f( ancho / 2, 0.0, -largo / 2)  # Esquina de atrás a la derecha.
        glTexCoord2f(1.0, 1.0); glVertex3f( ancho / 2, 0.0,  largo / 2)  # Esquina de adelante a la derecha.
        glTexCoord2f(0.0, 1.0); glVertex3f(-ancho / 2, 0.0,  largo / 2)  # Esquina de adelante a la izquierda.
        glEnd()  # Termina el cuadrilátero.
        glPopMatrix()  # Restaura lo guardado, para que no afecte a las demás figuras.
        print(name)  # Imprime el nombre de la figura en la terminal.
    
    @staticmethod  # La función se llama directo desde la clase, sin "self".
    def teapot(size=1.0, color=(0.5, 0.5, 0.5), translate=(0.0, 0.0, 0.0), rotate=(0, 0.0, 1.0, 0.0), scale=(1.0, 1.0, 1.0), name = "teapot", visible = True):  # Dibuja una tetera; size = tamaño, y los demás parámetros son los mismos que en cube.
        if not visible:  # Revisa si la figura está marcada como no visible.
            return  # Sale de la función sin dibujar nada.
        glColor3f(*color)  # Asigna el color (R, G, B).
        glPushMatrix()  # Guarda la posición, giro y escala actuales.
        glTranslatef(*translate)  # Mueve la figura a la posición (x, y, z).
        glRotatef(*rotate)  # Gira la figura: (ángulo, x, y, z).
        glScalef(*scale)  # Cambia el tamaño en x, y, z.
        glutSolidTeapot(size)  # Dibuja la tetera sólida con el tamaño indicado.
        glPopMatrix()  # Restaura lo guardado, para que no afecte a las demás figuras.
        print(name)  # Imprime el nombre de la figura en la terminal.

    @staticmethod  # La función se llama directo desde la clase, sin "self".
    def sphere(radio=1.0, slices=32, stacks=32, color=(0.5, 0.5, 0.5), translate=(0.0, 0.0, 0.0), rotate=(0, 0.0, 1.0, 0.0), scale=(1.0, 1.0, 1.0), name = "sphere", visible = True):  # Dibuja una esfera; radio = tamaño, slices = divisiones verticales, stacks = divisiones horizontales (más = más redonda).
        if not visible:  # Revisa si la figura está marcada como no visible.
            return  # Sale de la función sin dibujar nada.
        glColor3f(*color)  # Asigna el color (R, G, B).
        glPushMatrix()  # Guarda la posición, giro y escala actuales.
        glTranslatef(*translate)  # Mueve la figura a la posición (x, y, z).
        glRotatef(*rotate)  # Gira la figura: (ángulo, x, y, z).
        glScalef(*scale)  # Cambia el tamaño en x, y, z.
        glutSolidSphere(radio, slices, stacks)  # Dibuja la esfera sólida con el radio y las divisiones indicadas.
        glPopMatrix()  # Restaura lo guardado, para que no afecte a las demás figuras.
        print(name)  # Imprime el nombre de la figura en la terminal.

    @staticmethod  # La función se llama directo desde la clase, sin "self".
    def cone(base=1.0, altura=2.0, slices=32, stacks=8, color=(0.5, 0.5, 0.5), translate=(0.0, 0.0, 0.0), rotate=(0, 0.0, 1.0, 0.0), scale=(1.0, 1.0, 1.0), name = "cone", visible = True):  # Dibuja un cono; base = radio de la base, altura = largo, slices = lados, stacks = divisiones a lo largo.
        if not visible:  # Revisa si la figura está marcada como no visible.
            return  # Sale de la función sin dibujar nada.
        glColor3f(*color)  # Asigna el color (R, G, B).
        glPushMatrix()  # Guarda la posición, giro y escala actuales.
        glTranslatef(*translate)  # Mueve la figura a la posición (x, y, z).
        glRotatef(*rotate)  # Gira la figura: (ángulo, x, y, z).
        glScalef(*scale)  # Cambia el tamaño en x, y, z.
        glutSolidCone(base, altura, slices, stacks)  # Dibuja el cono sólido (nace apuntando hacia +Z).
        glPopMatrix()  # Restaura lo guardado, para que no afecte a las demás figuras.
        print(name)  # Imprime el nombre de la figura en la terminal.

    @staticmethod  # La función se llama directo desde la clase, sin "self".
    def torus(radio_interior=0.3, radio_exterior=1.0, lados=24, anillos=48, color=(0.5, 0.5, 0.5), translate=(0.0, 0.0, 0.0), rotate=(0, 0.0, 1.0, 0.0), scale=(1.0, 1.0, 1.0), name = "torus", visible = True):  # Dibuja un toro (dona); radio_interior = grosor del tubo, radio_exterior = distancia del centro al tubo, lados = divisiones del tubo, anillos = divisiones de la vuelta completa.
        if not visible:  # Revisa si la figura está marcada como no visible.
            return  # Sale de la función sin dibujar nada.
        glColor3f(*color)  # Asigna el color (R, G, B).
        glPushMatrix()  # Guarda la posición, giro y escala actuales.
        glTranslatef(*translate)  # Mueve la figura a la posición (x, y, z).
        glRotatef(*rotate)  # Gira la figura: (ángulo, x, y, z).
        glScalef(*scale)  # Cambia el tamaño en x, y, z.
        glutSolidTorus(radio_interior, radio_exterior, lados, anillos)  # Dibuja el toro sólido con los radios y divisiones indicados.
        glPopMatrix()  # Restaura lo guardado, para que no afecte a las demás figuras.
        print(name)  # Imprime el nombre de la figura en la terminal.

    @staticmethod  # La función se llama directo desde la clase, sin "self".
    def tetrahedron(color=(0.5, 0.5, 0.5), translate=(0.0, 0.0, 0.0), rotate=(0, 0.0, 1.0, 0.0), scale=(1.0, 1.0, 1.0), name = "tetrahedron", visible = True):  # Dibuja un tetraedro (4 caras); no recibe tamaño, se cambia con scale.
        if not visible:  # Revisa si la figura está marcada como no visible.
            return  # Sale de la función sin dibujar nada.
        glColor3f(*color)  # Asigna el color (R, G, B).
        glPushMatrix()  # Guarda la posición, giro y escala actuales.
        glTranslatef(*translate)  # Mueve la figura a la posición (x, y, z).
        glRotatef(*rotate)  # Gira la figura: (ángulo, x, y, z).
        glScalef(*scale)  # Cambia el tamaño en x, y, z.
        glutSolidTetrahedron()  # Dibuja el tetraedro sólido (tamaño fijo).
        glPopMatrix()  # Restaura lo guardado, para que no afecte a las demás figuras.
        print(name)  # Imprime el nombre de la figura en la terminal.

    @staticmethod  # La función se llama directo desde la clase, sin "self".
    def octahedron(color=(0.5, 0.5, 0.5), translate=(0.0, 0.0, 0.0), rotate=(0, 0.0, 1.0, 0.0), scale=(1.0, 1.0, 1.0), name = "octahedron", visible = True):  # Dibuja un octaedro (8 caras); no recibe tamaño, se cambia con scale.
        if not visible:  # Revisa si la figura está marcada como no visible.
            return  # Sale de la función sin dibujar nada.
        glColor3f(*color)  # Asigna el color (R, G, B).
        glPushMatrix()  # Guarda la posición, giro y escala actuales.
        glTranslatef(*translate)  # Mueve la figura a la posición (x, y, z).
        glRotatef(*rotate)  # Gira la figura: (ángulo, x, y, z).
        glScalef(*scale)  # Cambia el tamaño en x, y, z.
        glutSolidOctahedron()  # Dibuja el octaedro sólido (tamaño fijo).
        glPopMatrix()  # Restaura lo guardado, para que no afecte a las demás figuras.
        print(name)  # Imprime el nombre de la figura en la terminal.

    @staticmethod  # La función se llama directo desde la clase, sin "self".
    def dodecahedron(color=(0.5, 0.5, 0.5), translate=(0.0, 0.0, 0.0), rotate=(0, 0.0, 1.0, 0.0), scale=(1.0, 1.0, 1.0), name = "dodecahedron", visible = True):  # Dibuja un dodecaedro (12 caras); no recibe tamaño, se cambia con scale.
        if not visible:  # Revisa si la figura está marcada como no visible.
            return  # Sale de la función sin dibujar nada.
        glColor3f(*color)  # Asigna el color (R, G, B).
        glPushMatrix()  # Guarda la posición, giro y escala actuales.
        glTranslatef(*translate)  # Mueve la figura a la posición (x, y, z).
        glRotatef(*rotate)  # Gira la figura: (ángulo, x, y, z).
        glScalef(*scale)  # Cambia el tamaño en x, y, z.
        glutSolidDodecahedron()  # Dibuja el dodecaedro sólido (tamaño fijo).
        glPopMatrix()  # Restaura lo guardado, para que no afecte a las demás figuras.
        print(name)  # Imprime el nombre de la figura en la terminal.

    @staticmethod  # La función se llama directo desde la clase, sin "self".
    def icosahedron(color=(0.5, 0.5, 0.5), translate=(0.0, 0.0, 0.0), rotate=(0, 0.0, 1.0, 0.0), scale=(1.0, 1.0, 1.0), name = "icosahedron", visible = True):  # Dibuja un icosaedro (20 caras); no recibe tamaño, se cambia con scale.
        if not visible:  # Revisa si la figura está marcada como no visible.
            return  # Sale de la función sin dibujar nada.
        glColor3f(*color)  # Asigna el color (R, G, B).
        glPushMatrix()  # Guarda la posición, giro y escala actuales.
        glTranslatef(*translate)  # Mueve la figura a la posición (x, y, z).
        glRotatef(*rotate)  # Gira la figura: (ángulo, x, y, z).
        glScalef(*scale)  # Cambia el tamaño en x, y, z.
        glutSolidIcosahedron()  # Dibuja el icosaedro sólido (tamaño fijo).
        glPopMatrix()  # Restaura lo guardado, para que no afecte a las demás figuras.
        print(name)  # Imprime el nombre de la figura en la terminal.



# # Cada cara: (normal, 4 vértices en sentido contrario a las manecillas, visto desde afuera)
# _CARAS = [
#     (( 0, 0, 1), [(-.2,-.5, .2), ( .2,-.5, .2), ( .5, .5, .5), (-.5, .5, .5)]),  # Frente.
#     (( 0, 0,-1), [( .2,-.5,-.2), (-.2,-.5,-.2), (-.5, .5,-.5), ( .5, .5,-.5)]),  # Atrás.
#     (( 1, 0, 0), [( .2,-.5, .2), ( .2,-.5,-.2), ( .5, .5,-.5), ( .5, .5, .5)]),  # Derecha.
#     ((-1, 0, 0), [(-.2,-.5,-.2), (-.2,-.5, .2), (-.5, .5, .5), (-.5, .5,-.5)]),  # Izquierda.
#     (( 0, 1, 0), [(-.5, .5, .5), ( .5, .5, .5), ( .5, .5,-.5), (-.5, .5,-.5)]),  # Arriba.
#     (( 0,-1, 0), [(-.2,-.5,-.2), ( .2,-.5,-.2), ( .2,-.5, .2), (-.2,-.5, .2)]),  # Abajo.
# ]

# # Se crean UNA sola vez, al cargar el archivo.
# VERTICES = np.array([v for _, vs in _CARAS for v in vs], dtype=np.float32)       # 24 vértices (x, y, z).
# NORMALES = np.array([n for n, _ in _CARAS for _ in range(4)], dtype=np.float32)  # 1 normal por vértice.
# INDICES  = np.arange(24, dtype=np.uint32)

# class meshArray:

#     @staticmethod
#     def cube_array(size=1.0, color=(0.5, 0.5, 0.5), translate=(0.0, 0.0, 0.0), rotate=(0, 0.0, 1.0, 0.0), scale=(1.0, 1.0, 1.0)):
#         glColor3f(*color)  # Asigna el color.
#         glPushMatrix()  # Guarda la posición, giro y escala actuales.
#         glTranslatef(*translate)  # Mueve la figura.
#         glRotatef(*rotate)  # Gira la figura.
#         glScalef(size * scale[0], size * scale[1], size * scale[2])  # Tamaño y escala juntos.

#         glEnableClientState(GL_VERTEX_ARRAY)  # Avisa que los vértices vienen de un arreglo.
#         glEnableClientState(GL_NORMAL_ARRAY)  # Avisa que las normales vienen de un arreglo.
#         glVertexPointer(3, GL_FLOAT, 0, VERTICES)  # Apunta al arreglo de vértices (3 números cada uno).
#         glNormalPointer(GL_FLOAT, 0, NORMALES)  # Apunta al arreglo de normales.
#         glDrawElements(GL_QUADS, INDICES.size, GL_UNSIGNED_INT, INDICES)  # Dibuja todo el cubo en una sola llamada.
#         glDisableClientState(GL_NORMAL_ARRAY)  # Apaga el arreglo de normales.
#         glDisableClientState(GL_VERTEX_ARRAY)  # Apaga el arreglo de vértices.

#         glPopMatrix()  # Restaura lo guardado.



class light:
    @staticmethod  # Se llama directo desde la clase: light.sun(...).
    def sun(color=(1.0, 0.95, 0.8), ambient=(0.25, 0.25, 0.30), direction=(1.0, 2.0, 1.5), visible=True):  # color = luz directa (R,G,B), ambient = luz base (R,G,B), direction = hacia dónde está el sol (x,y,z), visible = enciende o apaga el sol.
        if not visible:  # Revisa si el sol está apagado.
            glDisable(GL_LIGHTING)  # Apaga todo el sistema de iluminación.
            return  # Sale sin configurar nada más.
        glEnable(GL_LIGHTING)  # Activa el sistema de iluminación.
        glEnable(GL_LIGHT0)  # Enciende la luz número 0.
        glEnable(GL_COLOR_MATERIAL)  # Hace que glColor3f siga funcionando con luz.
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)  # El color de glColor3f se usa como color del material.
        glEnable(GL_NORMALIZE)  # Corrige las normales cuando usas glScalef.
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (*color, 1.0))  # Luz directa; el 1.0 es la opacidad.
        glLightfv(GL_LIGHT0, GL_AMBIENT, (*ambient, 1.0))  # Luz base: evita caras totalmente negras.
        glLightfv(GL_LIGHT0, GL_POSITION, (*direction, 0.0))  # Dirección del sol; el 0.0 final lo hace direccional.