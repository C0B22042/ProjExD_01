import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kotons = list()
    koton = pg.transform.flip(pg.image.load("ex01/fig/3.png"), True, False)
    kotons.append([koton,0 , 0])
    kotons.append([pg.transform.rotozoom(koton,10,1), 300, 200])
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-tmr, 0])
        screen.blit(bg_img, (-tmr+1600, 0))
        koton = kotons[(tmr//4)%2]
        screen.blit(koton[0], (300, 200))
        pg.display.update()
        tmr += 1
        if tmr >= 1600:
            tmr = 0
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()