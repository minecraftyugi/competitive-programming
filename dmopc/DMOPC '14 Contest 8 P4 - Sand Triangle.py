import math

n = input()
root = int(math.ceil((1 + math.sqrt(1 + 8 * n)) / 2))
start = (root - 1) * (root - 2) / 2 + 1
end = root * (root - 1) / 2
ans = (end - start + 1) / 2.0 * (start + end)
print int(ans)
