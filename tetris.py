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

    
    def calculatePos(self, template, cell):
       
        pixelOffsetX = self.blockOffsetX * BLOCKSIZE 
        pixelOffsetY = self.blockOffsetY * BLOCKSIZE
        y = ((template[cell][1] + pixelOffsetY) // BLOCKSIZE) - 1
        x = ((template[cell][0] + pixelOffsetX) // BLOCKSIZE) - 7
        return x, y

    def checkCollisionY(self,board):
        template = blocks[self.type]
        for pixel in range(4):
            x, y = self.calculatePos(template, pixel)
            #check if reach edges or other block
            print(str(x) + " " + str(y))
            if y + 1 == BOARD_BLOCKS_HEIGHT or board.getCell(x, y + 1) != 0:
                return True
        return False

    def checkCollisionX(self, board, offsetX):
        template = blocks[self.type]
        for pixel in range(4):
            x, y = self.calculatePos(template, pixel)
            #check if reach edges or other block
            if x + offsetX == BOARD_BLOCKS_WIDTH  or x + offsetX == -1 or board.getCell(x + offsetX, y) != 0:
                return True
        return False

    def storeBlock(self, board):
        template = blocks[self.type]
        for pixel in range(4):
            x, y = self.calculatePos(template, pixel)
            board.setCell(x, y, self.color)

    def moveBlockY(self, blockOffsetX, blockOffsetY):
        self.blockOffsetX += blockOffsetX
        self.blockOffsetY += blockOffsetY
        
    def moveBlockX(self, blockOffsetX):
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
        for i, a in enumerate(range(0, sizeX)):
            row = []
            for cell in range(0, sizeY):
                row.append(0)    
            self.cells.append(row)

    def getCell(self, i, j):
        return self.cells[i][j]

    def setCell(self, i, j, val):
        self.cells[i][j] = val

    def printCell(self, i, j):
        colorType = self.getCell(i, j)
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

    def checkLine(self):
        #For each col
        for row in range(0, BOARD_BLOCKS_HEIGHT):
            count = 0
            for col in range(0, BOARD_BLOCKS_WIDTH):
                #check if empty
                if self.getCell(col, row) != 0:
                    count += 1
            # if line full
            if count == BOARD_BLOCKS_WIDTH - 1:
                print(row)
                return True, row
        return False, None

    def eraseLine(self, row):
        return None
                    
    

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
        self.tickSpeed = 0.1
        self.board = Board(self.screen, BOARD_BLOCKS_WIDTH, BOARD_BLOCKS_HEIGHT)

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
                        if (self.activeBlock.checkCollisionX(self.board, 1)) != True:
                            self.activeBlock.moveBlockX(1)
                    if event.key == pygame.K_w:
                        if (self.activeBlock.checkCollisionX(self.board, -1)) != True:
                            self.activeBlock.moveBlockX(-1)
                        

            # draw board
            #pygame.draw.rect(self.screen, (255,255,255), [BOARD_OFFSETX * BLOCKSIZE, BOARD_OFFSETY * BLOCKSIZE, BLOCKSIZE * BOARD_BLOCKS_WIDTH, BLOCKSIZE * BOARD_BLOCKS_HEIGHT])
            self.board.printBoard()

            # Every x second
            if self.timeElapsed > (self.defaultRate * self.tickSpeed): 
                

                # randomly choose a block if first iteration
                if self.activeRow == 0:
                    self.CreateNewActiveBlock()

                # check collision
                if (self.activeBlock.checkCollisionY(self.board)) == True:
                    self.activeRow = 0
                    # insert block into board
                    self.activeBlock.storeBlock(self.board)
                    
                else:
                    self.activeRow += 1
                    # draw the block (falling)
                    self.activeBlock.moveBlockY(0, 1)

                    self.activeBlock.drawBlock(self.screen)

                    # Reset time to X0
                    self.timeElapsed = 0 
                
                
                # check if an entire ligne is drawn   
                self.board.checkLine()         
                #if (self.board.checkLine()) == True:
                    #self.board.eraseLine()


                pygame.display.flip()            


if __name__ == "__main__":
    game = Game()
    game.run()