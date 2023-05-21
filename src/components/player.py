#다 안썼수..
import os
import json
import pygame as pg
from .. import setup, tools
from .. import Setting as Set
from ..components import powerup

class Player(pg.sprite.Sprite):
    def __init__(self, player_name):
        pg.sprite.Sprite.__init__(self)
        self.player_name = player_name
        self.load_data()
        self.setup_timer()
        self.setup_state()
        self.setup_speed()
        self.load_images()
        
        if Set.DEBUG:
            self.right_frames = self.big_fire_frames[0]
            self.left_frames = self.big_fire_frames[1]
            self.big = True
            self.fire = True
            
        self.frame_index = 0
        self.state = Set.WALK
        self.image = self.right_frames[self.frame_index]
        self.rect = self.image.get_rect()
        
    def restart(self):
        if self.dead:
            self.dead = False
            self.big = False
            self.fire = False
            self.set_player_image(self.small_normal_frames, 0)
            self.right_frames = self.small_normal_frames[0]
            self.left_frames = self.small_normal_frames[1]
        self.state = Set.STAND
        
    def load_data(self):
        player_file = 'student'+'.json'
        file_path = os.path.join('src', 'data', player_file)
        f = open(file_path)
        self.player_data = json.load(f)
        
    def setup_timer(self):
        self.walking_timer = 0
        self.death_timer = 0
        self.flagpole_timer = 0
        self.transition_timer = 0
        self.hurt_invincible_timer = 0
        self.invincible_timer = 0
        self.last_fireball_time = 0

    def setup_state(self):
        self.facing_right = True
        self.allow_jump = True
        self.allow_fireball = True
        self.dead = False
        self.big = False
        self.fire = False
        self.hurt_invincible = False
        self.invincible = False
        self.crouching = False

    def setup_speed(self):
        speed = self.player_data[Set.PLAYER_SPEED]
        self.x_vel = 0
        self.y_vel = 0
        
        self.max_walk_vel = speed[Set.MAX_WALK]
        self.max_run_vel = speed[Set.MAX_RUN]
        self.max_y_vel = speed[Set.MAX_Y_VEL]
        self.walk_accel = speed[Set.WALK_ACCEL]
        self.run_accel = speed[Set.RUN_ACCEL]
        self.jump_vel = speed[Set.JUMP_VEL]
        
        self.gravity = Set.GRAVITY
        self.max_x_vel = self.max_walk_vel
        self.x_accel = self.walk_accel
        
    def load_images(self):
        sheet = setup.GFX['chara_images']
        frames_list = self.player_data[Set.PLAYER_FRAMES]

        self.right_frames = []
        self.left_frames = []

        self.right_small_normal_frames = []
        self.left_small_normal_frames = []
        self.right_big_normal_frames = []
        self.left_big_normal_frames = []
        self.right_big_fire_frames = []
        self.left_big_fire_frames = []
        
        for name, frames in frames_list.items():
            for frame in frames:
                image = tools.get_image(sheet, frame['x'], frame['y'], 
                                    frame['width'], frame['height'],
                                    Set.BLACK, Set.SIZE_MULTIPLIER)
                left_image = pg.transform.flip(image, True, False)

                if name == Set.RIGHT_SMALL_NORMAL:
                    self.right_small_normal_frames.append(image)
                    self.left_small_normal_frames.append(left_image)
                elif name == Set.RIGHT_BIG_NORMAL:
                    self.right_big_normal_frames.append(image)
                    self.left_big_normal_frames.append(left_image)
                elif name == Set.RIGHT_BIG_FIRE:
                    self.right_big_fire_frames.append(image)
                    self.left_big_fire_frames.append(left_image)
        
        self.small_normal_frames = [self.right_small_normal_frames,
                                    self.left_small_normal_frames]
        self.big_normal_frames = [self.right_big_normal_frames,
                                    self.left_big_normal_frames]
        self.big_fire_frames = [self.right_big_fire_frames,
                                    self.left_big_fire_frames]
                                    
        self.all_images = [self.right_small_normal_frames,
                           self.left_small_normal_frames,
                           self.right_big_normal_frames,
                           self.left_big_normal_frames,
                           self.right_big_fire_frames,
                           self.left_big_fire_frames]
        
        self.right_frames = self.small_normal_frames[0]
        self.left_frames = self.small_normal_frames[1]