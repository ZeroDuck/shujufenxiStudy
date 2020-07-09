# -*- coding: utf-8 -*-
'''
@Filename      :绘制多个条形图.py
@Function      :
@Time          :2020/07/09 23:33:50
@Author        :Zero
@Version       :1.0
@software      :VScode
'''


from matplotlib import pyplot as plt
from matplotlib import font_manager
import matplotlib

# 设置中文字符显示
font = {'family': 'Microsoft YaHei',
        'weight': 'bold',
        'size': '15'}
matplotlib.rc("font", **font)

my_font = font_manager.FontProperties(fname=r"C:\Windows\Fonts\simfang.ttf")

#数据
a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]

#设置图片格式大小
plt.figure(figsize=(20,8),dpi=80)

#设置横坐标为电影名，纵坐标为票房，x_14为开始的四个起点，x_15,x_16为起点加宽度间隔
jiange=0.3
x_14 = list(range(len(a)))
x_15 = [i+jiange for i in x_14]
x_16 = [i+jiange*2 for i in x_14]

#设置横坐标
plt.xticks(x_15,a,fontproperties=my_font)
plt.bar(x_14,b_14, width=0.3,label="14日票房",color = "yellow")
plt.bar(x_15,b_15, width=0.3,label="15日票房",color = "orange")
plt.bar(x_16,b_16, width=0.3,label="16日票房",color = "green")

plt.legend(prop = my_font, loc = "best")
plt.show()
