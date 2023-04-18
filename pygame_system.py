import pygame as pg
import sys

def main():
    pg.display.set_caption("はじめてのPygame")#ゲームの初期化
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    fonto  = pg.font.Font(None, 80)
    tmr = 0#時計の初期化

    while True:#無限ループするところ
        for event in pg.event.get():#userからの入力をここで処理
            if event.type == pg.QUIT: return#quit=✖ボタンのクリック押されたら戻る
        
        tmr += 1
        txt = fonto.render(str(tmr), True, (255, 255, 255))
        screen.fill((0, 0, 0))
        screen.blit(txt, [300, 200])#txtをスクリーンの300,200の位置に張り付ける
        pg.display.update()
        clock.tick(1)#引数にフレームレート（単位時間当たり）今回は１秒に１回while文が回ってるから時間のカウント


if __name__ == "__main__":#他のファイルをインポートするときは以下のコード動かない。インポート終わったら以下のコードが動く
    pg.init()#毎回書かなきゃいけない。多分初期化？
    main()
    pg.quit()#これも毎回
    sys.exit()#システムの終了