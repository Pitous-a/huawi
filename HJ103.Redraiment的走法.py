# @nc app=nowcoder id=24e6243b9f0446b081b1d6d32f2aa3aa topic=37 question=21326 lang=Python3
# 2024-08-24 10:03:19
# https://www.nowcoder.com/practice/24e6243b9f0446b081b1d6d32f2aa3aa?tpId=37&tqId=21326
# [HJ103] Redraiment的走法

# @nc code=start

import sys

n, nums = int(input()), list(map(int, input().split()))
dp = [1 for i in range(n)]
for i in range(1, n):
    maxnum = -1
    maxj = -1
    for j in range(0, i):
        if nums[i] > nums[j] and dp[j] > maxnum:
            maxnum = dp[j]
            maxj = j
    if maxj >= 0:
        dp[i] += dp[maxj]

print(max(dp))
# @nc code=end
