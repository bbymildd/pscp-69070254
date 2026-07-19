"""ink"""
import math as m
def main():
    """ink"""
    pi = 3.1416
    expand, people = input().split()
    expand = float(expand)
    people = int(people)

    count = 0
    while count < people:
        x, y = map(float, input().split())
        radius = m.sqrt(x ** 2 + y ** 2)
        area = pi * (radius ** 2)
        time = m.ceil(area / expand)
        print(time)
        count += 1
main()
