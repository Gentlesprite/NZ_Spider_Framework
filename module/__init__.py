# coding=UTF-8
# Author:Gentlesprite
# Software:PyCharm
# Time:2025/2/25 21:03
# File:__init__.py
from loguru import logger

AUTHOR: str = 'Gentlesprite'
APP_NAME: str = 'NSF'
__version__: str = '0.8'
__copyright__: str = f'Copyright (C) 2024-2025 {AUTHOR}.'
logger.add('history.log', rotation='5 MB', encoding='UTF-8', enqueue=True, retention='10 days')
logger.info(f'{__copyright__} Version:{__version__}')
