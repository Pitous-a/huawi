# @nc app=nowcoder id=d9162298cb5a437aad722fccccaae8a7 topic=37 question=21227 lang=Python3
# 2024-08-05 17:15:44
# https://www.nowcoder.com/practice/d9162298cb5a437aad722fccccaae8a7?tpId=37&tqId=21227
# [HJ4] 字符串分隔

# @nc code=start

import sys


def split_str(input_str):
    n = len(input_str)
    if n <= 8:
        pad = 8 - n
        print(input_str + "0" * pad)
    else:
        print(input_str[0:8])
        split_str(input_str[8:])


# 读取文件路径
# global n
try:
    input_file = sys.argv[1]
    with open(input_file, "r") as f:
        n = f.readline().strip()
except:
    n = input()
split_str(n)


# @nc code=end
