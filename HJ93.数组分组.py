# @nc app=nowcoder id=9af744a3517440508dbeb297020aca86 topic=37 question=21316 lang=Python3
# 2024-08-20 15:57:46
# https://www.nowcoder.com/practice/9af744a3517440508dbeb297020aca86?tpId=37&tqId=21316
# [HJ93] 数组分组

# @nc code=start

import sys

n, numsall = input(), list(map(int, input().split()))

a5 = [i for i in numsall if i % 5 == 0]
b3 = [i for i in numsall if i % 3 == 0 and i % 5 != 0]
nums = [i for i in numsall if i % 5 != 0 and i % 3 != 0]

def dfs(nums, a5, b3):
    if not nums:
        if sum(a5) == sum(b3):
            return True
        else:
            return False
    else:
        num = nums[0]
        if dfs(nums[1:], a5 + [num], b3):
            return True
        if dfs(nums[1:], a5, b3 + [num]):
            return True
        return False
if dfs(nums, a5, b3):
    print("true")
else:
    print("false")

# @nc code=end
