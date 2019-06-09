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
        self.grid = [[random.randint(0, 1) for j in range(row)] for i in range(col)]
        self.grid[0][1] = 2
        self.pos = (0, 1)


    def draw(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                pygame.draw.rect(screen,
                                 self.color,
                                 (self.x + col* self.margin,
                                  self.y + row * self.margin,
                                  self.width, self.height),
                                 self.w)

                if self.grid[row][col] == 2:
                    pygame.draw.rect(screen,
                                     CC.YELLOW,
                                     (self.x + col * self.margin,
                                      self.y + row * self.margin,
                                      self.width, self.height))
                if self.grid[row][col] == 1:
                    pygame.draw.rect(screen,
                                     CC.BLUE,
                                     (self.x + col * self.margin,
                                      self.y + row * self.margin,
                                      self.width, self.height))

    def update(self):
        self.draw()
        self.move()


    def move(self):
        keys = pygame.key.get_pressed()

        try:
            if keys[pygame.K_RIGHT] and self.grid[self.pos[0]][self.pos[1]+1] == 0:
                self.grid[self.pos[0]][self.pos[1]] = 0
                self.grid[self.pos[0]][self.pos[1] + 1] = 2
                self.pos = (self.pos[0],self.pos[1]+1)


            if keys[pygame.K_DOWN] and \
                self.grid[self.pos[0] + 1][self.pos[1]] == 0:

                self.grid[self.pos[0]][self.pos[1]] = 0
                self.grid[self.pos[0] + 1][self.pos[1]] = 2
                self.pos = (self.pos[0] + 1, self.pos[1])


            if keys[pygame.K_UP] and \
                            self.grid[self.pos[0] - 1][self.pos[1]] == 0:

                self.grid[self.pos[0]][self.pos[1]] = 0
                self.grid[self.pos[0] - 1][self.pos[1]] = 2
                self.pos = (self.pos[0] - 1, self.pos[1])

            if keys[pygame.K_LEFT] and self.grid[self.pos[0]][self.pos[1]-1] == 0:
                self.grid[self.pos[0]][self.pos[1]] = 0
                self.grid[self.pos[0]][self.pos[1] - 1] = 2
                self.pos = (self.pos[0],self.pos[1] - 1)

        except Exception:
            pass
