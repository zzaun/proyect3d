# Liberias para multiplataforma (evita problemas de GLUT en Wayland)
import os
os.environ["PYOPENGL_PLATFORM"] = "x11"

# Liberias del sistema
import sys, importlib, traceback  # Para recargar los archivos cuando se guardan.

# scene: es donde se crea la escena
from scene import *  # Trae los demás nombres (audio, mesh, etc.).
import scene  # Se usa como draw.drawingScene() para que se pueda recargar.

'''
    Metas y limites:
        No mas de 3 archivos, unificar todo.
        Dejar todo simple, no significa simplificar.
        Nada de modular-a-secas, Sera semi-modular
'''
# Parámetros de configuración
size = (1000, 700)
fps = 12  # Fotogramas por segundo máximos.
titleWindows = "Windows OpenGL .GL .GLU .GLUT Goofy"
backgraung = sysScene.paleta(0)
carpeta = os.path.dirname(os.path.abspath(__file__))  # Carpeta del proyecto.

def firma():  # Fecha de la última modificación de los .py de la carpeta.
    return max(os.path.getmtime(os.path.join(carpeta, f)) for f in os.listdir(carpeta) if f.endswith(".py"))

def recargar():  # Vuelve a leer los archivos del proyecto sin cerrar la ventana.
    locales = [m for m in list(sys.modules.values())  # Módulos cargados...
               if getattr(m, "__file__", None)  # ...que tienen archivo...
               and os.path.dirname(os.path.abspath(m.__file__)) == carpeta  # ...en esta carpeta (ignora .venv)...
               and m.__name__ != "__main__"]  # ...y que no son este archivo.
    for m in reversed(locales):  # Primero los que otros usan (meshs), al final draw.
        try:
            importlib.reload(m)  # Recarga el archivo.
        except Exception:
            traceback.print_exc()  # Si hay un error, lo muestra y la ventana sigue abierta.

def runWinodws():  # Abre la ventana y la mantiene abierta; se actualiza sola al guardar cambios.
    giro, inclinacion, distancia = 20.0, 28.0, 5.0  # Vista: giro horizontal, inclinación vertical y lejanía.
    cursor_x, cursor_y = 0, 0  # Última posición del ratón.
    ultima = firma()  # Última modificación vista.

    def renderScene():  # Dibuja la escena.
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Limpia la pantalla.
        glLoadIdentity()  # Reinicia la posición y el giro.
        glTranslatef(0.0, 0.0, -distancia)  # Aleja la cámara.
        glRotatef(inclinacion, 1.0, 0.0, 0.0)  # Gira la escena verticalmente.
        glRotatef(giro, 0.0, 1.0, 0.0)  # Gira la escena horizontalmente.
        glTranslatef(0.0, -0.46, 0.0)  # Baja el punto central.
        scene.drawingScene()  # Dibuja las figuras (draw.py).
        glutSwapBuffers()  # Muestra lo dibujado.

    def adjustWindows(ancho, alto):  # Se ejecuta al abrir la ventana y cada vez que cambia de tamaño.
        alto = max(alto, 1)  # Evita dividir entre cero si la ventana se minimiza.
        glViewport(0, 0, ancho, alto)  # La zona de dibujo ocupa toda la ventana.
        glMatrixMode(GL_PROJECTION)  # Activa el modo de perspectiva.
        glLoadIdentity()  # Borra la perspectiva anterior.
        gluPerspective(60.0, ancho / alto, 0.1, 100.0)  # Proporción real: los modelos no se deforman.
        glMatrixMode(GL_MODELVIEW)  # Regresa al modo de posicionamiento de figuras.

    def maus(button, accion, x, y):  # Clics y rueda del ratón.
        nonlocal distancia, cursor_x, cursor_y  # Permite modificar las variables de runWinodws.
        if accion == GLUT_DOWN:  # Si se presionó un botón.
            cursor_x, cursor_y = x, y  # Guarda dónde empezó el arrastre.
            if button == 3:  # Rueda hacia arriba.
                distancia *= 0.92  # Acerca la cámara.
            elif button == 4:  # Rueda hacia abajo.
                distancia *= 1.08  # Aleja la cámara.

    def move_maus(x, y):  # Arrastre del ratón.
        nonlocal giro, inclinacion, cursor_x, cursor_y  # Permite modificar las variables de runWinodws.
        giro += (x - cursor_x) * 0.4  # Gira según el movimiento horizontal.
        inclinacion += (y - cursor_y) * 0.4  # Inclina según el movimiento vertical.
        cursor_x, cursor_y = x, y  # Guarda la nueva posición.

    def tick(valor):  # Se ejecuta "fps" veces por segundo: revisa cambios y pide un fotograma.
        nonlocal ultima  # Permite modificar la última modificación vista.
        actual = firma()  # Fecha de modificación actual.
        if actual != ultima:  # Si algún archivo cambió.
            ultima = actual  # Guarda la nueva fecha.
            recargar()  # Recarga los archivos.
        glutPostRedisplay()  # Pide redibujar (un fotograma).
        glutTimerFunc(1000 // fps, tick, 0)  # Programa el siguiente en 1000/12 = 83 ms.

    glutInit()  # Inicia GLUT.
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)  # Color, doble búfer y profundidad.
    glutInitWindowSize(*size)  # Tamaño inicial de la ventana.
    glutCreateWindow(titleWindows.encode())  # Crea la ventana con su título.
    glClearColor(*backgraung)  # Color de fondo.
    glEnable(GL_DEPTH_TEST)  # Las figuras de adelante tapan a las de atrás.
    glutDisplayFunc(renderScene)  # Función que dibuja.
    glutReshapeFunc(adjustWindows)  # Función que se ejecuta al cambiar el tamaño.
    glutMouseFunc(maus)  # Función de clics y rueda.
    glutMotionFunc(move_maus)  # Función de arrastre.
    glutTimerFunc(1000 // fps, tick, 0)  # Inicia el ciclo de fotogramas.
    glutMainLoop()  # Mantiene la ventana abierta.

def main():
    # Inicializa música de fondo (una sola vez, no se reinicia al recargar)
    # audio.backgroundMusic(path="Americano.mp3", volumen=0.5)
    runWinodws()  # Abre la ventana.

if __name__ == "__main__":
    main()














