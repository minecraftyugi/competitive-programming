num = int(raw_input())
student = []
ans = []
right = 0

for i in xrange(num):
    a = raw_input()
    student.append(a)

for i in xrange(num):
    b = raw_input()
    ans.append(b)

for i in xrange(num):
    if student[i] == ans[i]:
        right += 1

print right
