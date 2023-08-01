import pygame
import random

# Initialize PyGame
pygame.init()

# Set up the screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Random Moving Objects in PyGame")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Player
player_width, player_height = 50, 50
player_x, player_y = screen_width // 2, screen_height // 2
player_speed = 5

# Platforms
platform_width, platform_height = 100, 20
platform_y = screen_height - 50

clock = pygame.time.Clock()

def draw_player():
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

def draw_platform(x):
    pygame.draw.rect(screen, WHITE, (x, platform_y, platform_width, platform_height))

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    draw_player()
    draw_platform(screen_width // 3)
    draw_platform(2 * screen_width // 3)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
