def lru(function):
    cache = {}

    def wrapper(*args, **kwargs):
        check = True
        for k in kwargs.keys():
            if k in cache:
                print("Found in cache", k, cache[k])
            else:
                check = False
        if check:
            return cache[kwargs.keys()]
        value = function(*args, **kwargs)
        for k, v in value.items():
            cache[k] = v
            print("Added in cache", k, cache[k])
        return value
    return wrapper


@lru
def some_function(*args, **kwargs):
    for k, v in kwargs.items():
        kwargs[k] = v * sum(args[0])
    return kwargs


d = {'x': 1, 'y': 2, 'z': 3}
a = [1, 2, 3, 4]
print(some_function(a, **d))
