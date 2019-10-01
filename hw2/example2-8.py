def get_partition(S):
    import collections
    parts = []
    while S:
        letters = list(collections.Counter(S).keys())
        a = S.find(letters[0])
        b = S.rfind(letters[0])
        seq_len = 0
        check = False
        while not check:
            sublet = set(S[a: b + 1])
            for letter in sublet:
                start_index = S.find(letter)
                end_index = S.rfind(letter)
                if start_index < a:
                    a = start_index
                elif end_index > b:
                    b = end_index
            if seq_len == b - a:
                check = True
            else:
                seq_len = b - a
        parts.append(S[a: b + 1])
        if a != 0 and b != len(S):
            S = S[:a] + S[b:]
        elif a == 0:
            S = S[b + 1:]
    return parts


if __name__ == "__main__":
    print(get_partition("qbqbcbqcqdufugduhxjhk)lxj"))
