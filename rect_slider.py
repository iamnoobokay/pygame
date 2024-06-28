import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Slider Example')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


class Slider:
    def __init__(self, x, y, width, height, min_val, max_val, initial_val):
        self.rect = pygame.Rect(x, y, width, height)
        self.min_val = min_val
        self.max_val = max_val
        self.val = initial_val
        self.button_rect = pygame.Rect(x, y - 10, 20, 30)
        self.dragging = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                mouse_x = event.pos[0]
                self.val = self.min_val + \
                    (self.max_val - self.min_val) * \
                    (mouse_x - self.rect.x) / self.rect.width
                self.val = max(self.min_val, min(self.max_val, self.val))

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, self.rect)
        self.button_rect.x = self.rect.x + (self.rect.width - self.button_rect.width) * (
            self.val - self.min_val) / (self.max_val - self.min_val)
        pygame.draw.rect(screen, RED, self.button_rect)


class RectangleDrawer:
    def __init__(self):
        self.rect_width = 40
        self.rect_height = 30

    def draw(self, screen, num_rectangles):
        for i in range(num_rectangles):
            rect_x = (i % 10) * (self.rect_width + 10) + 50
            rect_y = (i // 10) * (self.rect_height + 10) + 50
            pygame.draw.rect(screen, BLACK, (rect_x, rect_y,
                             self.rect_width, self.rect_height))


def main():
    slider = Slider(100, 550, 600, 10, 0, 100, 10)
    rect_drawer = RectangleDrawer()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            slider.handle_event(event)

        # Clear screen
        screen.fill(WHITE)

        # Draw slider
        slider.draw(screen)

        # Draw rectangles
        rect_drawer.draw(screen, int(slider.val))

        # Update display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
