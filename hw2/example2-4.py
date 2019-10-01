def get_most_frequent(words, k):
    a = set(words)
    b = [words.count(word) for word in a]
    d = sorted(zip(a, b), key=lambda x: x[1], reverse=True)
    d = [v for v, k in d]
    return d[:k]


if __name__ == "__main__":
    print(get_most_frequent([
        "hello", "world", "hello", "my", "dear", "world", "hello"
    ], 4))
