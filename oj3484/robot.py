"""robot"""
def main():
    """robot"""
    size, money = input().split()
    size = int(size)
    money = float(money)

    tile = []
    for _ in range(size):
        row = list(map(int, input().split()))
        tile.append(row)

    total_t = 0
    total_p = 0

    for row in tile:
        bad_t = 0
        bad_p = 0

        for value in row:
            if value > 0:
                bad_t += 1
                total_t += 1

            bad_p += value
            total_p += value

        print(*row, bad_t, bad_p)

    col_t = [0] * size
    col_p = [0] * size

    for i in range(size):
        for j in range(size):
            if tile[i][j] > 0:
                col_t[j] += 1
            col_p[j] += tile[i][j]

    print(*col_t)
    print(*col_p)
    print(total_t, total_p, f"{total_p * money:.2f}")

main()
