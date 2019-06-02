from setting import  *

class Grid:

    def __init__(self, row, col, color=CC.RED, x=WIDTH//2, y=HEIGHT//2, width=10, height=10, w=1):
        self.row = row
        self.col = col
        self.margin = width
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.w = w
        # self.grid = [
        #     [0,0,0,0,0],
        #     [0,1,0,0,0],
        #     [0,0,2,0,0],
        #     [0,0,0,0,0],
        # ]


    def draw(self):
        for row in range(self.row):
            for col in range(self.col):
                pygame.draw.rect(screen,
                                 self.color,
                                 (self.x + col* self.margin,
                                  self.y + row * self.margin,
                                  self.width, self.height),
                                 self.w)
                # if self.grid[row][col] == 1:
                #     pygame.draw.circle(screen, self.color,
                #                        (self.x + col* self.margin + self.width//2,
                #                       self.y + row * self.margin + self.height//2),self.width//3
                #                      )
                # if self.grid[row][col] == 2:
                #     pygame.draw.circle(screen, CC.BLUE,
                #                        (self.x + col * self.margin + self.width // 2,
                #                         self.y + row * self.margin + self.height // 2), self.width // 3
                #                        )

    def update(self):
        self.draw()
        self.move()


    def move(self):
        pass