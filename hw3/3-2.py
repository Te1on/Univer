def divider_generator(number):
    for i in range(1, number):
        if number % i == 0:
            yield i


if __name__ == "__main__":
    dividers = divider_generator(1024)
    for i in dividers:
        print(i)
