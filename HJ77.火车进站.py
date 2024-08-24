# @nc app=nowcoder id=97ba57c35e9f4749826dc3befaeae109 topic=37 question=21300 lang=Python3
# 2024-08-19 14:45:24
# https://www.nowcoder.com/practice/97ba57c35e9f4749826dc3befaeae109?tpId=37&tqId=21300
# [HJ77] 火车进站

# @nc code=start

import sys

r=[]

def dfs(res, stack, out):
    if not res and not stack:
        r.append(' '.join(list(map(str, out))))
    else:
        # 入站
        if res:
            dfs(res[1:], stack+[res[0]], out)
        # 出站
        if stack:
            dfs(res, stack[:-1], out+[stack[-1]])

n,nums=int(input()),list(map(int,input().split()))
dfs(nums,[],[])
print("\n".join(map(str, sorted(r))))


# @nc code=end
