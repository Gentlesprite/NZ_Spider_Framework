# coding=UTF-8
# Author:Gentlesprite
# Software:PyCharm
# Time:2024/10/2 14:06
# File:build
# coding=UTF-8
# Author:Gentlesprite
# Software:PyCharm
# Time:2024/8/18 17:51
# File:build.py
import os
from module import __version__, __copyright__, APP_NAME

ico_path = 'doc/icon.ico'
output = 'output'
main = 'main.py'

build_command = f'nuitka --standalone --onefile '
build_command += f'--output-dir={output} --file-version={__version__} --product-version={__version__} '
build_command += f'--windows-icon-from-ico="{ico_path}" --assume-yes-for-downloads '
build_command += f'--output-filename="{APP_NAME}_{__version__}.exe" --copyright="{__copyright__}" --mingw64 '
build_command += f'--remove-output '
build_command += f'--script-name={main}'
if __name__ == '__main__':
    try:
        print(build_command)
        os.system(build_command)
    except ImportError:
        print('请先使用命令:"pip install nuitka==2.4.8"安装Nuitka后重试。')
    except KeyboardInterrupt:
        print('键盘中断。')
