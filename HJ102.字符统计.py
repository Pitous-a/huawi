# @nc app=nowcoder id=c1f9561de1e240099bdb904765da9ad0 topic=37 question=21325 lang=Python3
# 2024-08-23 16:17:24
# https://www.nowcoder.com/practice/c1f9561de1e240099bdb904765da9ad0?tpId=37&tqId=21325
# [HJ102] 字符统计

# @nc code=start

import sys

n = input()
sn = set(n)
dic = {}
for i in sn:
    dic[i] = n.count(i)

# 使用sorted函数对字典进行排序，先按出现次数排序，再按ASCII码排序
sorted_dic = sorted(dic.items(), key=lambda x: (x[1], ord(x[0])))

# 将排序后的结果转换回字典
sorted_dic = dict(sorted_dic)

print(sorted_dic)
# @nc code=end
