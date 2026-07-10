"""temp"""
def main():
    """temp"""
    tem = float(input())
    font = input()
    want = input()

    cel = ""
    kel = cel + 273.15
    far = ((cel * 9)/ 5) + 32
    ran = (cel + 273.15) * (9/5)

    if font == "C":
        tem = float(cel)
        if want == "F" or want == "K" or want == "R":
            print(f"{cel:.2f}")
    elif font == "F":
        tem = float(far)
        if want == "C" or want == "K" or want == "R":
            print(f"{cel:.2f}")
    elif font == "K":
        tem = float(kel)
        if want == "F" or want == "C" or want == "R":
            print(f"{cel:.2f}")
    elif font == "R":
        tem = float(ran)
        if want == "F" or want == "K" or want == "C":
            print(f"{cel:.2f}")

main()
