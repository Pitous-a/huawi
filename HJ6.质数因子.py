# @nc app=nowcoder id=196534628ca6490ebce2e336b47b3607 topic=37 question=21229 lang=Python3
# 2024-08-05 19:05:01
# https://www.nowcoder.com/practice/196534628ca6490ebce2e336b47b3607?tpId=37&tqId=21229
# [HJ6] 质数因子

# @nc code=start

import sys
import math


def f(n):
    n = int(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            print(i, end=" ")
            n = n // i
    if n >= 2:
        print(n)


# 读取文件路径
try:
    input_file = sys.argv[1]
    with open(input_file, "r") as f1:
        n = f1.readline().strip()
except:
    n = input()
f(n)

# @nc code=end
