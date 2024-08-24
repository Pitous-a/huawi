# @nc app=nowcoder id=f9a4c19050fc477e9e27eb75f3bfd49c topic=37 question=21264 lang=Python3
# 2024-08-10 14:17:10
# https://www.nowcoder.com/practice/f9a4c19050fc477e9e27eb75f3bfd49c?tpId=37&tqId=21264
# [HJ41] 称砝码

# @nc code=start

while True:
    try:
        n = int(input())
        m = list(map(int,input().split()))
        x = list(map(int,input().split()))
    except:
        break
    else:
        amount = []
        weights = {0,}
        for i in range(n):
            for j in range(x[i]):
                amount.append(m[i])
                 
        for i in amount:
            for j in list(weights):
                weights.add(i+j)
        print(len(weights))


# @nc code=end
