import pygame
import datetime
import os

pygame.init()
screen = pygame.display.set_mode((1200, 800))
WHITE = (255, 255, 255)
CLOCK_CENTER = (600, 400)

base = 'images'
bg = pygame.image.load(os.path.join(base, 'clock.png')).convert_alpha()
body = pygame.image.load(os.path.join(base, 'mickey_body.png')).convert_alpha()
hand_l_img = pygame.image.load(os.path.join(base, 'hand_left.png')).convert_alpha()
hand_r_img = pygame.image.load(os.path.join(base, 'hand_right.png')).convert_alpha()

bg = pygame.transform.scale(bg, (700, 700))
body = pygame.transform.scale(body, (300, 300))

def make_hand_surface(image, width, height):
    temp_surface = pygame.Surface((width, height * 2), pygame.SRCALPHA)
    resized_hand = pygame.transform.scale(image, (width, height))
    temp_surface.blit(resized_hand, (0, 0))
    return temp_surface

hand_l_base = make_hand_surface(hand_l_img, 70, 220)
hand_r_base = make_hand_surface(hand_r_img, 85, 190)

clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    now = datetime.datetime.now()
    s = now.second
    m = now.minute

    s_angle = -(s * 6)
    m_angle = -(m * 6 + s * 0.1)

    rot_s = pygame.transform.rotate(hand_l_base, s_angle)
    rot_m = pygame.transform.rotate(hand_r_base, m_angle)

    rect_s = rot_s.get_rect(center=CLOCK_CENTER)
    rect_m = rot_m.get_rect(center=CLOCK_CENTER)

    screen.fill(WHITE)
    
    screen.blit(bg, bg.get_rect(center=CLOCK_CENTER))
    screen.blit(body, body.get_rect(center=CLOCK_CENTER))
    
    screen.blit(rot_s, rect_s)
    screen.blit(rot_m, rect_m)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()