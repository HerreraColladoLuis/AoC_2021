def read_input():
    input = open("C:\\Users\\IYD-LHC\\PycharmProjects\\AoC-2021\\venv\\input-files\\input-day-ten.txt", "r")
    list = []
    for line in input.readlines():
        line = line.rstrip()
        list.append(line)
    return list

def to_compute_line(line):
    char_queue = []
    for i in range(0,len(line)):
        input_char = line[i]
        if input_char == "[":
            char_queue.append("]")
        elif input_char == "(":
            char_queue.append(")")
        elif input_char == "{":
            char_queue.append("}")
        elif input_char == "<":
            char_queue.append(">")
        else:
            if input_char != char_queue[len(char_queue)-1]:
                if input_char == "]":
                    return 57
                elif input_char == ")":
                    return 3
                elif input_char == "}":
                    return 1197
                elif input_char == ">":
                    return 25137
            else:
                char_queue.pop(len(char_queue)-1)
    return 0

def to_compute_incomplete_line(line):
    char_queue = []
    for i in range(0, len(line)):
        input_char = line[i]
        if input_char == "[":
            char_queue.append("]")
        elif input_char == "(":
            char_queue.append(")")
        elif input_char == "{":
            char_queue.append("}")
        elif input_char == "<":
            char_queue.append(">")
        else:
            if input_char != char_queue[len(char_queue)-1]:
                return 0
            else:
                char_queue.pop(len(char_queue) - 1)
    if len(char_queue) != 0:
        completion_list = char_queue[::-1]
        total_score = 0
        for character in completion_list:
            total_score = total_score*5
            if character == ")":
                total_score = total_score + 1
            elif character == "]":
                total_score = total_score + 2
            elif character == "}":
                total_score = total_score + 3
            elif character == ">":
                total_score = total_score + 4
    else:
        return 0
    return total_score

def to_solve_p1(list):
    total_score = 0
    for line in list:
        line_score = to_compute_line(line)
        total_score = total_score + int(line_score)
    return total_score

def to_solve_p2(list):
    score_list = []
    for line in list:
        line_score = to_compute_incomplete_line(line)
        if int(line_score) != 0:
            score_list.append(int(line_score))
    score_list.sort()
    return score_list[int((len(score_list)-1)/2)]

print(to_solve_p2(read_input()))
