import pygame
import random
pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chicken Gold: Empire - By Raphael Daniel")
DHAHABU = (255, 215, 0)
NYEKUNDU = (255, 0, 0)
KIJANI = (34, 139, 34)
BLACK = (0, 0, 0)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 32)
chicken_x = WIDTH // 2
chicken_y = HEIGHT - 100
chicken_size = 40
enemies = []
for i in range(5):
    enemies.append([random.randint(0, WIDTH-40), random.randint(-600, 0)])
golds = []
for i in range(8):
    golds.append([random.randint(0, WIDTH-20), random.randint(-800, 0)])
gold_coins = 0
speed = 5
running = True
while running:
    screen.fill(KIJANI)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and chicken_x > 0:
        chicken_x -= speed
    if keys[pygame.K_RIGHT] and chicken_x < WIDTH - chicken_size:
        chicken_x += speed
    pygame.draw.ellipse(screen, DHAHABU, (chicken_x, chicken_y, chicken_size, chicken_size-10))
    pygame.draw.circle(screen, NYEKUNDU, (chicken_x+30, chicken_y+10), 8)
    for enemy in enemies:
        enemy[1] += 4
        pygame.draw.rect(screen, BLACK, (enemy[0], enemy[1], 40, 40))
        if enemy[1] > HEIGHT:
            enemy[1] = random.randint(-600, 0)
            enemy[0] = random.randint(0, WIDTH-40)
        if chicken_x < enemy[0]+40 and chicken_x+chicken_size > enemy[0] and chicken_y < enemy[1]+40 and chicken_y+chicken_size > enemy[1]:
            gold_coins = 0
            chicken_x = WIDTH // 2
    for gold in golds:
        gold[1] += 3
        pygame.draw.circle(screen, DHAHABU, (gold[0]+10, gold[1]+10), 10)
        if gold[1] > HEIGHT:
            gold[1] = random.randint(-800, 0)
            gold[0] = random.randint(0, WIDTH-20)
        if chicken_x < gold[0]+20 and chicken_x+chicken_size > gold[0] and chicken_y < gold[1]+20 and chicken_y+chicken_size > gold[1]:
            gold_coins += 10
            gold[1] = random.randint(-800, 0)
            gold[0] = random.randint(0, WIDTH-20)
    text = font.render(f"Gold: {gold_coins}", True, DHAHABU)
    screen.blit(text, (10, 10))
    text2 = font.render("Chicken Gold: Empire", True, BLACK)
    screen.blit(text2, (WIDTH//2-90, HEIGHT-50))
    pygame.display.update()
    clock.tick(60)
pygame.quit()