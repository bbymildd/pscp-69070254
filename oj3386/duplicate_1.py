"""duplicate"""
def main():
    """duplicate"""
    num1 = int(input())
    num2 = int(input())
    group1 = []
    for _ in range(num1):
        student1 = int(input())
        group1.append(student1)

    group2 = []
    for _ in range(num2):
        student2 = int(input())
        group2.append(student2)

    duplicate = []
    for stu2 in group2:
        if stu2 in group1:
            duplicate.append(stu2)

    if duplicate:
        duplicate.sort(reverse=True)
        for student in duplicate:
            print(student)
    else:
        print("Nope")

main()
