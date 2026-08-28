"""lottery"""
def main():
    """lottery"""
    prize_font = input().split()
    buy_font = input().split()
    p = prize_font[0] + prize_font[1]
    b = buy_font[0] + buy_font[1]

    if p == b:
        print("1000000")
    elif p[0] != b[0] and p[1:6] == b[1:6]:
        print("100000")
    elif p[3:6] == b[3:6]:
        if p[0] == b[0]:
            print("2000")
        elif p[0] != b[0]:
            print("200")
    elif p[4:6] == b[4:6]:
        if p[0] == b[0]:
            print("1000")
        else:
            print("100")
    elif p[0] == b[0]:
        print("20")
    else:
        print("0")

main()
