import sys
import numpy as np


def reverse_a_number(arg):
    num = []
    for i in arg:
        # １文字ずつ配列に格納
        num.append(i)
        # 配列を反転
        renum = num[::-1]
    # 配列の形を崩す
    result = ''.join(renum)
    # 数値へ変換
    result = int(result)
    return(result)


def main():
    # 入力は文字列扱い
    a = sys.argv[1]
    b = sys.argv[2]

    results = reverse_a_number(a) + reverse_a_number(b)
    print(results)


if __name__ == '__main__':
    main()