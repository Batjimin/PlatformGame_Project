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

    def update(self, game_info):
        self.current_time = game_info[s.CURRENT_TIME]
        if self.state == s.RESTING:
            self.resting()
        elif self.state == s.BUMPED:
            self.bumped()

    def resting(self):
        time_list = [375, 125, 125, 125]
        if (self.current_time - self.animation_timer) > time_list[self.frame_index]:
            self.frame_index += 1
            if self.frame_index == 4:
                self.frame_index = 0
            self.animation_timer = self.current_time

        self.image = self.frames[self.frame_index]
    
    def bumped(self):
        self.rect.y += self.y_vel
        self.y_vel += self.gravity
        
        if self.rect.y > self.rest_height + 5:
            self.rect.y = self.rest_height
            self.state = s.OPENED
            if self.type == s.TYPE_MUSHROOM:
                self.group.add(powerup.Mushroom(self.rect.centerx, self.rect.y))
            elif self.type == s.TYPE_FIREFLOWER:
                self.group.add(powerup.FireFlower(self.rect.centerx, self.rect.y))
            elif self.type == s.TYPE_LIFEMUSHROOM:
                self.group.add(powerup.ATTENDENCE(self.rect.centerx, self.rect.y))
        self.frame_index = 4
        self.image = self.frames[self.frame_index]
    
    def start_bump(self, score_group):
        self.y_vel = -6
        self.state = s.BUMPED
        
        if self.type == s.TYPE_COIN:
            self.group.add(Coin.Coin(self.rect.centerx, self.rect.y, score_group))
