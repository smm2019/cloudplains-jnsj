- 欢迎免费使用本订阅接口来自网络，仅作学习使用。
## 📧 播放器接口（安装好软件后，在配置中设置接口，再返回软件主界面）

- https://ghproxy.com/https://raw.githubusercontent.com/cloudplains/jnsj/main/out/tvbox.txt
- https://cloudplains.github.io/jnsj/out/tvbox.txt


# Github RAW 加速服务（样式，自己替换地址）


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

       


