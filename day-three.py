def read_input():
    input = open("C:\\Users\\IYD-LHC\\PycharmProjects\\AoC-2021\\venv\\input-files\\input-day-three", "r")
    list = []
    for line in input.readlines():
        line = line.rstrip()
        list.append(line)
    return list

def to_convert_binary_to_decimal(binary):
    decimal = 0
    for posicion, digito in enumerate(binary[::-1]):
        decimal += int(digito) * 2 ** posicion
    return decimal

def to_solve_p1(list):
    contador_unos_list = [0,0,0,0,0,0,0,0,0,0,0,0]
    contador_ceros_list = [0,0,0,0,0,0,0,0,0,0,0,0]
    gamma_rate = ""
    epsilon_rate = ""
    for report in list:
        for i in range(12):
            if report[i] == "0":
                contador_ceros_list[i] = contador_ceros_list[i]+1
            else:
                contador_unos_list[i] = contador_unos_list[i]+1
    for i in range(12):
        if contador_unos_list[i] > contador_ceros_list[i]:
            gamma_rate = gamma_rate+"1"
            epsilon_rate = epsilon_rate+"0"
        else:
            gamma_rate = gamma_rate+"0"
            epsilon_rate = epsilon_rate + "1"
    return to_convert_binary_to_decimal(gamma_rate)*to_convert_binary_to_decimal(epsilon_rate)

print(to_solve_p1(read_input()))
