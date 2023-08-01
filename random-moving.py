import pygame
import random

# Initialize PyGame
pygame.init()

# Set up the screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Random Moving Objects in PyGame")

# Random Moving Objects
object_width, object_height = 30, 30
object_speed_range = (2, 7)
objects = []

def create_random_object():
    return {
        'x': random.randint(0, screen_width - object_width),
        'y': random.randint(0, screen_height - object_height),
        'speed': random.randint(*object_speed_range)
    }

for _ in range(5): 
    objects.append(create_random_object())

def draw_object(obj):
    obj_dim = (obj['x'], obj['y'], object_width, object_height)
    pygame.draw.rect(screen, WHITE, obj_dim)

# Random Movement Algorithm
def update_random_movement(obj):
    # Change the direction randomly
    if random.random() < 0.01:  
        obj['speed'] = -obj['speed']

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
    player_pos = (player_x, player_y, player_width, player_height)
    pygame.draw.rect(screen, BLUE, player_pos)

def draw_platform(x):
    plat_pos = (x, platform_y, platform_width, platform_height)
    pygame.draw.rect(screen, WHITE, plat_pos)

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
    
    for obj in objects:
        obj['x'] += obj['speed']
        if obj['x'] > screen_width:
            obj['x'] = -object_width

        update_random_movement(obj)
        draw_object(obj)

    draw_player()
    draw_platform(screen_width // 3)
    draw_platform(2 * screen_width // 3)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
