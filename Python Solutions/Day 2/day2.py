##############################################################
##########          1202 Program Alarm         ###############
########## https://adventofcode.com/2019/day/2 ###############
########## 			by Jorge Gomez             ###############
##############################################################
from helpers import read_file_numbers


def part2(arr):
    original_arr = arr
    for i in range(100):
        for j in range(100):
            arr = original_arr.copy()
            arr[1] = i
            arr[2] = j

            result = program_alarm(arr)
            if result == 19690720:
                print(f"Noun {i} verb {j}")
                return (100 * i) + j


def program_alarm(arr):
    """Return the modified program alarm at index 0
    1 means adding
    2 means multiplying
    99 means halt the program
    """
    initial = 0
    last = 4

    code_sub_array = arr[initial:last]
    while code_sub_array[0] != 99:
        opcode = code_sub_array[0]
        index1 = code_sub_array[1]
        index2 = code_sub_array[2]
        place_to_change = code_sub_array[3]
        if opcode == 1:
            arr[place_to_change] = arr[index1] + arr[index2]
        else:
            arr[place_to_change] = arr[index1] * arr[index2]

        initial = last
        last += 4
        code_sub_array = arr[initial:last]
    return arr[0]


if __name__ == "__main__":
    code = read_file_numbers('input.txt', ',')
    print(program_alarm(code))

    code = read_file_numbers('original_input.txt', ',')
    print(part2(code))
