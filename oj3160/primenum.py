"""prime"""
def main():
    """prime"""
    start, stop = map(int, input().split())
    nub = 0
    primes = []

    while start <= stop:
        if start > 1:
            prime = True
            divisor = 2

            while divisor < start:
                if not start % divisor:
                    prime = False
                    break
                divisor += 1

            if prime:
                primes.append(start)
                nub += 1

        start += 1

    if primes:
        print(*primes)

    print(f"Total primes: {nub}")

main()
