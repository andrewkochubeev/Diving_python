def is_attacking(q1, q2):
    if q1[0] + q1[1] == q2[0] + q2[1] or q1[0] - q1[1] == q2[0] - q2[1]:
        return True
    if q1[0] == q2[0] or q1[1] == q2[1]:
        return True
    return False
   
tested_coords = []
queens = []
for i in range(64):
    is_first = False
    queens.clear()
    for x in range(1, 9):
        for y in range(1, 9):
            if (x, y) not in tested_coords and not is_first:
                queens.append((x, y))
                tested_coords.append((x, y))
                is_first = True
    is_add = True
    while len(queens) < 8:
        if is_add:
            is_add = False
        else:
            break
        for x in range(1, 9):
            for y in range(1, 9):
                temp = (x, y)
                check = True
                for item in queens:
                    if is_attacking(temp, item):
                        check = False
                if check and not is_add:
                    queens.append(temp)
                    is_add = True
    if len(queens) > 6:
        print(f'{queens}, {len(queens)}')
