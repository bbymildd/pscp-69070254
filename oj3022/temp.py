"""temp"""
def main():
    """temp"""
    temp = float(input())
    font = input()
    want = input()

    if font == "C":
        c = temp
    elif font == "F":
        c = (temp - 32) * 5 / 9
    elif font == "K":
        c = temp - 273.15
    else:
        c = (temp * 5 / 9) - 273.15

    if want == "C":
        print(f"{c:.2f}")
    elif want == "F":
        print(f"{c * (9 / 5) + 32:.2f}")
    elif want == "K":
        print(f"{c + 273.15:.2f}")
    elif want == "R":
        print(f"{(c + 273.15) * 9 / 5:.2f}")

main()
