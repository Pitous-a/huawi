# @nc app=nowcoder id=3ab09737afb645cc82c35d56a5ce802a topic=37 question=21230 lang=Python3
# 2024-08-05 19:57:46
# https://www.nowcoder.com/practice/3ab09737afb645cc82c35d56a5ce802a?tpId=37&tqId=21230
# [HJ7] 取近似值

# @nc code=start

import sys


def f(n):
    print(round(float(n)))


# 读取文件路径
try:
    input_file = sys.argv[1]
    with open(input_file, "r") as f1:
        n = f1.readline().strip()
except:
    n = input()
f(n)


# @nc code=end
