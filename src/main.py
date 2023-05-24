
from . import tools
from . import Setting as Set
from . state import Menu, Loading, System

def main():
    game = tools.Control()
    state_dict = {
                  Set.MENU: Menu.Menu(),
                  Set.LOADING: Loading.LoadScreen(),
                  Set.SYSTEM: System.System(),
                  Set.GAME_OVER: Loading.GameOver(),
                  Set.TIME_OUT: Loading.TimeOut()
                }
    game.setup_states(state_dict, Set.MENU)
    game.main()