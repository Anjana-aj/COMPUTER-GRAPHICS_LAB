from OpenGL.GL import *;
from OpenGL.GLU import *;
from OpenGL.GLUT import *;
import numpy as np
import sys

sys.setrecursionlimit(10000)

pointSize=2

def init():
	glClearColor(1.0,1.0,1.0,1.0)
	gluOrtho2D(0,500, 0,500)

def boundaryFill(x,y,fillcolor,bcolor):
	im=glReadPixels(x,y,1.0,1.0,GL_RGB,GL_FLOAT,None)
	if (im[0][0][0] != bcolor[0] or im[0][0][1] != bcolor[1] or im[0][0][2] != bcolor[2]) and (im[0][0][0] != fillcolor[0] or im[0][0][1] != fillcolor[1] or im[0][0][2] != fillcolor[2]):
		glColor3f(fillcolor[0],fillcolor[1],fillcolor[2])
		glPointSize(pointSize)
		glBegin(GL_POINTS)
		glVertex2i(x,y)
		glEnd()
		glFlush()
		boundaryFill(x+pointSize,y,fillcolor,bcolor)
		boundaryFill(x-pointSize,y,fillcolor,bcolor)
		boundaryFill(x,y+pointSize,fillcolor,bcolor)
		boundaryFill(x,y-pointSize,fillcolor,bcolor)

def mouse(btn,state,x,y):
	y=500-y
	if(btn==GLUT_LEFT_BUTTON):
		if(state==GLUT_UP):
			boundaryFill(x,y,[0,1,0],[1,0,0])

def world():
	glLineWidth(10);
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(1,0,0);
	glBegin(GL_LINE_LOOP)
	glVertex2i(50,200)
	glVertex2i(300,50)
	glVertex2i(70,80)
	glEnd();
	glFlush();


def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(50,50)
	glutCreateWindow("Boundary Fill")
	init()
	glutDisplayFunc(world)
	glutMouseFunc(mouse)
	glutMainLoop()
main()
