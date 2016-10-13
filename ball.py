from pygame import Rect
from pygame import image
from pygame import Surface


class Ball(object):
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
        if self.x < 0:
            self.x = 600 / 2
            self.y = 400 / 2
        if self.x > 600:
            self.x = 600 / 2
            self.y = 400 / 2
        if self.y <= 0:
            self.y_direction *= -1
        elif self.y >= 400 - self.rect.height:
            self.y_direction *= -1

    def __init__(self, x, y, filename):
        self.x = x
        self.y = y
        self.sprite = image.load(filename)
        self.rect = Rect(self.sprite.get_rect())
        self.rect.x = x
        self.rect.y = y
