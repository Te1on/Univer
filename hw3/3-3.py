def out_cycle(filename):
    while True:
        with open(filename, 'r') as f:
            for line in f:
                yield line.replace('\n', '')


if __name__ == "__main__":
    lines = out_cycle("text.txt")
    for i, line in enumerate(lines):
        print(line)
        if i > 100:
            break
