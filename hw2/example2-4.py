def get_most_frequent(words, k):
    import collections
    return [w for w, k in (collections.Counter(words).most_common(k))]


if __name__ == "__main__":
    print(get_most_frequent([
        "hello", "world", "hello", "my", "dear", "world", "hello"
    ], 3))
