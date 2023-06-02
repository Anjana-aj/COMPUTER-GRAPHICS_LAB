from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

import math
import sys

x=0.0
y=0.0
theta=0
WINDOW_SIZE=500


def init():
	glClearColor(0.0,0.0,0.0,1.0)
	gluOrtho2D(-500,500,-500,500)
	

def square():

	global x
	global y
	global theta
	
	glColor3f(0.0,0.0,1,0)
	glClear(GL_COLOR_BUFFER_BIT)
	
	glBegin(GL_QUADS)
	
	glVertex2f((x-100)*math.cos(theta)-(y-100)*math.sin(theta),(y-100)*math.cos(theta)+(x-100)*math.sin(theta))
	glVertex2f((x+100)*math.cos(theta)-(y-100)*math.sin(theta),(y-100)*math.cos(theta)+(x+100)*math.sin(theta))
	glVertex2f((x+100)*math.cos(theta)-(y+100)*math.sin(theta),(y+100)*math.cos(theta)+(x+100)*math.sin(theta))
	glVertex2f((x-100)*math.cos(theta)-(y+100)*math.sin(theta),(y+100)*math.cos(theta)+(x-100)*math.sin(theta))
	
	glEnd()
	
	
	glutSwapBuffers()
	
def animate(temp):

	global x
	global y
	global theta
	glutPostRedisplay()
	glutTimerFunc(int(1000/60),animate,int(0))
	
	if(theta>=360):
		theta=0
	theta+=1
	


def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(50,50)
	glutCreateWindow("start")
	glutDisplayFunc(square)
	glutTimerFunc(0,animate,0)
	init()
	glutMainLoop()
main()
	

