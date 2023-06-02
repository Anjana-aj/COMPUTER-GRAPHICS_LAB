from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

import sys
import math

x=0
y=0
theta=0

max_theta=90
dir=1
pendlength=100
bobradius=20

def init():
	glClearColor(0.0,0.0,0.0,1.0)
	gluOrtho2D(-500,500,-500,500)
	
	
def pendulum():

	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0.0,1.0,0.0)
	
	global x
	global y
	global max_theta
	global theta
	glLineWidth(5)
	glBegin(GL_LINES)
	glVertex2f(0,0)
	glVertex2f(x,y-100)
	
	glEnd()

	
	glColor3f(0.0,1.0,0.0)
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(x,y-80)
	
	for i in range(0,360,1):
		glVertex2f(bobradius*math.cos(math.pi*i/180.0)+x,bobradius*math.sin(math.pi*i/180.0)+y-80)
		
	glEnd()
	glutSwapBuffers()
	
	
def animate(temp):
	
	global x
	global y
	
	global max_theta
	global dir
	global theta
	global pendlength
	
	glutPostRedisplay()
	glutTimerFunc(int(1000/60),animate,int(0))
	
	if(dir==1):
	
		if(theta<max_theta):
			theta+=1
		else:
			dir=0
	elif(dir==0):
		if(theta>=-max_theta):
			theta-=1
		else:
			dir=1
			
			
	x=pendlength*math.sin(math.radians(theta))
	y=-pendlength*math.cos(math.radians(theta))
	
	
			
		
		
		
def main():
	
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB)
	glutInitWindowSize(50,50)
	glutInitWindowPosition(500,500)
	glutCreateWindow("rectangle")
	glutDisplayFunc(pendulum)
	glutTimerFunc(0,animate,0)
	glutIdleFunc(pendulum)

	init()
	glutMainLoop()
	
main()
	
	
	

