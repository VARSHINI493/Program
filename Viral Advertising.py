def viral_advertising(n):
    shared = 5
    cumulative_likes = 0
    for _ in range(n):
        likes = shared // 2
        cumulative_likes += likes
        shared = likes * 3
    return cumulative_likes

if __name__ == "__main__":
    n = 3
    print(viral_advertising(n))
