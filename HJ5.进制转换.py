# @nc app=nowcoder id=8f3df50d2b9043208c5eed283d1d4da6 topic=37 question=21228 lang=Python3
# 2024-08-05 18:51:44
# https://www.nowcoder.com/practice/8f3df50d2b9043208c5eed283d1d4da6?tpId=37&tqId=21228
# [HJ5] 进制转换

# @nc code=start

import sys
def f(n):
    print(int(n,16))
# 读取文件路径
try:
    input_file = sys.argv[1]
    with open(input_file, "r") as f1:
        n = f1.readline().strip()
except:
    n = input()
f(n)
# @nc code=end
