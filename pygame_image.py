import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img01 = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img02 = pg.transform.flip(bg_img01,True,False)
    kk_img01 = pg.image.load("ex01/fig/3.png")
    kk_img01 = pg.transform.flip(kk_img01,True,False)
    kk_img02 = pg.transform.rotozoom(kk_img01,3,1.0)
    kk_img03 = pg.transform.rotozoom(kk_img02,7,1.0)
    kk_img04 = pg.transform.rotozoom(kk_img02,10,1.0)
    kk_imgs = [kk_img01,kk_img02,kk_img03,kk_img04]

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        tmr += 1
    
        if tmr == 3200:
            tmr=0
        screen.blit(bg_img01, [-tmr,0])
        screen.blit(bg_img02, [1600-tmr,0])
        screen.blit(bg_img01,[3200-tmr,0])


        if tmr%300 >= 150:
            screen.blit(kk_imgs[0],[300,200])
        else:
            screen.blit(kk_imgs[1],[300,200])
 
        pg.display.update()

        clock.tick(100)
        print(tmr)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()