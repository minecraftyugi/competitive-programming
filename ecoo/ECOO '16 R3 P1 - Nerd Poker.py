from math import factorial, ceil, floor
import sys

raw_input = sys.stdin.readline
f = open(r"C:\Users\User\Desktop\ECOOCS_2016\Round 3\DATA\DATA11.TXT")
raw_input = f.readline

def expected_dice(total_dice, total_sides):
    """ (int, int) -> float

    Return the expected number of dice that will have an outcome of 1, with each
    dice having total_sides sides.

    >>> expected_dice(1, 20)
    0.05
    >>> expected_dice(125, 4)
    31.25
    >>> expected_dice(20, 20)
    1.0
    """

    p = 1.0 / total_sides
    return total_dice * p 

def expected_trials(p):
    """ (float) -> int

    Return the ceiling of the expected number of trials for an event (like
    rolling a one with a 20-sided die) to happen with a probability of p.
    Precondition: 0 < p < 1

    >>> expected_trials(0.05)
    20
    >>> expected_trials(0.5)
    2
    """
    
    return int(round(1 / p))

for i in xrange(10):
    n, s = map(int, raw_input().split())
    total_rolls = 0
    while n:
        num_dice = expected_dice(n, s)
        #print num_dice, total_rolls
        if num_dice > 0.5:
            total_rolls += 1 #it takes one roll to get multiple ones
            n -= int(round(num_dice)) #take the floor since fractions arent important
            #print total_rolls
        else:
            total_rolls += expected_trials(num_dice) #multiple rolls needed
            n -= 1 #we only get rid of one die after multiple rolls

    print total_rolls

def find_parent(node, visited):
    """ (int, set of int) -> int

    Return the parent of node, keeping track of visited nodes in visited.
    
    """
    
    if node == -1:
        for prev_node in visited:
            if prev_node != -1:
                parents[prev_node] = -1

        return -1
    
    if parents[node] == node:
        for prev_node in visited:
            parents[prev_node] = node
            
        return node

    visited.add(parents[node])        
    return find_parent(parents[node], visited)

##for i in xrange(10):
##    n, s = map(int, raw_input().split())
##    parents = {i:i for i in xrange(n+1)}
##    parents[n] = -1 #signifies end of dice
##    total_rolls = 0
##    curr_die = 0
##    next_die = 0
##    while find_parent(next_die, set([next_die])) != -1:
##        for j in xrange(s):
##            curr_die = find_parent(next_die, set([next_die]))
##            #curr_die = next_die
##            next_die = find_parent(curr_die + 1, set([curr_die + 1]))
##            if next_die == -1:
##                total_rolls += 1
##                next_die = parents[0]
##
##        for i in xrange(n):
##            find_parent(i, set([i]))
##
##        die = find_parent(curr_die, set([curr_die]))
##        parents[die] = find_parent(die + 1, set([die + 1]))
##        #parents[die] = find_parent(curr_die + 1, set([curr_die + 1]))
##        #print curr_die, next_die, total_rolls
##        #print parents
##
##    print total_rolls
