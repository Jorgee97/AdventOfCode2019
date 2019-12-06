##############################################################
##########            Secure Container         ###############
########## https://adventofcode.com/2019/day/3 ###############
########## 			by Jorge Gomez             ###############
##############################################################


def has_two_consecutive(n):
    n = str(n)
    repeat = 0
    for n1, n2 in zip(n, n[1:]):
        if n1 == n2:
            repeat += 1
        else:
            if repeat == 1:
                return True
            repeat = 0
    return repeat == 1


def is_password_incrementing(n: str) -> bool:
    for i in range(0, 5):
        if int(n[i]) > int(n[i+1]):
            return False
    return True


def does_have_adjacent_digits(n: str) -> bool:
    for i in range(0, 5): ## This is not fast, but I will refactor later.
        if n[i] == n[i+1]:
            return True
    return False


def possible_password(l_range: int, r_range: int) -> int:
    possible_passwords = 0
    for password in range(l_range, r_range):
        if not does_have_adjacent_digits(str(password)):
            continue
        if not is_password_incrementing(str(password)):
            continue
        possible_passwords += 1
    return  possible_passwords


def possible_password_part2(l_range: int, r_range: int) -> int:
    possible_passwords = 0
    for password in range(l_range, r_range):
        if not does_have_adjacent_digits(str(password)):
            continue
        if not is_password_incrementing(str(password)):
            continue
        if has_two_consecutive(password):
            possible_passwords += 1
    return  possible_passwords


if __name__ == "__main__":
    puzzle_input = "136760-595730".split('-')
    left_range = int(puzzle_input[0])
    right_range = int(puzzle_input[1])

    # Part one
    result = possible_password(left_range, right_range)
    print(result)

    # Part two
    result_part_2 = possible_password_part2(left_range, right_range)
    print(result_part_2)
