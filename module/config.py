# coding=UTF-8
# Author:Gentlesprite
# Software:PyCharm
# Time:2025/2/25 17:55
# File:config.py
# 全新周年庆超强Q币掉落活动活动配置文件,活动地址如下(已经配置好请求数据,直接在cookie.txt填入cookie内容即可使用):
# https://nz.qq.com/cp/a20250623act/
MAX_THREADS: int = 3  # 并发请求数。
iActivityId: str = '751315'
sServiceDepartment: str = 'group_a'
iFlowId: str = '1144653'
sMiloTag: str = 'AMS-nz-0730180939-qV5wRZ-751315-1144653'
e_code: str = '0'
g_code: str = '0'
eas_url: str = 'https://nz.qq.com/cp/a20250623act/'
eas_refer: str = 'https://nz.qq.com/web202403/activity-list.shtml'
sSDID: str = '4b2d65e0c50b99e7134a548308de4f6a'
headers: dict = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE',
    'cookie': None,
    'referer': 'https://nz.qq.com/'}
# 定义每天执行的时间点（小时:分钟）
schedule_times: list = [
    '00:00'
]
