#####################################################
## Function that creates the protocol file ##########
#####################################################
import os
from user_input_functions import *
from config_loader import load_config
import logging
import sys


def create_formation_schedule_files(config_data, sample_ID,cc_number, mass_electrodes):
    """
        Generates Biologic schedule files based on user input and configuration data
        stored in a configuration file.

        This function prompts the user for sample information, then generates schedule files
        based on the user's input and the configuration data.


        Schedule file for formation test with the following parameters:
                    1 cycle
                    Charge @ 0.1C to 4.3 V
                           0.05C current limit
                    Discharge @ 0.1C to 3.0 V

        Parameters:
        config_data : dict
            A dictionary containing the configuration values.
        """

    logging.debug(f'Generating formation protocol files for {sample_ID}')

    # Get the specific capacity of the material (nominal)
    spec_capacity = get_specific_capacity()

    # Create directory for files
    sample_directory = os.path.join(config_data['path_MPS_Biologic'], sample_ID + '-Protocols')

    # Check if the folder for protocols already exists
    if os.path.exists(sample_directory):
        overwrite = input(
            f"The folder for {sample_ID} protocols already exists. Do you want to overwrite existing files? (Y/N):")
        if overwrite.lower() != 'y':
            logging.error("Change the sample ID name and try again. Exiting the program.")
            input("Press Enter to exit.")
            sys.exit(1)
    else:
        os.makedirs(sample_directory)

    # Create coin Cell file names
    cc_name = [f"{sample_ID}-CC-{i + 1}" for i in range(cc_number)]

    # Replace lines in template and create filenames
    filenames = [] # Creates the name of each file including the mass of the active material
    for i in range(cc_number):
        # Calculate the battery capacity based on the specific nominal capacity and
        # the mass of the active material in the coin cell
        battery_capacity = round(spec_capacity * mass_electrodes[i], 5)

        # Set the current limit for the constant potential step as 0.05C
        current_limit = round((battery_capacity * 0.05) * 1000, 3)

        with open(os.path.join(config_data['path_MPS_Template'], config_data['file_MPS']), 'r') as file:
            filedata = file.read()
            filedata = filedata.replace(config_data['mass_electrode_template'], f'Mass of active material : {mass_electrodes[i]} mg')
            filedata = filedata.replace(config_data['capacity_cell_template'], f'Battery capacity : {battery_capacity} mA.h')
            filedata = filedata.replace(config_data['current_limit_cp_step_template'],
                                        f'Im                  0,000               {current_limit}             0,000')

        with open(os.path.join(sample_directory, f'Formation-Protocol_{cc_name[i]}.mps'), 'w') as file:
            file.write(filedata)

        filenames.append(f"{cc_name[i]}-Formation_{mass_electrodes[i]}_Mass.mpr")

    # Save filenames
    with open(os.path.join(sample_directory, f'{sample_ID}-Formation-Filenames.txt'), 'w') as f:
        for item in filenames:
            f.write(f"{item}\n")

    logging.info(f'Protocol files for {sample_ID} were created successfully in {sample_directory}')


def create_cycle_life_schedule_files(config_data, sample_ID, cc_number, mass_electrodes):
    """
        Generates Biologic schedule files based on user input and configuration data
        stored in a configuration file.

        Schedule file for cycle life test with the following parameters:
                    50 cycles
                    Charge @ 0.5C to 4.3 V
                           0.05C current limit
                    Discharge @ 1C to 3.0 V


        This function prompts the user for sample information, then generates schedule files
        based on the user's input and the configuration data.

        Parameters:
        config_data : dict
            A dictionary containing the configuration values.
        """

    logging.debug(f'Generating cycle life protocol files for {sample_ID}')

    # Get the specific capacity of the material (nominal)
    spec_capacity = get_specific_capacity()

    # Create directory for files
    sample_directory = os.path.join(config_data['path_MPS_Biologic'], sample_ID + '-Protocols')

    if os.path.exists(sample_directory):
        overwrite = input(
            f" The folder for {sample_ID} protocols already exists. Do you want to overwrite existing files? (Y/N):")
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

        with open(os.path.join(sample_directory, f'Cycle-Life-Protocol_{cc_name[i]}.mps'), 'w') as file:
            file.write(filedata)

        filenames.append(f"{cc_name[i]}-Cycle-Life_{mass_electrodes[i]}_Mass.mpr")

    # Save filenames
    with open(os.path.join(sample_directory, f'{sample_ID}-Cycle-Life-Filenames.txt'), 'w') as f:
        for item in filenames:
            f.write(f"{item}\n")

    logging.info(f'Protocol files for {sample_ID} were created successfully in {sample_directory}')


def create_formation_capacity_check_schedule_files(config_data, sample_ID, cc_number, mass_electrodes):
    """
        Generates Biologic schedule files based on user input and configuration data
        stored in a configuration file.

        Schedule file for formation + capacity check test with the following parameters:
                    Formation:
                    1 cycle
                    Charge @ 0.1C to 4.3 V
                           0.05C current limit
                    Discharge @ 0.1C to 3.0 V
                    Capacity Check:
                    1 cycle
                    Charge @ 0.2C to 4.3 V
                           0.05C current limit
                    Discharge @ 0.2C to 3.0 V


        This function prompts the user for sample information, then generates schedule files
        based on the user's input and the configuration data.

        Parameters:
        config_data : dict
            A dictionary containing the configuration values.
        """

    logging.debug(f'Generating formation + capacity check protocol files for {sample_ID}')

    # Get the specific capacity of the material (nominal)
    spec_capacity = get_specific_capacity()

    # Create directory for files
    sample_directory = os.path.join(config_data['path_MPS_Biologic'], sample_ID + '-Protocols')

    if os.path.exists(sample_directory):
        overwrite = input(
            f" The folder for {sample_ID} protocols already exists. Do you want to overwrite existing files? (Y/N):")
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

        with open(os.path.join(sample_directory, f'Formation-Capacity-Check-Protocol_{cc_name[i]}.mps'), 'w') as file:
            file.write(filedata)

        filenames.append(f"{cc_name[i]}-Formation-Capacity-Check_{mass_electrodes[i]}_Mass.mpr")

    # Save filenames
    with open(os.path.join(sample_directory, f'{sample_ID}-Formation-Capacity-Check-Filenames.txt'), 'w') as f:
        for item in filenames:
            f.write(f"{item}\n")

    logging.info(f'Protocol files for {sample_ID} were created successfully in {sample_directory}')