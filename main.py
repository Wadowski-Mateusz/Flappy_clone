# TODO
# - panel zakończenia gry
# - panel wyboru po uruchomieniu: start, opcje, top, wyjście
# - panel opcji: rodzielczość, fps cap
# - tutorial w menu (sterowanie)

#Python
from sys import exit
from enum import Enum, unique
from random import randint
import datetime

#Extra
import pygame

#Own
import const
import player as player_class
import pipe as pipe_class

@unique
class GameStage(Enum):
    MENU = 1
    GAME = 2
    DEATH_SCREEN = 3
    SCORE = 4
    OPTIONS = 5

#WINDOW
pygame.init()
screen = pygame.display.set_mode((const.window_width, const.window_height))
pygame.display.set_caption('Not Flappy v0.5 | 15 X 2022')

#GAME PREPARATION
clock = pygame.time.Clock()
surface_background = pygame.image.load('graphics/background.png').convert_alpha()

player = pygame.sprite.GroupSingle()
player.add(player_class.Player())

pipes = pygame.sprite.Group()
pipe_spawn = 30

test_font = pygame.font.Font(None, 50)

start = datetime.datetime.now()
t0 = datetime.datetime.now()

game_stage = GameStage.MENU.value

#GAME LOOP
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if game_stage == GameStage.MENU.value:
        background_menu = pygame.image.load('graphics/background_menu.png').convert_alpha()
        bird_size = 100
        bird = pygame.transform.scale(pygame.image.load('graphics/player.png').convert_alpha(), (bird_size, bird_size))
        screen.blit(background_menu, (0,0))
        screen.blit(bird, (const.window_width//2 - bird_size//2, const.window_height//2 - bird_size // 2))
        screen.blit(test_font.render("START", False, 'WHITE'), (const.window_width//2, const.window_height // 2 + 50))
        screen.blit(test_font.render("OPTIONS", False, 'WHITE'), (const.window_width//2, const.window_height // 2 + 100))
        screen.blit(test_font.render("BEST SCORES", False, 'WHITE'), (const.window_width//2, const.window_height // 2 + 150))
        screen.blit(test_font.render("EXIT", False, 'WHITE'), (const.window_width//2, const.window_height // 2 + 200))
        
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            game_stage = GameStage.GAME.value
        

    elif game_stage == GameStage.SCORE.value:
        game_stage = GameStage.DEATH_SCREEN.value

    elif game_stage == GameStage.OPTIONS.value:
        game_stage = GameStage.DEATH_SCREEN.value
    
    elif game_stage == GameStage.DEATH_SCREEN.value:
        for p in pipes:
            p.kill()
        pipe_spawn = 30
        text_surface = test_font.render(f'Your score: {int((t0 - start).seconds)}', False, 'Yellow')
        screen.blit(text_surface, (400, 500))

        if pygame.key.get_pressed()[pygame.K_RETURN]:
            game_stage = GameStage.GAME.value
            start = datetime.datetime.now()
            t0 = datetime.datetime.now()
            player.remove()
            player.add(player_class.Player())        

    elif game_stage == GameStage.GAME.value:
        screen.blit(surface_background, (0,0)) #block image transfer; (0,0) - position
        player.update()
        player.draw(screen)
        
        pipes.update()
        pipes.draw(screen)

        pipe_spawn -= 1
        if pipe_spawn < 0:
            type = randint(0, 30)
            width = randint(20, 28)*5
            height = randint(120, 600)
            if type == 0:
                pipes.add(pipe_class.Pipe(type, width, height))
            elif type == 1:
                pipes.add(pipe_class.Pipe(type, width, height))
            else:
                separation = randint(90, 180)
                top = randint(25, const.window_height - separation - 50)
                bottom = const.window_height - top - separation
                pipes.add(pipe_class.Pipe(0, width, top))
                pipes.add(pipe_class.Pipe(1, width, bottom))
            pipe_spawn = randint(const.frame_cap, const.frame_cap * 3 // 2)
        ###
        text_surface = test_font.render(f'{int((datetime.datetime.now() - start).seconds)} | {int(1000000/(datetime.datetime.now() - t0).microseconds)}', False, 'Red')
        t0 = datetime.datetime.now()
        screen.blit(text_surface, (0, 0))
        ###

        if pygame.sprite.spritecollide(player.sprite, pipes, False):
            text_surface = test_font.render("DEAD", False, 'Red')
            screen.blit(text_surface, (500, 300))
            game_stage = GameStage.DEATH_SCREEN.value

    pygame.display.update()     
    clock.tick(const.frame_cap)
