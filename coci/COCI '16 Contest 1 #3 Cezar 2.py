def first_diff(s1, s2):
    for i in xrange(min(len(s1), len(s2))):
        if s1[i] != s2[i]:
            return i

    if len(s1) >= len(s2):
        #this order is not possible
        return -1

    #any order can work
    return -2

def has_cycle(tree):
    visited = [0]*26
    for i in xrange(97, 123):
        if not visited[i-97]:
            result = dfs(i, tree, set([i]), visited)
            if result:
                return True
    
    return False

def dfs(node, tree, stack, visited):
    for child in tree[node]:
        if child in stack:
            return True
        elif not visited[child-97]:
            stack.add(child)
            result = dfs(child, tree, stack, visited)
            if result:
                return True

    stack.remove(node)       
    visited[node-97] = 1
    return False

def topsort(tree):
    visited = [0]*26
    post_order = []
    for i in xrange(97, 123):
        if not visited[i-97]:
            explore(i, tree, post_order, visited)

    post_order.reverse()
    return post_order

def explore(node, tree, post, visited):
    for child in tree[node]:
        if not visited[child-97]:
            explore(child, tree, post, visited)
            
    visited[node-97] = 1
    post.append(node)

if __name__ == "__main__":
    n = input()
    words = []
    for i in xrange(n):
        words.append(raw_input())

    order = map(int, raw_input().split())
    for i in xrange(n):
        order[i] -= 1

    tree = {i:set() for i in xrange(97, 123)}
    new_order = [0]*n
    for i in xrange(n):
        new_order[i] = words[order[i]]

    valid = True
    for i in xrange(n-1):
        for j in xrange(i+1, n):
            s1, s2 = new_order[i], new_order[j]
            index = first_diff(s1, s2)
            if index == -1:
                valid = False
            elif index != -2:
                tree[ord(s1[index])].add(ord(s2[index]))

    if valid and not has_cycle(tree):
        post = topsort(tree)
        ans = [0]*26
        for i in xrange(26):
            ans[post[i]-97] = chr(i+97)
            
        print "DA"
        print "".join(ans)
    else:
        print "NE"
