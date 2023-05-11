# 스크린 크기
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

#참고용 RGB값. 사용하고 싶은 색 있으면 여기에 추가.
GRAY         = (100, 100, 100)
NAVYBLUE     = ( 60,  60, 100)
WHITE        = (255, 255, 255)
RED          = (255,   0,   0)
GREEN        = (  0, 255,   0)
FOREST_GREEN = ( 31, 162,  35)
BLUE         = (  0,   0, 255)
SKY_BLUE     = ( 39, 145, 251)
YELLOW       = (255, 255,   0)
ORANGE       = (255, 128,   0)
PURPLE       = (255,   0, 255)
CYAN         = (  0, 255, 255)
BLACK        = (  0,   0,   0)
NEAR_BLACK   = ( 19,  15,  48)
GOLD         = (255, 215,   0)

#게임 시스템
MAIN_MENU = 'main menu'
LOAD_SCREEN = 'load screen'
TIME_OUT = 'time out'
GAME_OVER = 'game over'
LEVEL = 'level'

#게임 요소
TOTAL_COIN = 'total coin'
SCORE = 'score'
TOP_SCORE = 'top score'
Attendence = 'attendence' #생명 = 출석
CURRENT_TIME = 'current time'
YOUR_NAME = 'player name'

#벽돌상태
STAYED = 'stayed'
BUMPED = 'bumped'
OPENED = 'opened'

#플레이어 상태. auto walking은 깃발 도달 시 사용.
STAND = 'standing'
WALK = 'walk'
JUMP = 'jump'
FALL = 'fall'
FLY = 'fly'
SMALL_TO_BIG = 'small to big'
BIG_TO_FIRE = 'big to fire'
BIG_TO_SMALL = 'big to small'
FLAGPOLE = 'flag pole'
WALK_AUTO = 'walk auto'     # not handle key input in this state
END_OF_LEVEL_FALL = 'end of level fall'
IN_CASTLE = 'in castle'
DOWN_TO_PIPE = 'down to pipe'
UP_OUT_PIPE = 'up out of pipe'

#플레이어 이동. 중력 조절 필요.
PLAYER_SPEED = 'speed'
WALK_ACCEL = 'walk_accel'
RUN_ACCEL = 'run_accel'
JUMP_VEL = 'jump_velocity'
MAX_Y_VEL = 'max_y_velocity'
MAX_RUN_SPEED = 'max_run_speed'
MAX_WALK_SPEED = 'max_walk_speed'
SMALL_TURNAROUND = .35
JUMP_GRAVITY = .31
GRAVITY = 1.00

#부. 상태명 변경할 수도 있음.
LEFT = 'left'
RIGHT = 'right'
JUMPED_ON = 'jumped on'
DEATH_JUMP = 'death jump'

#깃발
TOP_OF_POLE = 'pole top'
SLIDE_DOWN = 'pole slide'
BOTTOM_OF_POLE = 'pole bottom'

#사출기
FLYING = 'flying'
BOUNCING = 'bouncing'
EXPLODING = 'exploding'
