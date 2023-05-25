import pygame as pg

from src.main import main

#직접 실행될때만 작동. 다른 모듈에서 불러올때는 실행 x.
#Start debuging은 이 파일에서 실행할 것.
if __name__ == '__main__':
    main()
    pg.quit()
    