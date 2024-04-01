n, k = map(int, raw_input().split())
total = [0]*n
lowest = [0]*n
for i in range(k):
    scores = map(int, raw_input().split())
    for j in range(n):
        total[j] += scores[j]

    for j in range(n):
        rank = 1
        for l in range(n):
            if total[l] > total[j]:
                rank += 1

        lowest[j] = max(lowest[j], rank)

score = max(total)
for i in range(n):
    if total[i] == score:
        print "Yodeller {} is the TopYodeller: score {}, worst rank {}".format(
            i+1, score, lowest[i])
