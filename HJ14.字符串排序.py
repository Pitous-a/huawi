# @nc app=nowcoder id=5af18ba2eb45443aa91a11e848aa6723 topic=37 question=21237 lang=Python3
# 2024-08-06 14:19:06
# https://www.nowcoder.com/practice/5af18ba2eb45443aa91a11e848aa6723?tpId=37&tqId=21237
# [HJ14] 字符串排序

# @nc code=start

import sys


num = int(input())
stack = []
for i in range(num):
    stack.append(input())
print("\n".join(sorted(stack)))


# @nc code=end
