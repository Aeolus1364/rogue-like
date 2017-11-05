import pygame
import collide


class Entity:
    def __init__(self, x, y, x_length, y_length, sprite, surface, collide, color):
        self.x = x
        self.y = y
        self.x_length = x_length
        self.y_length = y_length
        self.sprite = sprite
        self.surface = surface
        self.collision_type = collide
        self.color = color

    def render(self):
        # self.surface.blit(self.sprite, (self.x, self.y))  # render sprite
        pygame.draw.rect(self.surface, self.color, [self.x, self.y, self.x_length, self.y_length])

    def collide(self, player):
        if self.collision_type == 0:
            return False
        elif self.collision_type == 1:
            collide.collision_prevent(player, self)
            return False
        elif self.collision_type == 2:
            if collide.collision_detect(player, self):
                return True
