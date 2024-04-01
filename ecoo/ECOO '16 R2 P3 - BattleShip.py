import sys

raw_input = sys.stdin.readline
f = open(r"C:\Users\User\Desktop\ECOOCS_2016\Round 2\DATA\DATA32.TXT", "r")
raw_input = f.readline
def check_adj(grid, currentLocation, shipCoords):
    """ (list of list of int, list of int, list of list of int) -> bool

    Return True iff the currentLocation is a valid position. A position is
    considered valid if it fits in grid and there are no hits adjacent to the
    shipCoords.
    
    """
    
    directions = [(0, 1), (1, 1), (1, 0), (0, -1), \
                  (-1, -1), (-1, 0), (1, -1), (-1, 1)]
    
    for direction in directions:
        checkLocation = [currentLocation[0] + direction[0], \
                         currentLocation[1] + direction[1]]

        #if there is a hit at an adjacent position, and that position is not a
        #part of the coordinates of the current ship we're checking, then our
        #current location is invalid
        if not is_out_of_bounds(grid, checkLocation):
            if grid[checkLocation[0]][checkLocation[1]] == 0 and \
               checkLocation not in shipCoords:
                return False
            
    return True

def is_out_of_bounds(grid, currentLocation):
    """ (list of list of int, list of int) -> bool

    Return True iff currentLocation is within the boundaries of grid.
    
    """
    
    return not (0 <= currentLocation[0] < len(grid) and \
                0 <= currentLocation[1] < len(grid[0]))

def find_valid(grid, size):
    """ (list of list of int, int) -> int

    Return the number of possible and known locations of a ship with length
    size in grid.
    
    """
    
    shipCount = 0
    #check all possible veritcal ships
    for row in xrange(len(grid)):
        for column in xrange(len(grid[0])):
            ship_coords = [[row + i, column] for i in xrange(size)]
            valid_ship = True
            
            for i in xrange(size):
                currentLocation = [row + i, column]
                if is_out_of_bounds(grid, currentLocation):
                    valid_ship = False

                if valid_ship:    
                    currentCell = grid[currentLocation[0]][currentLocation[1]]
                    if currentCell == -1:
                        valid_ship = False
                        
                    if not check_adj(grid, currentLocation, ship_coords):
                        valid_ship = False

            if valid_ship:
                shipCount += 1

    #check all possible horizontal ships            
    for row in xrange(len(grid)):
        for column in xrange(len(grid[0])):
            ship_coords = [[row, column + i] for i in xrange(size)]
            valid_ship = True
            
            for i in xrange(size):
                currentLocation = [row, column + i]
                if is_out_of_bounds(grid, currentLocation):
                    valid_ship = False

                if valid_ship:    
                    currentCell = grid[currentLocation[0]][currentLocation[1]]
                    if currentCell == -1:
                        valid_ship = False

                    if not check_adj(grid, currentLocation, ship_coords):
                        valid_ship = False

            if valid_ship:
                shipCount += 1
                
    return shipCount

for i in xrange(10):
    s, l = map(int, raw_input().strip().split())
    grid = [[] for i in xrange(s)]
    for j in xrange(s):
        row = raw_input().strip()
        for char in row:
            if char == "h":
                grid[j].append(0)
            elif char == "m":
                grid[j].append(-1)
            else:
                grid[j].append(1)

    print find_valid(grid, l)
