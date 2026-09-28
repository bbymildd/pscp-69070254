"""point"""
def main():
    """point"""
    sett = int(input())
    for _ in range(sett):
        num = int(input())
        points = []
        for _ in range(num):
            x, y = map(int,input().split())
            points.append((x,y))

        points.sort(key=lambda point: (point[0] + point[1], -point[1]))

        for x,y in points:
            print(x,y)

main()
