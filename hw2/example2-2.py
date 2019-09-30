def get_sorted_squares(nums):
    nums = [i ** 2 for i in nums]
    nums.sort()
    return nums


if __name__ == "__main__":
    print(get_sorted_squares([-4, -1, 0, 3, 10]))  # =>  Output: [0, 1, 9, 16, 100]
    print(get_sorted_squares([-7, -3, 2, 3, 11]))  # =>  Output: [4, 9, 9, 49, 121]
