
import sys, pygame

width = 100
height = width
size = width, height
BLACK = 0, 0, 0


if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode( size )

    screen.fill( BLACK )
    pygame.display.flip()
