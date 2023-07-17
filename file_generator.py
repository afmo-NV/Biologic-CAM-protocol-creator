#####################################################
## Function that creates the protocol file ##########
#####################################################
import os
from user_input_functions import *
from config_loader import load_config
import logging
import sys


def create_schedule_files(config_data):
    """
        Generates schedule files based on user input and configuration data.

        This function prompts the user for sample information, then generates schedule files
        based on the user's input and the configuration data.

        Parameters:
        config_data : dict
            A dictionary containing the configuration values.
        """

    # User Input
    sample_ID = get_sample_id()
    cc_number = get_coin_cell_number()
    mass_electrodes = get_mass_electrodes(cc_number, config_data['cam_min_value'],
                                                     config_data['cam_max_value'])
    spec_capacity = get_specific_capacity()

    # Create directory for files
    sample_directory = os.path.join(config_data['path_MPS_Biologic'], sample_ID)

    if os.path.exists(sample_directory):
        overwrite = input(
            f"The folder for {sample_ID} already exists. Do you want to overwrite existing files? (Y/N): ")
        if overwrite.lower() != 'y':
            logging.error("Change the sample ID name and try again. Exiting the program.")
            input("Press Enter to exit.")
            sys.exit(1)
    else:
        os.makedirs(sample_directory)

    # Coin Cell file names
    cc_name = [f"{sample_ID}-CC-{i + 1}" for i in range(cc_number)]

    # Replace lines in template and create filenames
    filenames = [] # Creates the name of each file including the mass of the active material
    for i in range(cc_number):
        battery_capacity = round(spec_capacity * mass_electrodes[i], 5)
        current_limit = round((battery_capacity * 0.05) * 1000, 3)

        with open(os.path.join(config_data['path_MPS_Template'], config_data['file_MPS']), 'r') as file:
            filedata = file.read()
            filedata = filedata.replace(config_data['mass_electrode_template'], f'Mass of active material : {mass_electrodes[i]} mg')
            filedata = filedata.replace(config_data['capacity_cell_template'], f'Battery capacity : {battery_capacity} mA.h')
            filedata = filedata.replace(config_data['current_limit_cp_step_template'],
                                        f'Im                  0,000               {current_limit}             0,000')

        with open(os.path.join(sample_directory, f'Formation-Protocol_{sample_ID}_{cc_name[i]}.mps'), 'w') as file:
            file.write(filedata)

        filenames.append(f"{cc_name[i]}_{mass_electrodes[i]}_Mass")

    # Save filenames
    with open(os.path.join(sample_directory, f'{sample_ID}-Filenames.txt'), 'w') as f:
        for item in filenames:
            f.write(f"{item}\n")

    logging.info(f'Protocol files for {sample_ID} were created successfully in {sample_directory}')
