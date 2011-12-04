
import sys, pygame

width = 100
height = width
size = width, height
BLACK = 0, 0, 0


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode( size )

    keepGoing = True
    while keepGoing:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                keepGoing = False

        screen.fill( BLACK )
        pygame.display.flip()

    pygame.quit()
