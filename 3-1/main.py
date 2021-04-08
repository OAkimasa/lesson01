import numpy as np


def main():
    a = np.arange(1, 10)

    result = []
    for i in range(1, 10):
        b = a*i
        result.append(b)

    print(*result, sep='\n')


if __name__ == '__main__':
    main()