def beautiful_days(i, j, k):
    return sum(1 for x in range(i, j + 1) if abs(x - int(str(x)[::-1])) % k == 0)

if __name__ == "__main__":
    i = 20
    j = 23
    k = 6
    print(beautiful_days(i, j, k))
