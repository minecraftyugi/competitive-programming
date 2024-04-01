class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.nutrients = [0] * 2501

def create_node(s):
    stack = []
    num = ""
    idx = 0
    while idx < len(s):
        ch = s[idx]
        if ch.isdigit():
            num += ch
        elif not ch.isdigit() and num:
            node = Node(int(num))
            num = ""
            idx -= 1
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
        elif ch == "(":
            node = Node(None)
            stack.append(node)
        elif ch == ")":
            if len(stack) == 1:
                return stack[-1]

            node = stack.pop()
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node

        idx += 1

    return Node(int(num))

def max_output(tree, growth):
    ans = 0
    if tree.nutrients[growth]:
        return tree.nutrients[growth]
    elif tree.val:
        for i in range(growth+1):
            tree.nutrients[i] = tree.val + i
            
        return tree.nutrients[growth]
    elif growth == 0:
        tree.nutrients[growth] = 2
        return tree.nutrients[growth]
    else:
        dp_l = [0] * (growth+1)
        dp_r = [0] * (growth+1)
        for i in range(growth, -1, -1):
            for j in range(i+1):
                sub_growth = i - j
                cap = j
                tmp = min(max_output(tree.left, sub_growth), (1 + cap)**2)
                dp_l[i] = max(dp_l[i], tmp)

        for i in range(growth, -1, -1):
            for j in range(i+1):
                sub_growth = i - j
                cap = j
                tmp = min(max_output(tree.right, sub_growth), (1 + cap)**2)
                dp_r[i] = max(dp_r[i], tmp)

        for i in range(growth+1):
            best = 0
            for j in range(i+1):
                best = max(best, dp_l[j] + dp_r[i - j])

            tree.nutrients[i] = best
     
    return tree.nutrients[growth]

tree = input()
growth = int(input())
root = create_node(tree)
print(max_output(root, growth))
