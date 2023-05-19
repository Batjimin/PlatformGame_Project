#발판이랍니다
import pygame as pg
from .. import setup,tools
from .. import Setting as Set
from . import Coin, Etc, powerup


def createTileList(tile_group,num,x,y,type,color,direction):
    size = 43
    tmp_x = x
    tmp_y = y
    for i in range(num):
        if direction == Set.VERTICAL:
            tmp_y = y + i *size
        else:
            tmp_x = x + i *size
        tile_group.add(Tile(tmp_x,tmp_y,type,color))

def createTile(tile_group, item, system):
    if Set.COLOR in item :
        color = item[Set.COLOR]
    else : 
        color = Set.COLOR_TYPE_BROWN #미정
    
    x,y,type = item['x'], item['y'], item['type']
    if type == Set.TYPE_COIN:  
        tile_group.add(Tile(x,y,type,color,system.coin_group))
    elif(type==Set.TYPE_PAPER or 
         type == Set.TYPE_HOT6 or 
         type ==Set.TYPE_GPT or
         type == Set.TYPE_REDBULL or
         type == Set.TYPE_LIFE_COFFEE
         ) :    
        tile_group.add(Tile(x,y,type,color))
    else :
        if Set.TILE_NUM in item:
            createTileList(tile_group,item[Set.TILE_NUM],x,y,type,color,item['direction'])
        else:
            tile_group.add(Tile(x,y,type,color))

class Tile(EtSet.Stuff):
    def __init__(self,x,y,type,color =Set.BROWN, group=None, name=Set.MAP_TILE):
        brown_rect = [(),()] #시트 만들어지면 좌표입력
        green_rect = [(),()]
        if color == Set.COLOR_TYPE_BROWN:
            frame_rect = brown_rect
        else:
            frame_rect = green_rect
        EtSet.Stuff.__init__(self,x,y,setup,GFX['tile.set'], frame_rect,Set.TILE_SIZE_MULTIPLIER)

        self.rest_height = y
        self.state = Set.STAYED
        self.y_vel = 0
        self.gravity = 1.2
        self.type = type
        if self.type == Set.TYPE_COIN:
            self.coin_num = 10
        else:
            self.coin_num = 0
        self.group = group
        self.name = name
    
    def bumped(self):
        self.rect.y += self.y_vel
        self.y_vel += self.gravity

        if self.rect.y >= self.rest_height:
            self.rect.y = self.rest_height
            if self.type == Set.TYPE_COIN:
                if self.coin_num >0:
                    self.state = Set.STAYED
                else : 
                    self.state = Set.OPENED
            elif self.type == Set.TYPE_PAPER:
                self.state = Set.OPENED
                self.group.add(powerup.Paper(self.rect.centerx, self.rest_height))
            elif self.type == Set.TYPE_HOT6:
                self.state = Set.OPENED
                self.group.add(powerup.HOT6(self.rect.centerx, self.rest_height))
            elif self.type == Set.TYPE_LIFE_COFFEE:
                self.state = Set.OPENED
                self.group.add(powerup.Life_Coffee(self.rect.centerx, self.rest_height))
            else:
                self.state = Set.STAYED

    def update(self):
        if self.state == Set.BUMPED:
            self.bumped()
    
    def start_bump(self, score_group):
        self.y_vel -= 7
        
        if self.type == Set.TYPE_COIN:
            if self.coin_num > 0:
                self.group.add(Coin.Coin(self.rect.centerx, self.rect.y, score_group))
                self.coin_num -= 1
                if self.coin_num == 0:
                    self.frame_index = 1
                    self.image = self.frames[self.frame_index]
        elif (self.type == Set.TYPE_PAPER or 
            self.type == Set.TYPE_HOT6 or 
            self.type == Set.TYPE_LIFE_COFFEE or
            self.type == Set.TYPE_GPT):
            self.frame_index = 1
            self.image = self.frames[self.frame_index]
        
        self.state = Set.BUMPED
    
    def change_to_piece(self, group):
        arg_list = [(self.rect.x, self.rect.y - (self.rect.height/2), -2, -12),
                    (self.rect.right, self.rect.y - (self.rect.height/2), 2, -12),
                    (self.rect.x, self.rect.y, -2, -6),
                    (self.rect.right, self.rect.y, 2, -6)]
        
        for arg in arg_list:
            group.add(TilePiece(*arg))
        self.kill()
        
class TilePiece(Etc.Stuff):
    def __init__(self, x, y, x_vel, y_vel):
        Etc.Stuff.__init__(self, x, y, setup.GFX['tile_set'],
            [(68, 20, 8, 8)], Set.TILE_SIZE_MULTIPLIER)
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.gravity = .8
    
    def update(self, *args):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel
        self.y_vel += self.gravity
        if self.rect.y > Set.SCREEN_HEIGHT:
            self.kill()