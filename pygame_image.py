import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kotons = list()
    koton = pg.transform.flip(pg.image.load("ex01/fig/3.png"), True, False)
    for angle in range(0,10,1):
        kotons.append(pg.transform.rotozoom(koton,angle,1))
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-tmr, 0])
        screen.blit(bg_img2, (-tmr+1600, 0))
        screen.blit(bg_img, (-tmr+3200, 0))
        if ((tmr%(len(kotons)*2))//len(kotons)) == 0: k_tmr = tmr%len(kotons)
        else: k_tmr = -tmr%len(kotons)-1
        koton = kotons[k_tmr]
        screen.blit(koton, (300, 200))
        pg.display.update()
        tmr += 1
        if tmr >= 3200: tmr = 0
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()