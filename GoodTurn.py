def GoodTurn(x,y):
    if (x + y ) > 6:
        return "YES"
    else:
        return "NO"

t = int(input())
for _ in range(t):
    x,y = map(int, input().split())
    result = GoodTurn(x,y)
    print(result)
