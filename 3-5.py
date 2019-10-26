def out_cycle(filename, n=1):
    for i in range(n):
        with open(filename, 'r') as f:
            for line in f:
                yield line.replace('\n', '')


def filtering(filename):
    lines = out_cycle(filename)
    a = list(filter(lambda x: "NOD19" in x, lines))
    for i in a:
        yield i


if __name__ == "__main__":
    c = filtering("text.txt")
    for i in c:
        print(i)
