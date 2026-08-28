"""card"""
def main():
    """card"""
    card = input().upper()
    front = {"A" : "ace", "J" : "jack","Q" : "queen", "K" : "king"}
    back = {"D" : "diamonds", "H" : "hearts", "S" : "spades", "C" : "clubs"}

    if card[0] == "1":
        print(f"10 of {back[card[-1]]}")
    elif card[0].isalpha():
        print(f"{front[card[0]]} of {back[card[-1]]}")
    else:
        print(f"{card[0]} of {back[card[-1]]}")

main()
