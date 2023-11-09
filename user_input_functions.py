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


def get_specific_capacity():
    """
    Prompts the user to enter the specific capacity of the sample.
    :return: integer, the user input specific capacity.
    """
    return get_integer_input(
        "Enter the specific capacity of the sample in mA.h/g (Ni83:200, Ni88:205, Ni90 or higher:210): ")


def get_cycling_protocol():
    """
    Prompts the user to enter the cycling protocol for the sample.
    :return: str, the protocol for the sample.
    """
    while True:
        protocol = input("Enter cycling protocol F(Formation), FC(Formation and Capacity Check),"
                         "or CL(Cycle life):")
        if protocol in ['F', 'FC', 'CL']:
            return protocol
        else:
            print("Invalid input. Please enter F, FC, or CL.")
