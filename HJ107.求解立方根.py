# @nc app=nowcoder id=caf35ae421194a1090c22fe223357dca topic=37 question=21330 lang=Python3
# 2024-08-24 13:45:27
# https://www.nowcoder.com/practice/caf35ae421194a1090c22fe223357dca?tpId=37&tqId=21330
# [HJ107] 求解立方根

# @nc code=start

import sys

n = float(input())
flag = "-" if n < 0 else ""
s = abs(n) ** (1 / 3)
print(f"{flag}{s:.1f}")


# @nc code=end
