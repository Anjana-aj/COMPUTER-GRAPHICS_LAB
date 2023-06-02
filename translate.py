from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

import sys
import math

def clearscreen():
	glClear(GL_COLOR_BUFFER_BIT)
	gluOrtho2D(-100.0,100.0,-100.0,100.0)
def plotaxes():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0,1.0,1.0)
	glBegin(GL_LINES)
	glVertex2f(0,500)
	glVertex2f(0,-500)
	glEnd()
	glBegin(GL_LINES)
	glVertex2f(500,0)
	glVertex2f(-500,0)
	glEnd()
def plotgrid():
	glColor3f(0.202,0.202,0.202)
	for i in range(500,-500,50)
		if i!=0
			glBegin(GL_LINES)
			glVertex2f(i,500)
			glVertex2f(i,-500)
			glEnd()
			glBegin(GL_LINES)
			glVertex2f(500,i)
			glVertex2f(-500,i)
			glEnd()
def plottriangle(x1,x2,x3,y1,y2,y3):
	glBegin(GL_LINES)
	glVertex2f(x1,y1)
	glVertex2f(x2,y2)
	glEnd()
	glBegin(GL_LINES)
	glVertex2f(x2,y2)
	glVertex2f(x3,y3)
	glEnd()
	glBegin(GL_LINES)
	glVertex2f(x3,y3)
	glVertex2f(x1,y1)
	glEnd()
def translated(x1,x2,x3,y1,y2,y3,tx,ty):
	points=[(x1,y1),(x2,y2),(x3,y3)]
	newpoints=[]
	for point in points:
		newpoints.append([point[0]+tx),(point[1]+ty])
	plotaxes()
	plotgrid()
	glColor3f(1,0,0)
	glplottriangle(x1,x2,x3,y1,y2,y3)
	glColor3f(0,0,1)
	plottriangle(newpoints[0][0],newpoints[1][0],newpoints[2][0],newpoints[0][1],newpoints[1][1],newpoints[2][1])
	glFlush()
	
	
