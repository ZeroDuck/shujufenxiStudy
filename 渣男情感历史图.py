# -*- coding: utf-8 -*-
'''
@Filename      :渣男情感历史图.py
@Function      :
@Time          :2020/06/23 23:08:06
@Author        :Zero
@Version       :1.0
@software      :VScode
'''


from matplotlib import pyplot as plt
from matplotlib import font_manager
import matplotlib

#数据
y1 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
x = range(20)
y2 = [1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]


# 图片大小设置,中文字体设置,标题说明设置
plt.figure(figsize=(20, 8), dpi=80)
my_font = font_manager.FontProperties(fname=r"C:\Windows\Fonts\simkai.ttf")
font = {  'family' : 'Microsoft YaHei',  
          'weight' : 'bold'}
matplotlib.rc("font",**font)

plt.xlabel("年龄： 周岁")
plt.ylabel("交到女朋友个数： 位")
plt.title("渣男情感历史图")

#设置刻度
_xtick_labels = ["{}岁".format(i) for i in range(11,31)]
plt.xticks(x,_xtick_labels)

#设置网格
plt.grid(alpha=0.5)  #alpha为透明度，还有其他参数可以查看具体用法


#画图并区分曲线谁是谁的
plt.plot(x,y1,label= "自己", color = 'green', linestyle = '--')
plt.plot(x,y2,label= "同桌", linestyle = ':', linewidth =5)

#添加图例
plt.legend(prop = my_font, loc = "best") #这里的loc是图例的位置， prop参数是字体参数
plt.show()