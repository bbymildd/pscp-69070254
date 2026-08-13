"""game"""
def main():
    """game"""
    n = int(input())
    nub = 0
    for _ in range(n):
        sym = input()
        if sym == "+":
            nub += 10
        elif sym == "-":
            nub -=5
    print(nub)
main()
