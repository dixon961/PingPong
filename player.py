from pygame import Rect
from pygame import image
from pygame import Surface


class Player(object):
    x = 0
    y = 0

    rect = Rect(0, 0, 0, 0)
    sprite = Surface((0, 0))
    sprite_name = 'default.jpg'
    y_direction = 0
    x_direction = 0
    speed = 0.5

    def update(self):
        self.x += self.speed * self.x_direction
        self.y += self.speed * self.y_direction
        self.rect.x = self.x
        self.rect.y = self.y

    def __init__(self, x, y, filename):
        self.x = x
        self.y = y
        self.sprite = image.load(filename)
        self.rect = Rect(self.sprite.get_rect())
        self.rect.x = x
        self.rect.y = y
