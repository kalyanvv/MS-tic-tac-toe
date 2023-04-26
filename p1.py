import pygame, sys, random
from pygame.locals import *
pygame.init()
 
# Colours
BACKGROUND = (255, 255, 255)
 
# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My tictac toe')
 
# The main function that controls the game
def main () :
  looping = True
  moveX=80
  moveY=80
  # The main game loop
  while looping :
    # Get inputs
    for event in pygame.event.get():
      if event.type == QUIT :
        pygame.quit()
        sys.exit()
      
      if event.type==pygame.KEYDOWN and event.key==K_r:
        moveX=80
        moveY=80

      pressed = pygame.key.get_pressed()
      if (pressed[K_RIGHT] or pressed[K_d]) :
        moveX = moveX + 3
      if (pressed[K_LEFT] or pressed[K_a]) :
        moveX = moveX - 3
      
    # Processing
    # This section will be built out later
 
    # Render elements of the game
    WINDOW.fill(BACKGROUND)
    # takes all the commands which have been sent to the WINDOW and applies them to the actual screen in one go
    rect1=pygame.Rect(20,10,70,30)
    # circle=pygame.
    pygame.draw.rect(WINDOW,"green",rect1)
    pygame.draw.circle(WINDOW,"red",(moveX,moveY),50)
    
    
    
    pygame.display.update()
    fpsClock.tick(FPS)
 
main()