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

俊老仓库打开下面，第114行app/src/main/java/com/github/tvbox/osc/api/ApiConfig.java

takagen99仓库

app/src/main/res/values-zh/strings.xml

5、修改默认缩略图、硬解、dns地址：app/src/main/java/com/github/tvbox/osc/base/App.java
添加以下代码
//自定义默认配置，硬解，安全dns，缩略图
       if (!Hawk.contains(HawkConfig.IJK_CODEC)) {            Hawk.put(HawkConfig.IJK_CODEC, "硬解码");        } 
       if (!Hawk.contains(HawkConfig.DOH_URL)) {            Hawk.put(HawkConfig.DOH_URL, 2);        }
       if (!Hawk.contains(HawkConfig.SEARCH_VIEW)) {            Hawk.put(HawkConfig.SEARCH_VIEW, 2);        }
       
       

# 以上为互联网流传资源，不保证内容的真实性和可靠性。
# 本页面只是收集，供学习测试用，有需要自取。


