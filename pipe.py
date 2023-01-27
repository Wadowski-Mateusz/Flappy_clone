import pygame
import const
from random import randint

class Pipe(pygame.sprite.Sprite):
    def __init__(self, type, width, height):
        super().__init__()
        self.image = pygame.image.load('graphics/pipe.png').convert_alpha()
        if type == 0:
            self.rect = self.image.get_rect(topleft = (const.window_width, 0))
        else:
            self.image = pygame.image.load('graphics/pipe_red.png').convert_alpha()
            self.rect = self.image.get_rect(bottomleft = (const.window_width, const.window_height - height))

        self.rect.w += width
        self.rect.h += height
        self.image = pygame.transform.scale(self.image, (self.rect.w, self.rect.h))
        

    def update(self):
        self.rect.x -= 7
        if self.rect.x <= -self.rect.w:
            self.kill()