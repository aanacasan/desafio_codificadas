n = int(input())
x = 0
for _ in range(n):
    s = input()
    x += 1 if '++' in s else -1
print(x)