"""devide"""
def main():
    """devide"""
    num1 = int(input())
    num2 = int(input())
    dee = int(input())
    remain = int(input())

    count = 0

    while num2 >= num1:
        if num2 % dee == remain:
            count += 1
        num2 -= 1

    print(count)

main()
