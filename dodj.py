import pygame
import sys
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 400, 500
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Objects")

player_image = pygame.image.load("plane.png")
player_width, player_height = 40, 40  
player_image = pygame.transform.scale(player_image, (player_width, player_height))
player_rect = player_image.get_rect()
player_rect.center = (WIDTH // 2, HEIGHT - player_height // 2)

object_size = 20
object_speed = 10

falling_objects = []

def create_falling_object():
    x = random.randint(0, WIDTH - object_size)
    y = 0
    return {'x': x, 'y': y}

def draw_falling_objects(falling_objects):
    for obj in falling_objects:
        pygame.draw.rect(screen, WHITE, (obj['x'], obj['y'], object_size, object_size))

score = 0
game_over = False

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5

    screen.fill(BLACK)


    screen.blit(player_image, player_rect)

    if random.randint(1, 100) < 5:
        falling_objects.append(create_falling_object())

    for obj in falling_objects:
        obj['y'] += object_speed

    draw_falling_objects(falling_objects)


    for obj in falling_objects:
        if player_rect.colliderect(pygame.Rect(obj['x'], obj['y'], object_size, object_size)):
            game_over = True


    falling_objects = [obj for obj in falling_objects if obj['y'] <= HEIGHT]


    score += len(falling_objects)


    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
