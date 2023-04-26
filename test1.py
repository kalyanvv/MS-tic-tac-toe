import pygame
import sys

pygame.init()

WIDTH = 400
HEIGHT = 300
FONT_SIZE = 64
FPS = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont(None, FONT_SIZE)
clock = pygame.time.Clock()

counter = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # update counter
    counter += 1

    # clear screen
    screen.fill((0, 0, 0))

    # render counter text
    counter_text = font.render(str(counter), True, (255, 255, 255))
    counter_rect = counter_text.get_rect(center=(WIDTH/2, HEIGHT/2))
    screen.blit(counter_text, counter_rect)

    # update display
    pygame.display.update()

    # control frame rate
    clock.tick(FPS)

