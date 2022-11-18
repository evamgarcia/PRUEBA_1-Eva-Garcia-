import math
class Punto: 
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
        if self.x > 0 and self.y > 0:
            print("{} PERTENECE AL PRIMER CUADRANTE".format(self))
        elif self.x < 0 and self.y > 0:
            print("{} PERTENECE AL segundo CUADRANTE".format(self))
        elif self.x < 0 and self.y < 0:
            print("{} PERTENECE AL tercer CUADRANTE".format(self))
        elif self.x > 0 and self.y < 0:
            print("{} PERTENECE AL cuarto CUADRANTE".format(self))
        else:
            print("{} se encuentra sobre el origen".format(self))
    def vector(self, p):
        
