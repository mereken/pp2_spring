import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (239, 83, 80)
GREEN = (102, 187, 106)
BLUE = (66, 165, 245)

BRUSH_SIZE = 13
ERASER_SIZE = 20

current_color = BLACK

def draw_rect(surface, color, start_pos, end_pos):
    pygame.draw.rect(surface, color, pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])))

def draw_circle(surface, color, center, radius):
    pygame.draw.circle(surface, color, center, radius)

def draw_right_triangle(surface, color, start_pos, end_pos):
    pygame.draw.polygon(surface, color, [(start_pos[0], start_pos[1]),(start_pos[0],end_pos[1]),((start_pos[0] + end_pos[0]) // 2, start_pos[1]),(end_pos[0], end_pos[1])])

def draw_equilateral_triangle(surface, color, start_pos, end_pos):
    pygame.draw.polygon(surface, color, [(start_pos[0], end_pos[1]), ((start_pos[0] + end_pos[0]) // 2, start_pos[1]), (end_pos[0], end_pos[1])])

def draw_rhombus(surface, color, start_pos, end_pos):
    center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
    width = abs(end_pos[0] - start_pos[0])
    height = abs(end_pos[1] - start_pos[1])

def equilateral_triangle(surface, color, start_pos, end_pos):
    pygame.draw.polygon(surface, color, [(start_pos[1] - 50, end_pos[1] + 50), (x2, y2), (x2 + 50, y2 + 50)])


def right_triangle(screen):
    pygame.draw.polygon(screen, colors[current_color], [(x2, y2), (x2 + 50, y2), (x2, y2 - 50)])


def rhombus(screen):
    pygame.draw.polygon(screen, colors[current_color],
                        [(x2 - 30, y2 + 20), (x2, y2), (x2 + 30, y2 + 20), (x2, y2 + 40)])
    pygame.draw.polygon(surface, color, [(center[0],start_pos[1]), (end_pos[0], center[1]), (center[0], end_pos[1]), (start_pos[0], center[1])])
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Простой Paint")


left_button_pressed = False
right_button_pressed = False
drawing_mode = "brush"  
start_pos = (0, 0)  
screen.fill(WHITE)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                left_button_pressed = True
                start_pos = event.pos
            elif event.button == 3:  
                right_button_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                left_button_pressed = False
            elif event.button == 3:
                right_button_pressed = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:  
                drawing_mode = "rect"
            elif event.key == pygame.K_c: 
                drawing_mode = "circle"
            elif event.key == pygame.K_e:  
                drawing_mode = "eraser"
            elif event.key == pygame.K_d:  
                drawing_mode = "brush"
            elif event.key == pygame.K_1:
                drawing_mode = "right_triangle"
            elif event.key == pygame.K_2:
                drawing_mode == "equilateral_triangle"
            elif event.key == pygame.K_u:
                drawing_mode == "rhombus"
            elif event.key == pygame.K_4:
                drawing_mode == "square"
            elif event.key == pygame.K_k:  
                current_color = BLACK
            elif event.key == pygame.K_w:  
                current_color = WHITE
            elif event.key == pygame.K_r: 
                current_color = RED
            elif event.key == pygame.K_g: 
                current_color = GREEN
            elif event.key == pygame.K_b:  
                current_color = BLUE

    if left_button_pressed or right_button_pressed:
        if drawing_mode == "brush":
            if left_button_pressed:
                pygame.draw.circle(screen, current_color, pygame.mouse.get_pos(), BRUSH_SIZE)
            elif right_button_pressed:
                pygame.draw.circle(screen, current_color, pygame.mouse.get_pos(), BRUSH_SIZE*2)
        elif drawing_mode == "rect":
            if left_button_pressed:
                draw_rect(screen, current_color, start_pos, pygame.mouse.get_pos())
        elif drawing_mode == "circle":
            if left_button_pressed:
                radius = ((pygame.mouse.get_pos()[0] - start_pos[0])**2 + (pygame.mouse.get_pos()[1] - start_pos[1])**2)**0.5
                draw_circle(screen, current_color, start_pos, int(radius))
        elif drawing_mode == "eraser":
            if left_button_pressed:
                pygame.draw.circle(screen, WHITE, pygame.mouse.get_pos(), ERASER_SIZE)
        elif drawing_mode == "square":
            if left_button_pressed:
                end_pos = pygame.mouse.get_pos()
                square_size = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_position[1]))
                draw_rect(screen, current_color, start_pos, (start_position[0] + square_size, start_position[1] + square_size))
        elif drawing_mode == "right_triangle":
            if left_button_pressed:
                end_pos = pygame.mouse.get_pos()
                draw_rect(screen, current_color, start_pos, end_pos)
                pygame.draw.polygon(screen, current_color, [(start_pos[0], end_pos[1]), end_pos, start_pos])
        elif drawing_mode == "equilateral_triangle":
            if left_button_pressed:
                draw_equilateral_triangle(screen, current_color, start_pos, pygame.mouse.get_pos())
        elif drawing_mode == "rhombus":
            if left_button_pressed:
                # draw_rhombus(screen, current_color, start_pos, pygame.mouse.get_pos())
                end_pos = pygame.mouse.get_pos()
                side_length = abs(end_pos[0] - start_position[0])
                height = side_length * 3**0.5 / 2
                draw_rect(screen, current_color, start_pos, (start_pos[0] + side_length, start_pos[1] + height))
                pygame.draw.polygon(screen, current_color, [(start_pos[0], start_pos[1] + height), (start_pos[0] + side_length, start_pos[1] + height), (start_pos[0] + side_length / 2, start_pos[1])])
    pygame.display.flip()
pygame.quit()
