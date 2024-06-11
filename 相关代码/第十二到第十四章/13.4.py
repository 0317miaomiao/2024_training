import pygame
import sys
from pygame.sprite import Sprite, Group
from random import randint

class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.rain_speed = 1.0
        self.raindrop_width = 20
        self.raindrop_height = 20

class Rain(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # 加载图像并缩放
        self.image = pygame.image.load('alien.png')
        self.image = pygame.transform.scale(self.image, 
                        (self.settings.raindrop_width, self.settings.raindrop_height))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width + 2 * self.rect.width * randint(0, 10)
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.rain_speed
        self.rect.y = self.y

    def check_edges(self):
        if self.rect.top >= self.screen.get_rect().bottom:
            return True

class RainSimulation:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Rain Simulation")

        self.raindrops = Group()
        self._create_rain()

    def run_simulation(self):
        while True:
            self._check_events()
            self._update_raindrops()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_rain(self):
        raindrop = Rain(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        available_space_x = self.settings.screen_width - 2 * raindrop_width
        number_raindrops_x = available_space_x // (2 * raindrop_width)

        for raindrop_number in range(number_raindrops_x):
            self._create_raindrop(raindrop_number)

    def _create_raindrop(self, raindrop_number):
        raindrop = Rain(self)
        raindrop_width = raindrop.rect.width
        raindrop.x = raindrop_width + 2 * raindrop_width * raindrop_number
        raindrop.rect.x = raindrop.x
        self.raindrops.add(raindrop)

    def _update_raindrops(self):
        self.raindrops.update()

        for raindrop in self.raindrops.copy():
            if raindrop.check_edges():
                self.raindrops.remove(raindrop)
                self._create_raindrop(randint(0, 10))

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    rs = RainSimulation()
    rs.run_simulation()
