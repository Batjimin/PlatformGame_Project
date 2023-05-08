import pygame as pg

#키설정
keybinding = {
    'action': pg.K_SPACE,
    'jump' : pg.K_UP,
    'left' : pg.K_LEFT,
    'right' : pg.K_RIGHT,
    'down' : pg.K_DOWN 
} 

#이미지 받아오기
def get_image(sheet, x, y, width, height, colorkey, scale):
    image = pg.Surface([width,height])
    rect = image.get_rect()
    image.set_colorkey(colorkey)