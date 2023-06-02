from OpenGL.GL import *
from OpenGL.GLU import*
from OpenGL.GLUT import *

import sys
gx=0
gy=0
def init():
	glClearColor(0.0,0.0,0.0,1.0)
	gluOrtho2D(-200,500,-200,500)
	

def Square():
        
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1,0,0)
	glBegin(GL_QUADS)
	glVertex2f(100,100)
	glVertex2f(200,100)
	glVertex2f(200,200)
	glVertex2f(100,200)
	glEnd()
	glTranslatef(150,150,0)
	glRotatef(45,0,0,1,0)
	glTranslatef(-150,-150,0)
	glFlush()
def animate(temp):
	glutPostRedisplay()
	glutTimerFunc(int(1000/60),animate,int(0))
def main():
	glutInit(sys.argv)
	
	glutInitWindowSize(500,500)
	glutInitWindowPosition(0,0)
	glutCreateWindow("Square")
	glutDisplayFunc(Square)
	glutTimerFunc(0,animate,0)
	init()
	glutMainLoop()
main()
