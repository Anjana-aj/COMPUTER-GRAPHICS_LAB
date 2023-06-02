from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

import sys
import math

x=0.0
y=0.0
sx=0
sy=0
def init():
	glClearColor(0.0,0.0,0.0,1.0)
	gluOrtho2D(-500,500,-500,500)
	
def star():
	
	global x
	global y
	global tx
	global ty
	
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0.0,0.0,1.0)
	glBegin(GL_POLYGON)
	
	glVertex2f((x-100)*tx,(y+100)*ty)
	glVertex2f(x*tx, (y+300)*ty)
    	glVertex2f((x+ 100)*tx, (y + 100)*ty)
    	glVertex2f((x+ 300)*tx, y*ty)
    	glVertex2f((x+ 100)*tx, (y- 100)*ty)
    	glVertex2f(x*tx, (y- 300)*ty)
    	glVertex2f((x- 100)*tx, (y- 100)*ty)
    	glVertex2f((x- 300)*tx, y*ty)
    	glEnd()

	glutSwapBuffers()
def animate(temp):

	global x
	global y
	global sx
	global sy
	
	glutPostRedisplay()
	glutTimerFunc(50,animate,int(0))
	
	dir=0
	
	if(sx>=2 or sy>=2):
		sy=0
		sx=0
	else:
		sx=+0.01
		sy=+0.01
		dir=1
		
	if dir==1:
		sx-=1
		sy-=1
		

	
	
	
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB)
	glutInitWindowSize(50,50)
	glutInitWindowPosition(500,500)
	glutCreateWindow("start")
	glutDisplayFunc(star)
	glutTimerFunc(50,animate,0)
	init()
	glutMainLoop()
	
main()
