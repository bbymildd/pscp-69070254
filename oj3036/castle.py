"""castle"""
def main():
    """castle"""
    room = int(input())
    floor = 1
    while floor ** 2 < room:
        floor += 1
    first = (floor - 1) ** 2 + 1
    position = room - first + 1
    passed = (floor - 1) * 2
    if not position % 2:
        passed -= 1

    print(passed)

main()
