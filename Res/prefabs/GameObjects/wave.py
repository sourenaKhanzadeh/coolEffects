from setting import *
import math
import time

class Wave:

    def __init__(self, h=HEIGHT/2, w=WIDTH, freq=2,ampl=20, color=CC.RED):
        self.h = h
        self.w = w
        self.freq = freq
        self.ampl = self.maxA = ampl
        self.v = PS.DEFAULT_VELOCITY
        self.color = color
        self.da = PS.DEFAULT_VELOCITY




    def draw(self):
        for x in range(self.w):
            y = int((self.h) + self.ampl * math.sin(
                self.freq * ((float(x) / self.w) * (2 * math.pi) + (self.v * time.time()))))
            screen.set_at((x, y), self.color)


    def update(self):
        self.draw()
        self.move()

    def move(self):
        if self.ampl >= -self.maxA and self.maxA >= self.ampl:
            self.ampl -= self.da

        elif self.ampl <= -self.maxA:
            self.da = -self.da
            self.ampl -= self.da

        if self.ampl >= self.maxA:
            self.da = -self.da
            self.ampl -= self.da

        self.v += 0.00001
