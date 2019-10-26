def out_cycle(filename, n=3):
    for i in range(n):
        with open(filename, 'r') as f:
            for line in f:
                yield line.replace('\n', '')


if __name__ == "__main__":
    lines = out_cycle("text.txt")
    for line in lines:
        print(line)
