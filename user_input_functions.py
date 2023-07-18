##########################################################
# These are functions that take sample information #######
# from the user ##########################################

def get_sample_id():
    """
    Prompts the user to enter a sample ID.
    :return: string, the user input sample ID.
    """
    sample_ID = input("Enter name of the sample (DO NOT USE underscores '_'):")
    return sample_ID

def get_integer_input(prompt_message):
    """
    Prompts the user to input an integer, repeating until a valid integer is entered.
    This function is used in get_coin_cell_number
    :param prompt_message: string, the message displayed to the user when prompting for input.
    :return: integer, the user input.
    """
    while True:
        try:
            return int(input(prompt_message))
        except ValueError:
            print("Invalid input, please enter an integer value.")

def get_coin_cell_number():
    """
    Prompts the user to enter the number of coin cells.
    :return: integer, the user input number of coin cells.
    """
    return get_integer_input("How many coin cells are going to be run?:")


def get_float_input(prompt_message):
    """
    Prompts the user to input a float, repeating until a valid float is entered.
    :param prompt_message: string, the message displayed to the user when prompting for input.
    :return: float, the user input.
    """
    while True:
        try:
            return float(input(prompt_message))
        except ValueError:
            print("Invalid input, please enter a float "
                  "(Example 0.015) value.")

def get_mass_electrodes(cc_number, min_value, max_value):
    """
    Prompts the user to enter the mass of electrodes, with multiple checks for valid and expected values.
    min and max values are introduced to avoid typos when entering the values.
    :param cc_number: integer, the number of coin cells.
    :return: list of floats, the mass of electrodes entered by the user.
    """
    while True:
        try:
            mass_electrodes = list(map(float, input("Enter mass of electrodes separated by comma: ").split(',')))
            if len(mass_electrodes) != cc_number:
                print(
                    f'The number of mass values ({len(mass_electrodes)}) is not equal to the number of coin cells ({cc_number}). '
                    f'Please enter the values again.')
                continue
            for idx, x in enumerate(mass_electrodes):
                while x >= max_value or x <= min_value:
                    if x >= max_value:
                        print(f'Mass of electrode {idx + 1} out of spec (higher than {max_value}), '
                              f'please entry again this value')
                    if x <= min_value:
                        print(f'Mass of electrode {idx + 1} out of spec (lower than {min_value}), '
                              f'please entry again this value')
                    mass_electrodes[idx] = get_float_input('Correct value: ')
                    x = mass_electrodes[idx]
            return mass_electrodes
        except ValueError:
            print("Invalid input, please enter float values separated by commas.")


def get_specific_capacity():
    """
    Prompts the user to enter the specific capacity of the sample.
    :return: integer, the user input specific capacity.
    """
    return get_integer_input(
        "Enter the specific capacity of the sample in mA.h/g (Ni83:200, Ni88:205, Ni90 or higher:210): ")