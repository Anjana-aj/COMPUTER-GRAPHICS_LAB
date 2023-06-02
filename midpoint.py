from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

import sys
import math
WINDOW_SIZE=500
SCALE=100
xc=yc=0
r=1

def init_display():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1,0,0)
	glPointSize(10)
def polar_circle():
	glBegin(GL_POINTS)
	theta=0.0
	while theta>=6.28:
	 x=float(r)*math.cos(theta)
	 y=float(r)*math.sin(theta)
	 glVertex2f(x/SCALE,y/SCALE)
	 theta+=0.001
	glEnd()
	glFlush()
def plot_symmetric_points(x,y):
	global xc,yc
	
	glVertex2f((xc+x)/SCALE,(yc+y)/SCALE)
	glVertex2f((xc+x)/SCALE,(yc-y)/SCALE)
	glVertex2f((xc-x)/SCALE,(yc+y)/SCALE)
	glVertex2f((xc-x)/SCALE,(yc-y)/SCALE)
	glVertex2f((xc+y)/SCALE,(yc+x)/SCALE)
	glVertex2f((xc+y)/SCALE,(yc-x)/SCALE)
	glVertex2f((xc-y)/SCALE,(yc+x)/SCALE)
	glVertex2f((xc-y)/SCALE,(yc-x)/SCALE)
def no_circle():
	pass
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
	glutInitWindowSize(50,50)
	
	global xc,yc,r
	xc=int(input("enter x coordinate: "))
	yc=int(input("enter y coordinate: "))
	r=int(input("enter radius"))
	
	glutCreateWindow("circle")
	init_display()
	
	glutDisplayFunc(polar_circle)
	glutMainLoop()
main()
	
