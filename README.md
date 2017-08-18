# SpiderZi5Book

# 一点福利，有关于书


## 初衷

推荐一个网站--子乌书简。

现在越来越多的看电子书，也经常在网上找书。众多电子书网站中，子乌书简是我最喜欢的，免费，没有广告。

我还没买 kindle 的时候，在这里下了不少书，《古龙全集》、《群星，我的归宿》等。后来买了 kindle，有很多书可以直接在亚马逊买或者租，就逛得少了，不过偶尔还是会用，而且它还有针对 kindle 的推送可能，可以说非常的良心了。

前几天突然想起着看看有没有更新什么新书，这才发现作者已经很久没有更新内容，在国内不能访问网站了。我估摸着离关站也不远了，于是就想把书弄下来备份一下，毕竟我也不是随时都能越过长城。

花了两天，磕磕跘跘的写好了爬虫，把书都爬了下来（希望没有对作者的服务器带来太大的压力），想着也可以方便一下不能访问国外网站的人，就放到自己的服务器上。

### **福利在末尾**

## 总结

爬书的时候出现了一些问题，有的是因为忘了，有的是不会，这里放点自认为值得晒的

### 有关 Python
* #### 执行 Linux shell 命令
 这一会用到了两种方式，都是利用 OS 包
1、system 方法
```Python
# 将所要执行的命令包含参数合成 command 字符串，当做 system 函数的参数
os.system(command)
```
   2、直接执行命令，将命令当成一个方法
```Python
# os 后接命令，相当于函数的形式
os.mkdir(detailFolder)
```
* #### 截取文件格式后缀
利用【.】分割字符串，取最后一截即是文件后缀
```Python
filetype = link.split('.')[-1]
```
### 有关 Linux

* #### 行尾符问题
因为 Unix、Windows 编码格式问题，导致文件在 Linux 中执行时会报类似下面的问题
```Shell
-bash /var/ftp/SpiderZi5Book.py: /usr/bin/python^M: bad interpreter
```
解决方法有很多，这里放用的一种，替换掉所有的结尾符号
```Shell
# ^M 的输入方法为 同时按下 Ctrl 和 V ，再按 M
sed -i 's/^M//g' /var/SpiderZi5Book.py
```
* ####  添加中文支持 ，主要参考[搬瓦工centos设置中文](http://www.cellmean.com/%E6%90%AC%E7%93%A6%E5%B7%A5centos%E8%AE%BE%E7%BD%AE%E4%B8%AD%E6%96%87)
1、 安装中文支持组件
```Shell
yum groupinstall chinese-support
```
2、修改配置文件 vim /etc/sysconfig/i18，然后重启系统
```Shell
LANG="zh_CN.UTF-8"
SYSFONT="wqy-zenhei"
SUPPORTED="zh_CN:zh:en_US.UTF-8:en_US:en"
```
3、检查当前语言情况
```Shell
locale
```
若结果如下则 OK
>  LANG=zh_CN.UTF-8
LC_CTYPE=”zh_CN.UTF-8″
LC_NUMERIC=”zh_CN.UTF-8″
LC_TIME=”zh_CN.UTF-8″
LC_COLLATE=”zh_CN.UTF-8″
LC_MONETARY=”zh_CN.UTF-8″
LC_MESSAGES=”zh_CN.UTF-8″
LC_PAPER=”zh_CN.UTF-8″
LC_NAME=”zh_CN.UTF-8″
LC_ADDRESS=”zh_CN.UTF-8″
LC_TELEPHONE=”zh_CN.UTF-8″
LC_MEASUREMENT=”zh_CN.UTF-8″
LC_IDENTIFICATION=”zh_CN.UTF-8″
LC_ALL=

* ####  安装 vsftpd，主要参考[香菇肥牛的博客](https://qing.su/article/55.html)
1、登录 root 账户安装 vsftpd
```Shell
yum install vsftpd
```
2、 创建用户，实际以为系统用户
```Shell
# 创建用户
useradd ftpuser
# 如果需要同时指定新建 ftp 用户的目录可以这样
# useradd -d path -s  ftpuser
# 修改 ftpuser 的密码
#如果需要的话，删除用户
# userdel ftpuser
passwd ftpuser
```
3、更改配置文件
```Shell
# 具体修改项可再查相关文章
/etc/vsftpd/vsftpd.conf
```
4、启动服务
```Shell
# /后为关闭和重启命令
service vsftpd start/stop/restart
```


## 福利
* #### 书
**关注公众号，发送【书】，会自动回复链接地址**
* #### 代码
**爬虫代码本身倒没有太多可讲的，不过你若是感兴趣，可以去 Github 下载，顺便给个星星就更好了 ，地址是
https://github.com/myWythe/SpiderZi5Book**

---
我是 Wythe，iOS 开发者，对其他技术也有好奇。公众号 WytheTalk，从一个程序员的角度看世界，主要是技术分享，也有对互联网各种事的观点。
欢迎关注
![WytheTalk.jpg](http://upload-images.jianshu.io/upload_images/446839-6e1ec13cf518d34c.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
