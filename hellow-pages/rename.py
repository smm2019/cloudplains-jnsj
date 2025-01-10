# -*- coding: UTF-8 -*-
"""
@Author  ：远方的星
@Time   : 2021/4/16 9:16
@CSDN    ：https://blog.csdn.net/qq_44921056
@腾讯云   ： https://cloud.tencent.com/developer/column/91164
"""
import os

path = input('请输入你想更改的文件的路径（如D:/图片/风景）：')
file_list = os.listdir(path)
file_list.sort()  # 对列表内容进行排序，默认为升序

i = 0  # 用于记录重命名，方便重命名
for item in file_list:
    if item.endswith('.jpg'):  # 这里以.jpg进行判断文件名
        src = os.path.join(path, item)
        dst = os.path.join(os.path.abspath(path), str(i) + '.jpg')

        try:
            os.rename(src, dst)
            print('已将{}更改为{}'.format(src, dst))
            i += 1
        except Exception as e:
            print(e)
            print('{}更改失败'.format(src))
print('所有目标文件已完成全部更改')
