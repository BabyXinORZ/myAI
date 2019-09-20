# !/usr/bin/env python3
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
sys.path.append(BASE_DIR)

import sys
from code_check import CodeCheck
def main():
    code_checker = CodeCheck("code.py", 15)
    if not code_checker.check_code():
        print(code_checker.errormsg)
    else:
        print('pass')


if __name__ == '__main__':
    main()


