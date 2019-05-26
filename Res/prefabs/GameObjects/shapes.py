from abc import ABC, abstractmethod
from setting import *



class Shape(ABC):

    def __init__(self, x=WIDTH//2, y=HEIGHT//2, r=10, color=CC.RED, w=0):
        self.x = x
        self.y = y
        self.dx = self.dy = PS.DEFAULT_VELOCITY
        self.color = color
        self.r = r
        self.w = w

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def move(self):
        pass

    def update(self):
        self.draw()
        self.move()

    def randomPositions(self):
        self.x = random.randint(self.r, WIDTH - self.r)
        self.y = random.randint(self.r, HEIGHT - self.r)

    def randomColors(self):
        self.color = (random.randint(0, 250)+1,
                      random.randint(0, 250) + 1,
                      random.randint(0, 250) + 1)

    def randomDarkColors(self):
        self.color = (random.randint(0, 255//2) + 1,
                      random.randint(0, 255//2) + 1,
                      random.randint(0, 255//2) + 1)

    def randomLightColors(self):
        self.color = (random.randint(255 // 2, 255) + 1,
                      random.randint(255 // 2, 255) + 1,
                      random.randint(255 // 2, 255) + 1)

    def randomVelocities(self, minn ,maxx):
        self.dx = random.random() * maxx + minn
        self.dy = random.random() * maxx + minn

    def randomRadius(self, minn, maxx):
        self.r = random.randint(minn, maxx)

    def randomness(self):
        self.randomPositions()
        self.randomColors()
        self.randomVelocities(1, 0.5)
        self.randomRadius(1, 20)


class Circle(Shape):

    def draw(self):
        pygame.draw.circle(screen, self.color,(int(self.x), int(self.y)), int(self.r), int(self.w))

    def move(self):
        # going east
        if self.x + self.r > WIDTH:
            # velocity change direction
            self.dx = -self.dx

        #going west
        elif self.x - self.r < 0:
            # velocity change direction
            self.dx = -self.dx

        # going up
        if self.y - self.r < 0:
            self.dy = -self.dy
        # going down
        elif self.y + self.r > HEIGHT:
            self.dy = -self.dy

        self.x += self.dx
        self.y += self.dy

