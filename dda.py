from OpenGL.GL import*
from OpenGL.GLUT import*
from OpenGL.GLU import*
def init():
          glClearColor(0.0,0.0,0.0,1.0)
          gluOrtho2D(-300,300,-300,300)
def plotLine():
          deltax=x2-x1
          deltay=y2-y1
          steps=0
          if(abs(deltax)>abs(deltay)):
                  steps=abs(deltax)
          else:
                  steps=abs(deltay)
          xincrement=deltax/steps
          yincrement=deltay/steps
           
          
          glClear(GL_COLOR_BUFFER_BIT)
          glColor3f(0.0,1.0,0.0)
          glPointSize(5.0)
          glBegin(GL_POINTS)
          for step in range(1,steps+1)
                   glVertex2f(round(x1),round(x2))
                   x1=x1+increment
                   y1=y1+increment
          glEnd()
          glFlush()
          
def main():
          print("enter coordinates")
          x1=int(input("enter x1")
          y1=int(input("enter x2")
          x2=int(input("enter y1")
          y2=int(input("enter y2")
          glutInit(sys.argv)
          glutInitDisplayMode(GLUT_RGB)
          glutInitWindowSize(500,500)
          glutCreateWindowPosition(0,0)
          glutDisplayFunc(lamda:plotLine(x1,y1,x2,y2)
          glutIdleFunc(lamba:plotLine(x1,y1,x2,y2)
          init()
          glutMainLoop()
          
main()
          
          
          
