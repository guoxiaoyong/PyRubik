# author: Xiaoyong Guo

import copy
import sys

import numpy as np


MAX_ORDER = 10000
NUM_POSITIONS = (3**7) * (2**10) * ((2*3*4*5*6*7*8)**2) * 9 * 10 * 11 * 12


def _generate_rubik_states():
    r = [-1, 0, 1]
    x, y, z = np.meshgrid(r, r, r)
    x = x.flatten()
    y = y.flatten()
    z = z.flatten()
    c = np.vstack((x, y, z)).T
    state = [np.vstack((np.identity(3), x)).T for x in c]
    return [x for x in state if sum(abs(x[:, 3])) >= 2]


# noinspection PyPep8Naming
def _generate_rubik_transform():
    F = np.array([[+0, -1, +0], [+1, +0, +0], [+0, +0, +1]])
    B = np.array([[+0, +1, +0], [-1, +0, +0], [+0, +0, +1]])
    R = np.array([[+1, +0, +0], [+0, +0, -1], [+0, +1, +0]])
    L = np.array([[+1, +0, +0], [+0, +0, +1], [+0, -1, +0]])
    U = np.array([[+0, +0, -1], [+0, +1, +0], [+1, +0, +0]])
    D = np.array([[+0, +0, +1], [+0, +1, +0], [-1, +0, +0]])

    fru = {
      'f': (lambda x: x[2][3] == +1, lambda x: np.dot(F, x)),
      'b': (lambda x: x[2][3] == -1, lambda x: np.dot(B, x)),
      'r': (lambda x: x[0][3] == +1, lambda x: np.dot(R, x)),
      'l': (lambda x: x[0][3] == -1, lambda x: np.dot(L, x)),
      'u': (lambda x: x[1][3] == +1, lambda x: np.dot(U, x)),
      'd': (lambda x: x[1][3] == -1, lambda x: np.dot(D, x)),
    }
    return fru


def rubik_compile(code):
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


def rubik_order(code):
    rubik = Rubik()
    for n in range(MAX_ORDER):
        rubik.transform(code)
        if rubik.is_solved():
            break
    else:
        raise Exception("something wrong!")

    return n+1


class Rubik(object):
    def __init__(self):
        self.state = _generate_rubik_states()
        self.solved = copy.deepcopy(self.state)
        self.fru = _generate_rubik_transform()

    def atom_transform(self, t):
        assert t in set('fbrlud')
        for n, s in enumerate(self.state):
            if self.fru[t][0](s):
                self.state[n] = self.fru[t][1](s)

    def transform(self, t):
        code = rubik_compile(t)
        for c in code:
            self.atom_transform(c)

    def is_solved(self):
        def fun(x: np.array, y: np.array):
            # noinspection PyUnresolvedReferences
            return (x == y).all()
        return all(map(fun, self.state, self.solved))


def main(argv):
    code = argv[1]
    n_order = rubik_order(code)
    print('order = %s' % n_order)


if __name__ == '__main__':
    print(NUM_POSITIONS)
    main(sys.argv)
