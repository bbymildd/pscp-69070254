"""cat"""
import ast
def main():
    """fox"""
    num = int(input())
    cats = {}
    foxes = {}
    all_names = set()

    for _ in range(num):
        data = ast.literal_eval(input())

        for name, code in data.items():
            all_names.add(name)

            if code.startswith("Cat"):
                cats[code] = name
            else:
                foxes[code] = name

    if "Cat01" not in cats and "Garfield" not in all_names:
        cats["Cat01"] = "Garfield"

    if "Fox01" not in foxes and "Fubuki" not in all_names:
        foxes["Fox01"] = "Fubuki"

    print("Cat :", len(cats))
    print("Fox :", len(foxes))

    for code in sorted(cats, key=lambda x: int(x[3:])):
        print(cats[code], ":", code)

    for code in sorted(foxes, key=lambda x: int(x[3:])):
        print(foxes[code], ":", code)

main()
