import pygame as pg

pg.init() #初始化

# 设置宽高
WIDHT = 600
HEIGHT = 600

# 设置窗口
window = pg.display.set_mode((WIDHT,HEIGHT))
# 设置窗口的标题
pg.display.set_caption("第一个运行的游戏窗口")
# 设置窗口的背景色 fill((r，g，b))
window.fill((255,255,255))
# 主循环
while True:
#    渲染文字
    # 1.创建字体对象 SysFont(字体类型，字号大小)
    font = pg.font.SysFont("SimHei",22)

    # 2.创建文字对象 render(渲染的字体内容,True,(字体颜色rgb值))
    text = font.render("这是渲染在窗口的文字",True,(255,0,0))

    # 3.渲染到窗口
    window.blit(text,(0,0))

    for e in pg.event.get():
        if e .type == pg.QUIT:
            exit()
    
    # 更新渲染 
    pg.display.flip()