"""season"""
def main():
    """season"""
    mon = int(input())
    day = int(input())
    if mon == 1 or mon == 2 or (mon == 3 and day < 21):
        print("winter")
    elif mon == 4 or mon == 5 or (mon == 6 and day < 21):
        print("spring")
    elif mon == 7 or mon == 8 or (mon == 9 and day < 21):
        print("summer")
    elif mon == 10 or mon == 11 or (mon == 12 and day < 21):
        print("fall")
    if not mon % 3 :
        if mon == 3 and day >= 21:
            print("spring")
        elif mon == 6 and day >= 21:
            print("summer")
        elif mon == 9 and day >= 21:
            print("fall")
        elif mon == 12 and day >= 21:
            print("winter")

main()
