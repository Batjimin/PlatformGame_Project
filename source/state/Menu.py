#메인 메뉴 등 구성. 미완
import pygame as pg
from .. import tools
from .. import setup
from .. import Setting as Set
from .. components import Info

class Menu(tools.State):
    def __init__(self):
        tools.State.__init__(self)
        persist = {Set.COIN_TOTAL: 0,
                   Set.SCORE: 0,
                   Set.LIVES: 3,
                   Set.TOP_SCORE: 0,
                   Set.CURRENT_TIME: 0.0,
                   Set.LEVEL_NUM: 1,
                   Set.PLAYER_NAME: Set.PLAYER_MARIO}
        self.startup(0.0, persist)
        
    def startup(self, persist):
        self.next = Set.LOAD_SCREEN
        self.persist = persist
        self.game_info = persist
        self.overhead_info = Info.Info(self.game_info, Set.MAIN_MENU)

        self.setup_background()
        self.setup_player()
        self.setup_cursor()
        
    def setup_background(self):
        self.background = setup.GFX['backgroundImage']
        self.background_rect = self.background.get_rect()
        self.background = pg.transform.scale(self.background,
                                    (int(self.background_rect.width*Set.BACKGROUND_MULTIPLER),
                                    int(self.background_rect.height*Set.BACKGROUND_MULTIPLER)))

        self.viewport = setup.SCREEN.get_rect(bottom=setup.SCREEN_RECT.bottom)
        self.image_dict = {}
        image = tools.get_image(setup.GFX['title_screen'], 1, 60, 176, 88,
                            (255, 0, 220), Set.SIZE_MULTIPLIER)
        rect = image.get_rect()
        rect.x, rect.y = (170, 100)
        self.image_dict['NAME_BOX'] = (image, rect)
        
        
    def reset_game_info(self):
        self.game_info[Set.TOTAL_COIN] = 0
        self.game_info[Set.SCORE] = 0
        self.game_info[Set.ATTENDENCE] = 3
        self.game_info[Set.CURRENT_TIME] = 0.0
        
        self.persist = self.game_info
        