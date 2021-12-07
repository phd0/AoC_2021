import time
import math


def facto(value1, value2):
    result = 0
    for i in range(1, abs(value1 - value2) + 1):
        result += i
    return result


def solve(pa, data):
    result = []
    mini = 99999999999
    for d in range(len(data)):
        result.append(0)
        for i in range(len(data)):
            # print("d=",d,"data[i]=",data[i],d-data[i])
            if pa == 1:
                result[d] += abs(d - data[i])
            else:
                result[d] += facto(d, data[i])
        if result[d] < mini and result[d]:
            mini = result[d]
    return mini


if __name__ == "__main__":
    data = []
    with open("day07.txt") as f:
        line = f.readline()
    data = line.strip().split(",")
    tmp = map(int, data)
    data = list(tmp)
    print("Part 1=", solve(1, data))
    time_start = time.time()
    print("Part 2=", solve(2, data))
    tt = time.time() - time_start
    print("execute time: ", math.trunc(tt/60), ":", round(tt % 60, 2), sep='')
