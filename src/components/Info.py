#information . 아직 함수 내용 안적었음
import pygame as pg
from .. import setup, tools
from .. import Setting as Set
from . import Coin

class Character(pg.sprite.Sprite):
    def __init__(self, image):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()

class Info(): #게임 정보와 현재 게임 상태에 따라 라벨과 이미지를 생성하고 드로잉 

    def __init__(self, game_info, state):
        self.coin_total = game_info[Set.TOTAL_COIN]
        self.total_attendence = game_info[Set.ATTENDENCE]
        self.state = state
        self.game_info = game_info
        
        self.create_font_image_dict()
        self.create_info_labels()
        self.create_state_labels() #필요한 라벨 및 이미지 생성

        self.flashing_coin = Coin.FlashCoin(280, 53) 

    def update(self, system_info, system=None): #시스템(레벨=1)과 관련된 정보 처리, 시스템 단계 상태 확인 
        self.system = system
        self.handle_system_state(system_info)

    def create_state_labels(self): #프로그램 상태 별 라벨 생성. 라벨은 state속성을 바탕으로 생성된다.
        if self.state == Set.MENU:
            self.create_main_menu_labels()
        elif self.state == Set.LOADING:
            self.create_player_image()
            self.create_load_screen_labels()
        elif self.state == Set.LEVEL:
            self.create_system_labels()
        elif self.state == Set.GAME_OVER:
            self.create_game_over_labels()
        elif self.state == Set.TIME_OUT:
            self.create_time_out_labels()

    def draw(self, surface): #Info 객체의 정보&라벨을 지정된 Surface에 bilt
        self.draw_info(surface, self.state_labels)
        if self.state == Set.LOADING:
            surface.blit(self.player_image, self.player_rect)
            surface.blit(self.life_times_image, self.life_times_rect)
        surface.blit(self.flashing_coin.image, self.flashing_coin.rect)
    
    def draw_info(self, surface, label_list): # draw_info() 호출하여 정보 라벨을 그리고 blit() 메소드를 사용하여 이미지 그리기
        for label in label_list:
            for letter in label:
                surface.blit(letter.image, letter.rect)
                
    def create_system_labels(self):
        self.time = Set.TIME_LIMIT
        self.current_time = 0

        self.clock_time_label = []
        self.create_label(self.clock_time_label, str(self.time), 645, 55)
        self.state_labels = [*self.info_labels, self.clock_time_label]
    
    def create_label(self, label_list, string, x, y):
        for letter in string:
            label_list.append(Character(self.image_dict[letter]))
        self.set_label_rects(label_list, x, y)
        
    def update_text(self, text, score, reset=False):
        if reset and len(text) > len(str(score)):
            text.remove(text[0])
        index = len(text) - 1
        for digit in reversed(str(score)):
            rect = text[index].rect
            text[index] = Character(self.image_dict[digit])
            text[index].rect = rect
            index -= 1    
        
    def create_font_image_dict(self):

    def create_info_labels(self):

    def create_player_image(self):

    def create_main_menu_labels(self):

    def create_load_screen_labels(self):

     
    def create_game_over_labels(self):

    def create_time_out_labels(self):

    def set_label_rects(self, label_list, x, y):

    def handle_system_state(self, system_info):

    