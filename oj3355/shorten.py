"""short"""
def main():
    """short"""
    num = int(input())
    num_all = []
    while num != -1:
        num_all.append(num)
        num = int(input())

    if not num_all:
        return

    num_all = sorted(num_all)

    result = []
    start = num_all[0]
    end = num_all[0]

    for i in range(1, len(num_all)):
        if num_all[i] == end + 1:
            end = num_all[i]
        else:
            if start == end:
                result.append(str(start))
            else:
                result.append(f"{start}-{end}")

            start = num_all[i]
            end = num_all[i]

    if start == end:
        result.append(str(start))
    else:
        result.append(f"{start}-{end}")

    print(", ".join(result))

main()
