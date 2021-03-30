import sys


def main():
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    result = (a/b)*100

    print(str(result)+'%')


if __name__ == '__main__':
    main()
