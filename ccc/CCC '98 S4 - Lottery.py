import collections

n = input()
ans = []
mul = "X"
def solve(s):
    q = collections.deque()
    pop = False
    mul_count = 0
    for op in s:
        if op.isdigit():
            if pop:
                b, a = q.pop(), q.pop()
                q.append("({} {} {})".format(a, b, op))
            else:
                q.append(op)
        else:
            q.append(op)
            if op == mul:
                pop = True
                mul_count += 1
            else:
                pop = False

    while len(q) > 3:
        a, op, b = q.popleft(), q.popleft(), q.popleft()
        q.appendleft("({} {} {})".format(a, op, b))

    if mul_count == len(s) / 2:
        return q.pop()[1:-1]
    
    return " ".join(q)

for i in xrange(n):
    stack = raw_input().split()
    ans.append(solve(stack))
    
print "\n\n".join(ans)
