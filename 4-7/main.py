# -*- coding: utf-8 -*-
import sys


def main():
    args = sys.argv[1]
    targetch = sys.argv[2]
    print(args)

    names = []
    base = []
    targetcount = 0
    # 一文字ずつ判別する
    for i in args:
        # 名前ごとに一つの要素にまとめる
        if i != ',':
            base.append(i)
            name = ''.join(base)
            name = str.lower(name)
            if i == str.upper(targetch) or i == str.lower(targetch):
                targetcount = targetcount + 1
        # カンマが来たら要素を追加
        elif i == ',' and 1 <= targetcount:
            names.append(name)
            base = []
            targetcount = 0
        elif i == ',' and 0 == targetcount:
            base = []
    if 1 <= targetcount:
        names.append(name)  # 最後のnameも忘れずに追加

    sortednames = sorted(names)
    print(sortednames)


if __name__ == '__main__':
    main()
