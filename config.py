# coding=UTF-8
# Author:Gentlesprite
# Software:PyCharm
# Time:2024/10/2 11:45
# File:config
# 注意是将cookie填入里面！！否则会报错'',如果不懂需要远程(有偿)请联系微信Gentlesprite
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
cookies = 'miloPipRole=B9EE2911D0313B81FD3714DC29F1EBD1%7Cqc; eas_sid=01q7t213m482v4B6V1a2y8v0V8; PTTuserFirstTime=1723420800000; pgv_pvid=3393997984; ts_uid=1652794583; fqm_pvqid=ddbf8b35-f965-4d42-a2cd-8e05770e6433; qq_domain_video_guid_verify=498df76a07a7edb4; _qimei_h38=c71dd81acd6ddc097e5148090200000f118201; _qimei_q32=077106f3d268c8ad606e44a12ba0d126; _qimei_q36=e81ed7e0311138f68d33568c30001d317a18; RK=Wa1gSYoCw2; ptcz=d26a61d587eee5cf965d45be5e3a0e7243cc8792d4266c34267b1bdc8da059a6; PTTosSysFirstTime=1723939200000; PTTosFirstTime=1723939200000; acctype=qc; appid=101491592; openid=B9EE2911D0313B81FD3714DC29F1EBD1; access_token=90480B063CD79608E3567E8E9979B63F; refresh_token=; eas_entry=https%3A%2F%2Fwww.bing.com%2F; isHostDate=19998; isOsSysDate=19998; isOsDate=19998; pgv_info=ssid=s9431206172; ts_refer=www.bing.com/; weekloop=0-0-0-40; ts_last=nz.qq.com/web202403/activity-list.shtml; nzqqcomrouteLine=main_activity-list; IED_LOG_INFO_NEW=acctype%3Dqc%26openid%3DB9EE2911D0313B81FD3714DC29F1EBD1%26nickName%3D%25E9%259B%25AA%25E7%25A2%25A7%26avatarUrl%3Dhttp%253A%252F%252Fthirdqq.qlogo.cn%252Fek_qqapp%252FAQCibiae4sNww76szUES7T8X53VmLNVDyC4ZZ2c2GUIWO91ay49c9SaZmN3VszHRt5crH0DcSE%252F40; uin=; o2-gopenid=B9EE2911D0313B81FD3714DC29F1EBD1'

