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

meteor_image = pygame.image.load("meteorpng.png")
meteor_width, meteor_height = 40, 40
meteor_image = pygame.transform.scale(meteor_image, (meteor_width, meteor_height))

meteor2_image = pygame.image.load("meteor2.png")
meteor2_width, meteor2_height = 40, 40
meteor2_image = pygame.transform.scale(meteor2_image, (meteor2_width, meteor2_height))

player_image = pygame.image.load("plane.png")
player_width, player_height = 40, 40  
player_image = pygame.transform.scale(player_image, (player_width, player_height))
player_rect = player_image.get_rect()
player_rect.center = (WIDTH // 2, HEIGHT - player_height // 2)

background_image = pygame.image.load("background.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

object_size = 20
object_speed = 10

falling_objects = []

def create_falling_object():
    x = random.randint(0, WIDTH - meteor_width)
    y = 0
    return {'x': x, 'y': y}

def draw_falling_objects(falling_objects):
    for obj in falling_objects:
        screen.blit(meteor_image, (obj['x'], obj['y']))

score = 0
game_over = False

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    for obj in falling_objects:
        obj['y'] += object_speed

    draw_falling_objects(falling_objects)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5

    screen.fill(BLACK)

    screen.blit(background_image,(0,0))

    screen.blit(player_image, player_rect)

    if random.randint(1, 100) < 5:
        falling_objects.append(create_falling_object())
    
    if score >= 2000:
        meteor_image_to_use =   meteor2_image
    else:
        meteor_image_to_use = meteor_image
    
    for obj in falling_objects:
        screen.blit(meteor_image_to_use, (obj['x'], obj['y']))

    for obj in falling_objects:
        if player_rect.colliderect(pygame.Rect(obj['x'], obj['y'], meteor_width, meteor_height)):
            game_over = True


    falling_objects = [obj for obj in falling_objects if obj['y'] <= HEIGHT]

    if score >= 2000:
        meteor_image = meteor2_image


    score += len(falling_objects)


    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
