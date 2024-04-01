import sys

raw_input = sys.stdin.readline
#f = open("DATA41.TXT", "r")
#raw_input = f.readline
def validate_position(grid, position):
    """ (list of list of str, tuple of int) -> bool

    Return True iff the position is on the grid.
    
    """

    if not 0 <= position[0] < len(grid):
        return False

    if not 0 <= position[1] < len(grid[0]):
        return False

    return True

def is_clear(grid, position):
    """ (list of list of str, tuple of int) -> bool

    Return True iff the position on the grid is clear.
    Precondition: position is a valid position in grid.

    """

    return grid[position[0]][position[1]] in ".CFT"
    
def is_platform(grid, position):
    """ (list of list of str, tuple of int) -> bool

    Return True iff the position on the grid is a platform.
    Precondition: position is a valid position in grid.
    
    """

    return grid[position[0]][position[1]] == "="

def is_ladder(grid, position):
    """ (list of list of str, tuple of int) -> bool

    Return True iff the position on the grid is a ladder.
    Precondition: position is a valid position in grid.
    
    """

    return grid[position[0]][position[1]] == "#"

def drop(grid, position):
    """ (list of list of str, tuple of int) -> tuple of (bool, tuple of int)

    Return a tuple containing True and the position the brother will land
    after dropping, if the brother can actually land. Otherwise, return a tuple
    containing False and an error position.
    Precondition: the position isn't a platform, or the position is invalid.
    
    """

    if not validate_position(grid, position):
        return False, (-1, -1)

    x, y = position
    lower_position = (x+1, y)
    if not validate_position(grid, lower_position):
        return False, (-1, -1)
    
    if not is_clear(grid, lower_position) or is_ladder(grid, position):
        return True, position
    else:
        return drop(grid, lower_position)

def valid_default_moves(grid, position):
    """ (list of list of str, tuple of int) -> list of tuple of int

    Return all the valid default positions that all brothers can move to.
    Precondition: position is a valid position in grid and is not a drop
    position.

    """

    valid_positions = []
    x, y = position
    left = (x, y-1)
    right = (x, y+1)
    top = (x-1, y)
    bottom = (x+1, y)
    if validate_position(grid, left):
        if not is_platform(grid, left):
            can_move, left = drop(grid, left)
            if can_move:
                valid_positions.append(left)

    if validate_position(grid, right):
        if not is_platform(grid, right):
            can_move, right = drop(grid, right)
            if can_move:
                valid_positions.append(right)

    if validate_position(grid, top):
        if not is_platform(grid, top) and is_ladder(grid, position):
            valid_positions.append(top)

    if validate_position(grid, bottom):
        if is_ladder(grid, bottom):
            valid_positions.append(bottom)

    return valid_positions
    
def valid_hop_moves(grid, position):
    """ (list of list of str, tuple of int) -> list of tuple of int

    Return all the valid positions that hop can move to.
    Precondition: position is a valid position in grid.

    """

    valid_positions = valid_default_moves(grid, position)
    x, y = position
    left, mid = (x-1, y-1), (x-1, y)
    moves = [left, mid]
    all_valid = True
    if validate_position(grid, left):
        for move in moves:
            if is_platform(grid, move):
                all_valid = False

        if all_valid:
            can_move, left = drop(grid, left)
            if can_move:
                valid_positions.append(left)

    right, mid = (x-1, y+1), (x-1, y)
    moves = [right, mid]
    all_valid = True
    if validate_position(grid, right):
        for move in moves:
            if is_platform(grid, move):
                all_valid = False
        
        if all_valid:
            can_move, right = drop(grid, right)
            if can_move:
                valid_positions.append(right)

    top = (x-1, y)
    if validate_position(grid, top):
        if is_ladder(grid, top): #if top isn't ladder, top is platform or drop
            valid_positions.append(top)

    return valid_positions
            
def valid_skip_moves(grid, position):
    """ (list of list of str, tuple of int) -> list of tuple of int

    Return all the valid positions that skip can move to.
    Precondition: position is a valid position in grid.
    
    """

    valid_positions = valid_default_moves(grid, position)
    x, y = position
    left, mid = (x, y-2), (x, y-1)
    moves = [left, mid]
    all_valid = True
    if validate_position(grid, left):
        for move in moves:
            if is_platform(grid, move):
                all_valid = False

        if all_valid:
            can_move, left = drop(grid, left)
            if can_move:
                valid_positions.append(left)

    right, mid = (x, y+2), (x, y+1)
    moves = [right, mid]
    all_valid = True
    if validate_position(grid, right):
        for move in moves:
            if is_platform(grid, move):
                all_valid = False

        if all_valid:
            can_move, right = drop(grid, right)
            if can_move:
                valid_positions.append(right)

    return valid_positions
                
def valid_jump_moves(grid, position):
    """ (list of list of str, tuple of int) -> list of tuple of int

    Return all the valid positions that jump can move to.
    Precondition: position is a valid position in grid.
    
    """

    valid_positions = valid_default_moves(grid, position) + \
                      valid_hop_moves(grid, position) + \
                      valid_skip_moves(grid, position)
    x, y = position
    long_left, mid1, mid2 = (x, y-3), (x, y-2), (x, y-1)
    moves = [long_left, mid1, mid2]
    all_valid = True
    if validate_position(grid, long_left):
        for move in moves:
            if is_platform(grid, move):
                all_valid = False

        if all_valid:
            can_move, long_left = drop(grid, long_left)
            if can_move:
                valid_positions.append(long_left)

    high_left, mid1, mid2, mid3 = (x-1, y-2), (x-1, y-1), (x-1, y), (x, y-1)
    moves = [high_left, mid1, mid2, mid3]
    all_valid = True
    if validate_position(grid, high_left):
        for move in moves:
            if is_platform(grid, move):
                all_valid = False

        if all_valid:
            can_move, high_left = drop(grid, high_left)
            if can_move:
                valid_positions.append(high_left)

    long_right, mid1, mid2 = (x, y+3), (x, y+2), (x, y+1)
    moves = [long_right, mid1, mid2]
    all_valid = True
    if validate_position(grid, long_right):
        for move in moves:
            if is_platform(grid, move):
                all_valid = False

        if all_valid:
            can_move, long_right = drop(grid, long_right)
            if can_move:
                valid_positions.append(long_right)

    high_right, mid1, mid2, mid3 = (x-1, y+2), (x-1, y+1), (x-1, y), (x, y+1)
    moves = [high_right, mid1, mid2, mid3]
    all_valid = True
    if validate_position(grid, high_right):
        for move in moves:
            if is_platform(grid, move):
                all_valid = False

        if all_valid:
            can_move, high_right = drop(grid, high_right)
            if can_move:
                valid_positions.append(high_right)

    high_jump, mid = (x-2, y), (x-1, y)
    moves = [high_jump, mid]
    all_valid = True
    if validate_position(grid, high_jump):
        for move in moves:
            if is_platform(grid, move):
                all_valid = False

        if all_valid:
            can_move, high_jump = drop(grid, high_jump)
            if can_move:
                valid_positions.append(high_jump)

    return valid_positions
    
def solve(grid, positions, reachable_locations, brother, visited):
    """ (list of list of str, set of tuple of int, set of str,
         str, set of tuple of int) -> set of str

    Return all the reachable_locations for the brother, by exploring all
    positions the brother can be in grid. Keep track of visited positions in
    the visited set.
    Precondition: all positions are valid, and brother is either "hop", "skip",
    or "jump".

    """
    
    new_positions = set()
    for position in positions:
        if brother == "hop":
            locations = valid_hop_moves(grid, position)
        elif brother == "skip":
            locations = valid_skip_moves(grid, position)
        else:
            locations = valid_jump_moves(grid, position)

        for location in locations:
            cell = grid[location[0]][location[1]]
            if cell == "C":
                reachable_locations.add("C")
            elif cell == "F":
                reachable_locations.add("F")
            elif cell == "T":
                reachable_locations.add("T")

            if location not in visited:
                visited.add(location)
                new_positions.add(location)

    if new_positions:
        return solve(grid, new_positions, reachable_locations, brother, visited)

    return reachable_locations   
    
for i in xrange(10):
    w, h = map(int, raw_input().strip().split())
    grid = [[] for i in xrange(h)]

    #top left corner is (0, 0), bottom right corner is (h-1, w-1)
    for j in xrange(h):
        line = raw_input().strip()
        for index, char in enumerate(line):
            if char == "h":
                hop = (j, index)
                char = "."
            elif char == "s":
                skip = (j, index)
                char = "."
            elif char == "j":
                jump = (j, index)
                char = "."

            grid[j].append(char)

    can_move, hop = drop(grid, hop)
    if can_move:
        msg = "HOP"
        reachable_locations = solve(grid,set([hop]),set(),"hop",set([hop]))
        if reachable_locations:
            print msg, "".join(sorted(reachable_locations))
        else:
            print msg

    can_move, skip = drop(grid, skip)
    if can_move:
        msg = "SKIP"
        reachable_locations = solve(grid,set([skip]),set(),"skip",set([skip]))
        if reachable_locations:
            print msg, "".join(sorted(reachable_locations))
        else:
            print msg

    can_move, jump = drop(grid, jump)
    if can_move:
        msg = "JUMP"
        reachable_locations = solve(grid,set([jump]),set(),"jump",set([jump]))
        if reachable_locations:
            print msg, "".join(sorted(reachable_locations))
        else:
            print msg

    print ""
