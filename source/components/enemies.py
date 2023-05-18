# 몬스터 종류 확실히 정해야 함
import math
import pygame as pg
from .. import setup, tools
from .. import Setting as s

ENEMY_SPEED = 1


class Enemy(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
    
    def setup_enemy(self, x, y, direction, name, sheet, frame_rect_list,        # 몬스터 세팅
                        in_range, range_start, range_end, isVertical=False):
        self.frames = []
        self.frame_index = 0
        self.animate_timer = 0
        self.gravity = 1.5
        self.state = s.WALK
        
        self.name = name
        self.direction = direction
        self.load_frames(sheet, frame_rect_list)
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y
        self.in_range = in_range
        self.range_start = range_start
        self.range_end = range_end
        self.isVertical = isVertical
        self.set_velocity()
        self.death_timer = 0
    
    def load_frames(self, sheet, frame_rect_list):
        for frame_rect in frame_rect_list:
            self.frames.append(tools.get_image(sheet, *frame_rect, s.BLACK, s.SIZE_MULTIPLIER))

    def set_velocity(self): # 몬스터 속도
        if self.isVertical:
            self.x_vel = 0
            self.y_vel = ENEMY_SPEED
        else:
            self.x_vel = ENEMY_SPEED *-1 if self.direction == s.LEFT else ENEMY_SPEED
            self.y_vel = 0
            
    def update(self, game_info, level):
        self.current_time = game_info[s.CURRENT_TIME]
        self.handle_state()
        self.animation()
        self.update_position(level)

    def handle_state(self):             # 상태 (추가해도 됨)
        if (self.state == s.WALK or
            self.state == s.FLY):
            self.walking()
        elif self.state == s.FALL:
            self.falling()
        elif self.state == s.DEATH_JUMP:
            self.death_jumping()
        elif self.state == s.JUMPED_ON:
            self.jumped_on()
        elif self.state == s.REVEAL:
            self.revealing()
    
    def walking(self):
        if (self.current_time - self.animate_timer) > 125:
            if self.direction == s.RIGHT:
                if self.frame_index == 4:
                    self.frame_index += 1
                elif self.frame_index == 5:
                    self.frame_index = 4
            else:
                if self.frame_index == 0:
                    self.frame_index += 1
                elif self.frame_index == 1:
                    self.frame_index = 0
            self.animate_timer = self.current_time
    
    def falling(self):
        if self.y_vel < 10:
            self.y_vel += self.gravity
    
    def death_jumping(self):
        self.rect.y += self.y_vel
        self.rect.x += self.x_vel
        self.y_vel += self.gravity
        if self.rect.y > s.SCREEN_HEIGHT:
            self.kill()
    

    def start_death_jump(self, direction):
        self.y_vel = -8
        self.x_vel = 2 if direction == s.RIGHT else -2
        self.gravity = .5
        self.frame_index = 3
        self.state = s.DEATH_JUMP

    def animation(self):
        self.image = self.frames[self.frame_index]
