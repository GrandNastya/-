import pygame

from interface import Interface


class Main:
    def __init__(self):
        pygame.init()
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 600
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.interface = Interface()

def start(self):
    while True:
        self.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 0

    def draw(self):
        self.interface.draw(self.screen)




main = Main()
main.start()