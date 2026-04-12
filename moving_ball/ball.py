import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Начальные координаты центра шара
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
radius = 25
step = 20

clock = pygame.time.Clock()

done = False
while not done:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # Проверяем: если шагнем вверх, не выйдет ли край шара (y - radius) за 0
                if ball_y - step >= radius:
                    ball_y -= step
            elif event.key == pygame.K_DOWN:
                # Проверяем нижнюю границу (высота экрана)
                if ball_y + step <= HEIGHT - radius:
                    ball_y += step
            elif event.key == pygame.K_LEFT:
                # Проверяем левую границу
                if ball_x - step >= radius:
                    ball_x -= step
            elif event.key == pygame.K_RIGHT:
                # Проверяем правую границу (ширина экрана)
                if ball_x + step <= WIDTH - radius:
                    ball_x += step

    pygame.draw.circle(screen, RED, (ball_x, ball_y), radius)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()