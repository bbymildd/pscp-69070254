"""frog"""
def main():
    """frog"""
    first, goal = map(int, input().split())
    far = 0
    jump = 0
    while first >= 0:
        far += first
        first -= 2
        jump += 1
        if far >= goal:
            break
    if far >= goal:
        far = goal
        print(jump)
    else:
        print("-1")

main()
