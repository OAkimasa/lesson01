import sys


def main():
    a = int(sys.argv[1])
    check = a//24

    result = a - 24*check
    print(result)


if __name__ == '__main__':
    main()