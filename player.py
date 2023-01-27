import pygame
import const

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(midleft = const.player_start_position)
        self.gravity = -1


    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.gravity = -8
        if keys[pygame.K_LEFT]:
            if self.rect.x > 0:
                self.rect.x -= 4
        if keys[pygame.K_RIGHT]:
            if self.rect.x < const.window_width - 50:
                self.rect.x += 4

    def apply_gravity(self):
        if self.rect.top < 0:
            self.gravity = 0
            self.rect.top = 0
        elif self.rect.bottom > const.window_height:
            self.gravity = 0
            self.rect.bottom = const.window_height
        else:
            self.gravity += 1
            self.rect.y += self.gravity

    def update(self):
        self.player_input()
        self.apply_gravity()