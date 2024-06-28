import pygame
import sys
import random
pygame.init()
clock = pygame.time.Clock()
running = True

rects = []

for i in range(384):
    # rects[i] = [random.randint(100, 1200), 1]
    rects.append(random.randint(0, 720))

screen = pygame.display.set_mode((1920, 720))
running = True
sound = pygame.mixer.Sound("click.mp3")
j = 0
k = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    for i, height in enumerate(rects):
        left = i * 5
        rect = pygame.Rect(left, 720-height, 2, height)
        pygame.draw.rect(screen, (255, 0, 0), rect)

    for _ in range(50):
        if (j < len(rects)):
            if (k < len(rects) - j - 1):
                if (rects[k] > rects[k+1]):
                    temp = rects[k]
                    rects[k] = rects[k+1]
                    rects[k+1] = temp
                k += 1
            else:
                sound.play()
                k = 0
                j += 1
        else:
            pygame.quit()
    pygame.display.flip()
    clock.tick(60)
# pygame.quit()
