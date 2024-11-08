class Object:
    def __init__(self):
        self._HP = int()
        self._A = list()
        self._B = int()
        self._D = int()
        self._CZ = int()


class Unit(Object):
    def __init__(self):
        super().__init__()
    
    @property
    def HP(self):
        return self._HP

    @property
    def A(self):
        return self._A

    @property
    def B(self):
        return self._B

    @property
    def D(self):
        return self._D

    @property
    def CZ(self):
        return self._CZ
    
    def _copy(self, obj):
        pass

    def improve_HP(self):
        self._HP += 10

    def improve_A(self):
        self._A[1] += 2

    def improve_B(self):
        self._B += 2

    def improve_D(self):
        self._D += 4

    def improve_CZ(self):
        self._CZ += 20


class Archer(Unit):
    def __init__(self):
        super().__init__()
        self._HP = 40
        self._A = [3, 9]
        self._B = 2
        self._D = 4
        self._CZ = 500

class Ranger(Archer):
    def __init__(self, object):
        super().__init__()
        self._HP = object.HP + 10
        self.A[1] = object.A[1] + 2
        self._B = 2
        self._D = 4
        self._CZ = 500

class Grifon(Ranger):
    def __init__(self, object):
        super().__init__(object)
        self._HP = object.HP + 50
        self.A[0] = object.A[0] + 5
        self.A[1] = object.A[1] + 5
        self._B = object.B - 2
        self._D = 4
        self._CZ = object.CZ + 2000