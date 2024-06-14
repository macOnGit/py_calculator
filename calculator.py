import sys


def main():
    try:
        _, first_num, second_num = sys.argv
        answer = int(first_num) * int(second_num)
        sys.stdout.write(str(answer))
    except Exception:
        pass


if __name__ == "__main__":
    main()
