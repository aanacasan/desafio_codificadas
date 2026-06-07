n = int(input())
print(sum(sum(map(int, input().split())) >= 2 for _ in range(n)))