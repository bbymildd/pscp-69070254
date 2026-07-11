"""surprise"""
def main():
    """surprise"""
    total_score = float(input())
    top = float(input())
    left = total_score - top

    if top > 2 and (top*2 - left) > 2:
        print("Surprising")
    else:
        print("Not surprising")

main()
