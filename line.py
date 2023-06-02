from OpenGL.GL import*
from OpenGL.GLUT import*
from OpenGL.GLU import*

def clearscreen():
	glClearColor(0.0,0.0,0.0,1.0)
	gluOrtho2D(-1.0,1.0,-1.0,1.0)
def plot_lines():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0,0.0,0.0)
	glPointSize(5.0)
	glBegin(GL_LINES)
	glVertex2f(0.0,0.0)
	glVertex2f(1.0,1.0)
	glEnd()
	glFlush()
glutInit()
glutInitDisplayMode(GLUT_RGB)
glutCreateWindow("lines")
glutInitWindowPosition(500,500)
glutInitWindowSize(50,50)
glutDisplayFunc(plot_lines)
clearscreen()
glutMainLoop()

	
