total = input()
a, b = map(int, raw_input().split())
left = set(map(int, raw_input().split())) ^ set(map(int, raw_input().split()))
print total - (a + b - len(left)) / 2
