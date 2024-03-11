import pygame
import random

screen_width = screen_height = 800

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
done = False

number_of_stars = 100
speed = 0.1
stars = [] # К списку не нужны ключи и, в отличии от кортежа его можно изменять

def new_star() -> list:
    star = [random.randint(-screen_width // 2, screen_width // 2),
            random.randint(-screen_height // 2, screen_height // 2), 256, 10]
    return star

for i in range(0, number_of_stars):
    stars.append(new_star())

star_colors = [(random.randint(0, 255), random.randint(0, 255),
                random.randint(0, 255)) for _ in range(number_of_stars)] # создаёт список кортежей из трёх чисел в коллечестве number_of_stars
color_change_time = 1  # Частота изменения цвета в секундах
last_color_change = pygame.time.get_ticks() # Присваивается текущее время в миллисекундах с помощью `pygame.time.get_ticks()`

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0, 0, 0))
    current_time = pygame.time.get_ticks()

    for i in range(0, number_of_stars):
        s = stars[i]

        # x = s[0]
        # y = s[1]
        x = s[0] * 256 / s[2]
        y = s[1] * 256 / s[2]
        s[2] -= speed

        if x < -screen_width / 2 or x > screen_width / 2 or y < -screen_height / 2 or y > screen_height / 2:
            s = new_star()

        if s[3] < 255:
            s[3] += 0.15

        if s[3] > 256:
            s[3] = 255

        stars[i] = s

        x = (s[0] * 256 / s[2]) + screen_width / 2
        y = (s[1] * 256 / s[2]) + screen_height / 2

        if current_time - last_color_change > color_change_time * 1000: # Это условие проверяет, прошло ли определенное количество времени (в миллисекундах) с момента последнего изменения цвета звезды. Если это условие выполняется, значит пришло время изменить цвет.
            star_colors[i] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) # Здесь генерируется новый случайный цвет для звезды
            last_color_change = current_time # После изменения цвета обновляется значение `last_color_change` до текущего времени, чтобы запомнить время последнего изменения цвета.

        pygame.draw.circle(screen, star_colors[i], (x, y), 3)

    pygame.display.flip()
pygame.quit()