def is_attacking(q1, q2):
    if q1[0] + q1[1] == q2[0] + q2[1] or q1[0] - q1[1] == q2[0] - q2[1]:
        return True
    if q1[0] == q2[0] or q1[1] == q2[1]:
        return True
    return False
def find_pos(x_st, lst, step):
    if step == 1:
        lst.append((x_st, 1))
        return find_pos(1, lst, step + 1)
    elif 9 > step > 1:
        is_add = False #флаг добавления элемента
        for x in range(x_st, 9):
            temp = (x, step)
            check = True
            for item in lst:
                if is_attacking(temp, item):
                    check = False #Если нашлась хотя бы одна пара, бьющих друг друга
            if check and not is_add:
                lst.append(temp)
                is_add = True
                return find_pos(1, lst, step + 1)
        if not is_add:
            while True:
                x_st = lst.pop()[0] + 1
                step -= 1
                if x_st <= 8 or step == 1:
                    break
            if x_st == 9 and step == 1:
                return False
            return find_pos(x_st, lst, step)
    elif step == 9:
        return True
my_list = []
find_pos(1, my_list, 1)
print(f'{my_list},  1')
for i in range(2, 100):
    stp = 9
    while True:
        start = my_list.pop()[0] + 1
        stp -= 1
        if start <= 8:
            break
    if find_pos(start, my_list, stp):
        print(f'{my_list},  {i}')
    else:
        print('Возможные решения закончились')
        break
