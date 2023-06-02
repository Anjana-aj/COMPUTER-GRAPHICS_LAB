from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
x=0
y=0
angle1=90
theta=90
WINDOW_SIZE = 500


def init():
	glClearColor(1.0,1.0,1.0,1.0)
	gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

	

def clock():
	
	global angle1
	global theta
	global x
	global y
	
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0,1,0)
	i=0
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(0,0)
	for i in range(0,360,1):
		glVertex2f(80*math.cos(math.pi*i/180.0),80*math.sin(math.pi*i/180.0))


	glEnd()
	
	
	x1=60*math.cos(math.pi*angle1/180.0)
	y1=60*math.sin(math.pi*angle1/180.0)
	
	glColor3f(1,0,0)
	glLineWidth(2)
	glBegin(GL_LINES)
	glVertex2f(x,y)
	glVertex2f(x1,y1)
	
	glEnd()
	

	x1=70*math.cos(math.pi*theta/180.0)
	y1=70*math.sin(math.pi*theta/180.0)
	
	

	glColor3f(1,0,0)
	glLineWidth(5)
	glBegin(GL_LINES)
	glVertex2f(x1,y1)
	glVertex2f(x,y)
	
	
	glEnd()
	
	glutSwapBuffers()
	
def animate(temp):

	global angle1
	global theta
	
	if angle1>=360:
		angle1=0
	else:
		angle1-=1
		
	glutPostRedisplay()
	glutTimerFunc(int(1000/60),animate,0)

	
	
	
	
	
	

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB)
	glutInitWindowSize(50,50)
	glutInitWindowPosition(WINDOW_SIZE,WINDOW_SIZE)
	glutCreateWindow("start")
	glutDisplayFunc(clock)
	glutTimerFunc(0,animate,0)
	glutIdleFunc(clock)

	init()
	glutMainLoop()
	
main()
