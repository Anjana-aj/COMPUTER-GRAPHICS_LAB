from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

import sys
import math

WINDOW_SIZE=500
rotate_x=[0,0,0,0,0]
rotate_y=[0,0,0,0,0]
point_size=10
speed=[0,2,3,4,5]
DIS=[0,100,200,300,400]
THETA=[0,30,45,60,75,80]
RADIUS=[60,10,5,25,40]


def init():
	glClearColor(0.0,0.0,0.0,1.0)
	gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
	
def drawcircle(x,y,RADIUS):
	glColor3f(0.0,0.0,1.0)
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(x,y)
	for i in range(0,360,1):
		glVertex2f(RADIUS*math.cos(math.pi*i/180.0)+x,RADIUS*math.cos(math.pi*i/180.0)+y)
	glEnd()
def drawcircleorbit(DIS):
	glColor3f(0.0,0.0,1.0)
	glBegin(GL_POINTS)
	theta=0.0
	if theta<=6.28:
		x=float(DIS)*math.cos(theta)
		y=float(DIS)*math.sin(theta)
	glVertex2f(x,y)
	theta+=0.005
	glEnd()
	
	
	
	
def solarsystem(noofcircles):
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0.0,0.0,1.0)
	for i in range(0,noofcircles):
		drawcircleorbit(DIS[i])
		drawcircle(rotate_x[i],rotate_y[i],RADIUS[i])
		
	glFlush()
	glutSwapBuffers()
	
	
def animate(noofplanets):
	global rotate_x
	global rotate_y
	global speed
	global DIR
	glutPostRedisplay()
	glutTimerFunc(int(1000/60),animate,noofplanets)
	for i in range(0,noofplanets):
		rotate_x[i]=DIS[i]*math.cos(math.radians(THETA[i]))
		rotate_y[i]=-DIS[i]*math.sin(math.radians(THETA[i]))
	if(THETA[i]==360):
		THETA=0
	THETA[i]=THETA[i]+SPEED[i]
		
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB)
	glutInitWindowSize(0,0)
	glutInitWindowPosition(WINDOW_SIZE,WINDOW_SIZE)
	glutCreateWindow("solarsystem")
	glutDisplayFunc(solarsystem(5))
	glutTimerFunc(0,animate,5)
	init()
	glutMainLoop()
main()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
