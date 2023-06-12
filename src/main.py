
from . import tools
from . import Setting as Set
from . state import Menu, Loading, level


def main():
    game = tools.Control()
    state_dict = {
        Set.MAIN_MENU: Menu.Menu(),
        Set.LOAD_SCREEN: Loading.LoadScreen(),
        Set.LEVEL: level.Level(),
        Set.GAME_OVER: Loading.GameOver(),
        Set.TIME_OUT: Loading.TimeOut()
    }
    game.setup_states(state_dict, Set.MAIN_MENU)
    game.main()
