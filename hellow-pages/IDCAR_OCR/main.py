#IPTV直播源地址加解密
#开源地址：https://github.com/Cyril0563/IDCAR_OCR
#作者：Cyril0563
#由CSDN博客：https://blog.csdn.net/Alearn_/article/details/108587572
#增加性别、民族、出生、住址、修改而来
#时间：2022-08-08



import requests
import base64
import json
import os
import pandas as pd


def getAccessToken():
    url = "https://aip.baidubce.com/oauth/2.0/token"
    data = {
        'grant_type': 'client_credentials',
        'client_id': '你的百度ak密钥',
        'client_secret': '你的百度sk密钥'',
    }
    response = requests.post(url=url, data=data)
    data2 = json.loads(response.text)
    accesstoken = data2['access_token']
    return accesstoken


def get_images(path):
    files = os.listdir(path)  # 得到文件夹下所有文件的名称
    images = []
    for file in files:
        try:
            filePath = os.path.join(path, file)
            with open(filePath, 'rb') as f:
                image = base64.b64encode(f.read())
                images.append(image)
        except Exception as e:
            print(str(e))
    return images


def recognize_Pic(path):
    # step1: 获取accessToken
    access_token = getAccessToken()
    # step2: 获取图片集合
    images = get_images(path)

    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/idcard"
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    dic = []
    for image in images:
        name, sex, ethnic, dates, address, id_num = getText(image, request_url, headers)
        dic.append({'姓名': name, '性别': sex, '民族': ethnic, '出生': dates, '住址': address, '身份证号码': id_num})
    print(dic)
    writeExcel(dic)


def writeExcel(dic):
    pf = pd.DataFrame(dic)
    order = ['姓名', '性别', '民族', '出生', '住址', '身份证号码']
    pf = pf[order]
    file_path = pd.ExcelWriter(r'识别信息写入EXCEL路径')#E:\OCR\OCR.xlsx
    pf.fillna(' ', inplace=True)
    pf.to_excel(file_path, encoding='utf-8', index=False, sheet_name="身份证信息")
    file_path.save()


def getText(image, request_url, headers):
    params = {"id_card_side": "front", "image": image}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        data = response.json()
        print(data)
        name = data['words_result']['姓名']['words']
        sex = data['words_result']['性别']['words']
        ethnic = data['words_result']['民族']['words']
        datas = data['words_result']['出生']['words']
        address = data['words_result']['住址']['words']
        id_num = data['words_result']['公民身份号码']['words']
        return (name, sex, ethnic, datas, address, id_num)
    else:
        print('识别错误')


if __name__ == '__main__':
    path = r'身份证照片路径地址'#E:\IDCAR_TOP
    recognize_Pic(path)
