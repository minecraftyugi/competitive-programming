num = int(raw_input())
tunnel = []

for i in xrange(num):
    value = raw_input()
    value = value.split(" ")
    value = map(int, value)
    value = abs(value[0] - value[1])
    tunnel.append(value)

print max(tunnel)
    
