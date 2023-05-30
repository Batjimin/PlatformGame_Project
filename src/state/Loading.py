from .. import tools
from .. import Setting as Set
from ..components import Info

class LoadScreen(tools.State):
    def __init__(self):
        tools.State.__init__(self)
        self.time_list = [2400, 2600, 2635]
        
    def startup(self, current_time, persist):
        self.start_time = current_time
        self.persist = persist
        self.game_info = self.persist
        self.next = self.set_next_state()
        
        info_state = self.set_info_state()
        self.overhead_info = Info.Info(self.game_info, info_state)
    
    def set_next_state(self):
        return Set.LEVEL
    
    def set_info_state(self):
        return Set.LOADING

    def update(self, surface, keys_empty, current_time):
        if (current_time - self.start_time) < self.time_list[0]:
            surface.fill(Set.BLACK)
            self.overhead_info.update(self.game_info)
            self.overhead_info.draw(surface)
        elif (current_time - self.start_time) < self.time_list[1]:
            surface.fill(Set.BLACK)
        elif (current_time - self.start_time) < self.time_list[2]:
            surface.fill((106, 150, 252))
        else:
            self.done = True
            
            
#게임오버 - F학점
class GameOver(LoadScreen):
    def __init__(self):
        LoadScreen.__init__(self)
        self.time_list = [3000, 3200, 3235]

    def set_next_state(self):
        return Set.MENU
    
    def set_info_state(self):
        return Set.GAME_OVER

#시간초과 - ???
class TimeOut(LoadScreen):
    def __init__(self):
        LoadScreen.__init__(self)
        self.time_list = [2400, 2600, 2635]

    def set_next_state(self):
        if self.persist[Set.ATTENDENCE] == 0:
            return Set.GAME_OVER
        else:
            return Set.LOADING

    def set_info_state(self):
        return Set.TIME_OUT
