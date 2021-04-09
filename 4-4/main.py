# -*- coding: utf-8 -*-
import numpy as np
import random


def main():
    '''
    x = np.random.permutation(10)
    print(x)
    '''
    '''
    # 自作してみる
    N = 10  # 要素数
    arrnum = np.arange(N)
    randomNums = random.sample(arrnum, N)
    print(randomNums)
    '''
    # パターン2
    N = 10  # 要素数
    arrnum = np.arange(N)
    for i in arrnum:
        # ランダムにarrnumのインデックスを取得
        targetidx = random.choice(arrnum)
        # 一度削除する要素
        deletenum = arrnum[targetidx]

        # 削除して後ろに追加する
        arrnum = np.delete(arrnum, targetidx)
        arrnum = np.append(arrnum, deletenum)
        #print(arrnum)
    print(arrnum)


if __name__ == '__main__':
    main()
