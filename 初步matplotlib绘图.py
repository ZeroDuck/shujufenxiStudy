# -*- coding: utf-8 -*-
'''
@Filename      :初步matplotlib绘图.py
@Function      :
@Time          :2020/06/22 23:04:13
@Author        :Zero
@Version       :1.0
@software      :VScode
'''


from matplotlib import pyplot as plt
import random
import matplotlib 
from matplotlib import font_manager


#设置字体，显示中文汉字


# font = {'family' : 'Microsoft YaHei',  
#           'weight' : 'bold',  
#           'size'   : '10' #这里一定要是数字，显示字体大小，可以不要这行，用默认字体大小
#           }
# matplotlib.rc("font",**font)

# matplotlib.rc("font",family="Microsoft Yahei", weight = "bold", size = 8)


#第二种方法


my_font = font_manager.FontProperties(fname=r"C:\Windows\Fonts\simsun.ttc")



x = range(0,120)
y = [random.randint(20,35) for i in range(120)]
#设置图片大小
plt.figure(figsize = (20,8),dpi = 80)

plt.plot(x,y)

#设置刻度
_xtick_labels = ["11点{}分".format(i) for i in range(60)]
_xtick_labels += ["12点{}分".format(i) for i in range(60)]
plt.xticks(list(x)[::3], _xtick_labels[::3], rotation = 45,fontproperties= my_font)
_ytick_labels = ["{}°C".format(i) for i in y]
plt.yticks(y,_ytick_labels,fontproperties= my_font)

#添加坐标轴信息
plt.xlabel(r"时间 Time /min", fontproperties = my_font)
plt.ylabel(r"温度 Temperature /℃", fontproperties = my_font)
plt.title("初步学习，绘制随机的时间温度图", fontproperties = my_font)

plt.show()
