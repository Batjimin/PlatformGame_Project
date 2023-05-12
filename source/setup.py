import os
import pygame as pg
from . import Setting as s
from . import tools

pg.init()
pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP, pg.QUIT])
pg.display.set_caption(s.TITLE)             # 타이틀 전시
SCREEN = pg.display.set_mode(s.SCREEN_SIZE) # 스크린 사이즈에 맞춰 표시
SCREEN_RECT = SCREEN.get_rect()             # 

GFX = tools.load_gfx(os.path.join("resources","graphics"))