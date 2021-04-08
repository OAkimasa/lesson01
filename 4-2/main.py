import numpy as np


# 1回ごとに条件を確認しながら配列に追加していく
def main():
    nums = np.arange(1,51)
    nums3 = np.where(nums%3 == 0, 'WOW', nums)  # 3の倍数を WOW
    result = [np.where('3' in str(nums3[i]), 'WOW', nums3[i]
        ) for i in nums-1]  # さらに、strに変換した後に3を含むものを WOW
    print(*result, sep='\n')

    '''
    # jsと同じようにも書ける
    result = []
    append = result.append
    for i in range(1,51):
        stri = str(i)
        if '3' in stri or i%3 == 0:
            append('WOW')
        else:
            append(stri)
    print(*result, sep='\n')
    '''


if __name__ == '__main__':
    main()