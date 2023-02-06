import pygame

pygame.init()

# переменные
bg = pygame.image.load("images/bg.png")
bg = pygame.transform.scale(bg, (1000,1000))
car = pygame.image.load("images/car.png")
car = pygame.transform.scale(car, (64, 140))
car_2 = pygame.image.load("images/car_2.png")
car_2 = pygame.transform.scale(car_2, (64, 140))
finish = pygame.image.load("images/finish.png")
window = pygame.display.set_mode((1000, 600))
screen = pygame.Surface((1000, 600))

# bool
start_game = True
finish_1 = False
finish_2 = False

text_font = pygame.font.SysFont("comicsansmc", 80)
text_render = text_font.render("Выиграл игрок 1", 0, (0,0,0))
text_render_2 = text_font.render("Выиграл игрок 2", 0, (0,0,0))

y_car = 440
y_car_2 = 440


while start_game:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            start_game = False
        if i.type == pygame.KEYDOWN and i.key == pygame.K_w:
            y_car -= 5
        if i.type == pygame.KEYDOWN and i.key == pygame.K_UP:
            y_car_2 -= 5
    if y_car < 50 and finish_2 == False:
        screen.blit(text_render, (200, 200))
        finish_1 = True
    if y_car_2 < 50 and finish_1 == False:
        screen.blit(text_render_2, (200, 200))
        finish_2 = True
    window.blit(screen, (0,0))
    screen.blit(bg, (0,0))
    screen.blit(finish, (0,-80))
    screen.blit(car, (400, y_car))
    screen.blit(car_2, (500, y_car_2))

    pygame.display.update()





pygame.quit()
