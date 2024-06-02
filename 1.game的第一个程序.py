# 引入库
import pygame as pg #取别名

# 初始化pg
pg.init()

# 设置窗口的宽高
WIDHT = 600
HEIGHT = 600

# 设置一个游戏窗口
window = pg.display.set_mode((WIDHT,HEIGHT))

# 游戏的主循环
while True:
    # pass  作用：占位操作，保证代码结构的完整性
    # 监听用户事件关闭窗口
    for event in pg.event.get():
        # 事件是有很多类型的
        if event . type == pg.QUIT:
            exit()

# 游戏的最小框架
