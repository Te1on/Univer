def get_larger_perimeter(L):
    maxp = 0
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            for k in range(j + 1, len(L)):
                if (L[i] + L[j] > L[k]) & (L[i] + L[k] > L[j]) & (L[j] + L[k] > L[i]):
                    if maxp < L[i] + L[j] + L[k]:
                        maxp = L[i] + L[j] + L[k]
    return maxp


if __name__ == "__main__":
    import numpy as np
    np.random.seed(10)
    L = 10 * np.random.rand(5)
    print("maximum perimeter: {}".format(get_larger_perimeter(L)))
