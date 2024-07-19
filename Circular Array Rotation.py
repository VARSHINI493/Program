def circular_array_rotation(a, k, queries):
    n = len(a)
    k = k % n
    rotated = a[-k:] + a[:-k]
    return [rotated[q] for q in queries]

if __name__ == "__main__":
    a = [3, 4, 5]
    k = 2
    queries = [1, 2]
    print(circular_array_rotation(a, k, queries))
