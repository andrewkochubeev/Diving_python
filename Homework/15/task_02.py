from math import sqrt
import argparse

parser = argparse.ArgumentParser(description='Принимаем строку с коэффициентами')
parser.add_argument('-a', type=int, default=5)
parser.add_argument('-b', type=int, default=0)
parser.add_argument('-c', type=int, default=0)
args = parser.parse_args()
a, b, c = args.a, args.b, args.c
d = (b ** 2) - (4 * a * c)
if d < 0:
    print('корней нет')
elif d > 0:
    x1 = (sqrt(d) - b) / (2 * a)
    x2 = (-sqrt(d) - b) / (2 * a)
    print(f'корни {x1, x2}')
elif d == 0:
    print((-b) / (2 * a))
