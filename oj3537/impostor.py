"""impostor"""
import ast
def main():
    """impostor"""
    player = {}

    while True:
        text = input()
        if text == "Start":
            break

        player.update(ast.literal_eval(text))

    dead = {}

    while True:
        name = input()
        if name == "End":
            break

        if name in player:
            dead[name] = player.pop(name)

    impostor = 0
    for role in player.values():
        if role == "Impostor":
            impostor += 1

    print(impostor, "Impostor Remains")
    print("***Alive***")

    for name in sorted(player):
        print(name, ":", player[name])

    print("***Dead***")

    for name in sorted(dead):
        print(name, ":", dead[name])

main()
