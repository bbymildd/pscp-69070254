"""flower"""
from math import ceil
def main():
    """flower"""
    size, flower = map(int, input().split())

    diagonal = 0
    total = 0

    while total < flower:
        diagonal += 1
        total += diagonal

    print(ceil(diagonal / size))

main()
