"""RGB Mixed"""
def mix_color(c1, c2):
    """Mix value"""
    return (c1 + c2) // 2

def mix_rgb(c1, c2):
    """Mix color"""
    r_mix = mix_color(c1[0], c2[0])
    g_mix = mix_color(c1[1], c2[1])
    b_mix = mix_color(c1[2], c2[2])
    return r_mix, g_mix, b_mix

def main():
    """RGB"""
    color1 = list(map(int, input().split()))
    color2 = list(map(int, input().split()))
    r_mix, g_mix, b_mix = mix_rgb(color1, color2)
    print(f"{r_mix} {g_mix} {b_mix}")

main()
