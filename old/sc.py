import pygame
import math
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
  (1,-1,-1),
  (1,1,-1),
  (-1,1,-1),
  (-1,-1,-1),
  (1,-1,1),
  (1,1,1),
  (-1,-1,1),
  (-1,1,1)
)

edges = (
  (0,1),
  (0,3),
  (0,4),
  (2,1),
  (2,3),
  (2,7),
  (6,3),
  (6,4),
  (6,7),
  (5,1),
  (5,4),
  (5,7)
)

t=0
step = 0.01
def Cube():
  global t
  glBegin(GL_LINES)
  glColor3f(abs(math.sin(t)),0,0)
  t = t+step
  for edge in edges:
    for vertex in edge:
      glVertex3fv(vertices[vertex])
  glEnd()

def main():
  pygame.init()
  display = (800, 600)
  pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
  gluPerspective(45, (display[0]/display[1]), 0.1, 50)
  glTranslatef(0.0, 0.0, -5)
  glRotatef(20, 0, 0, 0)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
        print "Quit event!"
     
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    Cube()
    glRotatef(1,5,1,1)
    pygame.display.flip()
    pygame.time.wait(10)

main()

