
import sys, pygame

pygame.init()

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
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255

    font = pygame.font.Font( None, 20 )

    def __init__( self, obj, pos, color=WHITE ):
        if isinstance( obj, str ):
            obj = Renderable.font.render( obj, True, color )

        self.obj = obj
        self.pos = pos
        self.color = color

class TextInput( Renderable ):
    def __init__( self, text, pos, color=Renderable.WHITE ):
        self.text = text
        self.flush = False

        Renderable.__init__( self, text, pos, color )

    def update( self ):
        self.obj = Renderable.font.render( self.text, True, self.color )

    def capture_input( self, event ):
        if event.type == pygame.KEYDOWN:
            try:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key == pygame.K_RETURN:
                    self.flush = True
                elif event.key == pygame.K_TAB:
                    pass
                else:
                    self.text += chr( event.key )
            except ValueError:
                pass

            self.update()

class Tree:
    SPACING = 20
    TAB     = 10

    def __init__( self, parent=None ):
        self.parent   = parent
        self.children = []
        self.indent   = 0

        pos = 50, 50
        if parent:
            pos = parent.entry.pos
            pos = [ pos[0], pos[1] + 20 ]

            self.indent = parent.indent + 1

        self.entry = TextInput( "", pos )

    def reposition( self, y = 50 ):
        # Assumes self is correctly placed. 
        # But its children may be overlapping.
        self.entry.pos = 50 + Tree.TAB*self.indent, y
        for c in self.children:
            y += Tree.SPACING
            y = c.reposition( y )

        return y

    def paint_onto( self, window ):
        window.paint( self.entry )
        for c in self.children:
            c.paint_onto( window )


if __name__ == '__main__':
    window = Window( 500, 500 )

    root = curNode = Tree()

    while not window.close:
        for e in pygame.event.get():
            window.process_events( e )
            curNode.entry.capture_input( e )

        if curNode.entry.flush:
            curNode.entry.flush = False

            if curNode.parent:
                curNode = curNode.parent

            curNode.children.append( Tree(curNode) )
            curNode = curNode.children[ -1 ]

            root.reposition()
                
        root.paint_onto( window )

        window.display()

    pygame.quit()
