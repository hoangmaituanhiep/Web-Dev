import pygame, sys
from pathlib import Path
from entity import Big, Bullet, Gun

pygame.init()

screen = pygame.display.set_mode((720,720))
asset_path = Path(__file__).parent / "assets"
background = pygame.image.load(str(asset_path / "bg.png"))
gun = pygame.image.load(str(asset_path / "Objects" / "bullet-full.png"))
bullet = pygame.image.load(str(asset_path / "Objects" / "bullet.png"))

while True:
  for event in pygame.event.get():
    screen.blit(background, (0,0))
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()