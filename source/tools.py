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

    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state #상태 나타내는 문자열 start_name
        self.state = self.state_dict[self.state_name] #상태문자열 딕셔너리 넣고 state에 넣기
    
    def update(self):
        self.current_time = pg.time.get_ticks() #시간가져오기 
        if self.state.done:
            self.change_state() #상태 끝나면 변환
        self.state.update(self.screen, self.keys, self.current_time)
    
    def change_state(self): #flip state 
        previous = self.state_name
        self.state_name = self.state.next
        persist = self.state.cleanup() #유지데이터 삭제
        self.state = self.state_dict[self.state_name] 
        self.state.startup(self.current_time, persist) #새시작

    #이벤트 받아서 입력처리
    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.KEYDOWN:
                self.keys = pg.key.get_pressed()
            elif event.type == pg.KEYUP:
                self.keys = pg.key.get_pressed()
    
    #메인. 반복루프->업데이트, 프레임 조절
    def main(self):
        while not self.done :
            self.event_loop()
            self.update()
            pg.display.update() 
            self.clock.tick(self.fps) #프레임







