import pygame as pg
from abc import ABC, abstractmethod


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
    
#상태 *부모함수* 정의
class State():
    def __init__(self):
        self.start_time = 0.0
        self.current_time = 0.0
        self.done = False
        self.next = None
        self.persist = {} #유지 데이터 저장 딕셔너리
    
    @abstractmethod #추상 메소드 정의(자식에서 무조건 구현할 것)
    
    #시작
    def startup(self, current_time, persist):
        '''abstract method'''

    #끝나면 데이터 반환
    def cleanup(self):
        self.done = False
        return self.persist
    
    @abstractmethod
    #업데이트
    def update(self, surface, keys, current_time):
        '''abstract method'''
        
class Control():
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.current_time = 0.0
        self.done = False
        self.clock = pg.time() #time.Clock()일지도
        self.fps = 60
        self.keys = pg.key.get_pressed()
        self.state_dict = {}
        self.state_name = None
        self.state = None