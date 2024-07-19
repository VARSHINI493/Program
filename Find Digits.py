def find_digits(n):
    return sum(1 for d in str(n) if int(d) != 0 and n % int(d) == 0)

if __name__ == "__main__":
    n = 1012
    print(find_digits(n))
