# coin item
import pygame as pg
from .. import setup, tools
from .. import Setting as s


class Coin(pg.sprite.Sprite):
    def __init__(self, x, y, score_group):
        pg.sprite.Sprite.__init__(self)

        self.frames = []
        self.frame_index = 0
        self.load_frames()
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y - 5
        self.gravity = 1
        self.y_vel = -15
        self.animation_timer = 0
        self.initial_height = self.rect.bottom - 5
        self.score_group = score_group

    def load_frames(self):
        sheet = setup.GFX[s.OBJECTS_SHEET]
        frame_rect_list = [(52, 113, 8, 14), (4, 113, 8, 14),
                           (20, 113, 8, 14), (36, 113, 8, 14)]
        for frame_rect in frame_rect_list:
            self.frames.append(tools.get_image(
                sheet, *frame_rect, s.BLACK, s.TILE_SIZE_MULTIPLIER))
    
    def update(self, game_info):
        self.current_time = game_info[s.CURRENT_TIME]