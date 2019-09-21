def is_self_dividing(n):
    str_n = str(n)
    for digit in str_n:
        if n % int(digit) != 0:
            return False
    return True


if __name__ == '__main__':
    n = input("Enter number: ")
    print("This number is {}".format(is_self_dividing(int(n))))
