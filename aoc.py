import numpy as np


def d1():
    inp = './input/1.txt'

    def req_fuel(i):
        return int(np.floor(i/3)-2)

    with open(inp) as f:
        l = f.read()
        l = l.strip().split('\n')
        fuels = [req_fuel(int(item)) for item in l]
    print(f'part1: {sum(fuels)}')

    def req_total_fuel(i):
        res = 0
        fuel = req_fuel(i)
        while fuel > 0:
            res += fuel
            fuel = req_fuel(fuel)
        return res

    fuels = [req_total_fuel(int(item)) for item in l]
    print(f'part2: {sum(fuels)}')


if __name__ == "__main__":
    d1()
