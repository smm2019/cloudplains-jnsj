'''
#文件夹图片批量重命名
#开源地址：https://github.com/Cyril0563/PIC_EditAll
#作者：Cyril0563
#时间：2022-08-06
'''

import os
import sys
path = 'Images'
Piclist = os.listdir(path)
print("请选择要更改的图片类型序号：")
print("1.jpg|2.png|3.gif|4.bmp|5.jpeg|6.其它|7.退出")
num = input()
if num == '1':
        pic_text = input("请输入重命名前缀：(例如：测试_)，默认回车为空：")
        i = 0
        for item in Piclist:
                if item.endswith('.jpg'):
                        i = i + 1
                        name = pic_text+str(i).zfill(4)
                        src = os.path.join(os.path.abspath(path),item)
                        rep = os.path.join(os.path.abspath(path),name + '.jpg')
                try:
                        os.rename(src,rep)   # src 参数用于指定要进行重命名的目录或文件；rep 参数用于指定重命名后的目录或文件
                        print('已成功替换： %s 为： %s'%(src,rep))
                        # 将转换结果在终端打印出来以便检查
                except:
                        continue
elif num == '2':
        pic_text = input("请输入重命名前缀：(例如：测试_)，默认回车为空：")
        i = 0
        for item in Piclist:
                if item.endswith('.png'):
                        i = i + 1
                        name = pic_text+str(i).zfill(4)
                        src = os.path.join(os.path.abspath(path),item)
                        rep = os.path.join(os.path.abspath(path),name + '.png')
                        try:
                                os.rename(src,rep)
                                print('已成功替换： %s 为： %s'%(src,rep))
                        except:
                                continue
elif num == '3':
        pic_text = input("请输入重命名前缀：(例如：测试_)，默认回车为空：")
        i = 0
        for item in Piclist:
                if item.endswith('.gif'):
                        i = i + 1
                        name = pic_text+str(i).zfill(4)
                        src = os.path.join(os.path.abspath(path),item)
                        rep = os.path.join(os.path.abspath(path),name + '.gif')
                        try:
                                os.rename(src,rep)
                                print('已成功替换： %s 为： %s'%(src,rep))
                        except:
                                continue
elif num == '4':
        pic_text = input("请输入重命名前缀：(例如：测试_)，默认回车为空：")
        i = 0
        for item in Piclist:
                if item.endswith('.bmp'):
                        i = i + 1
                        name = pic_text+str(i).zfill(4)
                        src = os.path.join(os.path.abspath(path),item)
                        rep = os.path.join(os.path.abspath(path),name + '.bmp')
                        try:
                                os.rename(src,rep)
                                print('已成功替换： %s 为： %s'%(src,rep))
                        except:
                                continue
elif num == '5':
        pic_text = input("请输入重命名前缀：(例如：测试_)，默认回车为空：")
        i = 0
        for item in Piclist:
                if item.endswith('.jpeg'):
                        i = i + 1
                        name = pic_text+str(i).zfill(4)
                        src = os.path.join(os.path.abspath(path),item)
                        rep = os.path.join(os.path.abspath(path),name + '.jpeg')
                        try:
                                os.rename(src,rep)
                                print('已成功替换： %s 为： %s'%(src,rep))
                        except:
                                continue
elif num == '6':
        print("请输入要更改的图片类型：")
        type = input()
        pic_text = input("请输入重命名前缀：(例如：测试_)，默认回车为空：")
        i = 0
        for item in Piclist:
                if item.endswith(type):
                        i = i + 1
                        name = pic_text+str(i).zfill(4)
                        src = os.path.join(os.path.abspath(path),item)
                        rep = os.path.join(os.path.abspath(path),name + type)
                        try:
                                os.rename(src,rep)
                                print('已成功替换： %s 为： %s'%(src,rep))
                        except:
                                continue
elif num == '7':
        print("退出系统")
        sys.exit()
else:
        print("输入错误，请重新输入")