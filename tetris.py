import sys, pygame
import random

pygame.init()
SIZE = [860, 800]


class Block:

    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
    
    def draw_rect(self, screen, block):
        pygame.draw.rect(screen, block.color, [block.x, block.y, 35, 35])



class Block:

    
class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode(SIZE)
        # Set title to Tetris
        pygame.display.set_caption("Tetris")
         #Set the background to black
        self.screen.fill((0,0,0))

        self.clock = pygame.time.Clock()
        self.time_elapsed = 0
        self.row = 0
        self.default_rate = 800
        self.tick_speed = 1
        self.createBlocks()

    def createBlocks(self):   def createBlocks(self):

        #Init all the blocks / put here for now
        self.blocks = [
            [
                Block((255,0,0), 355, 30 + (self.row * 35)),
                Block((255,0,0), 390, 30 + (self.row * 35)),
                Block((255,0,0), 425, 30 + (self.row * 35)),
                Block((255,0,0), 425, 65 + (self.row * 35))
            ],

            [
                Block((255,0,0), 355, 30 + (self.row * 35)),
                Block((255,0,0), 390, 30 + (self.row * 35)),
                Block((255,0,0), 425, 30 + (self.row * 35)),
                Block((255,0,0), 460, 30 + (self.row * 35))
            ],

            [
                Block((255,0,0), 355, 30 + (self.row * 35)),
                Block((255,0,0), 390, 30 + (self.row * 35)),
                Block((255,0,0), 425, 30 + (self.row * 35)),
                Block((255,0,0), 390, 65 + (self.row * 35))
            ],

            [
                Block((255,0,0), 355, 30 + (self.row * 35)),
                Block((255,0,0), 355, 65 + (self.row * 35)),
                Block((255,0,0), 390, 65 + (self.row * 35)),
                Block((255,0,0), 390, 100 + (self.row * 35))
            ],
        ]

        #Init all the blocks / put here for now
        self.blocks = [
            [
                Block((255,0,0), 355, 30 + (self.row * 35)),
                Block((255,0,0), 390, 30 + (self.row * 35)),
                Block((255,0,0), 425, 30 + (self.row * 35)),
                Block((255,0,0), 425, 65 + (self.row * 35))
            ],

            [
                Block((255,0,0), 355, 30 + (self.row * 35)),
                Block((255,0,0), 390, 30 + (self.row * 35)),
                Block((255,0,0), 425, 30 + (self.row * 35)),
                Block((255,0,0), 460, 30 + (self.row * 35))
            ],

            [
                Block((255,0,0), 355, 30 + (self.row * 35)),
                Block((255,0,0), 390, 30 + (self.row * 35)),
                Block((255,0,0), 425, 30 + (self.row * 35)),
                Block((255,0,0), 390, 65 + (self.row * 35))
            ],

            [
                Block((255,0,0), 355, 30 + (self.row * 35)),
                Block((255,0,0), 355, 65 + (self.row * 35)),
                Block((255,0,0), 390, 65 + (self.row * 35)),
                Block((255,0,0), 390, 100 + (self.row * 35))
            ],
        ]

            

    def run(self):

        while 1:
           
            # init clock
            dt = self.clock.tick() 
            self.time_elapsed += dt

            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()            
        
            pygame.draw.rect(self.screen, (255,255,255), [250, 30, 350, 700])
            
            # init array for permanents blocks
            perm = []


            # Every x second
            print(self.row)
            if self.time_elapsed > (self.default_rate * self.tick_speed): 
                # update pos of curr block (falling)

                # randomly choose a block if first iteration
                if self.row == 0:
                    num = random.randint(0,3)

                # draw the block (falling)
                for x in self.blocks[num]:
                    x.draw_rect(self.screen, x)
                
                # Reset time to 0
                self.time_elapsed = 0 
                
                # If last self.row reach change block
                if self.row == 18:
                    self.row = 0
                else:
                    self.row += 1
                #print(self.row)

                pygame.display.flip()            


if __name__ == "__main__":
    game = Game()
    game.run()