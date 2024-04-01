s, k, i = map(int, raw_input().split())
import collections

s_line = map(int, raw_input().split())
s_line = collections.deque(s_line)
k_line = map(int, raw_input().split())
k_line = collections.deque(k_line)
i_line = map(int, raw_input().split())
i_line = collections.deque(i_line)
lines = [s_line, k_line, i_line]
s_time = 0
k_time = 0
i_time = 0
multiple = 1

def all_diff():
    return len(set(map(len, lines))) == 3
            
def get_longest():
    max_len = max(lines, key=len)
    for i in range(3):
        if len(lines[i]) == max_len:
            return i

def get_shortest():
    min_len = min(lines, key=len)
    for i in range(3):
        if len(lines[i]) == min_len:
            return i

def rebalance(times):
    while times > 0:
        if all_diff():
            line = get_longest()
            skier = lines[line].pop()
            next_line = get_shortest()
            lines[next_line].append(skier)
        else:
            break

        times -= 1
    

while s_line or k_line or i_line:
    while s_line:
        wait = s_line.popleft()
        if s_time + wait <= 30 * multiple:
            s_time += wait
        else:
            s_line.appendleft(wait)
            break

    while k_line:
        wait = k_line.popleft()
        if k_time + wait <= 30 * multiple:
            k_time += wait
        else:
            k_line.appendleft(wait)
            break

    while i_line:
        wait = i_line.popleft()
        if i_time + wait <= 30 * multiple:
            i_time += wait
        else:
            i_line.appendleft(wait)
            break

    multiple += 1
    s_len, k_len, i_len = len(s_line), len(k_line), len(i_line)
    if s_len == k_len or s_len == i_len or i_len == k_len:
        continue
    
    if s_len > k_len and s_len > i_len:
        if k_len > i_len:
            i_line.append(s_line.pop())
        elif i_len > k_len:
            k_line.append(s_line.pop())
    elif k_len > s_len and k_len > i_len:
        if s_len > i_len:
            i_line.append(k_line.pop())
        elif i_len > s_len:
            s_line.append(k_line.pop())
    elif i_len > s_len and i_len > k_len:
        if s_len > k_len:
            k_line.append(i_line.pop())
        elif k_len > s_len:
            s_line.append(i_line.pop())    

print 30 * (multiple - 2) + max(s_time%30, k_time%30, i_time%30)
