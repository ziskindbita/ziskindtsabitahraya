import pygame
import time
import random

black = (0,0,0)
white = (255,255,255)

pygame.init()

surfaceWidth = 800
surfaceHeight = 480
surface = pygame.display.set_mode((surfaceWidth, surfaceHeight))

pygame.display.set_caption('Helicopter')
clock = pygame.time.Clock()

img = pygame.image.load('Helicopter.png')
imgWidth = 100
imgHeight = 43

high_score = 0

def score(count):
  font = pygame.font.Font('freesansbold.ttf', 20)
  text = font.render("Score: "+ str(count), True, white)
  surface.blit(text, [0,0])

def highScore(count):
  font = pygame.font.Font('freesansbold.ttf', 20)
  text = font.render("High Score: "+ str(count), True, white)
  surface.blit(text, [0,30])

def blocks(x_block, y_block, gap, block_width, block_height):
  pygame.draw.rect(surface, white, [x_block, y_block, block_width, block_height])
  pygame.draw.rect(surface, white, [x_block, y_block + gap + block_height, block_width, surfaceHeight])

def replay_or_quit():
  for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()

    elif event.type == pygame.KEYDOWN:
      continue
    
    return event.key
  
  return None

def makeTextObjs(text, font):
  textSurface = font.render(text, True, white)
  return textSurface, textSurface.get_rect()

def msgSurface(text):
  smallText = pygame.font.Font('freesansbold.ttf', 20)
  largeText = pygame.font.Font('freesansbold.ttf', 120)

  titleTextSurf, titleTextRect = makeTextObjs(text, largeText)
  titleTextRect.center = (surfaceWidth / 2), (surfaceHeight / 2)
  surface.blit(titleTextSurf, titleTextRect)

  typTextSurf, typTextRect = makeTextObjs('Press any key to continue', smallText)
  typTextRect.center =  surfaceWidth / 2, ((surfaceHeight / 2) + 100)
  surface.blit(typTextSurf, typTextRect)

  pygame.display.update()
  time.sleep(1)

  while replay_or_quit() == None:
    clock.tick()

  main()

def gameOver():
  msgSurface('Anda Kalah')

def helicopter(x, y, image):
  surface.blit(img, (x,y))

def generateBlockHeight():
  return random.randint(40, surfaceHeight/2)

def main():
  x = 150
  y = 200

  x_block = surfaceWidth
  y_block = 0

  block_width = 80
  block_height = generateBlockHeight()
  gap = 125
  block_move = 6

  y_move = 0
  game_over = False

  current_score = 0
  global high_score

  while not game_over:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        game_over = True

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          y_move = -5
          
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
          y_move = 5

    y += y_move

    surface.fill(black)
    helicopter(x ,y, img)
    score(current_score)
    highScore(high_score)

    blocks(x_block, y_block, gap, block_width, block_height)
    x_block -= block_move

    if current_score > high_score:
      high_score = current_score

    if x_block < (-1 * block_width):
      x_block = surfaceWidth
      block_height = generateBlockHeight()

    if y > surfaceHeight-imgHeight or y < 0:
      gameOver()

    if x + imgWidth > x_block:
      if x < x_block + block_width:
        if y < y_block + block_height or y + imgHeight > block_height + gap:
          gameOver()
    
    if x < x_block and x > x_block - block_move:
      current_score += 1

    pygame.display.update()
    clock.tick(60)

main()
pygame.quit()
quit()