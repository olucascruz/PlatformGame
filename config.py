import pygame

WHITE = (255, 255, 255)
image_square = pygame.image.load("img/block_square.png")
image_player = pygame.image.load("img/player.png")
image_soldier = pygame.image.load("img/soldier.png")
image_background = pygame.image.load("img/industrial.png")
image_start = pygame.image.load("img/Start-Button.png")
map_data = [
    [2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
]
map_data2 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2],
    [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
    [2, 2, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
quadrant_size = 75
SCREEN_WIDTH = 900
SCREEN_HEIGHT = len(map_data) * quadrant_size

image_background_transformed = pygame.transform.scale(image_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
