import random
import collide
import player
import pygame
import entity

pygame.init()

DISPLAY_X = 1280
DISPLAY_Y = 720
FPS = 30

surface = pygame.display.set_mode((DISPLAY_X, DISPLAY_Y), pygame.FULLSCREEN)  # pygame.FULLSCREEN
clock = pygame.time.Clock()

# door = pygame.image.load("cell_door.png")


class Main:
    def __init__(self):
        self.game_exit = False
        self.use_joystick = False
        self.player = player.Player(surface, 300, 300, self.use_joystick)
        if pygame.joystick.get_count():
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
            self.use_joystick = True
            self.player.use_joystick = True
        self.entity1 = entity.Entity(400, 400, 80, 80, 0, surface, 0, (0,0,0))

    def use_joy(self, use):
        if use:
            self.use_joystick = True
            self.player.use_joystick = True
        if not use:
            self.use_joystick = False
            self.player.use_joystick = False

    def game_loop(self):
        while not self.game_exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_exit = True

                if not self.use_joystick:

                    if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_LEFT:
                            self.player.x_acceleration -= self.player.acceleration
                        if event.key == pygame.K_RIGHT:
                            self.player.x_acceleration += self.player.acceleration
                        if event.key == pygame.K_UP:
                            self.player.y_acceleration -= self.player.acceleration
                        if event.key == pygame.K_DOWN:
                            self.player.y_acceleration += self.player.acceleration
                        if event.key == pygame.K_w:
                            self.use_joy(True)

                    if event.type == pygame.KEYUP:

                        if event.key == pygame.K_LEFT:
                            self.player.x_acceleration = 0
                        if event.key == pygame.K_RIGHT:
                            self.player.x_acceleration = 0
                        if event.key == pygame.K_UP:
                            self.player.y_acceleration = 0
                        if event.key == pygame.K_DOWN:
                            self.player.y_acceleration = 0

            if self.use_joystick:
                x_axis = self.joystick.get_axis(0)
                y_axis = self.joystick.get_axis(1)

                # mapping controller floats (~-1 to ~1) to the max velocity
                self.player.x_velocity = round(self.joystick.get_axis(0) * self.player.max_velocity)
                self.player.y_velocity = round(self.joystick.get_axis(1) * self.player.max_velocity)

                if self.joystick.get_button(0):
                    self.use_joy(False)

            surface.fill((255, 255, 255))

            collide.collision_prevent(self.player)

            self.player.move()

            self.entity1.render()

            self.player.render()

            surface.blit(pygame.font.SysFont(None, 25).render(str(self.player.x) + ", " + str(self.player.y), True, (200, 0, 100)), [0,0])
            surface.blit(pygame.font.SysFont(None, 25).render(str(self.player.x_velocity) + ", " + str(self.player.y_velocity), True, (200, 0, 100)), [0,25])
            surface.blit(pygame.font.SysFont(None, 25).render(str(self.player.x_acceleration) + ", " + str(self.player.y_acceleration), True, (200, 0, 100)), [0,50])
            if self.use_joystick:
                surface.blit(pygame.font.SysFont(None, 25).render(
                    str(round(x_axis, 3)) + ", " + str(round(y_axis, 3)), True, (200, 0, 100)), [0, 75])

            pygame.display.update()
            clock.tick(FPS)


main = Main()
main.game_loop()
