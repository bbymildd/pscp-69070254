"""schoolmart"""
from decimal import Decimal, ROUND_HALF_UP
def main():
    """schoolmart"""
    mem = input()
    order = int(input())
    total = Decimal("0")

    for _ in range(order):
        price = Decimal(input())
        total += price

    if mem == "Y":
        total *= Decimal("0.95")
    elif total >= Decimal("500"):
        total *= Decimal("0.97")

    total = total.quantize(Decimal("0.01"),rounding=ROUND_HALF_UP)

    print(total)

main()
