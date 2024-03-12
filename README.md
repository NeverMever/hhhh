# Discription

Choosing the data for varaibales 
```
number_of_stars = 120
speed = 0.4
stars = []
```
For "stars" we choose list. The list does not need keys and, unlike a tuple, it can be modified.

```
def new_star() -> list:
    star = [random.randint(-screen_width // 2, screen_width // 2),
            random.randint(-screen_height // 2, screen_height // 2), 256, 0]
    return star
```
The first two values allow us to get a random point to generate a star.

# Generating a star
```
for i in range(0, number_of_stars):
    stars.append(new_star())

star_colors = [(random.randint(0, 255), random.randint(0, 255),
                random.randint(0, 255)) for _ in range(number_of_stars)] # создаёт список кортежей из трёх чисел в коллечестве number_of_stars
color_change_time = 1  # Частота изменения цвета в секундах
last_color_change = pygame.time.get_ticks() # Присваивается текущее время в миллисекундах с помощью `pygame.time.get_ticks()`
```
