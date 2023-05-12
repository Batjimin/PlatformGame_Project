import pygame as pg
from . import setup, tools
from . import Setting as Set
from . state import Menu, Loading, System

def main():
    game = tools.Control()
    state_dict = {
                  Set.MAIN_MENU: Menu.Menu(),
                  Set.LOAD_SCREEN: Loading.LoadScreen(),
                  Set.LEVEL: System.Level(),
                  Set.GAME_OVER: Loading.GameOver(),
                  Set.TIME_OUT: Loading.TimeOut()
                }
    game.setup_states(state_dict, Set.Menu)
    game.main()