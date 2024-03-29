
import sys, pygame
from vector import Vector

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

    DARK_BLUE   = [  25,  25, 100 ]
    DARK_PURPLE = [ 100,  25, 100 ]
    DARK_RED    = [ 100,  25,  25 ]


    font = pygame.font.Font( None, 20 )

    def __init__( self, obj, pos, color=WHITE ):
        if isinstance( obj, str ):
            obj = Renderable.font.render( obj, True, color )

        self.obj = obj
        self.pos = Vector( pos )
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

    COLOR          = Renderable.DARK_BLUE
    SELECTED_COLOR = Renderable.DARK_PURPLE
    ROOT_COLOR     = Renderable.DARK_RED

    def __init__( self, parent=None ):
        self.parent   = parent
        self.children = []
        self.selected = False
        self.root     = False

        pos = 50, 50
        if parent:
            pos = parent.entry.pos
            pos = [ pos[0], pos[1] + 60 ]

        self.entry = TextInput( "", pos )

    def dimensions( self ):
        return self.entry.obj.get_bounding_rect()

    def bounds( self ):
        return self.dimensions().move( self.entry.pos ).inflate( 20, 20 )

    def center( self ):
        return self.bounds().center

    def paint_onto( self, window ):
        # The connections must be drawn before the entry.
        for c in self.children:
            pygame.draw.line( window.screen, Renderable.WHITE, 
                              self.center(), c.center() )

        # Draw an oval before the text.
        rect = self.bounds()
        
        if self.selected:
            col = Tree.SELECTED_COLOR
        elif self.root:
            col = Tree.ROOT_COLOR
        else:
            col = Tree.COLOR

        pygame.draw.ellipse( window.screen, col, rect )

        # Draw the text over that oval.
        window.paint( self.entry )

        for c in self.children:
            c.paint_onto( window )

    def find_node_from_point( self, point ):
        if self.bounds().collidepoint( point ):
            return self
        else:
            if len( self.children ) > 0:
                for c in self.children:
                    ret = c.find_node_from_point( point )
                    if ret != None:
                        return ret

        # Point didn't collide with self and there either were no children to
        # check or they didn't collide either.
        return None

if __name__ == '__main__':
    window = Window( 500, 500 )

    root = curNode = Tree()

    root.root = True
    curNode.selected = True

    # When the mouse button goes down, hovering over a TextInput, that box
    # becomes stuck to the mouse. 
    stuckNode = None

    # Where on the TextInput got stuck. (Offset from mouse to TextInput.)
    stickOffset = 0, 0

    while not window.close:
        for e in pygame.event.get():
            window.process_events( e )

            if curNode:
                curNode.entry.capture_input( e )

            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                # mp = Mouse Position
                mp = Vector( pygame.mouse.get_pos() )
                stuckNode = root.find_node_from_point( mp )

                if not curNode:
                    stuckNode.children.append( Tree(stuckNode) )
                    curNode = stuckNode.children[ -1 ]
                    curNode.selected = True

                if stuckNode:
                    # sp = Stuck Position
                    sp = Vector( stuckNode.entry.pos )

                    stickOffset = sp - mp
            if e.type == pygame.MOUSEBUTTONUP   and e.button == 1:
                stuckNode = None

        if stuckNode:
            # Mouse button is assumed to be down. If it went up, the node
            # should become unstuck.
            mp = pygame.mouse.get_pos()
            so = stickOffset

            stuckNode.entry.pos = [ mp[0] + so[0], mp[1] + so[1] ]

        if curNode and curNode.entry.flush:
            curNode.entry.flush = False
            curNode.selected    = False

            curNode = None
                
        root.paint_onto( window )

        window.display()

    pygame.quit()
