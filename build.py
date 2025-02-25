# coding=UTF-8
# Author:Gentlesprite
# Software:PyCharm
# Time:2024/10/2 14:06
# File:build
# coding=UTF-8
# Author:Gentlesprite
# Software:PyCharm
# Time:2024/8/18 17:51
# File:build
import os
from main import NZSpiderFramework

app_name = 'NSF'
ico_path = 'doc/icon.ico'
output = 'output'
main = r'main.py'

file_version = NZSpiderFramework.VERSION
author = 'Gentlesprite'
copy_right = f'Copyright (C) 2024-2025 {author}.'

build_command = f'nuitka --standalone --onefile '
build_command += f'--output-dir={output} --file-version={file_version} '
build_command += f'--windows-icon-from-ico="{ico_path}" --assume-yes-for-downloads '
build_command += f'--output-filename="{app_name}_{file_version}.exe" --copyright="{copy_right}" --mingw64 '
build_command += f'--script-name={main}'
print(build_command)
# todo 获取当前版本并确认后才开始打包,以免系统环境变量非当前程序环境
os.system(build_command)
