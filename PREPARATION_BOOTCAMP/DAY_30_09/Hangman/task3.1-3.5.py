import pygame

# Task 3.2
pygame.init()
WIDTH = HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

# Task 3.4
background = pygame.image.load("assets/background.jpg").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))


# Task 3.5
def draw_stickman(surface, x=300, y=200, color=(0, 0, 0)):
    pygame.draw.circle(surface, color, (x, y), 30, 4)                     # head
    pygame.draw.line(surface, color, (x, y + 30),  (x, y + 150), 4)       # body
    pygame.draw.line(surface, color, (x, y + 60),  (x - 50, y + 110), 4)  # left arm
    pygame.draw.line(surface, color, (x, y + 60),  (x + 50, y + 110), 4)  # right arm.
    pygame.draw.line(surface, color, (x, y + 150), (x - 40, y + 230), 4)  # left leg
    pygame.draw.line(surface, color, (x, y + 150), (x + 40, y + 230), 4)  # right leg


# Task 3.3
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    draw_stickman(screen)
    pygame.display.flip()

pygame.quit()