
import sys, pygame

width = 500
height = width
size = width, height
BLACK = 0, 0, 0
WHITE = 255, 255, 255


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode( size )

    font = pygame.font.Font( None, 25 )
    text = font.render( "Hello World", True, WHITE )

    keepGoing = True
    while keepGoing:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                keepGoing = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    keepGoing = False

        screen.blit( text, [50,50] )

        pygame.display.flip()
        screen.fill( BLACK )

    pygame.quit()
