"""schoolmart"""
from decimal import Decimal, ROUND_HALF_UP
def main():
    """schoolmart"""
    mem = input()
    order = int(input())
    total = 0
    for _ in range(order):
        price = float(input())
        total += price
    if mem == "Y":
        dis = total * 0.05
        pay = total - dis
        net = Decimal(str(pay)).quantize(Decimal("0.01"), rounding = ROUND_HALF_UP)
        print(net)
    elif mem == "N":
        if total >= 500:
            dis = total * 0.03
            pay = total - dis
            net = Decimal(str(pay)).quantize(Decimal("0.01"), rounding = ROUND_HALF_UP)
            print(net)
        else:
            net = Decimal(str(total)).quantize(Decimal("0.01"), rounding = ROUND_HALF_UP)
            print(net)
main()
