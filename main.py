from setting import *

# while game is running
run = True

while run:
    # get PyGame events
    for event in pygame.event.get():
        # if quit button is pressed
        if event.type == pygame.QUIT:
            # close the window
            run = False

    # update screen
    updateBg()


# close PyGame
pygame.quit()