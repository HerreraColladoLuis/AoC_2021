def read_input():
    input = open("C:\\Users\\IYD-LHC\\PycharmProjects\\AoC-2021\\venv\\input-files\\input-day-one.txt", "r")
    list = []
    for line in input.readlines():
        list.append(int(line))
    return list

def to_solve_p1(list):
    prev_measurement = -1
    result = 0
    for measurement in list:
        if prev_measurement != -1:
            if measurement > prev_measurement:
                result = result + 1
        prev_measurement = measurement
    return result

def to_solve_p2(list):
    prev_sum = -1
    result = 0
    list_size = len(list)
    i = -1
    while i < list_size:
        i = i + 1
        if i+2 == list_size:
            break
        current_sum = list[i] + list[i + 1] + list[i + 2]
        if prev_sum != -1:
            if current_sum > prev_sum:
                result = result + 1
        prev_sum = current_sum
    return result

print(to_solve_p2(read_input()))
