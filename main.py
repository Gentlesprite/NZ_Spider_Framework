# coding=UTF-8
# Author:Gentlesprite
# Software:PyCharm
# Time:2024/10/2 13:06
# File:main
import os
import json
import time
import sched
import datetime
import requests
from loguru import logger
import threading
from config import *


class NZSpiderFramework:
    VERSION = '0.5'

    def __init__(self,
                 iActivityId: str,
                 sServiceDepartment: str,
                 iFlowId: str,
                 sMiloTag: str,
                 e_code: str,
                 g_code: str,
                 eas_url: str,
                 eas_refer: str,
                 s_SDID: str,
                 headers: dict,
                 schedule_times: list):
        logger.add('history.log', rotation='5 MB', encoding='utf-8', enqueue=True, retention='10 days')
        self.cookies: str or None = None
        self.iActivityId: str = iActivityId
        self.sServiceDepartment: str = sServiceDepartment
        self.iFlowId: str = iFlowId
        self.sMiloTag: str = sMiloTag
        self.e_code: str = e_code
        self.g_code: str = g_code
        self.eas_url: str = eas_url
        self.eas_refer: str = eas_refer
        self.s_SDID: str = s_SDID
        self.headers: dict = headers
        self.schedule_times: list = schedule_times
        self.get_cookie()

    def get_gift(self):
        data = {'sServiceType': 'nz',
                'iActivityId': self.iActivityId,
                'sServiceDepartment': self.sServiceDepartment,
                'iFlowId': self.iFlowId,
                'g_tk': '1842395457',
                'sMiloTag': self.sMiloTag,
                'e_code': self.e_code,
                'g_code': self.g_code,
                'eas_url': self.eas_url,
                'eas_refer': self.eas_refer}
        url = f'https://comm.ams.game.qq.com/ams/ame/amesvr?sServiceType=nz&iActivityId={iActivityId}&sServiceDepartment={sServiceDepartment}&sSDID={sSDID}'
        res = requests.post(url=url, data=data, headers=headers)
        res.encoding = res.apparent_encoding
        logger.info(json.loads(res.text))
        return json.loads(res.text)

    @staticmethod
    def to_hour_minute(seconds):
        remain_seconds = seconds % (24 * 3600)
        remain_hours = remain_seconds // 3600
        remain_seconds %= 3600
        remain_minutes = remain_seconds // 60
        return remain_hours, remain_minutes, remain_seconds

    def task(self):
        today = datetime.datetime.now().date()  # 获取当前的日期
        remain_do_time = []  # 获取所有距离下次任务的剩余时间的列表
        # 创建调度器对象
        scheduler = sched.scheduler(time.time, time.sleep)
        # 遍历每个时间点，将任务安排到调度器中
        for time_str in self.schedule_times:
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
        scheduler.enter(next_do_time, 1, self.run)
        logger.info(
            f"开始执行任务,当前时间:{datetime.datetime.now()} 距离下次执行任务还有%d:%02d:%02d" % (
                self.to_hour_minute(next_do_time)))
        scheduler.run()

    def run(self, max_threads: int = 10, first=False):
        threads = []
        if first:
            max_threads = 1
        for i in range(max_threads):
            thread = threading.Thread(target=self.get_gift)
            threads.append(thread)
        for thread in threads:
            thread.start()
        # 等待所有线程结束
        for thread in threads:
            thread.join()
        self.task()

    def get_cookie(self):
        cookie_file = 'cookie.txt'
        error_notice = '请先填写cookie.txt后重新运行程序!'
        # 确保文件存在，如果不存在则创建并提示用户
        if not os.path.exists(cookie_file):
            with open(cookie_file, 'w', encoding='utf-8') as f:
                f.write('')
            logger.warning(error_notice)
            return None

        # 读取 cookie 内容
        with open(cookie_file, 'r', encoding='utf-8') as f:
            cookie = f.read().strip()

        if cookie:
            if cookie.startswith("'"):
                cookie = cookie[1:]  # 去掉开头的'
            if cookie.endswith("'"):
                cookie = cookie[:-1]  # 去掉结尾的'
            self.cookies = cookie
        else:
            logger.warning(error_notice)
            self.cookies = None


if __name__ == "__main__":
    try:
        nsf = NZSpiderFramework(
            iActivityId=iActivityId,
            sServiceDepartment=sServiceDepartment,
            iFlowId=iFlowId,
            sMiloTag=sMiloTag,
            e_code=e_code,
            g_code=g_code,
            eas_url=eas_url,
            eas_refer=eas_refer,
            s_SDID=sSDID,
            headers=headers,
            schedule_times=schedule_times)

        if nsf.cookies:
            nsf.headers['cookie'] = nsf.cookies
            logger.info(f'版本:{NZSpiderFramework.VERSION},当前领取的最大并发数:{MAX_THREADS}。')
            nsf.run(max_threads=MAX_THREADS, first=True)
        else:
            os.system('pause')
            exit(0)
    except KeyboardInterrupt:
        logger.info('键盘中断。')
