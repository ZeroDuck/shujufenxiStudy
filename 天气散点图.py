# -*- coding: utf-8 -*-
'''
@Filename      :天气散点图.py
@Function      :
@Time          :2020/06/27 14:54:00
@Author        :Zero
@Version       :1.0
@software      :VScode
'''

from matplotlib import pyplot as plt
from matplotlib import font_manager
import matplotlib


#设置中文字体

font = {'family' : 'Microsoft YaHei',  
          'weight' : 'bold',  
          'size'   : '10'} 
matplotlib.rc("font", **font)

my_font = font_manager.FontProperties(fname = r"C:\Windows\Fonts\simkai.ttf")

#数据
y_3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y_10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]
x_3 = range(1,32)
x_10 = range(42,73)


#设置图形大小
plt.figure(figsize=(20, 8), dpi=80)

# 设置刻度

_x = list(x_3)+list(x_10)  #这里表示画出多少个刻度，并在中间留空
_xticks_labels = list("3月{}日".format(i) for i in x_3)
_xticks_labels += list("10月{}日".format(i-31) for i in x_10)
_yticks_labels =list("{}℃".format(i) for i in range(1,30))
plt.xticks(_x, _xticks_labels, rotation = 45, fontproperties = my_font)
plt.yticks(range(1,30), _yticks_labels,fontproperties = my_font)


plt.xlabel("日期", fontproperties = my_font)
plt.ylabel("气温：℃", fontproperties = my_font)
plt.title("3月份与10月份气温的散点图", fontproperties = my_font)
#绘图
plt.scatter(x_3, y_3, label = "三月份的气温")
plt.scatter(x_10, y_10, label ="十月份的气温")

plt.grid(alpha = 10)
#图例
plt.legend(loc = "upper left", prop = my_font)

plt.show()
