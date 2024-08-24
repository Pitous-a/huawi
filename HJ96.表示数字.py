# @nc app=nowcoder id=637062df51674de8ba464e792d1a0ac6 topic=37 question=21319 lang=Python3
# 2024-08-23 15:12:27
# https://www.nowcoder.com/practice/637062df51674de8ba464e792d1a0ac6?tpId=37&tqId=21319
# [HJ96] 表示数字

# @nc code=start

import sys

s = input()
r = ""
i = 0
while i < len(s):
    if not s[i].isdigit():
        r += s[i]
        i += 1
    else:
        r += "*"
        j = i + 1
        while j < len(s) and s[j].isdigit():
            j += 1
        r += s[i:j]
        r += "*"
        i = j
print(r)
# @nc code=end
