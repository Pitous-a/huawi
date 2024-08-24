# @nc app=nowcoder id=fe298c55694f4ed39e256170ff2c205f topic=37 question=21245 lang=Python3
# 2024-08-06 16:15:27
# https://www.nowcoder.com/practice/fe298c55694f4ed39e256170ff2c205f?tpId=37&tqId=21245
# [HJ22] 汽水瓶

# @nc code=start

import sys
def f(n):
    if n<2:
        return 0
    if n==2:
        return 1
    return n//3+f(n//3+n%3)
for line in sys.stdin:
    a = int(line.split()[0])
    if a == 0:
        break
    print(f(a))


# @nc code=end
