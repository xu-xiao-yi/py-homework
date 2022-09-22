# 作业概览

## 第一节课作业

### 问题：根据所讲内容安装软件，搭建好线上环境并验证IDE可运行。（提示：安装python、pycharm等）

#### 安装重点：直接下载官网的相关py3.8的安装包，安装时候记得勾选将python环境加入到环境变量中，不勾选后面还是需要自己配置系统环境变量。通过在cmd（命令提示符）中输入`python`然后返回python版本就是安装成功了。

- [x] 详细配置请见安装文档。

![image-20220921192153859](https://soft2176-use.oss-cn-hangzhou.aliyuncs.com/md-pic/image-20220921192153859.png)

## 第二节课作业

#### *具体代码请见当py-homework/samples/SecondClass文件夹下的内容*

- [x] ### 用索引取出下面list中的指定元素

  ![img](https://soft2176-use.oss-cn-hangzhou.aliyuncs.com/md-pic/clip_image002.jpg)

  #### *代码见../ListPrint/list_print.py*

  ##### 主要思路为：嵌套数组的获取和打印，根据数组下标来进行打印。

  ##### 运行结果为:

  ![image-20220922075513386](https://soft2176-use.oss-cn-hangzhou.aliyuncs.com/md-pic/image-20220922075513386.png)

  

- [x] ### 打印0-100，遇到21的时候跳出循环

  #### 代码见../JumpOut/jump_out.py

  ##### 主要思路为：跳出本次循环，即本次循环不参与运算所以使用continue，如果到这次循环就结束则使用break；这里默认的范围是0-100 首尾都取，所以range(0,101);

  ##### 运行结果为:

  ![image-20220922075550722](https://soft2176-use.oss-cn-hangzhou.aliyuncs.com/md-pic/image-20220922075550722.png)

- [x] ### 纸打印80以内的偶数

  #### 代码见../PrintDouble/print_double.py

  ##### 主要思路为：循环0-80范围内的i，i对2取余为0（偶数判定）就打印出来。
  
  ##### 运行结果为：
  
  ![image-20220922075621148](https://soft2176-use.oss-cn-hangzhou.aliyuncs.com/md-pic/image-20220922075621148.png)

## 第三节课作业

#### 具体代码请见当py-homework/samples/ThirdClass文件夹下的内容

###   对发送邮件代码进行修改，换成自己的邮箱并截图保存。

#### 代码见../mail/fetch_mail.py&send_mail.py

##### 主要思路为：首先套用相关代码，根据自己的需求修改邮件的信息。send_mail.py是利用SMTP协议进行发送邮件到指定邮箱。fetch_mail.py是利用POP协议进行获取最新的邮件，也可以进行删除的操作。首先搞清楚几个模板文件的用处。我这边用的是QQ邮箱作为自己的相关服务运营商。首先需要做的是进入QQ邮箱中，开启自己的相关协议。在邮箱-设置-账户-POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务，给它开启就行了。![image-20220921185629982](https://soft2176-use.oss-cn-hangzhou.aliyuncs.com/md-pic/image-20220921185629982.png)

##### 然后查看自己的授权码，需要发送短信到相关号码，然后就生成自己的授权码，该授权码就是自己等会py文件输入的密码（不是自己的邮箱密码），到这里我们相关的准备工作就都已经完成啦！

![image-20220921185834005](https://soft2176-use.oss-cn-hangzhou.aliyuncs.com/md-pic/image-20220921185834005.png)

### ![image-20220921185857462](https://soft2176-use.oss-cn-hangzhou.aliyuncs.com/md-pic/image-20220921185857462.png)

##### 然后我们进行测试（测试均已成功）

![image-20220921190028988](https://soft2176-use.oss-cn-hangzhou.aliyuncs.com/md-pic/image-20220921190028988.png)

![image-20220921190035231](https://soft2176-use.oss-cn-hangzhou.aliyuncs.com/md-pic/image-20220921190035231.png)

- [x] ###  对指导书中海龟画图和TCP/UDP的案例进行学习并运行结果。

#### 海龟：代码见../gui/trutle/* 下的文件

##### 重点思路：使用画笔和数学公式等进行计算来绘画，告知画笔的方向、颜色和前进距离，以及后面的各个步骤（具体还是数学公式等的使用）来使得小海龟走不同的道来实现不同的轨迹。最后调用done()使得窗口等待被关闭，否则将立刻关闭窗口



![image-20220921191247143](https://soft2176-use.oss-cn-hangzhou.aliyuncs.com/md-pic/image-20220921191247143.png)

- [x] ### TCP/UDP：代码见../gui/socket/* 下的文件

  ##### 重点思路：

  ##### 理解一下tcp/udp是干什么的.

  ##### TCP协议进行Socket编程在Python中十分简单，对于客户端，要主动连接服务器的IP和指定端口，对于服务器，要首先监听指定端口，然后，对每一个新的连接，创建一个线程或进程来处理。通常，服务器程序会无限运行下去。同一个端口，被一个Socket绑定了以后，就不能被别的Socket绑定了。

  ##### UDP的使用与TCP类似，但是不需要建立连接。此外，服务器绑定UDP端口和TCP端口互不冲突，也就是说，UDP的9999端口与TCP的9999端口可以各自绑定。

![image-20220921191537063](https://soft2176-use.oss-cn-hangzhou.aliyuncs.com/md-pic/image-20220921191537063.png)

![image-20220921191820089](https://soft2176-use.oss-cn-hangzhou.aliyuncs.com/md-pic/image-20220921191820089.png)

## 第四节课作业

- [x] ### 发散作业：写一个基于python的小项目。

  #### 具体代码请见当py-homework/samples/ForthClass文件夹下的内容

  ##### 详细见项目文档。

  ![image-20220921191050849]( https://soft2176-use.oss-cn-hangzhou.aliyuncs.com/md-pic/image-20220921191050849.png)

  ![image-20220921191129997](https://soft2176-use.oss-cn-hangzhou.aliyuncs.com/md-pic/image-20220921191129997.png)