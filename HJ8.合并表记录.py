# @nc app=nowcoder id=de044e89123f4a7482bd2b214a685201 topic=37 question=21231 lang=Python3
# 2024-08-06 10:19:18
# https://www.nowcoder.com/practice/de044e89123f4a7482bd2b214a685201?tpId=37&tqId=21231
# [HJ8] 合并表记录

# @nc code=start

import sys

# 读取文件路径
try:
    input_file = sys.argv[1]
    f1 = open(input_file, "r")
except:
    f1 = None


def cin():
    if f1:
        return f1.readline().strip()
    else:
        return input()


n = cin()
dic = {}
for i in range(int(n)):
    s = cin().split()
    k = int(s[0])
    v = int(s[1])
    if dic.get(k):
        dic[k] += v
    else:
        dic[k] = v
dic = sorted(dic.items(), key=lambda item: item[0])
for i in dic:
    print(i[0], i[1], sep=" ")


# @nc code=end
