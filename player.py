import pygame


class Player:
    def __init__(self, surface, x, y, use_joystick):
        self.surface = surface
        self.use_joystick = use_joystick
        self.x = x
        self.y = y
        self.x_past = x
        self.y_past = x
        self.x_velocity = 0
        self.y_velocity = 0
        self.x_acceleration = 0
        self.y_acceleration = 0
        self.acceleration = 4
        self.max_velocity = 5
        self.velocity_decay = 4
        self.x_length = 60
        self.y_length = 60
        self.color = (0, 255, 0)

    def move(self):
        # if velocity is below min, increase velocity
        if self.max_velocity > self.x_velocity > -self.max_velocity:
            self.x_velocity += self.x_acceleration
        if self.max_velocity > self.y_velocity > -self.max_velocity:
            self.y_velocity += self.y_acceleration

        self.x_past = self.x
        self.y_past = self.y

        self.x += self.x_velocity
        self.y += self.y_velocity

        # if the acceleration is 0 or if velocity exceeds max, decay velocity
        if not self.use_joystick:
            if self.x_acceleration == 0 or self.x_velocity > self.max_velocity or self.x_velocity < -self.max_velocity:
                if self.x_velocity > 0:
                    self.x_velocity -= self.velocity_decay
                elif self.x_velocity < 0:
                    self.x_velocity += self.velocity_decay
                if abs(self.x_velocity) < self.velocity_decay:
                    self.x_velocity = 0
            if self.y_acceleration == 0 or self.y_velocity > self.max_velocity or self.y_velocity < -self.max_velocity:
                if self.y_velocity > 0:
                    self.y_velocity -= self.velocity_decay
                elif self.y_velocity < 0:
                    self.y_velocity += self.velocity_decay
                if abs(self.y_velocity) < self.velocity_decay:
                    self.y_velocity = 0

        # if self.use_joystick:
        #     if abs(self.x_velocity) < self.velocity_decay:
        #         self.x_velocity = 0
        #     if abs(self.y_velocity) < self.velocity_decay:
        #         self.y_velocity = 0

    def render(self):
        # self.surface.blit()
        pygame.draw.rect(self.surface, self.color, [self.x, self.y, self.x_length, self.y_length])