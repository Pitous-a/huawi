# @nc app=nowcoder id=4b1658fd8ffb4217bc3b7e85a38cfaf2 topic=37 question=21309 lang=Python3
# 2024-08-19 19:29:04
# https://www.nowcoder.com/practice/4b1658fd8ffb4217bc3b7e85a38cfaf2?tpId=37&tqId=21309
# [HJ86] 求最大连续bit数

# @nc code=start

import sys

while True:
    try:
        a = bin(int(input()))
        b = str(a)
        for i in range(len(a)):
            if "1" * (len(a) - i) in b:
                print(len(a) - i)
                break
    except:
        break


# @nc code=end
