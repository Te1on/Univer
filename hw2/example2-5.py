def is_valid(braces_string):
    if len(braces_string) % 2 != 0:
        return False
    queue = []
    for brace in braces_string:
        if brace == '(':
            queue.append(')')
        elif brace == ')':
            if not queue or brace != queue.pop():
                return False
    return not queue


if __name__ == "__main__":
    print(is_valid('()()(('))
