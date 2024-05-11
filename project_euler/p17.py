HUNDRED = 7
THOUSAND = 8
AND = 3
SINGLES = {1:3,
           2:3,
           3:5,
           4:4,
           5:4,
           6:3,
           7:5,
           8:5,
           9:4
           }
TEENS = {10:3,
         11:6,
         12:6,
         13:8,
         14:8,
         15:7,
         16:7,
         17:9,
         18:8,
         19:8
         }
TENS = {20:6,
        30:6,
        40:5,
        50:5,
        60:5,
        70:7,
        80:6,
        90:6
        }

SINGLES_SUM = sum(SINGLES.values())

def get_sub_hundred_sum():
    total = 0

    #sum first 19 numbers
    total += SINGLES_SUM + sum(TEENS.values())
    
    #sum 20 to 99
    for num, count in TENS.items():
        total += count
        total += count * 9 + SINGLES_SUM

    return total

def get_sub_thousand_sum():
    total = 0

    #sum 100 to 999
    for num, count in SINGLES.items():
        total += count + HUNDRED
        total += get_sub_hundred_sum()
        total += (count + HUNDRED + AND) * 99

    return total

print(get_sub_hundred_sum() + get_sub_thousand_sum() + SINGLES[1] + THOUSAND)
