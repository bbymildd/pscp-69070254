"""bill"""
def main():
    """bill"""
    eat = int(input())

    if eat <= 500:
        ser = eat + 50
        vat = ser * 0.07
        pay = vat + ser
        print(f"{pay:.2f}")
    elif 10000 > eat > 500:
        ser = (eat * 0.1) + eat
        vat = ser * 0.07
        pay = vat + ser
        print(f"{pay:.2f}")
    elif eat >= 10000:
        ser = eat + 1000
        vat = ser * 0.07
        pay = vat + ser
        print(f"{pay:.2f}")

main()
