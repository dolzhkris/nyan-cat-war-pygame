import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров экрана и FPS
screen_width = 1200
screen_height = 600
FPS = 40
base_flame_rate = 40

# Загрузка изображений
ships_rev = pygame.image.load('images/ship22.png')
ships_rev_rect = ships_rev.get_rect()
ships_rev_rect.left = 0

ship = pygame.image.load('images/ship2.png')
ship_rect = ship.get_rect()
ship_rect.left = 0

# Инициализация часов и шрифта
clock = pygame.time.Clock()
font = pygame.font.SysFont('Times New Roman', 24)

# Загрузка фона
bg = pygame.image.load('images/background.jpg')
bg_rect = bg.get_rect()

# Установка экрана
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Nyan Cat War')

# Класс для хранения и обновления топ-скорости
class TopScore:
    def __init__(self):
        self.high_score = 0

    def topscore(self, score):
        if score > self.high_score:
            self.high_score = score
        return self.high_score

topscore = TopScore()

# Класс НЛО
class NLO:
    def __init__(self):
        self.NLO = pygame.image.load('images/nlo.png')
        self.NLO = pygame.transform.scale(self.NLO, (100, 86))
        self.NLO_rect = self.NLO.get_rect()
        self.NLO_rect.width -= 10
        self.NLO_rect.height -= 10
        self.NLO_rect.top = screen_height / 2
        self.NLO_rect.right = screen_width
        self.up = True
        self.down = False
        self.NLO_velocity = 10
        self.flames_velocity = 20

    def update(self):
        screen.blit(self.NLO, self.NLO_rect)
        if self.NLO_rect.top <= ships_rev_rect.bottom:
            self.up = False
            self.down = True
        elif self.NLO_rect.bottom >= ship_rect.top:
            self.up = True
            self.down = False

        if self.up:
            self.NLO_rect.top -= self.NLO_velocity
        elif self.down:
            self.NLO_rect.top += self.NLO_velocity

# Класс для управления снарядами
class Flames:
    def __init__(self):
        self.flames = pygame.image.load('images/flame.png')
        self.flames_img = pygame.transform.scale(self.flames, (20, 20))
        self.flames_img_rect = self.flames_img.get_rect()
        self.flames_img_rect.right = nlo.NLO_rect.left
        self.flames_img_rect.top = nlo.NLO_rect.top + 30

    def update(self):
        screen.blit(self.flames_img, self.flames_img_rect)
        if self.flames_img_rect.left > 0:
            self.flames_img_rect.left -= nlo.flames_velocity

# Класс для управления Нян Котом
class NyanCat:
    nyan_cat_velocity = 10

    def __init__(self):
        self.nyan_cat = pygame.image.load('images/nyancat.png')
        self.nyan_cat = pygame.transform.scale(self.nyan_cat, (80, 66))
        self.nyan_cat_rect = self.nyan_cat.get_rect()
        self.nyan_cat_rect.left = 50
        self.nyan_cat_rect.top = screen_height / 2 - 100
        self.up = False
        self.down = True

    def update(self):
        screen.blit(self.nyan_cat, self.nyan_cat_rect)
        if self.up:
            self.nyan_cat_rect.top -= self.nyan_cat_velocity
        if self.down:
            self.nyan_cat_rect.top += self.nyan_cat_velocity

        if self.nyan_cat_rect.top <= ships_rev_rect.bottom or self.nyan_cat_rect.bottom >= ship_rect.top:
            game_over()

# Функция для завершения игры
def game_over():
    pygame.mixer.music.stop()
    music = pygame.mixer.Sound('musicandsounds/gameover.mp3')
    music.play()
    topscore.topscore(score)
    game_over_icon = pygame.image.load('images/gameover.png')
    game_over_icon = pygame.transform.scale(game_over_icon, (700, 250))
    game_over_icon_rect = game_over_icon.get_rect()
    game_over_icon_rect.center = (screen_width / 2, screen_height / 2)

    screen.blit(game_over_icon, game_over_icon_rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    music.stop()
                    game_loop()

# Функция для старта игры
def start_game():
    start_game_icon = pygame.image.load('images/start.png')
    start_game_icon = pygame.transform.scale(start_game_icon, (500, 300))
    start_game_icon_rect = start_game_icon.get_rect()
    start_game_icon_rect.center = (screen_width / 2, screen_height / 2)
    screen.blit(start_game_icon, start_game_icon_rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    game_loop()

# Функция для проверки уровня и обновления переменных
def check_level(score):
    global level, new_flame_rate
    if score < 10:
        ships_rev_rect.bottom = 50
        ship_rect.top = screen_height - 50
        level = 1
        new_flame_rate = base_flame_rate
    elif score < 20:
        level = 2
        new_flame_rate = base_flame_rate // 2  # Увеличение частоты выпуска снарядов
    elif score < 30:
        level = 3
        new_flame_rate = base_flame_rate // 3  # Еще большее увеличение частоты
    else:
        level = 4
        new_flame_rate = base_flame_rate // 4  # Максимальное увеличение частоты

# Основной игровой цикл
def game_loop():
    global nlo
    global score
    global level

    nlo = NLO()
    nyan_cat = NyanCat()

    new_flame_counter = 0
    score = 0
    flame_list = []
    pygame.mixer.music.load('musicandsounds/fonmusic.mp3')
    pygame.mixer.music.play(-1, 0.0)

    while True:
        screen.blit(bg, bg_rect)
        check_level(score)
        nlo.update()
        nyan_cat.update()

        new_flame_counter += 1
        if new_flame_counter >= new_flame_rate:
            new_flame_counter = 0
            flame_list.append(Flames())

        for flame in flame_list:
            if flame.flames_img_rect.left <= 0:
                flame_list.remove(flame)
                score += 1
            flame.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    nyan_cat.up = True
                    nyan_cat.down = False
                elif event.key == pygame.K_DOWN:
                    nyan_cat.up = False
                    nyan_cat.down = True
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    nyan_cat.up = False
                    nyan_cat.down = True
                elif event.key == pygame.K_DOWN:
                    nyan_cat.up = False
                    nyan_cat.down = True

        score_font = font.render('Score: ' + str(score), True, (255, 255, 255))
        score_font_rect = score_font.get_rect()
        score_font_rect.center = (200, ships_rev_rect.bottom + score_font_rect.height / 2)
        screen.blit(score_font, score_font_rect)

        level_font = font.render('Level: ' + str(level), True, (255, 255, 255))
        level_font_rect = level_font.get_rect()
        level_font_rect.center = (500, ships_rev_rect.bottom + score_font_rect.height / 2)
        screen.blit(level_font, level_font_rect)

        top_score_font = font.render('Top Score: ' + str(topscore.high_score), True, (255, 255, 255))
        top_score_font_rect = top_score_font.get_rect()
        top_score_font_rect.center = (800, ships_rev_rect.bottom + score_font_rect.height / 2)
        screen.blit(top_score_font, top_score_font_rect)

        screen.blit(ships_rev, ships_rev_rect)
        screen.blit(ship, ship_rect)

        for flame in flame_list:
            if flame.flames_img_rect.colliderect(nyan_cat.nyan_cat_rect):
                game_over()

        pygame.display.update()
        clock.tick(FPS)

start_game()
