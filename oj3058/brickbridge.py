"""brick"""
def main():
    """bridge"""
    konlek = int(input())
    konyai = int(input())
    goal = int(input())

    useyai = goal // 5
    if useyai > konyai:
        useyai = konyai

    wantlek = goal - (useyai * 5)

    if wantlek <= konlek:
        print(wantlek)
    else:
        print("-1")

main()
