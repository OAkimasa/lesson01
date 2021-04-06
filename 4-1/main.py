import sys
import numpy as np


def main():
    args = sys.argv

    # args[0]は 'main.py' なので除く(ここまでstr)
    del args[0]

    args = [float(i) for i in args]
    result = np.median(args)

    print(result)


if __name__ == '__main__':
    main()