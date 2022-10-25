import os
import shutil

"""
一个文件夹中有多个文件，把所有文件分成 num 份，新建文件夹放入
"""

# 文件存放地址
file_path = 'D:\invoice\\'
# 每个文件夹存放的个数
num = 200
list_ = os.listdir(file_path)
if num > len(list_):
    print('num长度需小于:', len(list_))
    exit()
if int(len(list_) % num) == 0:
    num_file = int(len(list_) / num)
else:
    num_file = int(len(list_) / num) + 1
cnt = 0
for n in range(1, num_file + 1):  # 创建文件夹
    new_file = os.path.join(file_path + str(n))
    if os.path.exists(new_file + str(cnt)):
        print('该路径已存在，请解决冲突', new_file)
        exit()
    print('创建文件夹：', new_file)
    os.mkdir(new_file)
    list_n = list_[num * cnt:num * (cnt + 1)]
    for m in list_n:
        old_path = os.path.join(file_path, m)
        new_path = os.path.join(new_file, m)
        shutil.copy(old_path, new_path)
    cnt += 1