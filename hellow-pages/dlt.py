import random
"""
使用python模拟大乐透号码生成器。选号规则为：
前区在1-35的范围内随机产生不重复的5个号码，
后区在1-12的范围内随机产生不重复的2个号码。
"""


def card():
    front_list = list(range(1, 36))               # 前区数字列表
    front = random.sample(front_list, 5)          # 随机取5个数字
    back_list = list(range(1, 13))                # 后区数字列表
    back = random.sample(back_list, 2)            # 随机取两个数字
    front.sort()                                  # 将两个列表进行升序排序
    back.sort()
    for j in front:
        print('%02d' % j, end=' ')                # 依次输出每个值，且个位数前面自动补0
    print(end='/ ')                            # 前区与后区之间有一定间隔
    for k in back:
        print('%02d' % k, end=' ')
    print('')

print("本程序由Anguss编写,仅供娱乐使用")
number = input('机选注数：')
for i in range(int(number)):
    card()
input("按任意键退出..........")