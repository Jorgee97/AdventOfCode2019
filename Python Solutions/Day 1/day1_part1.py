##############################################################
########## The Tyranny of the Rocket Equation  ###############
########## https://adventofcode.com/2019/day/1 ###############
########## 			by Jorge Gomez             ###############
##############################################################
from helpers import read_file


def calculate_fuel(m):
    """Return an integer
    Fuel required to launch a given module(m)  is based on its mass.
    Specifically, to find the fuel required for a module,
    take its mass, divide by three, round down, and subtract 2.
    """
    return (m // 3) - 2


if __name__ == '__main__':
    modules = read_file('input.txt')
    total_amount_of_fuel = sum([calculate_fuel(int(m)) for m in modules])
    print(total_amount_of_fuel)
