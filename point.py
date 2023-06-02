from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

def clearscreen():
	glClearColor(0.0,0.0,0.0,1.0)
	gluOrtho2D(-1.0,1.0,-1.0,1.0)
def plotpoints():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0,1.0,0.0)
	glPointSize(10.0)
	glBegin(GL_POINTS)
	glVertex2f(0.0,0.0)
	glEnd()
	glFlush()
glutInit()
glutInitDisplayMode(GLUT_RGB)
glutCreateWindow("points")
glutInitWindowPosition(500,500)
glutInitWindowSize(50,50)
glutDisplayFunc(plotpoints)
clearscreen()
glutMainLoop()
