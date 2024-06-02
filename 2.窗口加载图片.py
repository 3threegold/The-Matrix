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
    # 加载一张图片到窗口
    # vscode的相对路径是相对于当前工程目录的，再写相对路径之前请先看完这个链接，里面有关于python的相对路径的说明，非常重要！！！非常重要！！！非常重要！！！
    # https://blog.csdn.net/weixin_43698776/article/details/135633558
    img = pg.image.load("images/蓝胖子.jpg")
    # 将图片渲染到窗口 blit(绘制内容，(横坐标，纵坐标))
    window.blit(img,(0,0))
    for e in pg.event.get():
        if e .type == pg.QUIT:
            exit()
    
    # 更新渲染
    pg.display.flip()