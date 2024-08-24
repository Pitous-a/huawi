# @nc app=nowcoder id=d3d8e23870584782b3dd48f26cb39c8f topic=37 question=21253 lang=Python3
# 2024-08-06 17:14:49
# https://www.nowcoder.com/practice/d3d8e23870584782b3dd48f26cb39c8f?tpId=37&tqId=21253
# [HJ30] 字符串合并处理

# @nc code=start

import sys

import re

# 构造函数加密字符，如果是[0-9A-Fa-f]则按规则返回加密值，否则返回原始值
def encrypt(x):
    if re.search(r"[0-9A-Fa-f]", x):
        return hex(int(bin(int(x, 16))[2:].rjust(4, "0")[::-1], 2))[2:].upper()
    else:
        return x


while True:
    try:
        a = list(input().replace(" ", ""))  # 去除输入中的空格，并将输入的字符处理成列表
        a[::2] = sorted(a[::2])  # 奇数位置从小到大排序
        a[1::2] = sorted(a[1::2])  # 偶数位置从小到大排序
        res = ""
        for i in a:
            res += encrypt(i)  # 调用加密函数，遍历输出结果
        print(res)
    except:
        break


# @nc code=end
