import sys, pygame
import random

pygame.init()
SIZE = [860, 800]
BLOCKSIZE = 35

blocks = [
    [ # L
        (355,30),
        (390,30),
        (425,30),
        (425,65)
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
        (355,656),
        (390,65),
        (390,100)
    ],
]


unactiveBlocks = []




class Block:

    def __init__(self, color, x, y, blocktype):
        self.color = color
        self.blockOffsetX = x
        self.blockOffsetY = y
        self.type = blocktype

    def moveBlock(self, blockOffsetX, blockOffsetY):
        self.blockOffsetX += blockOffsetX
        self.blockOffsetY += blockOffsetY



    def drawBlock(self, screen):
        template = blocks[self.type]
        for i in range(4):
            pixelOffsetX = self.blockOffsetX * BLOCKSIZE
            pixelOffsetY = self.blockOffsetY * BLOCKSIZE
            pygame.draw.rect(screen, self.color, [template[i][0] + pixelOffsetX, template[i][1] + pixelOffsetY, BLOCKSIZE, BLOCKSIZE])
    


class Board:

    def __init__(self, sizeX, sizeY):
        self.SIZEX = sizeX
        self.SIZEY = sizeY

    

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
            pygame.draw.rect(self.screen, (255,255,255), [250, 30, 350, 700])

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
                    # Store active block 
                    unactiveBlocks.append(self.activeBlock)
                   
                else:
                    self.activeRow += 1

                pygame.display.flip()            


if __name__ == "__main__":
    game = Game()
    game.run()