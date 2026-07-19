"""devide"""
def main():
    """devide"""
    num1 = int(input())
    num1 = (num1 // 10) * 10
    num = []
    while num1 >= 0:
        num.append(num1)
        num1 -= 10

    print(*num)
main()
