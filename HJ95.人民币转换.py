# @nc app=nowcoder id=00ffd656b9604d1998e966d555005a4b topic=37 question=21318 lang=Python3
# 2024-08-23 11:09:27
# https://www.nowcoder.com/practice/00ffd656b9604d1998e966d555005a4b?tpId=37&tqId=21318
# [HJ95] 人民币转换

# @nc code=start

import sys


def f(n: str):
    chinaNumDict = {
        "0": "零",
        "1": "壹",
        "2": "贰",
        "3": "叁",
        "4": "肆",
        "5": "伍",
        "6": "陆",
        "7": "柒",
        "8": "捌",
        "9": "玖",
    }
    pre = "人民币"
    n = n.split(".")
    cunit = ["万", "亿"]
    unit = ["", "拾", "佰", "仟"]
    mid = ""
    z = int(n[0])
    res = []
    while z:
        split_z = z % 10**4
        if split_z:
            s = str(split_z)
            t_r = ""
            for i in range(len(s)):
                t_r += (
                    ""
                    if (s[i] == "1" and len(s) - i - 1 == 1)
                    or (i == len(s) - 1 and s[i] == "0")
                    else s[i]
                ) + (unit[len(s) - i - 1] if s[i] != "0" else "")
            # print(t_r)
            res.append(t_r)
        else:
            res.append("0")
        z //= 10**4
    cunit_point = 0
    c_cunit = ""
    for i in range(len(res)):
        if not i:
            continue
        res[i] += cunit[cunit_point] + c_cunit + ("0" if i > 1 else "")
        new_cunit_point = (cunit_point + 1) % len(cunit)
        if cunit_point > new_cunit_point:
            c_cunit += cunit[cunit_point]
        cunit_point = new_cunit_point
    mid = "".join(res[::-1])
    suf = ""
    if int(n[1]) == 0:
        suf += "元整"
    else:
        suf += f"{'元' if int(n[0])>=1 else ''}{n[1][0]+'角' if int(n[1][0])>0 else ''}{n[1][1]+'分' if int(n[1][1])>0 else ''}"
    r = list(pre + mid + suf)
    for i, it in enumerate(r):
        if it in chinaNumDict.keys():
            r[i] = chinaNumDict[it]
    return "".join(r)


n = input()
print(f(n))


# @nc code=end
