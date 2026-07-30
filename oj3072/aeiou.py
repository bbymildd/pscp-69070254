"""aeiou"""
def main():
    """aeiou"""
    name = input().lower()
    a = name.count("a")
    e = name.count("e")
    i = name.count("i")
    o = name.count("o")
    u = name.count("u")

    if 1 <= len(name) < 1000:
        if name.find("a") != -1:
            print(f"a : {a}")
        if name.find("e") != -1:
            print(f"e : {e}")
        if name.find("i") != -1:
            print(f"i : {i}")
        if name.find("o") != -1:
            print(f"o : {o}")
        if name.find("u") != -1:
            print(f"u : {u}")

main()
