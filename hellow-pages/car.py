"""
在1.0基础上，提供某品牌汽车的首页，依次爬取改该品牌汽车的所有车型的所有车身外观图
"""
import requests
from bs4 import BeautifulSoup
import os, shutil
from pyquery import PyQuery as pq
from tqdm import tqdm

def make_dir(dir):
    if os.path.exists(dir):
        shutil.rmtree(dir, ignore_errors=True)
    os.makedirs(dir)
    print('Folder successfully created', dir)


def save_img(img_urls, data_dir):
    i = 0
    for src in img_urls:
        img_name = '%d.jpg'%(i)
        src = 'http:' + src
        content = requests.get(src).content
        with open(os.path.join(data_dir, img_name), 'wb') as f:
            f.write(content)
            f.close()
        print('Successful preservation %s'%(os.path.join(data_dir, img_name)))
        i += 1


class Spider:
    def __init__(self, url, ori_url, name = ''):
        self.ori_url = ori_url
        self.data_dir = name + os.path.split(url)[1]
        self.url = url
        self.soup = BeautifulSoup(requests.get(url=url).text, 'lxml')

        make_dir(self.data_dir)

        self.img_urls = []
        self.car_type_urls = []
        print('Name: %s, Original URL: %s, Fetch From %s, Save as: %s' % (name, self.ori_url, self.url, self.data_dir))

    def get_car_type_url(self):
        print('Start Get Car Type...')
        for div in tqdm(self.soup.find_all('div', {'class':'uibox-con carpic-list02'})):
            for li in div.contents[0].contents:
                obj = {
                    'name':'',
                    'sum':'',
                    'url':'',
                    'detail_url': None
                }
                li = li.contents
                obj['url'] = self.ori_url + li[0].get('href')
                obj['name'] = li[1].contents[0].contents[0].get('title')
                self.car_type_urls.append(obj)
        pass

    def get_car_detail_url(self):
        print('Start Get Detail Information...')
        for car_type in tqdm(self.car_type_urls):
            for div in pq(url=car_type['url'])('.uibox').items():
                flag = False
                for a in div('.uibox-title a').items():
                    if a.text() == '车身外观':
                        car_type['detail_url'] = None if a.attr('href') is None else (self.ori_url + a.attr('href'))
                        car_type['sum'] = div('.uibox-title .uibox-title-font12').text()
                        flag = True
                        break
                if flag:
                    break

        print(self.car_type_urls, len(self.car_type_urls))

    def download_img(self):
        print('Start Download...')
        for car_obj in tqdm(self.car_type_urls):
            img_dir = os.path.join(self.data_dir, car_obj['name']+car_obj['sum'])
            make_dir(img_dir)
            if car_obj['detail_url'] is None:
                continue
            img_urls = []
            for img in BeautifulSoup(requests.get(url=car_obj['detail_url']).text, 'lxml').find_all('img'):
                src = str(img.get('src')).replace('480x360_0_q95_c42_', '1024x0_1_q95_')
                if src.find('1024x0_1_q95_') == -1:
                    continue
                img_urls.append(src)
            save_img(img_urls, img_dir)

if __name__ == '__main__':
    ori_url = 'https://car.autohome.com.cn'
    url = 'https://car.autohome.com.cn/pic/brand-91.html'
    name = '红旗'
    s = Spider(url, ori_url, name)
    s.get_car_type_url()
    s.get_car_detail_url()
    s.download_img()
    pass
