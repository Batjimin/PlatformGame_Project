# 스크린 크기
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# 색상
BLACK        = (  0,   0,   0)
RED          = (255,   0,   0)
YELLOW       = (255, 255,   0)

# 게임 상태
MAIN_MENU = 'main menu'
LOAD_SCREEN = 'load screen'
TIME_OUT = 'time out'
GAME_OVER = 'game over'
LEVEL = 'level'

# 구성요소
MAP_IMAGE = 'image_name' 
MAP_BUS = 'BUS'         # 교내 셔틀 (파이프와 같은 역할)
MAP_BRICK = 'brick'     # QR코드 벽돌
BRICK_NUM = 'brick_num'
TYPE_NONE = 0
TYPE_COIN = 1
TYPE_STAR = 2

MAP_BOX = 'box'
TYPE_COFFEE         = 3          # 커피 (성장 버프)
TYPE_DRINK          = 4          # 에너지드링크 (속도 버프)
TYPE_LIFEMUSHROOM   = 5          # 생명 추가
MAP_ENEMY = 'enemy'

ENEMY_TYPE_GOOMBA = 0
ENEMY_TYPE_KOOPA = 1
ENEMY_TYPE_FLY_KOOPA = 2
ENEMY_TYPE_PIRANHA = 3
ENEMY_TYPE_FIRESTICK = 4
ENEMY_TYPE_FIRE_KOOPA = 5
ENEMY_RANGE = 'range'

# 벽돌 상태
RESTING = 'resting'
BUMPED = 'bumped'
OPENED = 'opened'

# 아이템 상태
REVEAL = 'reveal'
SLIDE = 'slide'

# 플레이어 상태
STAND = 'standing'
WALK = 'walk'
JUMP = 'jump'
FALL = 'fall'
FLY = 'fly'
SMALL_TO_BIG = 'small to big'
BIG_TO_FIRE = 'big to fire'
BIG_TO_SMALL = 'big to small'
FLAGPOLE = 'flag pole'

# 플레이어 능력
PLAYER_SPEED = 'speed'
WALK_ACCEL = 'walk_accel'
RUN_ACCEL = 'run_accel'
JUMP_VEL = 'jump_velocity'
MAX_Y_VEL = 'max_y_velocity'
MAX_RUN_SPEED = 'max_run_speed'
MAX_WALK_SPEED = 'max_walk_speed'
SMALL_TURNAROUND = .35
JUMP_GRAVITY = .31
GRAVITY = 1.01

# 적 목록


# 일반몹 행동 
LEFT = 'left'
RIGHT = 'right'
JUMPED_ON = 'jumped on'
DEATH_JUMP = 'death jump'

# 보스몹 행동
SHELL_SLIDE = 'shell slide'

# 깃발 상태
TOP_OF_POLE = 'top of pole'
SLIDE_DOWN = 'slide down'
BOTTOM_OF_POLE = 'bottom of pole'