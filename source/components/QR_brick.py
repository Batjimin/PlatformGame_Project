# itembox
import pygame as pg
from .. import setup, tools
from .. import Setting as s
from . import Coin, powerup


class QR_brick(pg.sprite.sprite):
    def __init__(self, x, y, type, group=None, name=s.QR_BRICK):
        pg.sprite.Sprite.__init__(self)

        self.frames = []
        self.frame_index = 0
        self.load_frames()
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.rest_height = y
        self.animation_timer = 0
        self.first_half = True   # First half of animation cycle
        self.state = s.STAYED
        self.y_vel = 0
        self.gravity = 1.2
        self.type = type
        self.group = group
        self.name = name
