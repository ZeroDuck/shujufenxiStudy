# -*- coding: utf-8 -*-
'''
@Filename      :单个条形图初试.py
@Function      :
@Time          :2020/07/09 22:49:03
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


# 数据
a = ["战狼2", "速度与激情8", "功夫瑜伽", "西游伏妖篇", "变形金刚5：最后的骑士", "摔跤吧！爸爸", "加勒比海盗5：死无对证", "金刚：骷髅岛", "极限特工：终极回归",
     "生化危机6：终章", "乘风破浪", "神偷奶爸3", "智取威虎山", "大闹天竺", "金刚狼3：殊死一战", "蜘蛛侠：英雄归来", "悟空传", "银河护卫队2", "情圣", "新木乃伊", ]

b = [56.01, 26.94, 17.53, 16.49, 15.45, 12.96, 11.8, 11.61, 11.28,
     11.12, 10.49, 10.3, 8.75, 7.55, 7.32, 6.99, 6.88, 6.86, 6.58, 6.23]

# 数据处理
plt.figure(figsize=(20, 8), dpi=80)

plt.xticks(fontproperties = my_font)
plt.yticks(range(len(a)), a, fontproperties=my_font, rotation=0)


#画图，bar是直筒型（粗细是weigh），barh是横放型（粗细是height），同时改一下上面的xy坐标轴的信息。
plt.barh(range(len(a)), b, height=0.5, color="Y")


#保存图片
plt.savefig("./movie.png")
plt.grid(alpha=0.5)

plt.show()
