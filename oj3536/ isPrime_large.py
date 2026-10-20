"""prime"""
def main():
    """prime"""
    num = int(input())

    if num < 2:
        print("NO")
        return

    i = 2
    while i * i <= num:
        if not num % i:
            print("NO")
            return
        i += 1

    print("YES")

main()
