import sys, random, pygame
from game_class import GameLife


pygame.init()
w, h = (1600, 1000)
game_life_field_size = (160, 100)
screen = pygame.display.set_mode((w, h),)

matrix = GameLife(game_life_field_size)
matrix.create_figure(cords=(50,50), figure="random")
rect_w = 6
rect_h = 6


while True:
    matrix.step()
    for x in range(game_life_field_size[0]):
        for y in range(game_life_field_size[1]):
            array = matrix.show()
            color = (array[x][y] * 255,
                     array[x][y] * random.randint(100, 255),
                     array[x][y] * random.randint(30, 100)) \
                if array[x][y] == 1 else (100,50,100)

            rect_x = x * rect_w + w / 5
            rect_y = y * rect_h + h / 5
            pygame.draw.rect(screen, color,(rect_x, rect_y, rect_w, rect_h))
    matrix.create_figure(figure="random_call")

    pygame.display.update()
    screen.fill((100,53,100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()