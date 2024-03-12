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
# Base structure of the code

```
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0, 0, 0))
    current_time = pygame.time.get_ticks() # Declare current time
```
for event in pygame.event.get(): - is a loop that loops through a list of events created by Pygame. 
if event.type == pygame.quit: is a condition that checks the type of the event. In this case, we are checking if the event is a request to quit the application.

```
    for i in range(0, number_of_stars):
        s = stars[i]

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
```
It retrieves the current star's properties (x, y, z, and brightness), calculates the new x and y coordinates based on the ratio of the original x and y positions divided by the z position and scaled by 256. Then decreases the z position by the value stored in the speed variable. If the star's x or y falls outside the boundaries of the screen, a new star is created using the new_star() function. The brightness of the star increases by 0.15 if it's less than 255, and this value is capped at 255 if it exceeds this value. Finally, the updated star properties are stored back into the list of stars at the current index.

```
x = (s[0] * 256 / s[2]) + screen_width / 2
y = (s[1] * 256 / s[2]) + screen_height / 2
```
Now let's implement the movement and verification mechanism. We need to calculate its x and y coordinates for each star at each step in accordance with the perspective (z coordinate).
We can do this as discussed in lecture using the following formulas:
$$X_s = \\frac{X*256}{Z} + X_c$$
$$Y_s = \\frac{X*256}{Z} + Y_c$$



