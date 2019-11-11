def out_cycle(filename):
    while True:
        with open(filename, 'r') as f:
            for line in f:
                yield line.replace('\n', '')


def filtering(filename):
    gen_cycle = out_cycle(filename)
    while True:
        for line in gen_cycle:
            if "NOD19" in line:
                yield line


if __name__ == "__main__":
    gen_filter = filtering("text.txt")
    for i, l in enumerate(gen_filter):
        print(l)
        if i > 100:
            break

