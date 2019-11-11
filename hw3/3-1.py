def lru_cache(function):
    cache_dict = {}

    def wrapper(*args, **kwargs):
        args_key = args
        kwargs_key = ('kwargs',)
        kwargs_key = kwargs_key + tuple(kwargs.items())
        key = args_key + kwargs_key

        if key in cache_dict:
            print("Found in cache")
            return cache_dict.get(key)

        result = function(*args, **kwargs)
        cache_dict[key] = result
        print("Added in cache")
        return result

    return wrapper


@lru_cache
def sum_two_numbers(a, b, c=3):
    return a + b


if __name__ == "__main__":
    sum_two_numbers(1, 2, c=3)
    sum_two_numbers(1, 2, c=3)
