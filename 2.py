#шаблон
import pygame
#создаём переменные для ширины и высоты
WIDTH = 360
HEIGHT = 480

FPS = 30 # переменная для ограничения по фпс

# Создание цветов в RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем игру и окно
pygame.init() #запуск pygame
pygame.mixer.init() #запуск штуки для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #создаём окно игры
pygame.display.set_caption("Game 3000") # название игры
clock = pygame.time.Clock()

# Цикл игры
running = True
while running:
    clock.tick(FPS) # Команда tick() просит pygame определить, сколько занимает цикл(кадр), а затем сделать паузу, чтобы цикл (кадр) длился нужное время
                    # в общем нужно для того чтобы игра работла в 30 FPS
    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверка на закрытие окна
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    
    # Рендеринг
    
    screen.fill(BLACK)
    # После отрисовки всего, переворачиваемт экран
    pygame.display.flip()

pygame.quit()