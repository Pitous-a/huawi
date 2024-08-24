# @nc app=nowcoder id=88ddd31618f04514ae3a689e83f3ab8e topic=37 question=21322 lang=Python3
# 2024-08-23 15:46:47
# https://www.nowcoder.com/practice/88ddd31618f04514ae3a689e83f3ab8e?tpId=37&tqId=21322
# [HJ99] 自守数

# @nc code=start

import sys


def iszishou(m: int):
    return str(m**2)[-len(str(m)) :] == str(m)


n = int(input())
s = 0
for i in range(n + 1):
    if iszishou(i):
        s += 1
print(s)


# @nc code=end
