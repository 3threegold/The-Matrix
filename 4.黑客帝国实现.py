import pygame as pg
'''
pygame是一个第三方库，需要安装

安装命令（在cmd里执行下面的命令）：
pip install pygame

如果下载报错，请看这个链接，里面有详细的pip介绍和报错解决方法
https://blog.csdn.net/weixin_43698776/article/details/135575203
'''

import random
'''
random是Python内置的随机数函数库，不需要下载
'''
pg.init()

# 设置窗口的宽度和高度
WIDHT = 1000
HEIGHT = 600
# 每列文字的字符间距
font_px = 22

# 窗口，固定的语法
window = pg.display.set_mode((WIDHT,HEIGHT))
# 设置画布
bg_face = pg.Surface((WIDHT,HEIGHT),flags=pg.SRCALPHA)
pg.Surface.convert(bg_face)
# 画布透明度的颜色 rgb(r,g,b,0-255)，0表示完全透明
bg_face.fill(pg.Color(0,0,0,28))
# 标题
pg.display.set_caption("黑客帝国")
# 背景色
window.fill((0,0,0))

# 准备26个英文字母用于页面的内容显示
words = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c',
         'v', 'b', 'n', 'm']

# 1.创建字体对象
font = pg.font.SysFont("SimHei",20)

# 2.创建26个文字对象
# texts = []
# for i in words:
#     text = font.render(i,True,(0,255,0))
#     texts.append(text)

# 以上内容可以简写 列表推导式
texts = [font.render(i,True,(0,255,0)) for i in words]

# 能绘制的列数
columns = int(WIDHT/font_px)

# 用列表来装行数，决定纵坐标
# for只能遍历一个可迭代的对象（比如列表、字符串。只有这种类型的数据才能一个个循环，一个单纯的数字是不能循环的）
# range(10) 返回一个可迭代的对象，这个对象是一个数字序列，从0开始，到9结束，你可以打印range(10)看看，代码：print(list(range(10)))
drops = [0 for i in range(columns)]

# 主循环
while True:

    window.blit(bg_face,(0,0))
    for e in pg.event.get():
        if e.type == pg.QUIT:
            exit()
    # 循环的列数
    # n = 0
    for n in range(columns):
        # 随机取一个文字对象来渲染到窗口
        text = random.choice(texts)
        # 将文字对象渲染
        window.blit(text,(n * font_px, drops[n] * font_px ))
        drops[n] += 1
        # print(f'这是横坐标，第{i}列')
        # print(f'这是纵坐标，第{drops[i]}行')
        # 通过概率事件，让文字随机掉
        if random.random() > 0.95 or drops[n] * font_px > HEIGHT:
            drops[n] = 0
    # 更新窗口
    pg.display.flip()
    # 给一定的暂停时间，让文字缓慢下落
    pg.time.delay(50)