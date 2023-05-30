
from . import tools
from . import Setting as Set
from . state import Menu, Loading, level

def main():
    game = tools.Control()
    state_dict = {
                  Set.MENU: Menu.Menu(),
                  Set.LOADING: Loading.LoadScreen(),
                  Set.LEVEL: level.LEVEL(),
                  Set.GAME_OVER: Loading.GameOver(),
                  Set.TIME_OUT: Loading.TimeOut()
                }
    game.setup_states(state_dict, Set.MENU)
    game.main()