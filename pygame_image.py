import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kk_img01 = pg.image.load("ex01/fig/3.png")
    kk_img01 = pg.transform.flip(kk_img01,True,False)
    kk_img02 = pg.transform.rotozoom(kk_img01,10,1.0)
    kk_imgs = [kk_img01,kk_img02]

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        tmr += 1
        screen.blit(bg_img, [0, 0])
        if tmr%2 == 0:
            screen.blit(kk_imgs[0],[300,200])
        else:
            screen.blit(kk_imgs[1],[300,200])

        #screen.blit(kk_img,[300,200])
        pg.display.update()

        clock.tick(100)
        print(tmr)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()