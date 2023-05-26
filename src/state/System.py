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
        self.setup_elevator()
        self.setup_slider()
        self.setup_static_coin()
        self.setup_tile_and_qr()
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
        
    def setup_elevator(self):
        self.elevator_group = pg.sprite.Group()
        if Set.MAP_ELEVATOR in self.map_data:
            for data in self.map_data[Set.MAP_ELEVATOR]:
                self.elevator_group.add(Etc.Elevator(data['x'], data['y'],
                    data['width'], data['height'], data['type']))
                
    def setup_flagpole(self):
        self.flagpole_group = pg.sprite.Group()
        if Set.MAP_FLAGPOLE in self.map_data:
            for data in self.map_data[Set.MAP_FLAGPOLE]:
                if data['type'] == Set.FLAGPOLE_TYPE_FLAG:
                    sprite = Etc.Flag(data['x'], data['y'])
                    self.flag = sprite
                elif data['type'] == Set.FLAGPOLE_TYPE_POLE:
                    sprite = Etc.Pole(data['x'], data['y'])
                else:
                    sprite = Etc.PoleTop(data['x'], data['y'])
                self.flagpole_group.add(sprite)

    def draw(self, surface): #이게...맞나?
        self.level.blit(self.background, self.viewport, self.viewport)
        self.powerup_group.draw(self.level)
        self.tile_group.draw(self.level)
        self.qr_group.draw(self.level)
        self.coin_group.draw(self.level)
        self.dying_group.draw(self.level)
        self.tilepiece_group.draw(self.level)
        self.flagpole_group.draw(self.level)
        self.shell_group.draw(self.level)
        self.enemy_group.draw(self.level)
        self.player_group.draw(self.level)
        self.static_coin_group.draw(self.level)
        self.slider_group.draw(self.level)
        self.elevator_group.draw(self.level)
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
        
    def setup_tile_and_qr(self):
        self.coin_group = pg.sprite.Group()
        self.powerup_group = pg.sprite.Group()
        self.brick_group = pg.sprite.Group()
        self.brickpiece_group = pg.sprite.Group()

        if Set.MAP_TILE in self.map_data:
            for data in self.map_data[Set.MAP_TILE]:
                tile.createTile(self.qr_group, data, self)
        
        self.qr_group = pg.sprite.Group()
        if Set.MAP_QR in self.map_data:
            for data in self.map_data[Set.MAP_QR]:
                if data['type'] == Set.TYPE_COIN:
                    self.qr_group.add(QR_brick.QR_brick(data['x'], data['y'], data['type'], self.coin_group))
                else:
                    self.qr_group.add(QR_brick.QR_brick(data['x'], data['y'], data['type'], self.powerup_group))
        
        
        
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
        
    def update_flag_score(self):
        base_y = Set.GROUND_HEIGHT - 80
        
        y_score_list = [(base_y, 100), (base_y-120, 400),
                    (base_y-200, 800), (base_y-320, 2000),
                    (0, 5000)]
        for y, score in y_score_list:
            if self.player.rect.y > y:
                self.update_score(score, self.flag)
                break
            
            
            
    
    
    def setup_checkpoints(self):
        self.checkpoint_group = pg.sprite.Group()
        for data in self.map_data[Set.MAP_CHECKPOINT]:
            if Set.ENEMY_GROUPID in data:
                enemy_groupid = data[Set.ENEMY_GROUPID]
            else:
                enemy_groupid = 0
            if Set.MAP_INDEX in data:
                map_index = data[Set.MAP_INDEX]
            else:
                map_index = 0
            self.checkpoint_group.add(Etc.Checkpoint(data['x'], data['y'], data['width'], 
                data['height'], data['type'], enemy_groupid, map_index))
            
            
    def check_checkpoints(self):
        checkpoint = pg.sprite.spritecollideany(self.player, self.checkpoint_group)
        
        if checkpoint:
            if checkpoint.type == Set.CHECKPOINT_TYPE_ENEMY:
                group = self.enemy_group_list[checkpoint.enemy_groupid]
                self.enemy_group.add(group)
            elif checkpoint.type == Set.CHECKPOINT_TYPE_FLAG:
                self.player.state = Set.FLAGPOLE
                if self.player.rect.bottom < self.flag.rect.y:
                    self.player.rect.bottom = self.flag.rect.y
                self.flag.state = Set.SLIDE_DOWN
                self.update_flag_score()
            elif checkpoint.type == Set.CHECKPOINT_TYPE_CASTLE:
                self.player.state = set.IN_CASTLE
                self.player.x_vel = 0
                self.castle_timer = self.current_time
                self.flagpole_group.add(Etc.CastleFlag(8745, 322))
            elif (checkpoint.type == Set.CHECKPOINT_TYPE_COFFEE and
                    self.player.y_vel < 0):
                coffee_QR = QR_brick.QR_brick(checkpoint.rect.x, checkpoint.rect.bottom - 40,
                                Set.TYPE_LIFE_COFFEE, self.powerup_group)
                coffee_QR.start_bump(self.moving_score_list)
                self.QR_group.add(coffee_QR)
                self.player.y_vel = 7
                self.player.rect.y = coffee_QR.rect.bottom
                self.player.state = Set.FALL
            elif checkpoint.type == Set.CHECKPOINT_TYPE_ELEVATOR:
                self.player.state = Set.WALK_AUTO
            elif checkpoint.type == Set.CHECKPOINT_TYPE_ELEVATOR_UP:
                self.change_map(checkpoint.map_index, checkpoint.type)
            elif checkpoint.type == Set.CHECKPOINT_TYPE_MAP:
                self.change_map(checkpoint.map_index, checkpoint.type)
            elif checkpoint.type == Set.CHECKPOINT_TYPE_BOSS:
                self.player.state = Set.WALK_AUTO
            checkpoint.kill()
    
    
    
    def setup_slider(self):
        self.slider_group = pg.sprite.Group()
        if Set.MAP_SLIDER in self.map_data:
            for data in self.map_data[Set.MAP_SLIDER]:
                if Set.VELOCITY in data:
                    vel = data[Set.VELOCITY]
                else:
                    vel = 1
                self.slider_group.add(Etc.Slider(data['x'], data['y'], data['num'],
                    data['direction'], data['range_start'], data['range_end'], vel))

    
    def setup_sprite_groups(self):
        self.dying_group = pg.sprite.Group()
        self.enemy_group = pg.sprite.Group()
        self.shell_group = pg.sprite.Group()
        
        self.ground_step_elevator_group = pg.sprite.Group(self.ground_group,
                        self.elevator_group, self.step_group, self.slider_group)
        
    
    
    
    
    
    
    def check_player_x_collisions(self):
        ground_step_elevator = pg.sprite.spritecollideany(self.player, self.ground_step_elevator_group)
        tile = pg.sprite.spritecollideany(self.player, self.tile_group)
        qr = pg.sprite.spritecollideany(self.player, self.qr_group)
        enemy = pg.sprite.spritecollideany(self.player, self.enemy_group)
        shell = pg.sprite.spritecollideany(self.player, self.shell_group)
        powerup = pg.sprite.spritecollideany(self.player, self.powerup_group)
        coin = pg.sprite.spritecollideany(self.player, self.static_coin_group)

        if qr:
            self.adjust_player_for_x_collisions(qr)
        elif tile:
            self.adjust_player_for_x_collisions(tile)
        elif ground_step_elevator:
            if (ground_step_elevator.name == Set.MAP_ELEVATOR and
                ground_step_elevator.type == Set.ELEVATOR_TYPE_HORIZONTAL):
                return
            self.adjust_player_for_x_collisions(ground_step_elevator)
        elif powerup:
            if powerup.type == Set.TYPE_COFFEE:
                self.update_score(1000, powerup, 0)
                if not self.player.big:
                    self.player.y_vel = -1
                    self.player.state = Set.SMALL_TO_BIG
            elif powerup.type == Set.TYPE_HOT6:
                self.update_score(1000, powerup, 0)
                if not self.player.big:
                    self.player.state = Set.SMALL_TO_BIG
                elif self.player.big and not self.player.fire:
                    self.player.state = Set.BIG_TO_FIRE
            elif powerup.type == Set.TYPE_STAR:
                self.update_score(1000, powerup, 0)
                self.player.invincible = True
            elif powerup.type == Set.TYPE_LIFE_COFFEE:
                self.update_score(500, powerup, 0)
                self.game_info[Set.ATTENDENCE] += 1
            if powerup.type != Set.TYPE_FIREBALL:
                powerup.kill()
        elif enemy:
            if self.player.invincible:
                self.update_score(100, enemy, 0)
                self.move_to_dying_group(self.enemy_group, enemy)
                direction = Set.RIGHT if self.player.facing_right else Set.LEFT
                enemy.start_death_jump(direction)
            elif self.player.hurt_invincible:
                pass
            elif self.player.big:
                self.player.y_vel = -1
                self.player.state = Set.BIG_TO_SMALL
            else:
                self.player.start_death_jump(self.game_info)
                self.death_timer = self.current_time
        elif shell:
            if shell.state == Set.SHELL_SLIDE:
                if self.player.invincible:
                    self.update_score(200, shell, 0)
                    self.move_to_dying_group(self.shell_group, shell)
                    direction = Set.RIGHT if self.player.facing_right else Set.LEFT
                    shell.start_death_jump(direction)
                elif self.player.hurt_invincible:
                    pass
                elif self.player.big:
                    self.player.y_vel = -1
                    self.player.state = Set.BIG_TO_SMALL
                else:
                    self.player.start_death_jump(self.game_info)
                    self.death_timer = self.current_time
            else:
                self.update_score(400, shell, 0)
                if self.player.rect.x < shell.rect.x:
                    self.player.rect.left = shell.rect.x 
                    shell.direction = Set.RIGHT
                    shell.x_vel = 10
                else:
                    self.player.rect.x = shell.rect.left
                    shell.direction = Set.LEFT
                    shell.x_vel = -10
                shell.rect.x += shell.x_vel * 4
                shell.state = Set.SHELL_SLIDE
        elif coin:
            self.update_score(100, coin, 1)
            coin.kill()

    def adjust_player_for_x_collisions(self, collider):
        if collider.name == Set.MAP_SLIDER:
            return

        if self.player.rect.x < collider.rect.x:
            self.player.rect.right = collider.rect.left
        else:
            self.player.rect.left = collider.rect.right
        self.player.x_vel = 0