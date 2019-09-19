def get_digit_sum(n):
    str_n = str(abs(n))
    n_sum = 0
    for digit in str_n:
        n_sum += int(digit)
    if n % n_sum == 0:
        return '**TRUE**'
    else:
        return '**FALSE**'


if __name__ == "__main__":
    print(get_digit_sum(10))
