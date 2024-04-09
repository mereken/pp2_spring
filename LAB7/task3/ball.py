import pygame
import sys
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Moving Ball')
WHITE = (255, 255, 255)
RED = (255, 0, 0)
screen.fill(WHITE)


radius = 25
ball_x = 375
ball_y = 275

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        if ball_y - 5 >= radius:
            ball_y -= 5
    if keys[pygame.K_DOWN]:
        if ball_y + 5 <= 600 - radius:
            ball_y += 5
    if keys[pygame.K_LEFT]:
        if ball_x - 5 >= radius:
            ball_x -= 5
    if keys[pygame.K_RIGHT]:
        if ball_x + 5 <= 800 - radius:
            ball_x += 5
        
    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (ball_x, ball_y), radius, 0)
    
    pygame.display.flip()
 