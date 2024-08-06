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
