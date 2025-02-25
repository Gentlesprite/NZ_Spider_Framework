# coding=UTF-8
# Author:Gentlesprite
# Software:PyCharm
# Time:2024/10/2 13:06
# File:main.py
from module import logger, __version__
from module.config import *
from module.spider import NZSpiderFramework

if __name__ == '__main__':
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
        cookies: str = nsf.cookies
        if cookies:
            nsf.headers['cookie'] = cookies
            logger.info(f'当前领取的最大并发数:{MAX_THREADS}。')
            nsf.run(max_threads=MAX_THREADS, first=True)
        else:
            exit(0)
    except KeyboardInterrupt:
        logger.info('键盘中断。')
    finally:
        input('按Enter键退出. . .')
