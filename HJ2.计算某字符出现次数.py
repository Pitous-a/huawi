# @nc app=nowcoder id=a35ce98431874e3a820dbe4b2d0508b1 topic=37 question=21225 lang=Python3
# 2024-08-02 14:06:57
# https://www.nowcoder.com/practice/a35ce98431874e3a820dbe4b2d0508b1?tpId=37&tqId=21225
# [HJ2] 计算某字符出现次数

# @nc code=start

import sys

# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))

s = input()
char = input().lower()
count = 0
for c in s:
    if c.lower() == char:
        count += 1
print(count)
# @nc code=end
