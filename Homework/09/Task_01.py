import json
import csv
from random import randint


def save_to_json(func):
    def wrapper(*args, **kwargs):
        f_name = args[0]
        with open(f_name, 'r', newline='') as f_read, open('results.json', 'w') as f_write:
            csv_file = csv.reader(f_read)
            data = []
            for line in csv_file:
                lst = line[0].split()
                a = int(lst[0])
                b = int(lst[1])
                c = int(lst[2])
                res = func(a, b, c)
                data.append({'parameters': [a, b, c], 'result': res})
            json.dump(data, f_write)
    return wrapper

def generate_csv_file(file_name, rows):
    with open(file_name, 'w', newline = '', encoding = 'utf-8') as f:
        csv_write = csv.writer(f, delimiter=' ')
        for i in range(rows):
            a = randint(1, 10)
            b = randint(1, 10)
            c = randint(1, 10)
            row = (a, b, c)
            csv_write.writerow(row)

@save_to_json
def find_roots(a, b, c):
    d = b ** 2 - 4 * a * c
    if d == 0:
        return -b / (2 * a)
    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return (x1, x2)

#generate_csv_file('input_data.csv', 10)
#with open('input_data.csv', 'r', newline='') as f:
    #csv_file = csv.reader(f)
    #for line in csv_file:
        #print(line)
#find_roots('input_data.csv')
#with open('results.json', 'r', encoding='utf-8') as f:
    #data = json.load(f)
#print(data)
