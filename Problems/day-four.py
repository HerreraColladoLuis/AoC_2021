def read_input():
    input = open("C:\\Users\\IYD-LHC\\PycharmProjects\\AoC-2021\\venv\\input-files\\input-day-four.txt", "r")
    list = []
    for line in input.readlines():
        line = line.rstrip()
        list.append(line)
    return list

def to_solve_p1(list):
    card_list = []
    number_list = list[0].split(",")
    number_count = -1
    card_count = -1
    for number in number_list:
        number_count = number_count+1
        i = 2

        while i < len(list):
            marked = 0
            card_count = card_count + 1
            line_count = 0
            if number_count == 0:
                default_card = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

            for j in range(0,5):
                line_count = line_count + 1
                if marked == 1:
                    i = i + (6-line_count)
                    break
                row = list[i].split(" ")
                for a in range(0,5):
                    if row[a] == "":
                        row.remove("")

                for k in range(0,5):
                    if number == row[k]:
                        marked = 1
                        if number_count == 0:
                            default_card[j][k] = 1
                            card_list.append(default_card)
                        else:
                            card_list[card_count][j][k] = 1
                i = i+1
            i = i+1 
    return 0

to_solve_p1(read_input())
