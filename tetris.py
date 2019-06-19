import sys, pygame
import random

pygame.init()
BLOCKSIZE = 35

# These measurements are all number of blocks
BOARD_OFFSETX = 7
BOARD_OFFSETY = 1
BOARD_BLOCKS_WIDTH = 10
BOARD_BLOCKS_HEIGHT = 20
SIZEX = (BOARD_OFFSETX * 2 + BOARD_BLOCKS_WIDTH) * BLOCKSIZE
SIZEY = (BOARD_OFFSETY * 2 + BOARD_BLOCKS_HEIGHT) * BLOCKSIZE

SIZE = [SIZEX , SIZEY]

blocks = [
    [ # L
        (355,30),
        (390,30),
        (425,30),
        (425,65)
    ],

    [ # Square
        (355, 30),
        (355, 65),
        (390, 30),
        (390, 65)
    ],

    [ # line
        (355, 30),
        (390, 30),
        (425, 30),
        (460, 30)
    ],

    [ # half-cross
        (355,30),
        (390,30),
        (425,30),
        (390,65)
    ],

    [ # zigzag
        (355,30),
        (355,65),
        (390,65),
        (390,100)
    ],
]


COLORS = [
    [255,255,255], [255,0,0], [0,255,0], [0,0,255]
]



class Block:

    def __init__(self, color, x, y, blocktype):
        self.color = color
        self.blockOffsetX = x
        self.blockOffsetY = y
        self.type = blocktype

    def moveBlock(self, blockOffsetX, blockOffsetY):
        self.blockOffsetX += blockOffsetX
        self.blockOffsetY += blockOffsetY
        print(blockOffsetX)
        print(blockOffsetY)


    def drawBlock(self, screen):
        template = blocks[self.type]
        for i in range(4):
            pixelOffsetX = self.blockOffsetX * BLOCKSIZE 
            pixelOffsetY = self.blockOffsetY * BLOCKSIZE
            print(template[i][0] + pixelOffsetX)
            print(template[i][1] + pixelOffsetY)
            pygame.draw.rect(screen, self.color, [template[i][0] + pixelOffsetX, template[i][1] + pixelOffsetY, BLOCKSIZE, BLOCKSIZE])
    

class Board:

    def __init__(self, screen, sizeX, sizeY):
        self.SIZEX = sizeX
        self.SIZEY = sizeY
        self.screen = screen
        self.cells = []
        for i, a in enumerate(range(0, sizeY)):
            row = []
            for cell in range(0, sizeX):
                row.append(0)    
            self.cells.append(row)

    def printCell(self, i, j):
        colorType = self.cells[i][j]
        x = BOARD_OFFSETX * BLOCKSIZE
        y = BOARD_OFFSETY * BLOCKSIZE
        x += i * BLOCKSIZE
        y += j * BLOCKSIZE 
        pygame.draw.rect(self.screen, COLORS[colorType], [x, y, BLOCKSIZE, BLOCKSIZE])

    def printBoard(self):
        for i, row in enumerate(self.cells):
            for j, col in enumerate(row): 
                self.printCell(i,j)
    

class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode(SIZE)
        # Set title to Tetris
        pygame.display.set_caption("Tetris")
         #Set the background to black
        self.screen.fill((0,0,0))

        self.clock = pygame.time.Clock()
        self.timeElapsed = 0
        self.activeRow = 0
        self.activeBlock = None
        self.defaultRate = 800
        self.tickSpeed = 1
        self.board = Board(self.screen, 20, 10)


    def run(self):

        while 1:
           
            # init clock
            dt = self.clock.tick() 
            self.timeElapsed += dt

            # detect quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()   
                
                # if key pressed then rotate
                #if event.type == pygame.KEYDOWN:
                    #if event.key == pygame.K_e:
                        

            # draw board
            #pygame.draw.rect(self.screen, (255,255,255), [BOARD_OFFSETX * BLOCKSIZE, BOARD_OFFSETY * BLOCKSIZE, BLOCKSIZE * BOARD_BLOCKS_WIDTH, BLOCKSIZE * BOARD_BLOCKS_HEIGHT])
            self.board.printBoard()

            # Every x second
            if self.timeElapsed > (self.defaultRate * self.tickSpeed): 
                

                # randomly choose a block if first iteration
                if self.activeRow == 0:
                    self.activeBlock = Block((255, 0, 0), 0, 0, random.randint(0,3))

                # draw the block (falling)
                self.activeBlock.moveBlock(0, 1)

                self.activeBlock.drawBlock(self.screen)
                
                # Reset time to 0
                self.timeElapsed = 0 
                
                # If last self.activeRow reach change block
                if self.activeRow == 17:
                    self.activeRow = 0
                   
                else:
                    self.activeRow += 1

                pygame.display.flip()            


if __name__ == "__main__":
    game = Game()
    game.run()