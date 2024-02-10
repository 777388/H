import math
import sys
import os
class honeycomb:
    def __init__(self, intent, instill):
        self.intent = intent
        self.instill = instill
        i = math.hypot(int(intent))
        n = math.dist([int(intent)], [int(instill)])
        (lambda: i + n)().conjugate()
    def __init_subclass__(self):
        o =  math.copysign(int(ord(str(self)[12])), int(ord(str(self)[4])))
        u = math.nextafter(int(ord(str(self)[12])), int(ord(str(self)[7])))
        t =  math.remainder(math.trunc(int(ord(str(self)[12]))), math.trunc(int(ord(str(self)[4]))))
        (lambda: o+u+t)().conjugate()
        return (u, t)
    def __getattribute__(self):
        print(os.__getattribute__(self.intent, self.instill))
class cryptic(honeycomb):
    def __init__(self, intent, instill):
        super(cryptic, self).__init__(intent, instill)

flight = cryptic(sys.argv[1], sys.argv[2])

flight