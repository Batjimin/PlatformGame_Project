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

class Info():
    def __init__(self, game_info, state):
        self.coin_total = game_info[Set.TOTAL_COIN]
        self.total_attendence = game_info[Set.ATTENDENCE]
        self.state = state
        self.game_info = game_info
        
        self.create_font_image_dict()
        self.create_info_labels()
        self.create_state_labels()
        self.flashing_coin = Coin.FlashCoin(280, 53)

    def update(self, level_info, level=None):
        self.level = level
        self.handle_level_state(level_info)

    def create_state_labels(self):
        if self.state == Set.MENU:
            self.create_main_menu_labels()
        elif self.state == Set.LOADING:
            self.create_player_image()
            self.create_load_screen_labels()
        elif self.state == Set.LEVEL:
            self.create_level_labels()
        elif self.state == Set.GAME_OVER:
            self.create_game_over_labels()
        elif self.state == Set.TIME_OUT:
            self.create_time_out_labels()

    def draw(self, surface):
        self.draw_info(surface, self.state_labels)
        if self.state == Set.LOADING:
            surface.blit(self.player_image, self.player_rect)
            surface.blit(self.life_times_image, self.life_times_rect)
        surface.blit(self.flashing_coin.image, self.flashing_coin.rect)
    
    def draw_info(self, surface, label_list):
        for label in label_list:
            for letter in label:
                surface.blit(letter.image, letter.rect)

    def create_font_image_dict(self):

    def create_info_labels(self):

    def create_player_image(self):

    def create_main_menu_labels(self):

    def create_load_screen_labels(self):

    def create_level_labels(self):

    def create_game_over_labels(self):

    def create_time_out_labels(self):

    def create_label(self, label_list, string, x, y):

    def set_label_rects(self, label_list, x, y):

    def update(self, level_info, level=None):
        self.level = level
        self.handle_level_state(level_info)

    def handle_level_state(self, level_info):

    def update_text(self, text, score, reset=False):