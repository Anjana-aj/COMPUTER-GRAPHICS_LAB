from OpenGL.GL import*
from OpenGL.GLUT import*
from OpenGL.GLU import*

def clearscreen():
	glClearColor(0.0,0.0,0.0,1.0)
	gluOrtho2D(-1.0,1.0,1.0,-1.0)
def plottriangle():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0,0.0,0.0)
	glPointSize(5.0)
	glBegin(GL_TRIANGLES)
	glVertex2f(3.0,0.0)
	glVertex2f(2.0,0.0)
	glVertex2f(1.0,0.0)
	glEnd()
	glFlush()
glutInit()
glutInitDisplayMode(GLUT_RGB)
glutCreateWindow("traingle")
glutInitWindowPosition(500,500)
glutInitWindowSize(50,50)
glutDisplayFunc(plottriangle)
clearscreen()
glutMainLoop()

main()

