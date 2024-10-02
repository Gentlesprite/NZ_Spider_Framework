# coding=UTF-8
# Author:Gentlesprite
# Software:PyCharm
# Time:2024/10/2 11:45
# File:config
# 注意是将cookie填入里面！！否则会报错'',如果不懂需要远程请联系微信Gentlesprite
'''
cookie获取方法:打开https://nz.qq.com/cp/a20240822treasure/index.html?e_code=544119
最好使用edge浏览器,不要使用wegame自带的浏览器,因为没法按F12
1.登录你需要领取的账号并选择好大区
2.按F12,在弹出来界面里面选择console,中文叫做控制台
3.在控制台输入document.cookie然后回车
4.然后你就会发现打印出来了一串字符,复制下来,注意不要复制前后的引号,把复制的内容粘贴进cookies = '复制的内容'
千万注意这个引号只能一个,不能这样是'' ''2个引号就请删一对引号
5.配置完成以后保存然后python main.py就行了后续我会打包成exe配置好只需要双击exe即可
'''
cookies = ''

