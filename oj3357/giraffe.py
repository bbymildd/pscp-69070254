"""giraffe"""
def main():
    """giraffe"""
    num_g = int(input())

    tall_g = 0
    g_list = []

    for _ in range(num_g):
        tall = int(input())
        g_list.append(tall)

    if num_g == 1:
        print(1)
        return

    for i in range(num_g):
        if not i:
            if g_list[i] > g_list[i + 1]:
                tall_g += 1

        elif i == num_g - 1:
            if g_list[i] > g_list[i - 1]:
                tall_g += 1

        else:
            if g_list[i - 1] < g_list[i] > g_list[i + 1]:
                tall_g += 1

    print(tall_g)

main()
