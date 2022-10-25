import random
"""
使用python模拟快乐8生成器。选号规则为：
在1-80的范围内随机产生不重复的10个号码，
"""

def card():
    front_list = list(range(1, 81))               # 数字列表
    front = random.sample(front_list, 10)          # 随机取10个数字
    front.sort()                                  # 将两个列表进行升序排序
    for j in front:
        print('%02d' % j, end=' ')                # 依次输出每个值，且个位数前面自动补0
    print('')

print("本程序由Anguss编写,仅供娱乐")
number = input('请输入注数：')
for i in range(int(number)):
    card()
input("按任意键退出..........")