n = input()
vert = [[0]*(n+1) for i in xrange(n+1)]
horiz = [[0]*(n+1) for i in xrange(n+1)]
for i in xrange(1, n+1):
    grid = raw_input().replace(".", "0").replace("#", "1")
    for j in xrange(1, n+1):
        vert[j][i] = vert[j][i-1] + int(grid[j-1])
        horiz[i][j] = horiz[i][j-1] + int(grid[j-1])

size = 1
for i in xrange(1, n+1):
    for j in xrange(1, n+1):
        low = j-1
        changed = False
        while low + size <= n:
            high = low + size
            if vert[j][high] - vert[j][low] != 0 or horiz[i][high] - horiz[i][low] != 0:
                if changed:
                    size -= 1

                break

            size += 1
            
            
        
print size    
import pprint
pprint.pprint(vert)
pprint.pprint(horiz)
