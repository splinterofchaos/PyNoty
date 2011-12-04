
import sys, pygame

pygame.init()

width = 500
height = width
size = width, height
BLACK = 0, 0, 0
WHITE = 255, 255, 255

class Window:
    def __init__(self, x, y ):
        self.dimensions = x, y
        self.screen = pygame.display.set_mode( self.dimensions )

        self.clearColor = 0, 0, 0

        self.close = False

    def process_events( self, event ):
        if event.type == pygame.QUIT or \
           ( event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE ):
            self.close = True

    def paint( self, renderable ):
        self.screen.blit( renderable.obj, renderable.pos )

    def display( self ):
        pygame.display.flip()

        self.screen.fill( self.clearColor )


class Renderable:
    font = pygame.font.Font( None, 20 )

    def __init__( self, obj, pos, color=WHITE ):
        if isinstance( obj, str ):
            obj = Renderable.font.render( obj, True, color )

        self.obj = obj
        self.pos = pos

class TextInput( Renderable ):
    def __init__( self, text, pos, color=WHITE ):
        Renderable.__init__( self, text, pos, color )

if __name__ == '__main__':
    window = Window( 500, 500 )

    hello = TextInput( "Hello World", [50,50] )

    while not window.close:
        for e in pygame.event.get():
            window.process_events( e )

        window.paint( hello )
        window.display()

    pygame.quit()
