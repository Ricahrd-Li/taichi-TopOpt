import numpy as np


class Node(object):
    def __init__(self, *pos):
        self.init_pos(*pos)  # position
        self.ID = None  # index
        self.force = []  # force vector
        self.disp = []  # displacement vector
        self.cont_elems = [] # connected elements
        self.adj_nds = [] # adjacent nodes

    def __repr__(self):
        return "Node:%r" % (self.pos,)

    def __getitem__(self, index):
        return self.pos[index]

    def __setitem__(self, index, val):
        l = self.pos
        l[index] = val
        self.pos = l

    def __eq__(self, other):
        assert issubclass(type(other), Node), "Must be Node type"
        a = np.array(self.pos)
        b = np.array(other.pos)
        if np.isclose(a, b).all():
            return True
        else:
            return False

    def init_pos(self, *pos):
        self.x = 0.
        self.y = 0.
        self.z = 0.

        if len(pos) == 1:
            self.dim = len(pos[0])
            if self.dim == 2:
                self.x = pos[0][0] * 1.
                self.y = pos[0][1] * 1.
                self.z = 0.0
                self.pos = (self.x, self.y, self.z)
            elif self.dim == 3:
                self.x = pos[0][0] * 1.
                self.y = pos[0][1] * 1.
                self.z = pos[0][2] * 1.
                self.pos = (self.x, self.y, self.z)
            else:
                raise AttributeError("Node dimension must be 2 or 3")

        elif len(pos) == 2:
            self.pos = tuple(pos)
            self.dim = 2
            self.x = pos[0] * 1.
            self.y = pos[1] * 1.
            self.z = 0.0
            self.pos = (self.x, self.y, self.z)
        elif len(pos) == 3:
            self.pos = tuple(pos)
            self.dim = 3
            self.x = pos[0] * 1.
            self.y = pos[1] * 1.
            self.z = pos[2] * 1.
            self.pos = (self.x, self.y, self.z)
        else:
            raise AttributeError("Node dimension must be 2 or 3")

    def set_force(self, *forces):
        for force in forces:
            assert len(force) == self.dim, "The dimension must be the same."
            self.force += force

    def clear_force(self):
        self.force = []

    def set_disp(self, *disps):
        for disp in disps:
            assert len(disp) == self.dim, "The dimension must be the same."
            self.disp += disp

    def clear_disp(self):
        self.disp = []


if __name__ == '__main__':
    nd = Node([2,3,4])
    print(nd)
    nd.set_force([3,4,5])
    print(nd.force)
    nd.set_disp([0.,1.,0.])
    print(nd.disp)
    nd.ID = 4
    print(nd.ID)
    nd.y = 2.
    print(nd)