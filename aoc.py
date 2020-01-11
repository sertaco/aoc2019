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


def d2():
    inp = './input/2.txt'

    def intcode(l, noun, verb):
        l[1] = noun
        l[2] = verb

        i = 0
        # l = [1,1,1,4,99,5,6,0,99]
        while l[i] != 99:
            if l[i] == 1:
                l[l[i + 3]] = l[l[i + 1]] + l[l[i + 2]]
            elif l[i] == 2:
                l[l[i + 3]] = l[l[i + 1]] * l[l[i + 2]]
            i += 4
        return l[0]

    with open(inp) as f:
        l = f.read()
    l = [int(item) for item in l.split(',')]

    l_copy = l.copy()
    print('part1: ', intcode(l_copy, 12, 2))

    for i in range(99):
        for j in range(99):
            l_copy = l.copy()
            if intcode(l_copy, i, j) == 19690720:
                print('part2: ', 100 * i + j)


def d3():
    inp = './input/3.txt'

    with open(inp) as f:
        l = f.read()
    l = l.split('\n')
    w1, w2 = l[0].split(','), l[1].split(',')

    # w1 = ['R8','U5','L5','D3']
    # w2 = ['U7','R6','D4','L4']

    def find_trace(w1):
        trace = [(0, 0)]
        for cmd in w1:
            if cmd[0] == 'R':
                for i in range(int(cmd[1:])):
                    trace.append((trace[-1][0] + 1, trace[-1][1]))
            elif cmd[0] == 'L':
                for i in range(int(cmd[1:]) ):
                    trace.append((trace[-1][0] - 1, trace[-1][1]))
            elif cmd[0] == 'D':
                for i in range(int(cmd[1:])):
                    trace.append((trace[-1][0], trace[-1][1] - 1))
            elif cmd[0] == 'U':
                for i in range(int(cmd[1:])):
                    trace.append((trace[-1][0], trace[-1][1] + 1))
        return trace

    def dist_to_origin(trace):
        dist = dict()
        for pt in trace:
            dist[pt] = sum([abs(item) for item in pt])
        return dist

    trace_w1 = find_trace(w1)
    trace_w2 = find_trace(w2)

    dist_trace_w1 = dist_to_origin(trace_w1)
    dist_trace_w2 = dist_to_origin(trace_w2)

    intersections = []
    dist_origin_intersections = []
    for pt in dist_trace_w1:
        if pt != (0, 0):
            if pt in dist_trace_w2:
                intersections.append(pt)
                dist_origin_intersections.append(dist_trace_w2[pt])
    print(f'part1: {min(dist_origin_intersections)}')

    def steps_to_point(pt, trace):
        for i, item in enumerate(trace):
            if item == pt:
                return i

    total_steps_list = []
    for pt in intersections:
        total_steps_list.append(steps_to_point(pt, trace_w1) + steps_to_point(pt, trace_w2))
    print(f'part2: {min(total_steps_list)}')


def d4():
    inp = '128392-643281'
    inp = inp.split('-')

    def rules(no):
        no = str(no)
        flag = False
        for i, item in enumerate(no):
            if i < 5:
                if no[i] > no[i+1]:
                    return False
                elif no[i] == no[i+1]:
                    flag = True
        return flag

    valid_pass = []
    for i in range(int(inp[0]), int(inp[1])):
        if rules(i):
            valid_pass.append(i)
    print(f'part1: {len(valid_pass)}')

    def r1(no):
        no = str(no)
        for i, item in enumerate(no):
            if i < 5:
                if no[i] > no[i+1]:
                    return False
        return True

    def r2(no):
        no = str(no)
        i = 0
        while i < 5:
            if no[i] == no[i + 1]:
                if i == 4:
                    return True
                elif no[i+2] == no[i]:
                    i = i + 2
                    while i < 5:
                        if no[i] == no[i+1]:
                            i += 1
                        else:
                            break
                else:
                    return True
            i += 1
        return False

    valid_pass = []
    for i in range(int(inp[0]), int(inp[1])):
        if r1(i) and r2(i):
            valid_pass.append(i)
    print(f'part2: {len(valid_pass)}')


if __name__ == "__main__":
    d4()



