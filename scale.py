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
	
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0.0,0.0,1.0)
	
	glBegin(GL_LINES)
	glVertex2f(x,(y+100))
	glVertex2f((x-20),(y+20))
	
	glVertex2f((x-20),(y+20))
	glVertex2f((x-100),y)

	

	glVertex2f((x-100),y)
	glVertex2f((x-20),(y-20))

	
	glVertex2f((x-20),(y-20))
	glVertex2f(x,(y-100))

	

	glVertex2f(x,(y-100))
	glVertex2f((x+20),(y-20))

	
		
	glVertex2f((x+20),(y-20))
	glVertex2f((x+100),y)
	
	

	glVertex2f((x+100),y)
	glVertex2f((x+20),(y+20))

	

	glVertex2f((x+20),(y+20))
	glVertex2f(x,(y+100))
	
	glEnd()
	glutSwapBuffers()
def animate(temp):

	global x
	global y
	global sx
	global sy
	glScalef(2.0,2.0,0.0)
	glutPostRedisplay()
	glutTimerFunc(50,animate,int(0))
	
	

	
	
	
	
	
	
	
	
	
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
