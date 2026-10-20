"""bfullypair"""
def main():
    """bfullypair"""
    data = input()
    count = {}

    for char in data:
        if char not in count:
            count[char] = 0
        count[char] += 1

    result = ""

    for char in data:
        if count[char] % 2 == 1:
            result += char
            count[char] = 0

    if result:
        print(result)
    else:
        print("fully paired")

main()
