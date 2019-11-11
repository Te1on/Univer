def out_cycle(filename):
    while True:
        with open(filename, 'r') as f:
            for line in f:
                yield line.replace('\n', '')


def get_len(filename):
    gen_cycle = out_cycle(filename)
    while True:
        for i in gen_cycle:
            yield len(i)


if __name__ == "__main__":
    gen_len = get_len("text.txt")
    for i, l in enumerate(gen_len):
        print(l)
        if i > 100:
            break

