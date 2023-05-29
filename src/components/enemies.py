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

    def jumped_on(self):
        pass
    
    def revealing(self):
        pass
    
    def sliding(self):        
        if self.direction == s.RIGHT:
            self.x_vel = 10
        else:
            self.x_vel = -10
    
    def animation(self):
        self.image = self.frames[self.frame_index]
        
    def update_position(self,system):  #위치 업데이트
        self.rect.x += self.x_vel
        self.check_x_collisions()

        if self.in_range and self.isVertical:
            if self.rect.y < self.range_start:
                self.rect.y = self.range_start
                self.y_vel = ENEMY_SPEED
            elif self.rect.bottom > self.range_end:
                self.rect.bottom = self.range_end
                self.y_vel = -1 * ENEMY_SPEED

        self.rect.y += self.y_vel
        if (self.state != s.DEATH_JUMP and 
            self.state != s.FLY):
            self.check_y_collisions()
            
        if self.rect.x <= 0:
            self.kill()
        elif self.rect.y > (system.viewport.bottom):
            self.kill()
        
    def check_x_collisions(self, system):
        if self.in_range and not self.isVertical:
            if self.rect.x < self.range_start:
                self.rect.x = self.range_start
                self.change_direction(s.RIGHT)
            elif self.rect.right > self.range_end:
                self.rect.right = self.range_end

                self.change_direction(s.LEFT)
        else:
            collider = pg.sprite.spritecollideany(self, system.elevator_group)
            if collider:
                if self.direction == s.RIGHT:
                    self.rect.right = collider.rect.left
                    self.change_direction(s.LEFT)
                elif self.direction == s.LEFT:
                    self.rect.left = collider.rect.right
                    self.change_direction(s.RIGHT)

    def change_direction(self, direction):
        self.direction = direction
        if self.direction == s.RIGHT:
            self.x_vel = ENEMY_SPEED
            if self.state == s.WALK or self.state == s.FLY:
                self.frame_index = 4
        else:
            self.x_vel = ENEMY_SPEED * -1
            if self.state == s.WALK or self.state == s.FLY:
                self.frame_index = 0

    def check_y_collisions(self, System):
        if self.rect.bottom >= s.GROUND_HEIGHT:
            sprite_group = System.ground_step_pipe_group
        else:
            sprite_group = pg.sprite.Group(System.elevator_group,
                                           System.tile_group, System.QR_brick_group)
        sprite = pg.sprite.spritecollideany(self, sprite_group)
        if sprite and sprite.name != s.MAP_SLIDER:
            if self.rect.top <= sprite.rect.top:
                self.rect.bottom = sprite.rect.y
                self.y_vel = 0
                self.state = s.WALK
        System.check_is_falling(self)
        
        

class Boo(Enemy):
    def __init__(self, x, y, direction, color, in_range,
                 range_start, range_end, name=s.BOO):
        Enemy.__init__(self)
        frame_rect_list = self.get_frame_rect(color)
        self.setup_enemy(x, y, direction, name, setup.GFX[s.ENEMY_IMAGE],
                         frame_rect_list, in_range, range_start, range_end)
        
        self.frames.append(pg.transform.flip(self.frames[2], False, True))
        self.frames.append(pg.transform.flip(self.frames[0], True, False))
        self.frames.append(pg.transform.flip(self.frames[1], True, False))

    def get_frame_rect(self, color):
        if color == s.COLOR_TYPE_GREEN:
            frame_rect_list = [(0, 34, 16, 16), (30, 34, 16, 16),
                               (61, 30, 16, 16)]
        else:
            frame_rect_list = [(0, 4, 16, 16), (30, 4, 16, 16),
                               (61, 0, 16, 16)]
        return frame_rect_list

    def jumped_on(self):
        self.x_vel = 0
        self.frame_index = 2
        if self.death_timer == 0:
            self.death_timer = self.current_time
        elif (self.current_time - self.death_timer) > 500:
            self.kill()



class Boss(Enemy):
    def __init__(self, x, y, direction, color, in_range,
                range_start, range_end, name=s.BOSS):
        Enemy.__init__(self)
        frame_rect_list = self.get_frame_rect(color)
        self.setup_enemy(x, y, direction, name, setup.GFX[s.ENEMY_IMAGE],
                    frame_rect_list, in_range, range_start, range_end)
    
        self.frames.append(pg.transform.flip(self.frames[2], False, True))
        self.frames.append(pg.transform.flip(self.frames[0], True, False))
        self.frames.append(pg.transform.flip(self.frames[1], True, False))

    def get_frame_rect(self, color):
        if color == s.COLOR_TYPE_GREEN:
            frame_rect_list = [(150, 0, 16, 24), (180, 0, 16, 24),
                        (360, 5, 16, 15)]
        elif color == s.COLOR_TYPE_RED:
            frame_rect_list = [(150, 30, 16, 24), (180, 30, 16, 24),
                        (360, 35, 16, 15)]
        else:
            frame_rect_list = [(150, 60, 16, 24), (180, 60, 16, 24),
                        (360, 65, 16, 15)]
        return frame_rect_list