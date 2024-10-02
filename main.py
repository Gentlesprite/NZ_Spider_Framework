# coding=UTF-8
# Author:Gentlesprite
# Software:PyCharm
# Time:2024/10/2 13:06
# File:3
import json
import time
import sched
import datetime
import requests
from loguru import logger
import threading
from config import *

logger.add('get_history.log', rotation='5 MB', encoding='utf-8', enqueue=True, retention='10 days')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE',
    'cookie': cookies,
    'referer': 'https://nz.qq.com/'}


def gift_info():
    return {'sServiceType': 'nz',
            'iActivityId': '664008',
            'sServiceDepartment': 'group_a',
            'iFlowId': iFlowId,
            'g_tk': '1842395457',
            'sMiloTag': sMiloTag,
            'e_code': '544119',
            'g_code': '0',
            'eas_url': 'https://nz.qq.com/cp/a20240822treasure/index.html?e_code=544119',
            'eas_refer': 'https://nz.qq.com/web202403/activity-list.shtml'}


def get_suipian():
    url = 'https://comm.ams.game.qq.com/ams/ame/amesvr?sServiceType=nz&iActivityId=664008&sServiceDepartment=group_a&sSDID=f3afc8c2a11102e84aea4e1d2cdc1b97'

    post_data = {'sServiceType': 'nz',
                 'iActivityId': '664008',
                 'sServiceDepartment': 'group_a',
                 'iFlowId': iFlowId,
                 'g_tk': '1842395457',
                 'sMiloTag': sMiloTag,
                 'e_code': '544119',
                 'g_code': '0',
                 'eas_url': 'https://nz.qq.com/cp/a20240822treasure/index.html?e_code=544119',
                 'eas_refer': 'https://nz.qq.com/web202403/activity-list.shtml'}
    res = requests.post(url=url, data=post_data, headers=headers)
    res.encoding = res.apparent_encoding
    logger.debug(json.loads(res.text))
    return json.loads(res.text)


def to_hour_minute(seconds):
    remain_seconds = seconds % (24 * 3600)
    remain_hours = remain_seconds // 3600
    remain_seconds %= 3600
    remain_minutes = remain_seconds // 60
    return remain_hours, remain_minutes, remain_seconds


def task():
    # 定义每天执行的时间点（小时:分钟）
    schedule_times = [
        '00:00',
        '01:00',
        '02:00',
        '03:00',
        '04:00',
        '05:00',
        '06:00',
        '07:00',
        '08:00',
        '09:00',
        '10:00',
        '11:00',
        '12:00',
        '13:00',
        '14:00',
        '15:00',
        '16:00',
        '17:00',
        '18:00',
        '19:00',
        '20:00',
        '21:00',
        '22:00',
        '23:00'
    ]
    today = datetime.datetime.now().date()  # 获取当前的日期
    remain_do_time = []  # 获取所有距离下次任务的剩余时间的列表
    # 创建调度器对象
    scheduler = sched.scheduler(time.time, time.sleep)
    # 遍历每个时间点，将任务安排到调度器中
    for time_str in schedule_times:
        # 将当前日期与时间点拼接成一个完整的日期时间对象
        scheduled_time = datetime.datetime.strptime(f"{today} {time_str}", "%Y-%m-%d %H:%M")
        # 如果时间点已经过去，则加一天
        if scheduled_time < datetime.datetime.now():
            scheduled_time += datetime.timedelta(days=1)
        # 计算距离现在的秒数
        delay = (scheduled_time - datetime.datetime.now()).total_seconds()
        remain_do_time.append(delay)
        # 向调度器中添加任务
    next_do_time = min(remain_do_time)
    scheduler.enter(next_do_time, 1, run)
    logger.info(
        f"开始执行任务,当前时间:{datetime.datetime.now()} 距离下次执行任务还有%d:%02d:%02d" % (
            to_hour_minute(next_do_time)))
    scheduler.run()


def get_label():
    while True:
        gift = input('1.稀世精华*1\n2.稀世精华*2\n请选择1或2:')
        if gift == '1':
            iFlowId = '1067127'
            sMiloTag = 'AMS-nz-1002123956-c2yeEw-664008-1067127'
            break
        elif gift == '2':
            iFlowId = '1069241'
            sMiloTag = 'AMS-nz-1002124015-Gwgamm-664008-1069241'
            break
        else:
            print('请输入1或2!')
    return iFlowId, sMiloTag


def run(max_threads=10):
    threads = []
    for i in range(max_threads):
        thread = threading.Thread(target=get_suipian)
        threads.append(thread)
    for thread in threads:
        thread.start()
    # 等待所有线程结束
    for thread in threads:
        thread.join()
    task()


if __name__ == "__main__":
    iFlowId, sMiloTag = get_label()
    run(max_threads=5)  # 最好不要大于5,小心被封ip
