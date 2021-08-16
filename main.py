import random
import pygame
from itertools import product
import time


# todo : add multiple missiles, multiple enemies, their multiple missiles, remaining missile count.
# todo : remove bugs in enemy count and score.


# Classes.
class GameWindow:
    def __init__(self, height=None, width=None):
        # initialising pygame.
        pygame.init()
        if height is None:
            height = 800
        if height is None:
            width = 700
        self.height = height
        self.width = width
        self.window = pygame.display.set_mode((self.height, self.width))
        self.bg_img = None

    def get_window(self):
        return self.window

    def set_title(self, title=None):
        if title is None:
            title = "Space Shooter"
            pygame.display.set_caption(title)

    def set_logo(self, logo=None):
        if logo is None:
            logo = pygame.image.load("logo.png")
            pygame.display.set_icon(logo)

    def set_bg_img(self, bg_img=None):
        self.bg_img = bg_img
        if self.bg_img is None:
            self.bg_img = pygame.image.load('bg_img.jpg')

    def show_bg_img(self):
        # adding bg color to game window.
        self.window.fill((0, 0, 0))
        # adding bg image to the game window.
        self.window.blit(self.bg_img, (0, 0))

    def set_bg_music(self):
        # adding bg music to game window.
        pygame.mixer.music.load("bg_music.wav")
        # this will play the bg music again and again.
        pygame.mixer.music.play(-1)


class Character:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos


class Player:
    def __init__(self, x_pos, y_pos):
        if x_pos is None:
            x_pos = 0
        if y_pos is None:
            y_pos = 0
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.player_img = None

    def set_img(self, player_img=None):
        self.player_img = player_img
        if self.player_img is None:
            self.player_img = pygame.image.load("player.png")

    def show_img(self, window, x=None, y=None):
        if x is not None:
            self.x_pos = x
        if y is not None:
            self.y_pos = y
        window.blit(self.player_img, (self.x_pos, self.y_pos))


class Enemy:
    def __init__(self, x_pos, y_pos):
        if x_pos is None:
            x_pos = 0
        if y_pos is None:
            y_pos = 0
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enemy_img = None

    def set_img(self, player_img=None):
        self.player_img = player_img
        if self.player_img is None:
            self.enemy_img = pygame.image.load("player.png")

    def show_img(self, window, x=None, y=None):
        if x is not None:
            self.x_pos = x
        if y is not None:
            self.y_pos = y
        window.blit(self.enemy_img, (self.x_pos, self.y_pos))


class GameSounds:
    def __init__(self):
        # # # # # Fire Sound # # # # #
        self.fire_sound = pygame.mixer.Sound('laser.wav')

        # # # # # Explosion Sound # # # # #
        self.blast_sound = pygame.mixer.Sound('explosion.wav')


# functions.
# def player(screen, img, x, y):
#     screen.blit(img, (x, y))


def enemy(screen, img, x, y):
    screen.blit(img, (x, y))


def blast(screen, img, x, y):
    screen.blit(img, (x, y))


def fire_player_missile(screen, img, x, y):
    screen.blit(img, (x + 16, y + 10))


def fire_enemy_missile(screen, img, x, y):
    screen.blit(img, (x + 16, y + 22))


def show_score(screen, font, score, x, y, color):
    if color == 'green':
        score_text = font.render(f"Score : {score}", True, (0, 255, 0))
    else:
        score_text = font.render(f"Score : {score}", True, (255, 255, 255))
    screen.blit(score_text, (x, y))


def show_enemy_count(screen, font, enemies, x, y, color):
    if color == 'green':
        enemy_count_text = font.render(f"Enemies : {enemies}", True, (0, 255, 0))
    elif color == 'red':
        enemy_count_text = font.render(f"Enemies : {enemies}", True, (255, 0, 0))
    else:
        enemy_count_text = font.render(f"Enemies : {enemies}", True, (255, 255, 255))
    screen.blit(enemy_count_text, (x, y))


def show_game_over(screen, font, x, y):
    score_text = font.render(f"Game Over", True, (255, 0, 0))
    screen.blit(score_text, (x, y))


def show_you_won(screen, font, x, y):
    score_text = font.render(f"You Won!", True, (0, 255, 0))
    screen.blit(score_text, (x, y))


def show_player_health(screen, font, health, x, y, color):
    if color == 'green':
        player_health_text = font.render(f"Player's Health : {health}", True, (0, 255, 0))
    elif color == 'red':
        player_health_text = font.render(f"Player's Health : {health}", True, (255, 0, 0))
    elif color == 'blue':
        player_health_text = font.render(f"Player's Health : {health}", True, (0, 0, 255))
    else:
        player_health_text = font.render(f"Player's Health : {health}", True, (255, 255, 255))

    screen.blit(player_health_text, (x, y))


def show_enemy_health(screen, font, health, x, y, color):
    if color == 'green':
        enemy_health_text = font.render(f"Enemy's Health : {health}", True, (0, 255, 0))
    elif color == 'red':
        enemy_health_text = font.render(f"Enemy's Health : {health}", True, (255, 0, 0))
    elif color == 'blue':
        enemy_health_text = font.render(f"Enemy's Health : {health}", True, (0, 0, 255))
    else:
        enemy_health_text = font.render(f"Enemy's Health : {health}", True, (255, 255, 255))

    screen.blit(enemy_health_text, (x, y))


def main():
    game_window = GameWindow(800, 700)

    # # # # # Game Window or Screen # # # # #
    window = game_window.get_window()

    # # # # # Title # # # # #
    game_window.set_title()
    # # # # # Logo # # # # #
    game_window.set_logo()
    # # # # # Background Image # # # # #
    game_window.set_bg_img()
    # # # # # Background Music # # # # #
    game_window.set_bg_music()

    sounds = GameSounds()
    fire_sound = sounds.fire_sound
    blast_sound = sounds.blast_sound

    # # # # # player # # # # #
    # setting default x and y coordinates of player.
    player_img_width = 64
    player_x = (game_window.height // 2) - (player_img_width // 2)
    player_y = game_window.width - player_img_width - (game_window.width * 0.02)
    player = Player(player_x, player_y)
    # setting player's character's ship image.
    player.set_img(window)

    # space of game window to be left so player can not exceed boundary limits.
    space_left = 0.01
    max_left_space = game_window.height - (game_window.height - (game_window.height * space_left))
    max_right_space = game_window.height - player_img_width - (game_window.height * space_left)
    max_up_space = game_window.width - (game_window.width - game_window.width * space_left)
    max_down_space = game_window.width - player_img_width - (game_window.width * space_left)

    # setting speed of changing position of player.
    change_x = 1
    change_y = 1

    # speed of change to be made in position of player.
    player_x_change_left = 0
    player_x_change_right = 0
    player_y_change_up = 0
    player_y_change_down = 0

    # flags to overwrite buttons of same arrow pair.
    # means if left and right are pressed together then last pressed will be counted.
    flag_x_left = False
    flag_x_right = False

    # # # # # Enemy # # # # #
    # setting enemy's character's ship image.
    enemy_img_width = 64
    flag_y_up = False
    flag_y_down = False
    enemy_img = pygame.image.load("enemy.png")
    enemy_speed = 0.8
    # setting default x and y coordinates of enemy.
    enemy_x = random.randint(int(max_left_space), int(max_right_space))
    enemy_y = random.randint(int(game_window.width * 0.02), game_window.width // 3)

    # # # # # Player's Missile # # # # #
    # setting player's character's ship image.
    player_missile_img_width = 32
    player_missile_img = pygame.image.load("player_missile.png")
    # missile has two states : 'ready', 'fire'
    player_missile_state = 'ready'
    player_missile_speed = 1.5
    # setting default x and y coordinates of missile.
    player_missile_x = - player_missile_img_width
    player_missile_y = - player_missile_img_width

    # # # # # Enemy's Missile # # # # #
    # setting enemy's character's ship image.
    enemy_missile_img_width = 32
    enemy_missile_img = pygame.image.load("enemy_missile.png")
    # missile has two states : 'ready', 'fire'
    enemy_missile_state = 'ready'
    enemy_missile_speed = 0.7
    # setting default x and y coordinates of enemy's missile.
    enemy_missile_x = - enemy_missile_img_width
    enemy_missile_y = - enemy_missile_img_width

    # # # # # Blast # # # # #
    blast_img = pygame.image.load('blast.png')
    blast_img_width = 32
    enemy_blast_x = - blast_img_width
    enemy_blast_y = - blast_img_width
    player_blast_x = - blast_img_width
    player_blast_y = - blast_img_width
    blast_show_time = 0.1

    # # # # # Score # # # # #
    score_font = pygame.font.Font('Ubuntu-Medium.ttf', 32)
    score_font_x = max_left_space
    score_font_y = max_up_space

    # # # # # Player Health # # # # #
    player_health_font = pygame.font.Font('Ubuntu-Medium.ttf', 32)
    player_health_font_x = game_window.height - max_left_space - 280
    player_health_font_y = max_up_space

    # # # # # Enemy Health # # # # #
    enemy_health_font = pygame.font.Font('Ubuntu-Medium.ttf', 32)
    enemy_health_font_x = game_window.height - max_left_space - 280
    enemy_health_font_y = max_up_space + 40

    # # # # # Game Over # # # # #
    game_over_font = pygame.font.Font('Ubuntu-Medium.ttf', 64)
    game_over_font_x = 215
    game_over_font_y = 300

    # # # # # You Won # # # # #
    you_won_font = pygame.font.Font('Ubuntu-Medium.ttf', 64)
    you_won_font_x = 230
    you_won_font_y = 300

    # # # # # Enemy Count # # # # #
    enemy_count_font = pygame.font.Font('Ubuntu-Medium.ttf', 32)
    enemy_count_font_x = max_left_space
    enemy_count_font_y = max_up_space + 40

    # # # # # Game Loop # # # # #
    enemy_pos = 'left'
    running = True
    total_reset = True
    enemy_reset = True
    player_health = 5
    enemy_health = 3
    enemy_count = 5
    score = 0
    game_over = False
    you_won = False
    enemy_blast_flag = False
    enemy_blast_time = 0
    player_blast_flag = False
    player_blast_time = 0
    player_reset = False
    while running:
        if player_reset:
            enemy_missile_x = - player_missile_img_width
            enemy_missile_y = - player_missile_img_width
            enemy_missile_state = 'ready'
            player_reset = False

        if enemy_reset:
            player_missile_x = - player_missile_img_width
            player_missile_y = - player_missile_img_width
            player_missile_state = 'ready'
            enemy_reset = False

        if total_reset:
            if enemy_health != 3:
                enemy_count -= 1
            enemy_health = 3
            enemy_pos = 'left'
            enemy_x = random.randint(int(max_left_space), int(max_right_space))
            enemy_y = random.randint(int(game_window.width * 0.02), game_window.width // 3)
            player_missile_x = - player_missile_img_width
            player_missile_y = - player_missile_img_width
            player_missile_state = 'ready'
            enemy_missile_x = - enemy_missile_img_width
            enemy_missile_y = - enemy_missile_img_width
            enemy_missile_state = 'ready'
            total_reset = False

        # adding bg image.
        game_window.show_bg_img()

        # showing the score.
        if score >= 12:
            show_score(window, score_font, score, score_font_x, score_font_y, 'green')
        else:
            show_score(window, score_font, score, score_font_x, score_font_y, '')

        # showing the player's health.
        if player_health >= 4:
            show_player_health(window, player_health_font, player_health, player_health_font_x, player_health_font_y,
                               'green')
        if player_health == 3:
            show_player_health(window, player_health_font, player_health, player_health_font_x, player_health_font_y,
                               '')
        if player_health <= 2:
            show_player_health(window, player_health_font, player_health, player_health_font_x, player_health_font_y,
                               'red')

        # showing the Enemy Count.
        if enemy_count >= 4:
            show_enemy_count(window, enemy_count_font, enemy_count, enemy_count_font_x, enemy_count_font_y, 'red')
        if enemy_count == 3:
            show_enemy_count(window, enemy_count_font, enemy_count, enemy_count_font_x, enemy_count_font_y, '')
        if enemy_count <= 2:
            show_enemy_count(window, enemy_count_font, enemy_count, enemy_count_font_x, enemy_count_font_y, 'green')

        if you_won:
            show_you_won(window, you_won_font, you_won_font_x, you_won_font_y)

        if game_over:
            show_game_over(window, game_over_font, game_over_font_x, game_over_font_y)

        # getting the event list of happening events in game window inside game loop.
        event_list = pygame.event.get()
        event_type_list = [i.type for i in event_list]
        event_key_list = [i.key for i in event_list if (i.type == pygame.KEYUP) or (i.type == pygame.KEYDOWN)]

        # checking if quit / 'x' button was pressed.
        if pygame.QUIT in event_type_list:
            running = False

        if player_blast_flag and ((time.time() - player_blast_time) < blast_show_time):
            blast(window, blast_img, player_blast_x, player_blast_y)

        if (not game_over) and (not you_won):

            # showing the enemy's health.
            if enemy_health >= 3:
                show_enemy_health(window, enemy_health_font, enemy_health, enemy_health_font_x, enemy_health_font_y,
                                  'green')
            if enemy_health == 2:
                show_enemy_health(window, enemy_health_font, enemy_health, enemy_health_font_x, enemy_health_font_y, '')
            if enemy_health <= 1:
                show_enemy_health(window, enemy_health_font, enemy_health, enemy_health_font_x, enemy_health_font_y,
                                  'red')

            # drawing the enemy on the surface of game window at the start of the game.
            enemy(window, enemy_img, enemy_x, enemy_y)

            # drawing the player on the surface of game window at the start of the game.
            player.show_img(window, player_x, player_y)

            # listing keystroke events.
            if pygame.KEYDOWN in event_type_list:
                if pygame.K_LEFT in event_key_list:
                    player_x_change_left = - change_x
                    flag_x_left = True
                    flag_x_right = False
                if pygame.K_RIGHT in event_key_list:
                    player_x_change_right = change_x
                    flag_x_right = True
                    flag_x_left = False

                if pygame.K_UP in event_key_list:
                    player_y_change_up = - change_y
                    flag_y_up = True
                    flag_y_down = False
                if pygame.K_DOWN in event_key_list:
                    player_y_change_down = change_y
                    flag_y_down = True
                    flag_y_up = False

                if (pygame.K_SPACE in event_key_list) and (player_missile_state == 'ready'):
                    fire_sound.play()
                    player_missile_x = player_x
                    player_missile_y = player_y
                    fire_player_missile(window, player_missile_img, player_missile_x, player_missile_y)
                    player_missile_state = 'fire'

            if pygame.KEYUP in event_type_list:
                if pygame.K_LEFT in event_key_list:
                    player_x_change_left = 0
                    flag_x_left = False
                if pygame.K_RIGHT in event_key_list:
                    player_x_change_right = 0
                    flag_x_right = False

                if pygame.K_UP in event_key_list:
                    player_y_change_up = 0
                    flag_y_up = False
                if pygame.K_DOWN in event_key_list:
                    player_y_change_down = 0
                    flag_y_down = False

            # player movements.
            if ((player_x + player_x_change_left) >= max_left_space) and (
                    (player_x + player_x_change_left) <= max_right_space) and flag_x_left:
                player_x += player_x_change_left
            if ((player_x + player_x_change_right) >= max_left_space) and (
                    (player_x + player_x_change_right) <= max_right_space) and flag_x_right:
                player_x += player_x_change_right

            if ((player_y + player_y_change_up) >= max_up_space) and (
                    (player_y + player_y_change_up) <= max_down_space) and flag_y_up:
                player_y += player_y_change_up
            if ((player_y + player_y_change_down) >= max_up_space) and (
                    (player_y + player_y_change_down) <= max_down_space) and flag_y_down:
                player_y += player_y_change_down

            # enemy movements.
            if enemy_pos == 'left':
                enemy_x += enemy_speed
            if enemy_pos == 'right':
                enemy_x -= enemy_speed

            if enemy_x <= max_left_space:
                enemy_y += enemy_img_width
                enemy_pos = 'left'
            if enemy_x >= max_right_space:
                enemy_y += enemy_img_width
                enemy_pos = 'right'

            # player missile movements.
            if player_missile_y <= - player_missile_img_width:
                player_missile_y = - player_missile_img_width
                player_missile_x = - player_missile_img_width
                player_missile_state = 'ready'

            if player_missile_state == "fire":
                player_missile_y -= player_missile_speed
                fire_player_missile(window, player_missile_img, player_missile_x, player_missile_y)

            # enemy missile ready.
            if enemy_missile_state == 'ready':
                enemy_missile_x = enemy_x
                enemy_missile_y = enemy_y
                fire_enemy_missile(window, enemy_missile_img, enemy_missile_x, enemy_missile_y)
                enemy_missile_state = 'fire'

            # enemy missile movements.
            if enemy_missile_y >= game_window.width + enemy_missile_img_width:
                enemy_missile_y = - enemy_missile_img_width
                enemy_missile_x = - enemy_missile_img_width
                enemy_missile_state = 'ready'

            if enemy_missile_state == "fire":
                enemy_missile_y += enemy_missile_speed
                fire_enemy_missile(window, enemy_missile_img, enemy_missile_x, enemy_missile_y)

            # # # # # enemy-player collision or game-over system # # # # #

            # creating set of all coordinates of player positions.
            player_x_set = set(range(int(player_x), int(player_x + player_img_width), 1))
            player_y_set = set(range(int(player_y), int(player_y + player_img_width), 1))
            player_pos_set = set(product(player_x_set, player_y_set))

            # creating set of all coordinates of enemy positions.
            enemy_x_set = set(range(int(enemy_x), int(enemy_x + enemy_img_width), 1))
            enemy_y_set = set(range(int(enemy_y), int(enemy_y + enemy_img_width), 1))
            enemy_pos_set = set(product(enemy_x_set, enemy_y_set))

            # creating set of all coordinates of player missile positions.
            player_missile_x_set = set(
                range(int(player_missile_x), int(player_missile_x + player_missile_img_width), 1))
            player_missile_y_set = set(
                range(int(player_missile_y), int(player_missile_y + player_missile_img_width), 1))
            player_missile_pos_set = set(product(player_missile_x_set, player_missile_y_set))

            # creating set of all coordinates of enemy missile positions.
            enemy_missile_x_set = set(range(int(enemy_missile_x), int(enemy_missile_x + enemy_missile_img_width), 1))
            enemy_missile_y_set = set(range(int(enemy_missile_y), int(enemy_missile_y + enemy_missile_img_width), 1))
            enemy_missile_pos_set = set(product(enemy_missile_x_set, enemy_missile_y_set))

            # enemy - missile collision.
            if player_missile_pos_set & enemy_pos_set:
                enemy_health -= 1
                score += 1
                enemy_reset = True

            # player - missile collision.
            if enemy_missile_pos_set & player_pos_set:
                player_health -= 1
                player_reset = True

            # Enemy Reset.
            if enemy_health == 0:
                blast_sound.play()
                enemy_blast_x = enemy_x
                enemy_blast_y = enemy_y
                enemy_blast_flag = True
                enemy_blast_time = time.time()
                total_reset = True

            if enemy_blast_flag and ((time.time() - enemy_blast_time) < blast_show_time):
                blast(window, blast_img, enemy_blast_x, enemy_blast_y)
                if (time.time() - enemy_blast_time) >= blast_show_time:
                    enemy_blast_time = 0
                    enemy_blast_flag = False

            # player - enemy collision.
            if player_pos_set & enemy_pos_set:
                player_health -= 1
                total_reset = True

            # You Won.
            if score >= 15:
                you_won = True

            # Game Over.
            if (player_health == 0) and (not player_blast_flag):
                blast_sound.play()
                player_blast_x = player_x
                player_blast_y = player_y
                player_blast_time = time.time()
                player_blast_flag = True
                game_over = True

        # updating / attaching changes to the game window.
        pygame.display.update()


if __name__ == '__main__':
    main()
