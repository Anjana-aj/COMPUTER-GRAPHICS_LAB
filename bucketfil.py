from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

x=0
y=0
WINDOWSIZE=500
global_y=20

def init():

	glClearColor(0.0,0.0,0.0,1.0)
	gluOrtho2D(-WINDOWSIZE,WINDOWSIZE,-WINDOWSIZE,WINDOWSIZE)
	
def bucket():
	
	global x
	global y
	
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0.0,1.0,0.0)
	
	glBegin(GL_QUADS)
	
	glVertex2f(x-100,y)
	glVertex2f(x+100,y)
	glVertex2f(x+100,y+100)
	glVertex2f(x-100,y+100)
	
	glEnd()
	
	
	glBegin(GL_QUADS)
	
	glVertex2f(x-100,y)
	glVertex2f(x-300,y)
	glVertex2f(x-300,y+300)
	glVertex2f(x-100,y+300)
	
	glEnd()
	
	
	glBegin(GL_QUADS)
	glVertex2f(x+100,y)
	glVertex2f(x+300,y)
	glVertex2f(x+300,y+300)
	glVertex2f(x+100,y+300)
	
	glEnd()

	glBegin(GL_QUADS)
	glColor3f(1,0,0)
	glVertex2f(x-100,y+100)
	glVertex2f(x+100,y+100)
	glVertex2f(x+100,global_y+150)
	glVertex2f(x-100,global_y+150)
	
	glEnd()
	
	glutSwapBuffers()
	
def animate(temp):
	
	
	global global_y
	
	if global_y>150:
		global_y=0
	else:
		global_y+=1
		
	glutPostRedisplay()
	glutTimerFunc(int(1000/60),animate,int(0))
	
	
	
	

	

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB)
	glutInitWindowSize(50,50)
	glutInitWindowPosition(500,500)
	glutCreateWindow("start")
	glutDisplayFunc(bucket)
	glutTimerFunc(0,animate,0)
	glutIdleFunc(bucket)


	init()
	glutMainLoop()
	
main()
