# -*- coding: utf-8 -*-

errorLogs = [
  "Error 101:Invalid Exception AAA - 2020/01/01/01:00",
  "Error 3:Invalid Exception BBBB - 2020/01/01/02:00",
  "Error 22:Invalid Exception CCCCC - 2020/01/01/03:00"
]


def main():
    targets = ':'
    targetf = ' -'

    # error要素を1ずつ確認する
    for i in errorLogs:
        # 指定した文字のインデックスを取得する
        startidx = i.find(targets)
        finishidx = i.find(targetf)

        # スライスして出力
        result = i[startidx+1:finishidx]
        print(result)


if __name__ == '__main__':
    main()
