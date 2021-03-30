
import sys


def main():
    a = int(sys.argv[1])

    result100 = a//100
    result10 = (a - 100*result100)//10
    result1 = (a - 100*result100 - 10*result10)//1

    print('100円玉'+str(result100)+'枚, 10円玉'+str(result10)+'枚, 1円玉'+str(result1)+'枚')


if __name__ == '__main__':
    main()