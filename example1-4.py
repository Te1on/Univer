def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    n = input("Enter number: ")
    print("Answer: {}".format(is_prime(int(n))))
