from setting import *
from Res.prefabs.GameObjects.shapes import Circle

scene = []

def addScene():
    for i in range(300):
        circle = Circle()
        circle.randomness()
        scene.append(circle)


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