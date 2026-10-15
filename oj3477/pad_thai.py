"""pad"""
def main():
    """thai"""
    must = [
        "Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp",
        "Bean Sprouts", "Noodle", "Chives", "Lime", "Egg",
        "Oil", "Peanuts"
    ]
    raw = []
    bad_ingre = False

    while True:
        ingre = input()
        if ingre == "Cook":
            break
        if ingre not in must:
            bad_ingre = True
        else:
            raw.append(ingre)

    taste = []
    while True:
        feel = input()
        if feel == "End":
            break
        taste.append(feel)

    if bad_ingre:
        print("This is not Pad Thai!!!")
    elif set(raw) != set(must):
        print("This is bad!")
    elif set(taste) == {"Sweet", "Sour", "Salty"}:
        print("Delicious!")
    else:
        print("Not Bad...")

main()
