import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")#練習1
    bg_img_fl = pg.transform.flip(bg_img, True, False)
    kt_img = pg.image.load("fig/3.png")#練習3
    kt_img = pg.transform.flip(kt_img, True, False)
    kt_rct = kt_img.get_rect()
    kt_rct.center = 300,200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed()
        x = -1
        y = 0
        if key_lst[pg.K_UP]:
            x += 0
            y -= 1
        if key_lst[pg.K_DOWN]:
            x += 0
            y += 1
        if key_lst[pg.K_LEFT]:
            x += 0
        if key_lst[pg.K_RIGHT]:
            x += 2   
        kt_rct.move_ip((x,y))
        x = tmr%3200
        screen.blit(bg_img, [-x, 0])#練習2
        screen.blit(bg_img_fl, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(kt_img, kt_rct)
        pg.display.update()
        tmr += 1
        clock.tick(200)
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()