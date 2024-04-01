import sys

raw_input = sys.stdin.readline
#f = open("DATA41.txt")
#raw_input = f.readline
def dist(p1, p2):
    """ (tuple of int, tuple of int) -> int

    Return the squared distance between p1 and p2.

    >>> first = (0, 0)
    >>> second = (3, 4)
    >>> dist(first, second)
    25
    """

    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

def choose_party(l):
    """ (list of str) -> str

    Return whether the party of the newcomer will be R or D depending on the
    parties of the neighbours in l.
    Precondition: l will only contain the strings 'R' and 'D'

    >>> choose_party(['R','R','D'])
    'R'
    >>> choose_party(['R','D','D'])
    'D'
    >>> choose_party(['R','R','D','D'])
    'D'
    """

    r_count = 0
    d_count = 0
    for party in l:
        if party == 'R':
            r_count += 1
        else:
            d_count += 1

    if r_count > d_count:
        return 'R'

    return 'D'

for i in xrange(10):
    center_x, center_y = map(int, raw_input().strip().split())
    houses = [] #stores neighbour houses
    occupied = set() #stores unavailable house locations for fast lookups
    rep_count = 0 #stores number of locations where the newcomer is republican
    dem_count = 0 #stores number of locations where the newcomer is democrat
    for j in xrange(100):
        x, y, party = raw_input().strip().split()
        houses.append((int(x), int(y), party))
        occupied.add((int(x), int(y)))

    for x_offset in xrange(-50, 51):
        for y_offset in xrange(-50, 51):
            main_point = (center_x + x_offset, center_y + y_offset)
            if dist(main_point, (center_x, center_y)) > 50**2:
                continue #if point not in boundary, skip it
            if main_point in occupied:
                continue #we cant build a house in an occupied location
            
            houses.sort(key = lambda x: dist(main_point, (x[0], x[1])))
            third_distance = dist(main_point, (houses[2][0], houses[2][1]))
            closest_parties = [] #stores at least 3 parties for closest houses
            for i in xrange(3):
                closest_parties.append(houses[i][2])

            index = 3
            possible_tie = True
            while index <= 99 and possible_tie:
                x, y, party = houses[index]
                if dist(main_point, (x, y)) == third_distance:
                    closest_parties.append(party)
                else:
                    possible_tie = False

                index += 1
                
            newcomer_party = choose_party(closest_parties)
            if newcomer_party == "R":
                rep_count += 1
            else:
                dem_count += 1

    print round(100.0 * dem_count / (dem_count + rep_count), 1)
