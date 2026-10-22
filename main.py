# Liberia para multiplataforma
import os
os.environ["PYOPENGL_PLATFORM"] = "x11"

# Liberias graficas
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
# draw es donde se dibuja todo
from draw import *

'''
    Metas y limites:
        No mas de 3 archivos, unificar todo.
        Dejar todo simple, no significa simplificar.
        Nada de modular asecas, Sera semi-modular
'''
#Parametros de fconfiguracion
size = (1200, 900)
backgraung = (0.4, 0.4, 0.4, 1.0)

# Define la función main (principal)
def main():
    # Establece un número para medir la rotación horizontal de la vista.
    giro = 20.0

    # Establece un número para medir la inclinación vertical de la vista.
    inclinacion = 28.0
    
    # Establece un número para medir la lejanía de la vista.
    distancia = 5.0

    # Establece el valor inicial de la posición horizontal del ratón.
    cursor_x = 0

    # Establece el valor inicial de la posición vertical del ratón.
    cursor_y = 0

     # Define la función encargada de mostrar el contenido en la ventana.
    def mostrar():
        # Limpia los colores y las figuras anteriores de la pantalla.
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  
        # Restablece los valores iniciales de ubicación y rotación globales.
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -distancia)  # Mueve la posición de observación hacia atrás según la variable.
        glRotatef(inclinacion, 1.0, 0.0, 0.0)  # Gira la escena verticalmente según la variable.
        glRotatef(giro, 0.0, 1.0, 0.0)  # Gira la escena horizontalmente según la variable.
        glTranslatef(0.0, -0.46, 0.0)  # Mueve el punto central de dibujo hacia abajo.

        # Llamar funciones de dibujo
        drawing()

        # Muestra en la ventana todo el contenido dibujado.
        glutSwapBuffers()

    # Define la función que reacciona a los clics del ratón.
    def boton_raton(boton, accion, x, y):
        # Permite modificar las variables declaradas en la función principal.
        nonlocal distancia, cursor_x, cursor_y

        # Verifica si se presionó un botón.
        if accion == GLUT_DOWN:
            cursor_x = x  # Actualiza la variable con la coordenada horizontal actual.
            cursor_y = y  # Actualiza la variable con la coordenada vertical actual.

            #  Verifica si se cumple la condición de desplazamiento hacia adelante.
            if boton == 3:
                distancia = distancia * 0.92  # Reduce el valor de lejanía.
            # Verifica si se cumple la condición de desplazamiento hacia atrás.
            elif boton == 4:
                distancia = distancia * 1.08  # Aumenta el valor de lejanía.
            
            # Solicita que la ventana se actualice mostrando los cambios.
            glutPostRedisplay()
    
    # Define la función que reacciona al arrastrar el ratón.
    def movimiento_raton(x, y):
        # Permite modificar las variables declaradas en la función principal.
        nonlocal giro, inclinacion, cursor_x, cursor_y

        # Modifica el ángulo horizontal según el desplazamiento registrado.
        giro += (x - cursor_x) * 0.4
        # Modifica el ángulo vertical según el desplazamiento registrado.
        inclinacion += (y - cursor_y) * 0.4
        # Actualiza la variable con la nueva coordenada horizontal.
        cursor_x = x
        # Actualiza la variable con la nueva coordenada vertical.
        cursor_y = y

        #  Solicita que la ventana se actualice mostrando los cambios.
        glutPostRedisplay()

    # Inicia la preparación del entorno gráfico.
    glutInit()

    # Configura las propiedades iniciales de color y profundidad de la ventana.
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(*size)  # Establece el ancho y alto con los que abrirá la ventana.
    glutCreateWindow(b"PyOpenGL - Maceta del Lanzaguisantes (PvZ)")  # Crea la ventana asignándole el título.
    glClearColor(*backgraung)  # Define el color base para limpiar el fondo de la pantalla.

    # Activa el modo de cálculo para la perspectiva visual.
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, 1.0, 0.1, 100.0)  # Establece los límites del campo visual y la profundidad (proporción 1.0 porque la ventana es cuadrada).
    glMatrixMode(GL_MODELVIEW)  # Activa el modo de cálculo para el posicionamiento de figuras.
    glEnable(GL_DEPTH_TEST)  # Habilita el cálculo para que las figuras frontales oculten a las traseras.
    glutDisplayFunc(mostrar)  # Asigna la función que se encargará de dibujar en la ventana.
    glutMouseFunc(boton_raton)  # Asigna la función que detectará los clics dentro de la ventana.
    glutMotionFunc(movimiento_raton)  # Asigna la función que detectará el arrastre dentro de la ventana.
    glutMainLoop()  # Inicia el ciclo continuo que procesa los eventos y mantiene la ventana abierta.

# Verifica si el código se está ejecutando como el archivo principal.
if __name__ == "__main__":
    main()  # Llama a la función de inicio del programa.

