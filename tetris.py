import sys, pygame


pygame.init()
SIZE = [860, 800]


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode(SIZE)
        # Set title to Tetris
        pygame.display.set_caption("Tetris")
         #Set the background to black
        self.screen.fill((0,0,0))
        

    def run(self):

        # Set up virtual time
        clock = pygame.time.Clock()
        time_elapsed = 0
        row = 0

        while 1:
           
            # init clock
            dt = clock.tick() 
            time_elapsed += dt
            #print(time_elapsed)

            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()            
        
            pygame.draw.rect(self.screen, (255,255,255), [250, 30, 350, 700])

            # Every x seconde
            if time_elapsed > 800: 
                # update pos of curr block (falling)
                pygame.draw.rect(self.screen, (255,0,0), [355, 30 + (row * 35) , 35, 35])
                pygame.draw.rect(self.screen, (255,0,0), [390, 30 + (row * 35), 35, 35])
                pygame.draw.rect(self.screen, (255,0,0), [425, 30 + (row * 35), 35, 35])
                pygame.draw.rect(self.screen, (255,0,0), [425, 65 + (row * 35), 35, 35])
                
                # Reset time to 0
                time_elapsed= 0 
                
                # If last row reach change block
                if row == 18:
                    row = 0
                else:
                    row += 1

                pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()