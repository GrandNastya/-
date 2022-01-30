from hh.seed import Seed
from hh.level import Level
from hh.name import Name
from hh.shop_button import ShopButton


class Interface:
    def __init__(self):
        self.name = Name()
        self.seed = Seed()
        self.level = Level()
        self.shop_button = ShopButton()

    def draw(self, screen):
        self.shop_button.draw(screen)
