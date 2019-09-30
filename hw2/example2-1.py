def number_of_matches(J, S):
    return len([1 for a in S if a in J])


if __name__ == "__main__":
    print(number_of_matches('aA', 'aAAbbbb'))  # => 3
    print(number_of_matches('z', 'ZZ'))  # => 0
