"""arcade"""


def main():
    """arcade"""
    store, check = map(int, input().split())

    diff = [0] * 1442
    for _ in range(store):
        start, stop = map(int, input().split())
        diff[start] += 1
        diff[stop] -= 1

    opened = [0] * 1441
    current = 0
    for minute in range(1441):
        current += diff[minute]
        opened[minute] = current

    times = list(map(int, input().split()))

    result = []
    for i in range(check):
        result.append(opened[times[i]])

    print(*result)


main()
