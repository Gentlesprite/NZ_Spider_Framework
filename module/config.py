# coding=UTF-8
# Author:Gentlesprite
# Software:PyCharm
# Time:2025/2/25 17:55
# File:config.py
# 全新形态蛇载具活动配置文件,活动地址如下(已经配置好请求数据,直接在cookie.txt填入cookie内容即可使用):
# https://nz.qq.com/cp/a20250211kxjzj/?e_code=546570
MAX_THREADS: int = 10  # 并发请求数。
iActivityId: str = '700831'
sServiceDepartment: str = 'group_a'
iFlowId: str = '1106851'
sMiloTag: str = 'AMS-nz-0225175223-IXlkTs-700831-1106851'
e_code: str = '546570'
g_code: str = '0'
eas_url: str = 'https://nz.qq.com/cp/a20250211kxjzj/?e_code=546570'
eas_refer: str = 'https://nz.qq.com/web202403/activity-list.shtml'
sSDID: str = '4b2d0f92c26fdd71eeb0cee4be54b813'
headers: dict = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE',
    'cookie': None,
    'referer': 'https://nz.qq.com/'}
# 定义每天执行的时间点（小时:分钟）
schedule_times: list = [
    '10:00'
]
