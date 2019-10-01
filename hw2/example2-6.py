def get_two_sum(nums, k):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == k:
                return i, j
    return None


if __name__ == "__main__":
    print(get_two_sum([2, 7, 11, 15], 9))
