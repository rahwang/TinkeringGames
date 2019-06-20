import sys, pygame
import random

pygame.init()
BLOCKSIZE = 35

# These measurements are all number of blocks
PIXEL_OUTLINE = 2
BOARD_OFFSETX = 7
BOARD_OFFSETY = 1
BOARD_BLOCKS_WIDTH = 10
BOARD_BLOCKS_HEIGHT = 20
SIZEX = (BOARD_OFFSETX * 2 + BOARD_BLOCKS_WIDTH) * BLOCKSIZE
SIZEY = (BOARD_OFFSETY * 2 + BOARD_BLOCKS_HEIGHT) * BLOCKSIZE
SIZE = [SIZEX , SIZEY]

blockColors = []
blocks = [
    [ # L
        #(355,30),
        #(390,30),
        #(425,30),
        #(425,65)
        (((BOARD_OFFSETX + 3) * BLOCKSIZE), ((BOARD_OFFSETY) * BLOCKSIZE)),
        (((BOARD_OFFSETX + 4) * BLOCKSIZE), ((BOARD_OFFSETY) * BLOCKSIZE)),
        (((BOARD_OFFSETX + 5) * BLOCKSIZE), ((BOARD_OFFSETY) * BLOCKSIZE)),
        (((BOARD_OFFSETX + 5) * BLOCKSIZE), ((BOARD_OFFSETY + 1) * BLOCKSIZE))
    ],

    [ # Square
        (((BOARD_OFFSETX + 3) * BLOCKSIZE), ((BOARD_OFFSETY) * BLOCKSIZE)),
        (((BOARD_OFFSETX + 3) * BLOCKSIZE), ((BOARD_OFFSETY + 1) * BLOCKSIZE)),
        (((BOARD_OFFSETX + 4) * BLOCKSIZE), ((BOARD_OFFSETY) * BLOCKSIZE)),
        (((BOARD_OFFSETX + 4) * BLOCKSIZE), ((BOARD_OFFSETY + 1) * BLOCKSIZE)),
    ],

    [ # line
        (((BOARD_OFFSETX + 3) * BLOCKSIZE), ((BOARD_OFFSETY) * BLOCKSIZE)),
        (((BOARD_OFFSETX + 4) * BLOCKSIZE), ((BOARD_OFFSETY) * BLOCKSIZE)),
        (((BOARD_OFFSETX + 5) * BLOCKSIZE), ((BOARD_OFFSETY) * BLOCKSIZE)),
        (((BOARD_OFFSETX + 6) * BLOCKSIZE), ((BOARD_OFFSETY) * BLOCKSIZE)),
    ],

    [ # half-cross
        (((BOARD_OFFSETX + 3) * BLOCKSIZE), ((BOARD_OFFSETY) * BLOCKSIZE)),
        (((BOARD_OFFSETX + 4) * BLOCKSIZE), ((BOARD_OFFSETY) * BLOCKSIZE)),
        (((BOARD_OFFSETX + 5) * BLOCKSIZE), ((BOARD_OFFSETY) * BLOCKSIZE)),
        (((BOARD_OFFSETX + 4) * BLOCKSIZE), ((BOARD_OFFSETY + 1) * BLOCKSIZE)),
    ],

    [ # zigzag
        (((BOARD_OFFSETX + 3) * BLOCKSIZE), ((BOARD_OFFSETY) * BLOCKSIZE)),
        (((BOARD_OFFSETX + 3) * BLOCKSIZE), ((BOARD_OFFSETY + 1) * BLOCKSIZE)),
        (((BOARD_OFFSETX + 4) * BLOCKSIZE), ((BOARD_OFFSETY + 1) * BLOCKSIZE)),
        (((BOARD_OFFSETX + 4) * BLOCKSIZE), ((BOARD_OFFSETY + 2) * BLOCKSIZE)),
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

    def checkCollision(self,grid):
        template = blocks[self.type]
        for i in range(4):
            pixelOffsetX = self.blockOffsetX * BLOCKSIZE 
            pixelOffsetY = self.blockOffsetY * BLOCKSIZE
            y = ((template[i][1] + pixelOffsetY) // BLOCKSIZE) - 1
            x = ((template[i][0] + pixelOffsetX) // BLOCKSIZE) - 7
            
            #check if reach edges or other block
            if x + 1 == BOARD_BLOCKS_WIDTH or y + 1 == BOARD_BLOCKS_HEIGHT or grid[x][y + 1] != 0:
                return True
        return False

    def storeBlock(self, grid):
        template = blocks[self.type]
        for i in range(4):
            pixelOffsetX = self.blockOffsetX * BLOCKSIZE 
            pixelOffsetY = self.blockOffsetY * BLOCKSIZE
            y = ((template[i][1] + pixelOffsetY) // BLOCKSIZE) - 1
            x = ((template[i][0] + pixelOffsetX) // BLOCKSIZE) - 7
            grid[x][y]= self.color



    def fallBlock(self, blockOffsetX, blockOffsetY):
        self.blockOffsetX += blockOffsetX
        self.blockOffsetY += blockOffsetY
        
    def moveBlock(self, blockOffsetX):
        self.blockOffsetX += blockOffsetX


    def drawBlock(self, screen):
        template = blocks[self.type]
        for i in range(4):
            pixelOffsetX = self.blockOffsetX * BLOCKSIZE 
            pixelOffsetY = self.blockOffsetY * BLOCKSIZE

            pygame.draw.rect(screen, COLORS[0], [template[i][0] + pixelOffsetX, template[i][1] + pixelOffsetY, BLOCKSIZE, BLOCKSIZE])
            pygame.draw.rect(screen, COLORS[self.color], [template[i][0] + pixelOffsetX + PIXEL_OUTLINE, template[i][1] + pixelOffsetY + PIXEL_OUTLINE, BLOCKSIZE-PIXEL_OUTLINE * 2, BLOCKSIZE-PIXEL_OUTLINE * 2])
    

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

        pygame.draw.rect(self.screen, COLORS[0], [x, y, BLOCKSIZE, BLOCKSIZE]) 
        pygame.draw.rect(self.screen, COLORS[colorType], [x+PIXEL_OUTLINE, y+PIXEL_OUTLINE, BLOCKSIZE-PIXEL_OUTLINE*2, BLOCKSIZE-PIXEL_OUTLINE*2])

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
        self.tickSpeed = 0.3
        self.board = Board(self.screen, 20, 10)

    def CreateNewActiveBlock(self):
        randomColor = random.randint(1,len(COLORS)-1)
        randomBlockType = random.randint(0,len(blocks)-1)
        self.activeBlock = Block(randomColor, 0, 0, randomBlockType)



    def run(self):

        while 1:
           
            # init clock
            dt = self.clock.tick() 
            self.timeElapsed += dt

            # detect quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()   
                
                # if key pressed then rotate
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        self.activeBlock.moveBlock(1)
                    if event.key == pygame.K_w:
                        self.activeBlock.moveBlock(-1)
                        

            # draw board
            #pygame.draw.rect(self.screen, (255,255,255), [BOARD_OFFSETX * BLOCKSIZE, BOARD_OFFSETY * BLOCKSIZE, BLOCKSIZE * BOARD_BLOCKS_WIDTH, BLOCKSIZE * BOARD_BLOCKS_HEIGHT])
            self.board.printBoard()

            # Every x second
            if self.timeElapsed > (self.defaultRate * self.tickSpeed): 
                

                # randomly choose a block if first iteration
                if self.activeRow == 0:
                    self.CreateNewActiveBlock()

                # check collision
                if (self.activeBlock.checkCollision(self.board.cells)) == True:
                    self.activeRow = 0
                    # insert block into grid
                    self.activeBlock.storeBlock(self.board.cells)
                    
                else:
                    self.activeRow += 1
                    # draw the block (falling)
                    self.activeBlock.fallBlock(0, 1)

                    self.activeBlock.drawBlock(self.screen)

                    # Reset time to 0
                    self.timeElapsed = 0 
                
                
            

                pygame.display.flip()            


if __name__ == "__main__":
    game = Game()
    game.run()