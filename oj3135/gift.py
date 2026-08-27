"""gift_theft"""
def main():
    """gift_theft"""
    allmem, passed, theft = map(int, input().split())

    if theft == 1:
        print(1)
        return

    current = 1
    count = 1

    while True:
        current = (current + passed - 1) % allmem + 1
        if current == 1:
            break
        count += 1
        if current == theft:
            break

    print(count)

main()
