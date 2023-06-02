from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

import sys
import math

WINDOWSIZE=500
xc=0
yc=0
R=50
dir=1

def init():
	glClearColor(0.0,0.0,0.0,1.0)
	gluOrtho2D(-WINDOWSIZE,WINDOWSIZE,-WINDOWSIZE,WINDOWSIZE)
	
def drawSphere():
	global xc
	global yc
	global R
	
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0.0, 1.0, 1.0)
	glVertex2f(xc, yc+50)
	i = 0
	glBegin(GL_TRIANGLE_FAN)
	for i in range(0, 361, 1):
		glVertex2f(R * math.cos(math.pi * i / 180) + xc, R * math.sin(math.pi * i / 180) + yc+50)
	glEnd()	
	glFlush()
	
	glBegin(GL_LINES)
	glColor3f(0,1,0)
	glVertex2f(-300,0)
	glVertex2f(300,0)
	
	glEnd()
	glutSwapBuffers()
	
def animate(temp):

	global xc
	global yc
	global R
	global dir
	glutPostRedisplay()
	glutTimerFunc(int(1000/60),animate,int(0))
	
	if dir==1:
		if yc<400:
			xc+=0.5
			yc+=1.5
		else:
			dir=0
	else:
		if yc>50:
		
			yc-=1.5
			xc+=0.5
		else:
			dir=1

		
	
	





def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB)
	glutInitWindowSize(50,50)
	glutInitWindowPosition(500,500)
	glutCreateWindow("start")
	glutDisplayFunc(drawSphere)
	glutTimerFunc(0,animate,0)
	glutIdleFunc(drawSphere)
	init()
	glutMainLoop()
	
main()
