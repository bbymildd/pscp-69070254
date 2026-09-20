"""bigframe"""
def main():
    """bigframe"""
    data1 = input().rstrip()
    data2 = input().rstrip()
    data3 = input().rstrip()
    data4 = input().rstrip()
    data5 = input().rstrip()

    max_len = len(data1)

    if len(data2) > max_len:
        max_len = len(data2)
    if len(data3) > max_len:
        max_len = len(data3)
    if len(data4) > max_len:
        max_len = len(data4)
    if len(data5) > max_len:
        max_len = len(data5)

    print("*" * (max_len + 4))

    space = " " * (max_len - len(data1))
    print(f"* {data1}{space} *")

    space = " " * (max_len - len(data2))
    print(f"* {data2}{space} *")

    space = " " * (max_len - len(data3))
    print(f"* {data3}{space} *")

    space = " " * (max_len - len(data4))
    print(f"* {data4}{space} *")

    space = " " * (max_len - len(data5))
    print(f"* {data5}{space} *")

    print("*" * (max_len + 4))

main()
