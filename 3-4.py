def out_cycle(filename, n=1):
    for i in range(n):
        with open(filename, 'r') as f:
            for line in f:
                yield line.replace('\n', '')


def get_len(filename):
    lines = out_cycle(filename)
    l = list(map(len, lines))
    for i in l:
        yield i


if __name__ == "__main__":
    lengths = get_len("text.txt")
    for l in lengths:
        print(l)
