def read_input():
    input = open("C:\\Users\\IYD-LHC\\PycharmProjects\\AoC-2021\\venv\\input-files\\input-day-two.txt", "r")
    list = []
    for line in input.readlines():
        line = line.rstrip()
        list.append(line)
    return list

def to_parse_command(command):
    split_command = command.split(" ")
    return split_command

def to_solve_p1(list):
    horizontal = 0
    depth = 0
    for command in list:
        split_command = to_parse_command(command)
        direction = split_command[0]
        value = int(split_command[1])
        if direction == "forward":
            horizontal = horizontal + value
        elif direction == "down":
            depth = depth + value
        else:
            depth = depth - value
    return horizontal * depth

def to_solve_p2(list):
    horizontal = 0
    depth = 0
    aim = 0
    for command in list:
        split_command = to_parse_command(command)
        direction = split_command[0]
        value = int(split_command[1])
        if direction == "forward":
            horizontal = horizontal + value
            depth = depth + (aim * value)
        elif direction == "down":
            aim = aim + value
        else:
            aim = aim - value
    return horizontal * depth


print(to_solve_p2(read_input()))
