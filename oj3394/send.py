"""send"""
def main():
    """send"""
    send, first = map(int, input().split())
    send_to = []

    for _ in range(send):
        num = int(input())
        send_to.append(num)

    student = []
    count = 0
    current = first

    while current != 0 and current not in student:
        student.append(current)
        count += 1

        current = send_to[current - 1]

    print(count)

main()
