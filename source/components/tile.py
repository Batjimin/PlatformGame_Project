#발판이랍니다
import pygame as pg
from .. import setup,tools
from .. import Setting as Set
from . import Coin, Etc, powerup

def createTile(tile_group, item, system):
    if Set.COLOR in item :
        color = item[Set.COLOR]
    else : 
        color = Set.COLOR_TYPE_BROWN #미정
    
    x,y,type = item['x'], item['y'], item['type']
    if type == Set.TYPE_COIN:  
        tile_group.add(Tile(x,y,type,color,system.coin_group))
    elif(type)

