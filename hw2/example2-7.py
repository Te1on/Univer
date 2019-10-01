def get_three_sum(nums, target):
    d = dict(enumerate(nums))
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if target - (nums[i] + nums[j]) in d.values():
                return list(d.keys())[list(d.values()).index(target - (nums[i] + nums[j]))], i, j
    return None


if __name__ == "__main__":
    print(get_three_sum([2, 7, 11, 15], 24))
