from setting import *
from Res.prefabs.GameObjects.shapes import Circle
from Res.prefabs.GameObjects.wave import Wave
from Res.prefabs.GameObjects.grid import Grid

scene = []

def addScene():
    # for i in range(300):
    #     circle = Circle()
    #     circle.randomness()
    #     scene.append(circle)
    # scene.append(Wave())
    scene.append(Grid(10, 10, width=40, height=40, x=0, y=0))


# initialize scene
addScene()

# while game is running
run = True

while run:
    # delay PyGame
    pygame.time.delay(10)

    # get PyGame events
    for event in pygame.event.get():
        # if quit button is pressed
        if event.type == pygame.QUIT:
            # close the window
            run = False

    # fill the screen white
    screen.fill(CC.WHITE)

    # update scene
    for gameObject in scene:
        gameObject.update()

    # update screen
    pygame.display.update()

# close PyGame
pygame.quit()