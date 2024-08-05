# @nc app=nowcoder id=3245215fffb84b7b81285493eae92ff0 topic=37 question=21226 lang=Python3
# 2024-08-02 16:30:09
# https://www.nowcoder.com/practice/3245215fffb84b7b81285493eae92ff0?tpId=37&tqId=21226
# [HJ3] 明明的随机数

# @nc code=start

import sys

# 读取文件路径
try:
    input_file = sys.argv[1]
    with open(input_file, "r") as f:
        n = f.readline().strip()
        nums = []
        for i in range(int(n)):
            nums.append(int(f.readline().strip()))
        nums = sorted(list(set(nums)))
        for num in nums:
            print(num)
except:
    n = input()
    nums = []
    for i in range(int(n)):
        nums.append(int(input()))
    nums = sorted(list(set(nums)))
    for num in nums:
            print(num)
# @nc code=end
