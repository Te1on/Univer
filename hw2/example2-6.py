def get_two_sum(nums, k):
    d = dict(enumerate(nums))
    for i in d.keys():
        if k - d[i] in d.values():
            return list(d.keys())[list(d.values()).index(k - d[i])], i
    return None


if __name__ == "__main__":
    print(get_two_sum([2, 7, 11, 15], 9))
