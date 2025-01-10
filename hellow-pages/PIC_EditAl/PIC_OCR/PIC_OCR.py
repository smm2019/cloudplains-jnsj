'''
#手写表格图片转换为表格文件
#开源地址：https://github.com/Cyril0563/PIC_EditAll
#作者：Cyril0563
#时间：2022-08-10
'''

# 图片识别
from aip import AipOcr
# 时间模块
import time
# 网页获取
import requests
# 操作系统接口模块
import os





# 获取文件夹中所有图片
def get_image():
    images = []  # 存储文件夹内所有文件的路径（包括子目录内的文件）
    for root, dirs, files in os.walk(image_path):
        path = [os.path.join(root, name) for name in files]
        images.extend(path)
        #判断是否有图片
        if not images:
            print("没有图片")
            return
        else:
            return images




def Image_Excel(APP_ID, API_KEY, SECRET_KEY):
    #  调用百度AI接口
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    # 循环遍历文件夹中图片
    images = get_image()
    for image in images:
        # 以二进制方式打开图片
        img_open = open(image, 'rb')
        # 读取图片
        img_read = img_open.read()
        # 调用表格识别模块识别图片
        table = client.tableRecognitionAsync(img_read)
        # 获取请求ID
        request_id = table['result'][0]['request_id']
        # 获取表格处理结果
        result = client.getTableRecognitionResult(request_id)
        # 处理状态是“已完成”，获取下载地址
        while result['result']['ret_msg'] != '已完成':
            time.sleep(2)  # 暂停2秒再刷新
            result = client.getTableRecognitionResult(request_id)
        download_url = result['result']['result_data']
        #print(download_url)
        # 获取表格数据
        excel_data = requests.get(download_url)
        # 根据图片名字命名表格名称
        xlsx_name = image.split(".")[0] + ".xls"
        xlsx = open(xlsx_name, 'wb')
        # 将数据写入excel文件并保存到
        xlsx.write(excel_data.content)
        print("图片" + image + "识别成功")
        time.sleep(5)
        #关闭文件
        xlsx.close()
        img_open.close()
        # 删除图片
        os.remove(image)

if __name__ == '__main__':

    password = '15385639709'
    in_password = input('请输入密码：')
    if in_password == password:
        print('登录成功')
        print('正在识别中，请稍等...')
        #在目录下新建Images文件夹，存放图片

        image_path = 'Images'#input('请输入图片所在文件夹路径：')
        # 创建Images文件夹
        if not os.path.exists(image_path):
            os.makedirs(image_path)
            print("软件初始化成功……")
            print("检测到首次使用软件，请将需要识别的图片放置Images文件夹下")
            time.sleep(5)
            exit()
        else:
            APP_ID = ''#input('APP_ID:')
            API_KEY = ''#input('API_KEY:')
            SECRET_KEY = ''#input('SECRET_KEY:')
            Image_Excel(APP_ID, API_KEY, SECRET_KEY)
    else:
        print('密码错误')
        exit()