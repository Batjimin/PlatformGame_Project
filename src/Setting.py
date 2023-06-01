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
BROWN        = ()

# 구성요소 색
COLOR = 'color'
COLOR_TYPE_ORANGE = 0
COLOR_TYPE_GREEN = 1
COLOR_TYPE_RED = 2
COLOR_TYPE_BROWN = 3

#게임 시스템
MENU = 'menu'
LOADING = 'loading'
TIME_OUT = 'time out'
GAME_OVER = 'game over'
LEVEL = 'level'

#게임 요소
TOTAL_COIN = 'total coin'
SCORE = 'score'
TOP_SCORE = 'top score'
ATTENDENCE = 'attendence' #생명 = 출석
CURRENT_TIME = 'current time'
YOUR_NAME = 'player name'
PLAYER = 'player'
LEVEL_NUM = 'level num'

MAP_COIN = "coin"
MAP_IMAGE = 'image_name'
MAP_INDEX = 'map_index'
SUB_MAP = 'sub_map'
MAP_GROUND = 'ground'
MAP_SLIDER = 'slider'
MAP_ELEVATOR = 'elevator'     # 엘리베이터 (파이프와 같은 역할)
MAP_TILE = 'tile'             # QR코드 타일
MAP_FLAGPOLE = 'flagpole'
FLAGPOLE_TYPE_FLAG = 0
FLAGPOLE_TYPE_POLE = 1
FLAGPOLE_TYPE_TOP = 2
TILE_NUM = 'tile_num'
TYPE_NONE = 0
TYPE_COIN = 1
TYPE_PAPER = 2          # 족보(임시)
MAP_QR     = 'QR'
TYPE_COFFEE         = 3          # 커피     (성장 버프)
TYPE_HOT6           = 4          # 핫식스   (파이어 볼)
TYPE_REDBULL        = 5          # 레드불   (fly)
TYPE_LIFE_COFFEE    = 6          # 커피     (생명(출석)추가 커피 )
TYPE_GPT            = 7          # gpt형태  (블록 생성)
TYPE_FIREBALL       = 8

MAP_ENEMY   = 'enemy'
ENEMY_RANGE = 'range'
ENEMY_GROUPID = 'enemy_groupid'

HORIZONTAL = 0
VERTICAL = 1
VELOCITY = 'velocity'

ENEMY_TYPE_BOO            = 0   # 부 형태의 몬스터
ENEMY_TYPE_BOSS           = 1   # 과제 형태의 몬스터

#벽돌상태
STAYED = 'stayed'
BUMPED = 'bumped'
OPENED = 'opened'

#플레이어 상태. auto walking은 깃발 도달 시 사용.
STAND = 'standing'
WALK = 'walk'
JUMP = 'jump'
FALL = 'fall'
SMALL_TO_BIG = 'small to big'
BIG_TO_FIRE = 'big to fire'
BIG_TO_FLY = "big to fly"
BIG_TO_SMALL = 'big to small'
FLAGPOLE = 'flag pole'
WALK_AUTO = 'walk auto'
IN_CASTLE = 'in castle'
DOWN_ELEVATOR = 'elevator down'
UP_ELEVATOR = 'elevator up'

#플레이어 이동. 중력 조절 필요.
PLAYER_SPEED = 'speed'
WALK_ACCEL = 'walk_accel'
RUN_ACCEL = 'run_accel'
JUMP_VEL = 'jump_velocity'
MAX_Y_VEL = 'max_y_velocity'
MAX_RUN = 'max_run'
MAX_WALK = 'max_walk'
SMALL_TURNAROUND = .35
JUMP_GRAVITY = .31
GRAVITY = 1.00

# 적 목록
BOO = 'boo'
BOSS = 'boss'

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

# 아이템 상태
REVEAL = 'reveal'
SLIDE = 'slide'

# 배율
SIZE_MULTIPLIER = 2.5
TILE_SIZE_MULTIPLIER = 2.69
BACKGROUND_MULTIPLER = 2.679
GROUND_HEIGHT = SCREEN_HEIGHT - 62

# 제한 시간
TIME_LIMIT = 300

#이미지 시트
ITEM_IMAGE = 'item_images'
ENEMY_IMAGE = 'enemy_images'

DEBUG = False
DEBUG_START_X = 110
DEBUG_START_Y = 538

#프레임
PLAYER_FRAMES = 'image_frames'
RIGHT_SMALL_NORMAL = 'right_small_normal'
RIGHT_BIG_NORMAL = 'right_big_normal'
RIGHT_BIG_FIRE = 'right_big_fire'

# 체크 요소
MAP_CHECKPOINT = 'checkpoint'
CHECKPOINT_TYPE_ENEMY = 0
CHECKPOINT_TYPE_FLAG = 1
CHECKPOINT_TYPE_CASTLE = 2
CHECKPOINT_TYPE_COFFEE = 3
CHECKPOINT_TYPE_ELEVATOR = 4       
CHECKPOINT_TYPE_ELEVATOR_UP = 5    
CHECKPOINT_TYPE_MAP = 6         
CHECKPOINT_TYPE_BOSS = 7        