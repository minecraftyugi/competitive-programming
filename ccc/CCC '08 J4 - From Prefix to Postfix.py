"""
Binary Tree Representation

      1
    /   \
   /     \
  2       3
 / \     / \
4   5   6   7

1 is the root node
2 is the root's left subtree
3 is the root's right subtree

Operation Tree Representation

Given a prefix operation list like - - 3 + 2 1 9 , we can make a binary tree
showing how the operations will be executed.

     -
   /   \
  -     9
 /  \
3    +
    / \
   2   1

By doing a post order depth first traversal on our binary tree, we end up with
a postfix notation of 3 2 1 + - 9 - .
"""

def dfs(tree, start, visited, ans):
    """ (list, int, list, list) -> list

    Return a list of the operations in postfix order (or post traversal order
    in depth first search).

    """
    if not visited[2*start] and tree[2*start] != 0:
        #if left subtree hasnt been fully explored, explore it
        return dfs(tree, 2*start, visited, ans)
    elif not visited[2*start + 1] and tree[2*start + 1] != 0:
        #if right subtree hasnt been fully explored, explore it
        return dfs(tree, 2*start + 1, visited, ans)
    else:
        #mark current node as visited, since it has been fully explored on both
        #left and right subtrees. Append the operation at index node to ans
        visited[start] = 1
        ans.append(tree[start])
        if start == 1:
            #if root is visited, we are done
            return ans
        else:
            #otherwise go back up the tree to the parent node and finish
            #processing it. the parent node is at index start / 2
            return dfs(tree, start / 2, visited, ans)

def next_node(node):
    """ (int) -> int

        Return the next available node as an index for the operation to go in
        the tree.

    """
    if node % 2 == 0:
        #this is a left subtree. return the node corresponding to its right
        #subtree
        return node + 1
    else:
        #this is a right subtree. go back up the tree to its parent node to
        #check if that is a desired left subtree
        return next_node(node / 2)

expression = raw_input()
while expression != "0":
    ops = [0]*100 #our operation tree with a size of 100
    expression = expression.split()
    curr_parent = 1
    for operation in expression:
        ops[curr_parent] = operation
        if not operation.isdigit():
            #operation is a + or - , branch down into the tree. set the current
            #parent to the next available index, which is double the current
            #index
            curr_parent *= 2
        else:
            #operation is a number. we have reached a leaf node in our tree.
            #traverse back up the tree to find the next available index
            curr_parent = next_node(curr_parent)

    ans = dfs(ops, 1, [0]*100, []) #get our answer in a list
    print " ".join(ans) #print it in the right format
    expression = raw_input()
