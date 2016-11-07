# author: Xiaoyong Guo
import pdb
import copy
import numpy

class State(object):
  def __init__(self, s='fblrud', m='111111'):
    s = s.lower()
    assert set(s) == set('fblrud')
    assert set(m) <= set('01')
    self.s = list(s)
    self.m = m

  def __str__(self):
    z = zip(self.s, self.m)
    f = lambda x: 'o' if x[1] == '0' else x[0]
    r = map(f, z) 
    return ''.join(r)

  def __cmp__(self, other):
    return cmp(str(self), str(other))

  @property
  def front(self):
    return self.s[0]

  @front.setter
  def front(self, v):
    self.s[0] = v

  @property
  def back(self):
    return self.s[1]

  @back.setter
  def back(self, v):
    self.s[1] = v

  @property
  def left(self):
    return self.s[2]

  @left.setter
  def left(self, v):
    self.s[2] = v

  @property
  def right(self):
    return self.s[3]

  @right.setter
  def right(self, v):
    self.s[3] = v

  @property
  def up(self):
    return self.s[4]

  @up.setter
  def up(self, v):
    self.s[4] = v

  @property
  def down(self):
    return self.s[5]

  @down.setter
  def down(self, v):
    self.s[5] = v

  def rotate_lurd(self):
    ( self.left, self.up, 
      self.right, self.down ) = ( self.down, self.left, 
                                  self.up, self.right )

  def rotate_fubd(self):
    ( self.front, self.up, 
      self.back, self.down ) = ( self.down, self.front, 
                                 self.up, self.back)

  def rotate_lbrf(self):
    ( self.left, self.back, 
      self.right, self.front ) = ( self.front, self.left, 
                                   self.back, self.right )

  def Z(self, n=1):
    n = n%4
    for _ in range(n): 
      self.rotate_lurd()

  def X(self, n=1):
    n = n%4
    for _ in range(n): 
      self.rotate_fubd()

  def Y(self, n=1):
    n = n%4
    for _ in range(n): 
      self.rotate_lbrf()

  def copy(self):
    return copy.deepcopy(self)


class Rubik(object):
  def __init__(self):
    c='100000'
    F1={'coordinate': (+1,+1,+1), 'state': State() }
    F2={'coordinate': (+1,-1,+1), 'state': State() }
    F3={'coordinate': (-1,+1,+1), 'state': State() }
    F4={'coordinate': (-1,-1,+1), 'state': State() }
    F5={'coordinate': (+1,+0,+1), 'state': State() }
    F6={'coordinate': (-1,+0,+1), 'state': State() }
    F7={'coordinate': (+0,+1,+1), 'state': State() }
    F8={'coordinate': (+0,-1,+1), 'state': State() }
    F9={'coordinate': (+0,+0,+1), 'state': State(m=c) }
    B1={'coordinate': (+1,+1,-1), 'state': State() }
    B2={'coordinate': (+1,-1,-1), 'state': State() }
    B3={'coordinate': (-1,+1,-1), 'state': State() }
    B4={'coordinate': (-1,-1,-1), 'state': State() }
    B5={'coordinate': (+1,+0,-1), 'state': State() }
    B6={'coordinate': (-1,+0,-1), 'state': State() }
    B7={'coordinate': (+0,+1,-1), 'state': State() }
    B8={'coordinate': (+0,-1,-1), 'state': State() }
    B9={'coordinate': (+0,+0,-1), 'state': State(m=c) }
    M1={'coordinate': (+1,+1,+0), 'state': State() }
    M2={'coordinate': (+1,-1,+0), 'state': State() }
    M3={'coordinate': (-1,+1,+0), 'state': State() }
    M4={'coordinate': (-1,-1,+0), 'state': State() }
    M5={'coordinate': (+1,+0,+0), 'state': State(m=c) ) }
    M6={'coordinate': (-1,+0,+0), 'state': State(m=c) ) }
    M7={'coordinate': (+0,+1,+0), 'state': State(m=c) ) }
    M8={'coordinate': (+0,-1,+0), 'state': State(m=c) ) }

    self.state = [F1,F2,F3,F4,F5,F6,F7,F8,F9,
                  B1,B2,B3,B4,B5,B6,B7,B8,B9,
                  M1,M2,M3,M4,M5,M6,M7,M8]

  def getf(self):
    return [f for f in self.state if f['coordinate'][2] == +1]
        
  def getb(self):
    return [f for f in self.state if f['coordinate'][2] == -1]
 
  def getl(self):
    return [f for f in self.state if f['coordinate'][0] == -1]
 
  def getr(self):
    return [f for f in self.state if f['coordinate'][0] == +1]

  def getu(self):
    return [f for f in self.state if f['coordinate'][1] == +1]

  def getd(self):
    return [f for f in self.state if f['coordinate'][1] == -1]
 
  def rotate_z(self):
    rotz = lambda x: (-x(1), +x(0), +x(2))
