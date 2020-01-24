import pygame
import pygame.font


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for x in range(self.width):
            for y in range(self.height):
                if self.board[y][x] == 1:
                    pygame.draw.rect(screen, (255, 0, 0),
                                     ((self.left + x * self.cell_size, self.top + y * self.cell_size),
                                      (self.cell_size, self.cell_size)), 0)
                elif self.board[y][x] == 2:
                    pygame.draw.rect(screen, (255, 255, 255),
                                     ((self.left + x * self.cell_size, self.top + y * self.cell_size),
                                      (self.cell_size, self.cell_size)), 0)

                pygame.draw.rect(screen, (255, 255, 255),
                                 ((self.left + x * self.cell_size, self.top + y * self.cell_size),
                                  (self.cell_size, self.cell_size)), 2)

    def get_clicked(self, pos):
        cell_x = pos[0] // self.cell_size
        cell_y = pos[1] // self.cell_size
        if 0 <= cell_x <= self.width and 0 <= cell_y <= self.height and map[cell_y][cell_x] == '#':
            self.board[cell_y][cell_x] = (self.board[cell_y][cell_x] + 1)
            print(map[cell_y][cell_x])
        elif 0 <= cell_x <= self.width and 0 <= cell_y <= self.height and map[cell_y][cell_x] == '.':
            self.board[cell_y][cell_x] = (self.board[cell_y][cell_x] + 2)


def load_level(filename):
    filename = filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


map = load_level('map.txt')
print(map)  # 919191)


board = Board(10, 10)
board.set_view(0, 0, 50)
running = True
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
'''font = pygame.font.Font(None, 30)
text_coord = 300
intro_text = ["1",
                  "2",
                  "4"
                  "4"]
for line in intro_text:
    string_rendered = font.render(line, 1, pygame.Color('black'))
    intro_rect = string_rendered.get_rect()
    text_coord += 10
    intro_rect.top = text_coord
    intro_rect.x = 10
    text_coord += intro_rect.height
    screen.blit(string_rendered, intro_rect)'''
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.type == 1:
                board.get_clicked(event.pos)

    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
