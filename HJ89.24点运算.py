# @nc app=nowcoder id=7e124483271e4c979a82eb2956544f9d topic=37 question=21312 lang=Python3
# 2024-08-19 19:49:12
# https://www.nowcoder.com/practice/7e124483271e4c979a82eb2956544f9d?tpId=37&tqId=21312
# [HJ89] 24点运算

# @nc code=start

import sys

ls = input().split()

states = []
op = ["+", "-", "*", "//"]


def sort(al: list, res: list):
    if not res:
        states.append(al)
        return
    else:
        for i, it in enumerate(res):
            res.pop(i)
            sort(al + [it], res)
            res.insert(i, it)


def main():
    if "joker" in ls or "JOKER" in ls:
        return "ERROR"

    for i, it in enumerate(ls):
        if it == "J":
            ls[i] = "11"
        elif it == "Q":
            ls[i] = "12"
        elif it == "K":
            ls[i] = "13"
        elif it == "A":
            ls[i] = "1"
        else:
            # ls[i] = int(it)
            pass
    sort([], ls)
    for state in states:
        for op1 in op:
            for op2 in op:
                for op3 in op:
                    sentence = (
                        "("
                        + "("
                        + state[0]
                        + op1
                        + state[1]
                        + ")"
                        + op2
                        + state[2]
                        + ")"
                        + op3
                        + state[3]
                    )
                    # print(sentence)
                    # print(eval(sentence))
                    if eval(sentence) == 24:
                        # print(sentence)
                        return (
                            sentence.replace("//", "/")
                            .replace("11", "J")
                            .replace("12", "Q")
                            .replace("13", "K")
                            .replace("1", "A")
                            .replace("(", "")
                            .replace(")", "")
                        )


r = main()
if r:
    print(r)
else:
    print("NONE")
# @nc code=end
