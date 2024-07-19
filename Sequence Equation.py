def permutation_equation(p):
    return [p.index(p.index(i) + 1) + 1 for i in range(1, len(p) + 1)]

if __name__ == "__main__":
    p = [5, 2, 1, 3, 4]
    print(permutation_equation(p))
