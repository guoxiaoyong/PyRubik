import pygame
import math
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

class Cube(object):
  def __init__(self, center, radius, transform=None):
    self._center = center
    self._radius = radius
    self._transform = transform

    self._front = [self._vertex((+1,+1,+1)),
                   self._vertex((-1,+1,+1)),
                   self._vertex((-1,-1,+1)),
                   self._vertex((+1,-1,+1))]

    self._back = [self._vertex((+1,+1,-1)),
                  self._vertex((+1,-1,-1)),
                  self._vertex((-1,-1,-1)),
                  self._vertex((-1,+1,-1))]

    self._up = [self._vertex((+1,+1,+1)),
                self._vertex((-1,+1,+1)),
                self._vertex((-1,+1,-1)),
                self._vertex((+1,+1,-1))]

    self._down = [self._vertex((+1,-1,+1)),
                  self._vertex((+1,-1,-1)),
                  self._vertex((-1,-1,-1)),
                  self._vertex((-1,-1,+1))]

    self._right = [self._vertex((+1,+1,+1)),
                   self._vertex((+1,-1,+1)),
                   self._vertex((+1,-1,-1)),
                   self._vertex((+1,+1,-1))]

    self._left = [self._vertex((+1,+1,+1)),
                  self._vertex((+1,+1,-1)),
                  self._vertex((+1,-1,-1)),
                  self._vertex((+1,-1,+1))]

  def _vertex(self, x):
    x = np.array([x[0], x[1], x[2]])
    return self._center + self._radius*x

  def render(self):
    glBegin(GL_QUADS)

    glColor3f(1,0,0)
    for vertex in self._front:
      glVertex3fv(vertex)

    glColor3f(0.9,0.5,0.1)
    for vertex in self._back:
      glVertex3fv(vertex)

    glColor3f(1,1,0)
    for vertex in self._up:
      glVertex3fv(vertex)

    glColor3f(1,1,1)
    for vertex in self._down:
      glVertex3fv(vertex)

    glColor3f(0,1,0)
    for vertex in self._right:
      glVertex3fv(vertex)

    glColor3f(0,0,1)
    for vertex in self._left:
      glVertex3fv(vertex)

    glEnd()


center = np.array([0,0,0])
radius = 0.5
cube = Cube(center, radius)

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
        print("Quit event!")

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    cube.render()
    glRotatef(1,5,1,1)
    pygame.display.flip()
    pygame.time.wait(10)

main()
