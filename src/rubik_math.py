# author: Xiaoyong Guo
import pdb
import copy
import numpy as np

class Rubik(object):
  def __init__(self):
    r = range(-1,2)
    x, y, z = np.meshgrid(r, r, r)
    x = x.flatten()
    y = y.flatten()
    z = z.flatten()
    c = np.vstack((x, y, z)).T
    I = np.identity(3)
    self.state = [np.vstack((I, x)).T for x in c]

    self.state = [x for x in self.state \
                    if  sum(abs(x[:,3])) >= 2]
    self.solved = copy.deepcopy(self.state)

    F = np.array([[+0,-1,+0], [+1,+0,+0],[+0,+0,+1]])
    B = np.array([[+0,+1,+0], [-1,+0,+0],[+0,+0,+1]])
    R = np.array([[+1,+0,+0], [+0,+0,-1],[+0,+1,+0]])
    L = np.array([[+1,+0,+0], [+0,+0,+1],[+0,-1,+0]])
    U = np.array([[+0,+0,-1], [+0,+1,+0],[+1,+0,+0]])
    D = np.array([[+0,+0,+1], [+0,+1,+0],[-1,+0,+0]])

    tF = lambda x: np.dot(F,x)
    tB = lambda x: np.dot(B,x)
    tR = lambda x: np.dot(R,x)
    tL = lambda x: np.dot(L,x)
    tU = lambda x: np.dot(U,x)
    tD = lambda x: np.dot(D,x)

    isF = lambda x: x[2][3] == +1
    isB = lambda x: x[2][3] == -1
    isR = lambda x: x[0][3] == +1
    isL = lambda x: x[0][3] == -1
    isU = lambda x: x[1][3] == +1
    isD = lambda x: x[1][3] == -1

    self.fru = { 'f': (isF, tF), 
                 'b': (isB, tB),
                 'r': (isR, tR),
                 'l': (isL, tL), 
                 'u': (isU, tU),
                 'd': (isD, tD) };

  def atom_transform(self, t):
    assert t in set('fbrlud')
    for n, s in enumerate(self.state):
      if self.fru[t][0](s): 
        self.state[n] = self.fru[t][1](s)

  def compile(self, code):
    if len(code) == 0:
      return ''

    assert set(code.lower()) <= set('fbrlud123')
    assert code[0].lower() in set('fbrlud')

    result = []
    for c in code:
      if c.islower():  
         result.append(c)
      elif c.isupper():
         result.append(c.lower()*3)
      else:
         result.append(result[-1]*(int(c)-1))

    return ''.join(result)

  def transform(self, t):
    code = self.compile(t)
    for c in code:
      self.atom_transform(c)

  def is_solved(self):
    fun = lambda x, y: (x==y).all()
    return all(map(fun, self.state, self.solved))

  def order(self, code):
    n = 0
    while True:
      n += 1 
      rubik.transform(code)
      if rubik.is_solved(): 
        return n
      if n > 10000:
        raise Exception("something wrong!")


rubik = Rubik()
print rubik.order('ru')
