def save_the_prisoner(n, m, s):
    return (s - 1 + m - 1) % n + 1

if __name__ == "__main__":
    n = 5
    m = 2
    s = 1
    print(save_the_prisoner(n, m, s))
