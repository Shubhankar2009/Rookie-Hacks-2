import pygame
import random
import math
import time

from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('HACKATHON : A GAME')

# Landing Page

title_font = pygame.font.Font('font/PressStart2P-Regular.ttf', 30)
title_y = 10
title_x = 10

def title(x, y):
    pointt = title_font.render("HACKATHON : A GAME", True, (255, 255, 255))
    screen.blit(pointt, (title_x, title_y))

landingImg = pygame.image.load('images/landing.png')
landing_x = 10
landing_y = 50

def landing(x, y):
    screen.blit(landingImg, (x, y))

# Player
playerImg = pygame.image.load('images/coding.png')
player_x = 350
player_y = 4800
player_x_change = 0
player_y_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# Enemy

enemyImg = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 3

mylist = ['images/bad.png', 'images/banned.png', 'images/puzzle.png']

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load(random.choice(mylist)))
    enemy_x.append(1000)
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(0.6)
    enemy_y_change.append(0)


def enemy(x, y):
    screen.blit(enemyImg[i], (x, y))


# Bullet

bulletImg = pygame.image.load('images/bullet.png')
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 3
bullet_state = "ready"


def bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


# Score
score = 0
font = pygame.font.Font('font/PressStart2P-Regular.ttf', 32)
score_x = 4000
score_y = 20


def show_score(x, y):
    point = font.render("SCORE :" + str(score), True, (255, 255, 255))
    screen.blit(point, (score_x, score_y))


# Game Over
game_font = pygame.font.Font('font/PressStart2P-Regular.ttf', 70)
game_y = 200
game_x = 230


def game_over(x, y):
    point2 = game_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(point2, (game_x, game_y))


# Try Again
try_again_font = pygame.font.Font('font/PressStart2P-Regular.ttf', 25)
try_again_y = 300
try_again_x = 100


def try_again(x, y):
    point_t = try_again_font.render("PRESS TAB TO PARTICIPATE AGAIN", True, (255, 255, 255))
    screen.blit(point_t, (try_again_x, try_again_y))


# Bullet Left

bullet_left_font = pygame.font.Font('font/PressStart2P-Regular.ttf', 50)
bullet_left_y = 2000
bullet_left_x = 200
bullet_left = 20


def Bulletleftfunc(x, y):
    point_t = bullet_left_font.render("BULLET LEFT:" + str(bullet_left), True, (50, 50, 50))
    screen.blit(point_t, (bullet_left_x, bullet_left_y))


# First Position
first_font = pygame.font.Font('font/PressStart2P-Regular.ttf', 30)
first_y = 200
first_x = 100


def first(x, y):
    point_f = first_font.render("CONGRATULATION ! OUR WINNER", True, (255, 255, 255))
    screen.blit(point_f, (first_x, first_y))


# Second Position
second_font = pygame.font.Font('font/PressStart2P-Regular.ttf', 30)
second_y = 200
second_x = 60


def second(x, y):
    point_s = second_font.render("CONGRATULATION! OUR RUNNER UP", True, (255, 255, 255))
    screen.blit(point_s, (second_x, second_y))


# Third Position
third_font = pygame.font.Font('font/PressStart2P-Regular.ttf', 25)
third_y = 200
third_x = 50


def third(x, y):
    point_t = third_font.render("CONGRATULATION! OUR SECOND RUNNER UP", True, (255, 255, 255))
    screen.blit(point_t, (third_x, third_y))


# Your Project Zone
Yourproject_font = pygame.font.Font('font/PressStart2P-Regular.ttf', 50)
Yourproject_y = 1000
Yourproject_x = 20


def Yourproject(x, y):
    point_g = pygame.transform.rotate(Yourproject_font.render("YOUR PROJECT", True, (255, 255, 255)), 90)
    screen.blit(point_g, (Yourproject_x, Yourproject_y))


# Collision Function
def collision_happen(bullet_x, bullet_y, enemy_x, enemy_y):
    collision = math.sqrt((math.pow(enemy_x - bullet_x, 2)) + (math.pow(enemy_y - bullet_y, 2)))
    if collision < 27:
        return True
    else:
        return False

started = False
gameisover = False
run = True

# Main loop
while run:
    screen.fill((0, 0, 0))
    # Key Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change -= 1.5
            if event.key == pygame.K_RIGHT:
                player_x_change += 1.5
            if event.key == pygame.K_SPACE:
                if started:
                    if bullet_left != 0:
                        if bullet_state == "ready":
                            bullet_Sound = mixer.Sound('audio/laser.wav')
                            bullet_Sound.play()
                            bullet_x = player_x
                            bullet(player_x, bullet_y)
                            bullet_left -= 1
            # Restart Event
            if event.key == pygame.K_TAB:
                if gameisover:
                    Yourproject_y = 0
                    bullet_left = 20
                    score = 0
                    bullet_left_x = 200
                    gameisover = False
                    bullet_y_change = 3
                    started = True
            #Landing page to game
            if event.key == pygame.K_BACKSPACE:
                if not started:
                    player_y = 480
                    score_x = 400
                    Yourproject_y = 0
                    bullet_left_y = 200
                    started = True
                    landing_y = 10000
                    title_y = 10000
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_x_change = 0
            if event.key == pygame.K_RIGHT:
                player_x_change = 0
            if event.key == pygame.K_BACKSPACE:
                if not started:
                    landing_y = 10000
                    title_y = 10000
                    player_y = 480
                    score_x = 400
                    Yourproject_y = 0
                    bullet_left_y = 200
                    started = True

    # Enemy If Else
    for i in range(num_of_enemies):
        enemy_x[i] -= enemy_x_change[i]

        if enemy_x[i] <= 80:
            enemy_x[i] = random.randint(936, 1000)
            enemy_y[i] = random.randint(50, 250)
            # Decreasing Score BY One
            if score > 0:
                if gameisover == False:
                    score -= 1

        # Collision
        collide = collision_happen(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collide:
            explosion_Sound = mixer.Sound('audio/explosion.wav')
            explosion_Sound.play()
            score += 1
            print(score)
            bullet_y = 480
            bullet_state = "ready"
            enemy_x[i] = random.randint(936, 1000)
            enemy_y[i] = random.randint(0, 150)

        enemy(enemy_x[i], enemy_y[i])

    # Game Over
    if bullet_left == 0:
        if bullet_state == "ready":
            Yourproject_y = 2000
            gameisover = True
            try_again(try_again_x, try_again_y)
            if score >= 5:
                bullet_y_change = 0.1
                bullet_left_x = 2000
                started = False
                first(first_x, first_y)

            if score == 4:
                bullet_y_change = 0.1
                started = False
                bullet_left_x = 2000
                second(second_x, second_y)

            if score == 3:
                bullet_y_change = 0.1
                started = False
                bullet_left_x = 2000
                third(third_x, third_y)
            if score < 3:
                game_over(game_x, game_y)
                bullet_y_change = 0.1
                bullet_left_x = 2000
                gameover = True
                started = False
                try_again_y = 350
                try_again_x = 150

    if player_x <= 80:
        player_x = 80

    if player_x >= 936:
        player_x = 936

    if bullet_state == "fire":
        bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"

    player_x += player_x_change
    player(player_x, player_y)
    enemy(enemy_x[i], enemy_y[i])
    show_score(score_x, score_y)
    Bulletleftfunc(bullet_left_x, bullet_left_y)
    Yourproject(Yourproject_x, Yourproject_y)
    title(title_x, title_y)
    landing(landing_x, landing_y)
    pygame.display.update()
