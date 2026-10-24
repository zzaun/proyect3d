# Liberias de apollo
import numpy as np
import math  # Para seno, coseno y conversiones de ángulos.
import pygame  # Librería para el audio.

# Librerías gráficas
from OpenGL.GL import *  # Funciones principales de OpenGL (color, matrices, transformaciones).
from OpenGL.GLU import *  # Funciones de utilidad de OpenGL (perspectiva, cuádricas).
from OpenGL.GLUT import *  # Funciones de GLUT (ventana y figuras sólidas como glutSolidCube).

# Paleta de colores para el sismtea interno:


#   Mallas solidas
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

#   Mallas pero solo las aristas
class meshWire:
    @staticmethod
    def cube(size=1.0, color=(0.5, 0.5, 0.5), translate=(0.0, 0.0, 0.0), rotate=(0, 0.0, 1.0, 0.0), scale=(1.0, 1.0, 1.0), name = "cube", visible = True):
        if not visible:  # Revisa si la figura está marcada como no visible.
            return  # Sale de la función sin dibujar nada.
        glColor3f(*color)  # Asigna el color; el * separa la tupla en 3 números (R, G, B).
        glPushMatrix()  # Guarda la posición, giro y escala actuales.
        glTranslatef(*translate)  # Mueve la figura a la posición (x, y, z).
        glRotatef(*rotate)  # Gira la figura: primer valor es el ángulo, los otros 3 son el eje.
        glScalef(*scale)  # Cambia el tamaño en x, y, z (permite estirar o aplastar la figura).
        glutWireCube(size)  # Dibuja el cubo sólido con el lado indicado.
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
        glutWireCylinder(radio, altura, slices, stacks)  # Dibuja el cilindro sólido con tapas (nace acostado sobre Z).
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
        glutWireTeapot(size)  # Dibuja la tetera sólida con el tamaño indicado.
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
        glutWireSphere(radio, slices, stacks)  # Dibuja la esfera sólida con el radio y las divisiones indicadas.
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
        glutWireCone(base, altura, slices, stacks)  # Dibuja el cono sólido (nace apuntando hacia +Z).
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
        glutWireTorus(radio_interior, radio_exterior, lados, anillos)  # Dibuja el toro sólido con los radios y divisiones indicados.
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
        glutWireTetrahedron()  # Dibuja el tetraedro sólido (tamaño fijo).
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
        glutWireOctahedron()  # Dibuja el octaedro sólido (tamaño fijo).
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
        glutWireDodecahedron()  # Dibuja el dodecaedro sólido (tamaño fijo).
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
        glutWireIcosahedron()  # Dibuja el icosaedro sólido (tamaño fijo).
        glPopMatrix()  # Restaura lo guardado, para que no afecte a las demás figuras.
        print(name)  # Imprime el nombre de la figura en la terminal.

#   MALLAS PERSONALIZADAS MAS O MENOS
_quad = None  # Objeto de GLU que dibuja las figuras; se crea la primera vez que se necesita.
 
# Traducción de los textos que usa la clase a las constantes de GLU.
_ESTILOS = {"solido": GLU_FILL, "alambre": GLU_LINE, "puntos": GLU_POINT, "silueta": GLU_SILHOUETTE}  # Cómo se dibuja la malla.
_NORMALES = {"suaves": GLU_SMOOTH, "planas": GLU_FLAT}  # Suaves = figura lisa, planas = aspecto facetado.
 
def _preparar(estilo, normales, textura, adentro):  # Configura el objeto de GLU antes de dibujar.
    global _quad  # Permite guardar el objeto en la variable de arriba.
    if _quad is None:  # Si todavía no existe el objeto de GLU.
        _quad = gluNewQuadric()  # Lo crea (una sola vez).
    gluQuadricDrawStyle(_quad, _ESTILOS.get(estilo, GLU_FILL))  # Sólido, alambre, puntos o silueta.
    gluQuadricNormals(_quad, _NORMALES.get(normales, GLU_SMOOTH))  # Normales suaves o planas (para la luz).
    gluQuadricTexture(_quad, GL_TRUE if textura else GL_FALSE)  # Genera (o no) coordenadas de textura.
    gluQuadricOrientation(_quad, GLU_INSIDE if adentro else GLU_OUTSIDE)  # Normales hacia adentro o hacia afuera.

class meshQuad:  # Figuras redondeadas de GLU; se usan sin crear un objeto (meshQuad.tube(...)).
    @staticmethod  # La función se llama directo desde la clase, sin "self".
    def tube(radio_base=0.25, radio_tope=0.15, altura=1.0, slices=16, stacks=4, tapas=False, color=(0.5, 0.5, 0.5), translate=(0.0, 0.0, 0.0), rotate=(0, 0.0, 1.0, 0.0), scale=(1.0, 1.0, 1.0), name="tube", visible=True, estilo="solido", normales="suaves", textura=False, adentro=False):  # Cilindro con un radio en cada extremo; con radio_tope = 0 es un cono; tapas = cierra los extremos con discos.
        if not visible:  # Revisa si la figura está marcada como no visible.
            return  # Sale de la función sin dibujar nada.
        _preparar(estilo, normales, textura, adentro)  # Configura estilo, normales, textura y orientación.
        glColor3f(*color)  # Asigna el color (R, G, B).
        glPushMatrix()  # Guarda la posición, giro y escala actuales.
        glTranslatef(*translate)  # Mueve la figura a la posición (x, y, z).
        glRotatef(*rotate)  # Gira la figura: (ángulo, x, y, z).
        glScalef(*scale)  # Cambia el tamaño en x, y, z.
        gluCylinder(_quad, radio_base, radio_tope, altura, slices, stacks)  # Dibuja el tubo (nace sobre Z y sube hasta "altura").
        if tapas:  # Si se pidió cerrar los extremos.
            if radio_base > 0:  # La base solo se tapa si tiene radio.
                glPushMatrix()  # Guarda la posición actual para la tapa de abajo.
                glRotatef(180, 1, 0, 0)  # Voltea el disco para que mire hacia afuera (hacia atrás).
                gluDisk(_quad, 0, radio_base, slices, 1)  # Dibuja la tapa de abajo.
                glPopMatrix()  # Restaura lo guardado.
            if radio_tope > 0:  # El tope solo se tapa si tiene radio (un cono no lo necesita).
                glPushMatrix()  # Guarda la posición actual para la tapa de arriba.
                glTranslatef(0, 0, altura)  # Sube hasta el extremo del tubo.
                gluDisk(_quad, 0, radio_tope, slices, 1)  # Dibuja la tapa de arriba.
                glPopMatrix()  # Restaura lo guardado.
        glPopMatrix()  # Restaura lo guardado, para que no afecte a las demás figuras.
        # print(name)  # Imprime el nombre (déjalo comentado: se ejecuta en cada cuadro).
 
    @staticmethod  # La función se llama directo desde la clase, sin "self".
    def disk(radio_interior=0.0, radio_exterior=1.0, slices=32, loops=1, color=(0.5, 0.5, 0.5), translate=(0.0, 0.0, 0.0), rotate=(0, 0.0, 1.0, 0.0), scale=(1.0, 1.0, 1.0), name="disk", visible=True, estilo="solido", normales="suaves", textura=False, adentro=False):  # Disco plano; con radio_interior > 0 es una arandela (anillo).
        if not visible:  # Revisa si la figura está marcada como no visible.
            return  # Sale de la función sin dibujar nada.
        _preparar(estilo, normales, textura, adentro)  # Configura estilo, normales, textura y orientación.
        glColor3f(*color)  # Asigna el color (R, G, B).
        glPushMatrix()  # Guarda la posición, giro y escala actuales.
        glTranslatef(*translate)  # Mueve la figura a la posición (x, y, z).
        glRotatef(*rotate)  # Gira la figura: (ángulo, x, y, z).
        glScalef(*scale)  # Cambia el tamaño en x, y, z.
        gluDisk(_quad, radio_interior, radio_exterior, slices, loops)  # Dibuja el disco (nace en el plano XY, mirando hacia +Z).
        glPopMatrix()  # Restaura lo guardado, para que no afecte a las demás figuras.
        # print(name)  # Imprime el nombre (déjalo comentado: se ejecuta en cada cuadro).
 
    @staticmethod  # La función se llama directo desde la clase, sin "self".
    def partialDisk(radio_interior=0.0, radio_exterior=1.0, slices=32, loops=1, inicio=0.0, barrido=90.0, color=(0.5, 0.5, 0.5), translate=(0.0, 0.0, 0.0), rotate=(0, 0.0, 1.0, 0.0), scale=(1.0, 1.0, 1.0), name="partialDisk", visible=True, estilo="solido", normales="suaves", textura=False, adentro=False):  # Parte de un disco; inicio y barrido van en grados (0 = hacia arriba, y avanza hacia la derecha).
        if not visible:  # Revisa si la figura está marcada como no visible.
            return  # Sale de la función sin dibujar nada.
        _preparar(estilo, normales, textura, adentro)  # Configura estilo, normales, textura y orientación.
        glColor3f(*color)  # Asigna el color (R, G, B).
        glPushMatrix()  # Guarda la posición, giro y escala actuales.
        glTranslatef(*translate)  # Mueve la figura a la posición (x, y, z).
        glRotatef(*rotate)  # Gira la figura: (ángulo, x, y, z).
        glScalef(*scale)  # Cambia el tamaño en x, y, z.
        gluPartialDisk(_quad, radio_interior, radio_exterior, slices, loops, inicio, barrido)  # Dibuja solo la parte del disco indicada.
        glPopMatrix()  # Restaura lo guardado, para que no afecte a las demás figuras.
        # print(name)  # Imprime el nombre (déjalo comentado: se ejecuta en cada cuadro).
 
    @staticmethod  # La función se llama directo desde la clase, sin "self".
    def sphere(radio=1.0, slices=32, stacks=32, color=(0.5, 0.5, 0.5), translate=(0.0, 0.0, 0.0), rotate=(0, 0.0, 1.0, 0.0), scale=(1.0, 1.0, 1.0), name="sphere", visible=True, estilo="solido", normales="suaves", textura=False, adentro=False):  # Esfera; con pocos slices y stacks se ve facetada (de bajo polígono).
        if not visible:  # Revisa si la figura está marcada como no visible.
            return  # Sale de la función sin dibujar nada.
        _preparar(estilo, normales, textura, adentro)  # Configura estilo, normales, textura y orientación.
        glColor3f(*color)  # Asigna el color (R, G, B).
        glPushMatrix()  # Guarda la posición, giro y escala actuales.
        glTranslatef(*translate)  # Mueve la figura a la posición (x, y, z).
        glRotatef(*rotate)  # Gira la figura: (ángulo, x, y, z).
        glScalef(*scale)  # Cambia el tamaño en x, y, z (aplasta o estira la esfera).
        gluSphere(_quad, radio, slices, stacks)  # Dibuja la esfera con el radio y las divisiones indicadas.
        glPopMatrix()  # Restaura lo guardado, para que no afecte a las demás figuras.
        # print(name)  # Imprime el nombre (déjalo comentado: se ejecuta en cada cuadro).
 
##Sonido
class audio:
    _cache = {}  # Sonidos ya cargados, para no leer el archivo en cada fotograma.

    @staticmethod  # Se llama directo desde la clase: audio.backgroundMusic(...).
    def backgroundMusic(path="", volumen=0.5):  # path = archivo de audio (mp3, ogg, wav), volumen = de 0.0 a 1.0.
        pathAudio = "rcs/" + path
        if not pathAudio:  # Si no se indicó archivo.
            return  # No hace nada.
        pygame.mixer.init()  # Prepara el sistema de audio.
        pygame.mixer.music.load(pathAudio)  # Carga el archivo.
        pygame.mixer.music.set_volume(volumen)  # Ajusta el volumen.
        pygame.mixer.music.play(-1)  # Reproduce en bucle infinito (-1 = sin fin).

    @staticmethod  # Se llama directo desde la clase: audio.sound(...).
    def sound(path="", volumen=0.1, repetir=0):  # Efecto de sonido; path = archivo, volumen = de 0.0 a 1.0, repetir = veces extra que suena (0 = una sola vez).
        pathAudio = "rcs/" + path
        if not pathAudio:  # Si no se indicó archivo.
            return  # No hace nada.
        if not pygame.mixer.get_init():  # Si el sistema de audio todavía no está listo.
            pygame.mixer.init()  # Lo prepara (así funciona aunque no haya música de fondo).
        if pathAudio not in audio._cache:  # Si es la primera vez que se pide este archivo.
            audio._cache[pathAudio] = pygame.mixer.Sound(pathAudio)  # Lo carga y lo guarda.
        efecto = audio._cache[pathAudio]  # Toma el sonido guardado.
        efecto.set_volume(volumen)  # Ajusta el volumen de este efecto.
        efecto.play(loops=repetir)  # Lo reproduce encima de la música, sin cortarla.

# Ilumuniacion
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

class sysScene:
    def paleta(color=0):
        COLORES = {
            "GRIS": (0.3, 0.31, 0.33, 1.0),
            "RED": (1.0, 0.0, 0.0),
            "GREEN": (0.0, 2.0, 0.0),
            "BLUE": (0.0, 0.0, 3.0)
        }
        # Acepta un nombre ("ROJO", "rojo"), un id (3) o una tupla (1, 0, 0)
        if isinstance(color, str):
            return COLORES.get(color.upper(), COLORES["GRIS"])

        if isinstance(color, int):
            valores = list(COLORES.values())
            if 0 <= color < len(valores):
                return valores[color]
            return COLORES["GRIS"]
        # si ya es una tupla de color, se regresa tal cual
        return color
    
    #   Ejes
    def ejes(visibleMallas = False, visibleEjes = True):
        auxScale = 0.007
        tamaño = 20
        if visibleEjes:
            #EJE Z
            mesh.cylinder(name="EJE: Z", radio=auxScale, altura=50, rotate=convert.degrees(-90, 0, 0), translate=(0,-25,0), color=sysScene.paleta("GREEN"))
            mesh.cone(name="DIRECT: Z", scale=(0.1, 0.1, 0.1), altura=2, rotate=convert.degrees(-90, 0, 0), translate=(0, 4, 0), color=sysScene.paleta("GREEN"))
            #EJE X
            mesh.cylinder(name="EJE: X", radio=auxScale, altura=50, rotate=convert.degrees(0, 90, 0), translate=(-25, 0, 0), color=sysScene.paleta("RED"))
            mesh.cone(name="DIRECT: X", scale=(0.1, 0.1, 0.1), altura=2, rotate=convert.degrees(0, 90, 0), translate=(4, 0, 0), color=sysScene.paleta("RED"))
            #EJE Y
            mesh.cylinder(name="EJE: Y", radio=auxScale, altura=50, rotate=convert.degrees(0, 0, 0), translate=(0, 0, -25), color=sysScene.paleta("BLUE"))
            mesh.cone(name="DIRECT: Y", scale=(0.1, 0.1, 0.1), altura=2, rotate=convert.degrees(0, 0, 0), translate=(0, 0, 4), color=sysScene.paleta("BLUE"))
        #Malla
        salto = 0
        auxScale = 0.0015
        if visibleMallas:
            for i in range(100):
                mesh.cube(name="ejeX"+str(i), scale=(tamaño,auxScale,auxScale), translate=(0,0,-10 +salto),color=sysScene.paleta("RED"))
                mesh.cube(name="ejeY"+str(i), scale=(auxScale,auxScale,tamaño), translate=(-10 +salto,0,0),color=sysScene.paleta("BLUE"))
                salto += .2

class convert:
    @staticmethod  # Se llama directo desde la clase: convert.degrees(...).
    def degrees(x=0, y=0, z=0):  # Recibe el giro en X, Y y Z (en grados); devuelve (ángulo, x, y, z) para glRotatef.
        def multiplicar(a, b):  # Combina dos giros (cuaterniones) en uno solo.
            return (a[0]*b[0] - a[1]*b[1] - a[2]*b[2] - a[3]*b[3],  # Parte w del resultado.
                    a[0]*b[1] + a[1]*b[0] + a[2]*b[3] - a[3]*b[2],  # Parte x.
                    a[0]*b[2] - a[1]*b[3] + a[2]*b[0] + a[3]*b[1],  # Parte y.
                    a[0]*b[3] + a[1]*b[2] - a[2]*b[1] + a[3]*b[0])  # Parte z.

        rx, ry, rz = (math.radians(a) / 2 for a in (x, y, z))  # Pasa a radianes y toma la mitad de cada ángulo.
        qx = (math.cos(rx), math.sin(rx), 0.0, 0.0)  # Giro solo en X.
        qy = (math.cos(ry), 0.0, math.sin(ry), 0.0)  # Giro solo en Y.
        qz = (math.cos(rz), 0.0, 0.0, math.sin(rz))  # Giro solo en Z.

        q = multiplicar(qz, multiplicar(qy, qx))  # Combina: primero X, luego Y, luego Z.
        if q[0] < 0:  # Un giro y su opuesto son equivalentes; se elige el de ángulo menor.
            q = tuple(-v for v in q)  # Invierte los signos.

        w = min(1.0, q[0])  # Evita errores de redondeo antes de acos.
        resto = math.sqrt(1.0 - w * w)  # Tamaño de la parte que define el eje.
        if resto < 1e-6:  # Si casi no hay giro.
            return (0.0, 0.0, 1.0, 0.0)  # Regresa "sin giro" (eje válido, ángulo 0).

        grados = math.degrees(2.0 * math.acos(w))  # Ángulo total del giro combinado.
        return (grados, q[1] / resto, q[2] / resto, q[3] / resto)  # (ángulo, x, y, z).
