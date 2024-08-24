# @nc app=nowcoder id=6abde6ffcc354ea1a8333836bd6876b8 topic=37 question=21320 lang=Python3
# 2024-08-23 15:35:25
# https://www.nowcoder.com/practice/6abde6ffcc354ea1a8333836bd6876b8?tpId=37&tqId=21320
# [HJ97] 记负均正

# @nc code=start

import sys

n, nums = input(), list(map(int, input().split()))
s = 0
num = 0
f_num = 0
for i in nums:
    if i < 0:
        f_num += 1
    elif i != 0:
        s += i
        num += 1
if num == 0:
    num = 1
print(f_num, f"{s/num:.1f}")

# @nc code=end
