
import sys, pygame

width = 500
height = width
size = width, height
BLACK = 0, 0, 0
WHITE = 255, 255, 255

class Renderable:
    def __init__( self, obj, pos ):
        self.obj = obj
        self.pos = pos

class Window:
    def __init__(self, x, y ):
        pygame.init()

        self.dimensions = x, y
        self.screen = pygame.display.set_mode( self.dimensions )

        self.font = pygame.font.Font( None, 20 )

        self.clearColor = 0, 0, 0

    def paint( self, renderable ):
        self.screen.blit( renderable.obj, renderable.pos )

    def display( self ):
        pygame.display.flip()

        self.screen.fill( self.clearColor )

if __name__ == '__main__':
    window = Window( 500, 500 )

    textTmp = window.font.render( "Hello World", True, WHITE )
    hello = Renderable( textTmp, [50,50] )

    keepGoing = True
    while keepGoing:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                keepGoing = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    keepGoing = False

        window.paint( hello )
        window.display()

    pygame.quit()
