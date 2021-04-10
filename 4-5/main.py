import sys


def main():
    args = sys.argv[1:]
    print(*args)
    result = []

    # 引数に与えられたリストの、最小値とそれ以外のリストを返す関数
    def searchmin(array):
        # リストの先頭が最小値だと仮定する
        argmin = int(array[0])
        # 最小値以外のリスト
        pool = []
        # 同じ入力が２回以上ある場合に、このカウントを使う
        count = 0

        # ２回目以降のargsはコマンドライン引数ではないことに注意
        for i in args:
            i = int(i)
            if i <= argmin:
                if i < argmin:
                    pool.append(argmin)
                    argmin = i

                elif i == argmin:
                    count = count+1
                    argmin = i
                    # 最小値は、２回目以降に限って追加する
                    if 2 <= count:
                        pool.append(argmin)

            # 最小値以外はpoolへ追加
            elif argmin < i:
                pool.append(i)

        return argmin, pool

    # 初回のみargsはコマンドライン引数。最小値をresultに加えていく
    for i in args:
        argmin = searchmin(args)[0]

        # ２回目以降のargsは自作関数によって与えられる pool
        args = searchmin(args)[1]

        result.append(argmin)

    print(*result)


if __name__ == '__main__':
    main()
