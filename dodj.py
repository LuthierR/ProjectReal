import pygame
import sys
import random
# insp vid = https://youtu.be/uHIY4OGxh5k?si=AhYZK4ZQQpQxJaO4 series 1-Finish

# 1/11/2023
# 3/11/2023
# 5/11/2023
# 6/11/2023 add game over menu
# 7/11/2023 add game over menu quit and continue
pygame.init()

# Constants
WIDTH, HEIGHT = 500, 650
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Objects")


# meteor1
meteor_image = pygame.image.load("meteorpng.png")
meteor_width, meteor_height = 40, 40
meteor_image = pygame.transform.scale(meteor_image, (meteor_width, meteor_height))
# meteor2
meteor2_image = pygame.image.load("meteor2.png")
meteor2_width, meteor2_height = 40, 40
meteor2_image = pygame.transform.scale(meteor2_image, (meteor2_width, meteor2_height))
# player
player_image = pygame.image.load("plane.png")
player_width, player_height = 60, 60  
player_image = pygame.transform.scale(player_image, (player_width, player_height))
player_rect = player_image.get_rect()
player_rect.center = (WIDTH // 2, HEIGHT - player_height // 2)
# bg
background_image = pygame.image.load("background.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
# menu
menu_font = pygame.font.Font(None, 40)
menu_text = menu_font.render("Press SPACE to play", True, WHITE)
menu_rect = menu_text.get_rect(center=(WIDTH//2,HEIGHT//2))
# obj
object_size = 20
object_speed = 10
# game over
continue_font = pygame.font.Font(None, 30)
game_over_font = pygame.font.Font(None, 80)
game_over_text = game_over_font.render("GAME OVER", True, WHITE)
continue_text = continue_font.render("Press SPACE to CONTINUE", True, WHITE)
game_over_rect = game_over_text.get_rect(center=(WIDTH//2,HEIGHT//3))
continue_rect = continue_text.get_rect(center=(WIDTH//2,HEIGHT//2))
escape_font = pygame.font.Font(None, 20)
escape_text = escape_font.render("Press Continue and Hover mouse out the Window to Quit", True, WHITE)
escape_rect = escape_text.get_rect(center=(WIDTH//2,HEIGHT//3+200))
falling_objects = []

def display_game_over_statistics():
    screen.fill(BLACK)
    screen.blit(game_over_text, game_over_rect)

    stats_font = pygame.font.Font(None, 36)
    score_text = stats_font.render(f"Score: {score}", True, WHITE)
    stats_text_rect = score_text.get_rect(center=(WIDTH//2, HEIGHT//4))
    screen.blit(score_text, stats_text_rect)

    continue_text = continue_font.render("Press SPACE to Restart", True, WHITE)
    continue_rect = continue_text.get_rect(center=(WIDTH//2, HEIGHT//2))
    screen.blit(continue_text, continue_rect)

    pygame.display.update()

def create_falling_object():
    x = random.randint(0, WIDTH - meteor_width)
    y = 0
    return {'x': x, 'y': y}

def draw_falling_objects(falling_objects):
    for obj in falling_objects:
        screen.blit(meteor_image, (obj['x'], obj['y']))

# var defin
score = 0
game_over = False
game_started = False
clock = pygame.time.Clock()
delay_timer = 60

# main 
# def play():
while not game_over:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not game_started:
                game_started = True
        if keys[pygame.K_SPACE] and game_over == True:
            game_over = False
    for event in pygame.event.get():
            if not game_started and game_over:
                game_started = True
                game_over = False
                score = 0
                falling_objects = []
            elif event.key == pygame.K_ESCAPE:
                game_over = True
    

    if not game_started:
        screen.fill(BLACK)
        screen.blit(menu_text, menu_rect)
        pygame.display.update()
        continue

    for obj in falling_objects:
        obj['y'] += object_speed

    draw_falling_objects(falling_objects)


    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += 5

    screen.fill(BLACK)

    screen.blit(background_image,(0,0))

    screen.blit(player_image, player_rect)

    if random.randint(1, 100) < 5:
        falling_objects.append(create_falling_object())
    
    if score >= 2000:
        meteor_image_to_use =  meteor2_image
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


    # if game_over == True:
    #     screen.fill(BLACK)
    #     screen.blit(game_over_text, game_over_rect)
    #     screen.blit(continue_text, continue_rect)
    #     pygame.display.update()
    #     continue


    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         game_over = True
    #     elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
    #         if not game_started:
    #             game_started = True
    pygame.display.update()
    clock.tick(FPS)
# while game_over ==  True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             game_over = True
#         elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
#             if not game_started:
#                 game_started = True
                
    # if game_over == True:
    #     screen.fill(BLACK)
    #     screen.blit(game_over_text, game_over_rect)
    #     screen.blit(continue_text, continue_rect)
    #     pygame.display.update()

#     if keys[pygame.K_SPACE]:
#         game_over = True
    # if keys[pygame.K_LEFT] and player_rect.left > 0:
    #     player_rect.x -= 5
    # if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
    #     player_rect.x += 5
    while game_over:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if game_over:
                    game_started = True
                    game_over = False
                    score = 0
                    falling_objects = []
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)
        screen.blit(escape_text, escape_rect)
        screen.blit(game_over_text, game_over_rect)
        screen.blit(continue_text, continue_rect)
        pygame.display.update()
