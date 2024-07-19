def jumping_on_clouds_revisited(c, k):
    n = len(c)
    energy = 100
    i = 0
    while True:
        i = (i + k) % n
        energy -= 1
        if c[i] == 1:
            energy -= 2
        if i == 0:
            break
    return energy

if __name__ == "__main__":
    c = [0, 0, 1, 0, 0, 1, 1, 0]
    k = 2
    print(jumping_on_clouds_revisited(c, k))
