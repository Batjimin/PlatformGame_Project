#시스템. 미완. 주석도 없다!
import os
import json
import pygame as pg
from .. import setup, tools
from .. import Setting as Set
from ..components import Info, Etc, player, tile, QR_brick, enemies, powerup, Coin

class System(tools.State):
    def __init__(self):
        tools.State.__init__(self)
        self.player = None
        
    def startup(self, current_time, persist):
        self.game_info = persist
        self.persist = self.game_info
        self.game_info[Set.CURRENT_TIME] = current_time
        self.death_timer = 0    
        
        self.moving_score_list = []
        self.overhead_info = Info.Info(self.game_info, Set.SYSTEM)
        self.load_map()
        self.setup_background()
        self.setup_maps()
        self.ground_group = self.setup_collide(Set.MAP_GROUND)
        self.step_group = self.setup_collide(Set.MAP_STEP)
        self.setup_pipe()
        self.setup_slider()
        self.setup_static_coin()
        self.setup_tile_and_box()
        self.setup_player()
        self.setup_enemies()
        self.setup_checkpoints()
        self.setup_flagpole()
        self.setup_sprite_groups()
        
    def load_map(self):
        map_file = 'level_' + str(self.game_info[Set.SYSTEM_NUM]) + '.json'
        file_path = os.path.join('source', 'data', 'maps', map_file)
        f = open(file_path)
        self.map_data = json.load(f)
        f.close()
        
    def setup_collide(self, name):
        group = pg.sprite.Group()
        if name in self.map_data:
            for data in self.map_data[name]:
                group.add(Etc.Collider(data['x'], data['y'], 
                        data['width'], data['height'], name))
        return group
    
    def setup_background(self):
        img_name = self.map_data[Set.MAP_IMAGE]
        self.background = setup.GFX[img_name]
        self.bg_rect = self.background.get_rect()
        self.background = pg.transform.scale(self.background, 
                                    (int(self.bg_rect.width*Set.BACKGROUND_MULTIPLER),
                                    int(self.bg_rect.height*Set.BACKGROUND_MULTIPLER)))
        self.bg_rect = self.background.get_rect()

        self.level = pg.Surface((self.bg_rect.w, self.bg_rect.h)).convert()
        self.viewport = setup.SCREEN.get_rect(bottom=self.bg_rect.bottom)

    def setup_tile_and_box(self):
        self.coin_group = pg.sprite.Group()
        self.powerup_group = pg.sprite.Group()
        self.tile_group = pg.sprite.Group()
        self.tilepiece_group = pg.sprite.Group()

    def draw(self, surface): #이게...맞나?
        self.level.blit(self.background, self.viewport, self.viewport)
        self.powerup_group.draw(self.level)
        self.tile_group.draw(self.level)
        self.box_group.draw(self.level)
        self.coin_group.draw(self.level)
        self.dying_group.draw(self.level)
        self.tilepiece_group.draw(self.level)
        self.flagpole_group.draw(self.level)
        self.shell_group.draw(self.level)
        self.enemy_group.draw(self.level)
        self.player_group.draw(self.level)
        self.static_coin_group.draw(self.level)
        self.slider_group.draw(self.level)
        self.pipe_group.draw(self.level)
        for score in self.moving_score_list:
            score.draw(self.level)
        if Set.DEBUG:
            self.ground_step_pipe_group.draw(self.level)
            self.checkpoint_group.draw(self.level)

        surface.blit(self.level, (0,0), self.viewport)
        self.overhead_info.draw(surface)
        
    def setup_enemies(self):
        self.enemy_group_list = []
        index = 0
        for data in self.map_data[Set.MAP_ENEMY]:
            group = pg.sprite.Group()
            for item in data[str(index)]:
                group.add(enemies.create_enemy(item, self))
            self.enemy_group_list.append(group)
            index += 1
    
    def setup_player(self):
        if self.player is None:
            self.player = player.Player(self.game_info[Set.PLAYER_NAME])
        else:
            self.player.restart()
        self.player.rect.x = self.viewport.x + self.player_x
        self.player.rect.bottom = self.player_y
        if Set.DEBUG:
            self.player.rect.x = self.viewport.x + Set.DEBUG_START_X
            self.player.rect.bottom = Set.DEBUG_START_y
        self.viewport.x = self.player.rect.x - 110
        
    def update_game_info(self):
        if self.player.dead:
            self.persist[Set.ATTENDENCE] -= 1

        if self.persist[Set.ATTENDENCE] == 0:
            self.next = Set.GAME_OVER
        elif self.overhead_info.time == 0:
            self.next = Set.TIME_OUT
        elif self.player.dead:
            self.next = Set.LOADING
        else:
            self.game_info[Set.SYSTEM_NUM] += 1
            self.next = Set.LOADING

    def update_viewport(self):
        third = self.viewport.x + self.viewport.w//3
        player_center = self.player.rect.centerx
        
        if (self.player.x_vel > 0 and 
            player_center >= third and
            self.viewport.right < self.end_x):
            self.viewport.x += round(self.player.x_vel)
        elif self.player.x_vel < 0 and self.viewport.x > self.start_x:
            self.viewport.x += round(self.player.x_vel)
        
    def update_score(self, score, sprite, coin_num=0):
        self.game_info[Set.SCORE] += score
        self.game_info[Set.TOTAL_COIN] += coin_num
        x = sprite.rect.x
        y = sprite.rect.y - 10
        self.moving_score_list.append(Etc.Score(x, y, score))