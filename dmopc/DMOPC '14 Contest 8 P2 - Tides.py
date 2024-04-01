n = input()
values = map(int, raw_input().split())
minimum = min(values)
maximum = max(values)
pos1 = values.index(minimum)
pos2 = values.index(maximum) + 1
print ["unknown", 0][pos1 < pos2] or ["unknown",maximum - minimum][reduce(lambda a,b: b if a < b else 1e6, values[pos1:pos2]) != 1e6]
