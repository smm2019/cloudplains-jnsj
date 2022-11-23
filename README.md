# ⏰ 自动获取合并Pluto/TvBox等数据源接口配置文件

- 用 Python 实现自动合并 tvbox pluto 等配置文件数据源接口。TVBox、Pluto Player、猫影视TV等影视播放软件通用接口都可使用。Pluto兼容性最强。下载TvBox或者Pluto手机或电视盒子播放软件后，使用下面的网址作为配置文件。就能聚合几大视频平台和很多小的电影网站视频等。

## ⚠️ 注意

- 欢迎免费使用本订阅接口来自网络，仅作学习使用。
- 使用页面所提供的任意资源时，请务必遵守当地法律。

## 📧 播放器接口（安装好软件后，在配置中设置接口，再返回软件主界面）

- https://raw.iqiq.io/cloudplains.cn/jnsj/main/out/tvbox.txt
- https://ghproxy.com/https://raw.githubusercontent.com/cloudplains.cn/jnsj/main/out/tvbox.txt

# 自用知识汇总

# hellow-pages   为python 自学文件，部分源为github 开源采集，如有侵权请联系删除！

# tvbox-page     为自定义的一些tvbox文件；

# GitHub 中文化插件 https://greasyfork.org/zh-CN/scripts/435208

# Github RAW 加速服务（样式，自己替换地址）

香港 https://raw.iqiq.io/liu673cn/box/main/m.json

新加坡 https://raw.kgithub.com/liu673cn/box/main/m.json

日本

https://fastly.jsdelivr.net/gh/liu673cn/box@main/m.json

https://cdn.staticaly.com/gh/liu673cn/box/main/m.json

https://raw.fastgit.org/liu673cn/box/main/m.json

韩国

https://ghproxy.com/https://raw.githubusercontent.com/liu673cn/box/main/m.json

https://ghproxy.net/https://raw.githubusercontent.com/liu673cn/box/main/m.json

https://gcore.jsdelivr.net/gh/liu673cn/box@main/m.json

https://raw.githubusercontents.com/liu673cn/box/main/m.json

# Github 静态加速（样式，自己替换地址）

https://cdn.staticaly.com/gh/liu673cn/box/main/m.json

https://cdn.jsdelivr.net/gh/liu673cn/box@main/m.json

https://purge.jsdelivr.net/gh/


# 修改tvbox源代码

1、修改软件名称地址
app/src/main/res/values/strings.xml

2、修改版本号地址
app/src/main/AndroidManifest.xml

3、修改图标、背景地址

你的地址/app/src/main/res

drawable/app_bg.png为背景，把原来的删掉，自己上传一个新的；

drawable-hdpi/app_icon.png为图标1，把原来的删掉，自己上传一个新的；

drawable-xhdpi/app_icon.png为图标2，把原来的删掉，自己上传一个新的；

drawable-xxhdpi/app_icon.png为图标3，把原来的删掉，自己上传一个新的；

drawable-xxxhdpi/app_icon.png为图标4，把原来的删掉，自己上传一个新的；

4、修改内置源地址

第114行app/src/main/java/com/github/tvbox/osc/api/ApiConfig.java

       


