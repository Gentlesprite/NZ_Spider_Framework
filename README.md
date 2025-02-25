# 使用教程:

- `cookie`获取方法:使用**edge浏览器**打开需要领取的活动页面进行**登录并选好大区**（**不要使用**`wegame`自带的浏览器,因为没法按`F12`)。

- 按F12,在弹出来界面里面选择`console`，中文叫做控制台。

- ```shell
  # 在控制台输入以下内容然后回车(前提是确保你登录并选择了大区)。
  document.cookie
  ```

- 复制下面打印出来的一长串字符，全部复制完！

- 打开当前目录下的`cookie.txt`文本文件，将刚刚复制的长串字符粘贴进去然后保存。

- 在`F12`中点击网络，点击`F12`左上角红色的清除按键（避免找错网站），确保所以项都已被清除干净，然后此时点击需要领取的按钮。

  ```shell
  # python是必要的,推荐版本使用3.11.7以上。
  # 安装python与git并且配置环境变量(自行搜索安装)。
  # 使用git克隆代码(需要安装git)或者直接在项目仓库下载。
  git clone https://github.com/Gentlesprite/NZ_Spider_Framework.git
  cd NZ_Spider_Framework
  # 安装依赖。
  pip install -r requirements.txt
  ```

- #此时F12界面中点击并选择`amesvr?sServiceType=nz`然后找到并点击`载荷`或者叫`负载`，拉开表单数据，把表单数据里的数据对找填入到之后的`config.py`中对应的变量里面，并且配置好领取时间和并发数。

  ```shell
  python main.py
  ```

- 第一次打开软件的时候会执行一次领取操作，如果看见了领取返回的信息那就是配置完成了,下次整点就会并发执行。

- 要领取之前提前打开，并且全程联网不可关闭！

- 注意观察当前目录下的`history.log`，这个是领取的日志文件，领到了软件就可以关了。

- 因为软件是是多线程并发请求，如果发现逆战官网进不去或运行了一段时间软件报错了那就是`ip`被封了。重启家里光猫即可。软件默认设置的是**10次**并发，正常情况是不会封`ip`的，除非你多开本软件了。

# 支持作者:

![image](https://github.com/Gentlesprite/NZ_Spider_Framework/blob/main/doc/扫码支持作者.png)
