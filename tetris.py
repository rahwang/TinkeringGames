import sys, pygame
import random

pygame.init()
SIZE = [860, 800]
BLOCKSIZE = 35


class Block:

    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
    
    def drawBlock(self, screen, block):
        pygame.draw.rect(screen, block.color, [block.x, block.y, 35, 35])



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
        self.defaultRate = 800
        self.tickSpeed = 1
        self.createBlocks()

    def createBlocks(self):

        #Init all the blocks / put here for now
        self.blocks = [
            [
                Block((255,0,0), 355, 30 + (self.activeRow * BLOCKSIZE)),
                Block((255,0,0), 390, 30 + (self.activeRow * BLOCKSIZE)),
                Block((255,0,0), 425, 30 + (self.activeRow * BLOCKSIZE)),
                Block((255,0,0), 425, 65 + (self.activeRow * BLOCKSIZE))
            ],

            [
                Block((255,0,0), 355, 30 + (self.activeRow * BLOCKSIZE)),
                Block((255,0,0), 390, 30 + (self.activeRow * BLOCKSIZE)),
                Block((255,0,0), 425, 30 + (self.activeRow * BLOCKSIZE)),
                Block((255,0,0), 460, 30 + (self.activeRow * BLOCKSIZE))
            ],

            [
                Block((255,0,0), 355, 30 + (self.activeRow * BLOCKSIZE)),
                Block((255,0,0), 390, 30 + (self.activeRow * BLOCKSIZE)),
                Block((255,0,0), 425, 30 + (self.activeRow * BLOCKSIZE)),
                Block((255,0,0), 390, 65 + (self.activeRow * BLOCKSIZE))
            ],

            [
                Block((255,0,0), 355, 30 + (self.activeRow * BLOCKSIZE)),
                Block((255,0,0), 355, 65 + (self.activeRow * BLOCKSIZE)),
                Block((255,0,0), 390, 65 + (self.activeRow * BLOCKSIZE)),
                Block((255,0,0), 390, 100 + (self.activeRow * BLOCKSIZE))
            ],
        ]
            

    def run(self):

        while 1:
           
            # init clock
            dt = self.clock.tick() 
            self.timeElapsed += dt

            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()            
        
            pygame.draw.rect(self.screen, (255,255,255), [250, 30, 350, 700])
            
            # init array for permanents blocks
            perm = []


            # Every x second
            if self.timeElapsed > (self.defaultRate * self.tickSpeed): 
                # update pos of curr block (falling)

                # randomly choose a block if first iteration
                if self.activeRow == 0:
                    num = random.randint(0,3)

                # draw the block (falling)
                for x in self.blocks[num]:
                    x.drawBlock(self.screen, x)
                
                # Reset time to 0
                self.timeElapsed = 0 
                
                # If last self.activeRow reach change block
                if self.activeRow == 18:
                    self.activeRow = 0
                else:
                    self.activeRow += 1

                pygame.display.flip()            


if __name__ == "__main__":
    game = Game()
    game.run()