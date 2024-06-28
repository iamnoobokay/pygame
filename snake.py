import pygame
import random

pygame.init()
clock = pygame.time.Clock()
running = True
game_active = True

WINDOW_HEIGHT = 640
WINDOW_WIDTH = 720
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (34, 139, 34)
BLACK = 'black'
BLOCK_SIZE = 40
FOOD = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
TICK = 7
FOOD.fill(RED)
SCORE = 0
GAME_OVER_SOUND = pygame.mixer.Sound("game_over.wav")
EAT_SOUND = pygame.mixer.Sound("eat.mp3")
DOWN_SOUND = pygame.mixer.Sound('down.mp3')
LEFT_SOUND = pygame.mixer.Sound('left.mp3')
RIGHT_SOUND = pygame.mixer.Sound('right.mp3')
UP_SOUND = pygame.mixer.Sound('up.mp3')
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
flag = 1

snake = [(120, 40), (80, 40), (40, 40)]
direction = 'RIGHT'


def check_coordinates(check_coordinate):
    return check_coordinate not in snake


def randomFoodPosition():
    while True:
        x = random.randint(0, (WINDOW_WIDTH // BLOCK_SIZE) - 1) * BLOCK_SIZE
        y = random.randint(0, (WINDOW_HEIGHT // BLOCK_SIZE) - 1) * BLOCK_SIZE
        if check_coordinates((x, y)):
            return (x, y)


foodPos = randomFoodPosition()


def makeFood():
    screen.blit(FOOD, randomFoodPosition())


def drawGrids():
    for x in range(0, WINDOW_WIDTH, 40):
        for y in range(0, WINDOW_HEIGHT, 40):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
                LEFT_SOUND.play()
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'
                RIGHT_SOUND.play()
            elif event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
                UP_SOUND.play()
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
                DOWN_SOUND.play()

    head_x, head_y = snake[0]
    if direction == 'RIGHT':
        head_x += BLOCK_SIZE
    elif direction == 'LEFT':
        head_x -= BLOCK_SIZE
    elif direction == 'UP':
        head_y -= BLOCK_SIZE
    elif direction == 'DOWN':
        head_y += BLOCK_SIZE

    new_head = (head_x, head_y)

    if ((new_head[0] >= WINDOW_WIDTH or new_head[0] < 0) or (new_head[1] >= WINDOW_HEIGHT or new_head[1] < 0)):
        GAME_OVER_SOUND.play()
        game_active = not game_active

    if new_head in snake:
        GAME_OVER_SOUND.play()
        game_active = not game_active

    if game_active:
        snake.insert(0, new_head)
        if (new_head[0] == foodPos[0] and new_head[1] == foodPos[1]):
            foodPos = randomFoodPosition()
            screen.blit(FOOD, foodPos)
            SCORE += 1
            EAT_SOUND.play()
            screen.fill(BLACK)
            if (SCORE % 5 == 0):
                TICK += 2
        else:
            snake.pop()
            screen.fill(BLACK)

        for k, segment in enumerate(snake):
            color = ""
            if (k == 0):
                color = GREEN
            else:
                color = WHITE
            pygame.draw.rect(
                screen, color, [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE])

        drawGrids()
        screen.blit(FOOD, foodPos)
        pygame.display.flip()
        clock.tick(TICK)
    else:
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", True, GREEN)
        screen.blit(text, (WINDOW_WIDTH // 2 - text.get_width() //
                    2, WINDOW_HEIGHT // 2 - text.get_height() // 2))
        pygame.display.update()
        while not game_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_active = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                        game_active = True
