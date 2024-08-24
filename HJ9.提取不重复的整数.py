# @nc app=nowcoder id=253986e66d114d378ae8de2e6c4577c1 topic=37 question=21232 lang=Python3
# 2024-08-06 10:54:52
# https://www.nowcoder.com/practice/253986e66d114d378ae8de2e6c4577c1?tpId=37&tqId=21232
# [HJ9] 提取不重复的整数

# @nc code=start

import sys

a = input()
a = a[::-1]
num = []
for i in a:
    if i in num:
        continue
    else:
        num.append(i)
        print(i, end="")


# @nc code=end
