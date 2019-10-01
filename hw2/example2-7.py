def get_three_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == target:
                    return i, j, k
    return None


if __name__ == "__main__":
    print(get_three_sum([2, 7, 11, 15], 24))
