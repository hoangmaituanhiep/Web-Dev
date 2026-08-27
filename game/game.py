import pygame, sys

pygame.init()

screen = pygame.display.set_mode((720,720))

while True:
  for event in pygame.event.get():
    if event.type() == pygame.QUIT:
      pygame.quit()
      sys.exit()