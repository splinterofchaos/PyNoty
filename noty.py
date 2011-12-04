
import sys, pygame

width = 500
height = width
size = width, height
BLACK = 0, 0, 0
WHITE = 255, 255, 255

class Window:
    def __init__(self, x, y ):
        pygame.init()

        self.dimensions = x, y
        self.screen = pygame.display.set_mode( self.dimensions )

        self.font = pygame.font.Font( None, 20 )

        self.clearColor = 0, 0, 0

    def paint( self, obj, pos ):
        self.screen.blit( obj, pos )

    def display( self ):
        pygame.display.flip()

        self.screen.fill( self.clearColor )

if __name__ == '__main__':
    window = Window( 500, 500 )

    text = window.font.render( "Hello World", True, WHITE )

    keepGoing = True
    while keepGoing:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                keepGoing = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    keepGoing = False

        window.paint( text, [50,50] )
        window.display()

    pygame.quit()
