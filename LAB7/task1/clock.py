# import pygame
# import datetime
# from sys import exit


# pygame.init()
# screen = pygame.display.set_mode((1400, 1050))

# bg_image = pygame.image.load('mickey.png')
# sec_img = pygame.image.load('left.png')
# min_img = pygame.image.load('right.png')


# rect = bg_image.get_rect(center=(700, 525))

# process = True
# while process :
#     screen.blit(bg_image, (0, 0))
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             process = False

#     time = datetime.datetime.now().time()
#     angle_sec = -(time.second * 6)
#     sec_in_img = pygame.transform.rotate(sec_img, angle_sec)
#     sec_rect = sec_in_img.get_rect(center=rect.center)
#     screen.blit(sec_in_img, sec_rect.topleft)

#     min_angle = -(time.minute * 6)
#     nmin_img = pygame.transform.rotate(min_img, min_angle)
#     min_rect = nmin_img.get_rect(center=rect.center)
#     screen.blit(nmin_img, min_rect.topleft)

#     pygame.display.flip()


import pygame as pg 
from datetime import datetime as dt

pg.init()
screen = pg.display.set_mode((800, 800))
window_title = pg.display.set_caption("Mickeymouse clock")
# icon = pg.display.set_icon(pg.image.load(r"clock_assets/icon.png"))
clock = pg.time.Clock()

clock_surf = pg.image.load('mickey.png')
leftarm_surf = pg.image.load('left.png')
rightarm_surf = pg.image.load('right.png')
bg_rect = clock_surf.get_rect(center = (400, 400))

done = False

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    current_time = dt.now().time()

    seconds_angle = -(current_time.second * 6)
    minutes_angle = -(current_time.minute * 6)

    rotated_leftarm = pg.transform.rotate(leftarm_surf, seconds_angle)
    rotated_rightarm = pg.transform.rotate(rightarm_surf, minutes_angle)

    leftarm_rect = rotated_leftarm.get_rect(center = bg_rect.center)
    rightarm_rect = rotated_rightarm.get_rect(center = bg_rect.center)

    screen.blit(clock_surf, bg_rect)
    screen.blit(rotated_leftarm, leftarm_rect)
    screen.blit(rotated_rightarm, rightarm_rect)

    pg.display.flip()
    clock.tick(60)


# import pygame
# import sys
# import time
# import math

# pygame.init()

# # Set up the screen
# screen = pygame.display.set_mode((800, 800))
# pygame.display.set_caption("Simple Clock")

# # Load clock image and hands
# clock_img = pygame.image.load("mickey.png")
# long_hand = pygame.image.load("left.png")
# short_hand = pygame.image.load("right.png")

# # Clock variables
# clock_radius = 150
# clock_center = (400, 400)
# long_hand_length = 100
# short_hand_length = 80
# seconds_arc_length = 6

# clock_bg_color = (255, 255, 255)
# hand_color = (0, 0, 0)

# clock_font = pygame.font.SysFont(None, 36)

# def draw_clock():
#     screen.fill(clock_bg_color)
#     screen.blit(clock_img, (50, 50))

# def draw_hand(rot_angle, length, hand_img):
#     rotated_hand = pygame.transform.rotozoom(hand_img, -rot_angle, 1)
#     rotated_hand_rect = rotated_hand.get_rect(center=clock_center)
#     rotated_hand_rect.top = clock_center[1] - length
#     screen.blit(rotated_hand, rotated_hand_rect)

# def main():
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

#         current_time = time.localtime()
#         sec_angle = 360 * current_time.tm_sec / 60
#         min_angle = 360 * current_time.tm_min / 60

#         draw_clock()
#         draw_hand(sec_angle, long_hand_length, long_hand)
#         draw_hand(min_angle, short_hand_length, short_hand)

#         pygame.display.flip()
#         pygame.time.delay(1000)

# if __name__ == "__main__":
#     main()
