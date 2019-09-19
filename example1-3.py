def is_power_of_two(n):
    while n != 2:
        if n % 2 == 0:
            n = n / 2
        else:
            return "Nope"
    return "Yes"


if __name__ == "__main__":
    n = input("Input number: ")
    print('Answer: {}'.format(is_power_of_two(int(n))))
