from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*


def init():
	glClearColor(0.0,0.0,0.0,1.0)
	gluOrtho2D(500,-500,500,-500)
	
def plot_point():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0,0.0,0.0)
	glPointSize(5.0)
	glBegin(GL_POINTS)
	glVertex2f(50,50)
	glEnd()
	glFlush()
	
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(50,50)
	glutCreateWindow("point")
	glutDisplayFunc(plot_point)
	init()
	glutMainLoop()
main()
	
	

	
