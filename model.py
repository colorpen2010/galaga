import enemycl
import playercl

debug = False
paint = True
draw = True
player = playercl.Playerc(530, 530)
enemy1 = enemycl.Enemyc('original/enemy/big_green1.png', 'original/enemy/big_green2.png', 100, 100)
enemy2 = enemycl.Enemyc('original/enemy/butterfly_red1.png', 'original/enemy/butterfly_red2.png', 200, 100)


def cyber_tapok():
    enemy1.rect_remaker(draw)
    enemy2.rect_remaker(draw)
