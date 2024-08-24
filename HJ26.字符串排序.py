# @nc app=nowcoder id=5190a1db6f4f4ddb92fd9c365c944584 topic=37 question=21249 lang=Python3
# 2024-08-06 16:48:46
# https://www.nowcoder.com/practice/5190a1db6f4f4ddb92fd9c365c944584?tpId=37&tqId=21249
# [HJ26] 字符串排序

# @nc code=start

import sys


def sort_f(c: str):
    return c.lower()


s = list(input())
letters = sorted([c for c in s if c.isalpha()], key=sort_f)
result = []
letter_index = 0

for c in s:
    if c.isalpha():
        result.append(letters[letter_index])
        letter_index += 1
    else:
        result.append(c)

print("".join(result))


# @nc code=end
