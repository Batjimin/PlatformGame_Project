#시스템. 미완. 주석도 없다!
import os
import json
import pygame as pg
from .. import setup, tools
from .. import Setting as Set
from ..components import Info, stuff, player, brick, QR_brick, enemies, powerup, Coin

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
        self.overhead_info = Info.Info(self.game_info, Set.LEVEL)
        self.load_map()
        self.setup_background()
        self.setup_maps()
        self.ground_group = self.setup_collide(Set.MAP_GROUND)
        self.step_group = self.setup_collide(Set.MAP_STEP)
        self.setup_pipe()
        self.setup_slider()
        self.setup_static_coin()
        self.setup_brick_and_box()
        self.setup_player()
        self.setup_enemies()
        self.setup_checkpoints()
        self.setup_flagpole()
        self.setup_sprite_groups()
        
    def load_map(self):
        map_file = 'level_' + str(self.game_info[Set.LEVEL_NUM]) + '.json'
        file_path = os.path.join('source', 'data', 'maps', map_file)
        f = open(file_path)
        self.map_data = json.load(f)
        f.close()
        
    def setup_collide(self, name):
        group = pg.sprite.Group()
        if name in self.map_data:
            for data in self.map_data[name]:
                group.add(stuff.Collider(data['x'], data['y'], 
                        data['width'], data['height'], name))
        return group