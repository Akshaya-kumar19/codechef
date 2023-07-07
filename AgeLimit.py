def agelimit(x,y,z):
    if z >= x and z < y:
        return "YES"
    else:
        return "NO"
t = int(input())
for _ in range(t):
    x,y,z = map(int, input().split(" "))
    result = agelimit(x,y,z)
    print(result)
