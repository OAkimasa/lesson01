import sys


def main():
    a = int(sys.argv[1])
    if 2<=a<=4:
        result = '春'

    elif 5<=a<=7:
        result = '夏'

    elif 8<=a<=10:
        result = '秋'

    elif 11<=a<=12 or a==1:
        result = '冬'

    else:
        result = 'error'

    print(result)


if __name__ == '__main__':
    main()