"""bread"""
def main():
    """bread"""
    width, height, _, _ = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    x.insert(0, 0)
    x.append(width)

    y.insert(0, 0)
    y.append(height)

    width_list = []
    height_list = []

    for i in range(len(x) - 1):
        width_list.append(x[i + 1] - x[i])

    for i in range(len(y) - 1):
        height_list.append(y[i + 1] - y[i])

    area = []

    for w in width_list:
        for h in height_list:
            area.append(w * h)

    area.sort(reverse = True)

    print(area[0], area[1])

main()
