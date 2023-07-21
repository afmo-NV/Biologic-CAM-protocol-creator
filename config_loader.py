#####################################################
# Information stored in the configuration file ######
#####################################################
import os
import yaml
import logging


def load_config(config_directory, config_filename, protocol_type):
    """
        Loads the configuration file and returns all the values in
        that file.

        Parameters:
        config_directory : str
            The directory containing the configuration file.
        config_filename : str
            The name of the configuration file (yaml).

        Returns:
        config_data : dict
            A dictionary containing the configuration values.
        """
    config_file_path = os.path.join(config_directory, config_filename)

    # Check if the directory and the file exist
    if not os.path.isdir(config_directory):
        logging.error(f"Configuration directory not found: {config_directory}")
        #print(f"Configuration directory not found: {config_directory}")
        return None
    if not os.path.isfile(config_file_path):
        #print(f"Configuration file not found: {config_file_path}")
        logging.error(f"Configuration file not found: {config_file_path}")
        return None

    with open(os.path.join(config_directory, config_filename)) as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        doc = yaml.load(file, Loader=yaml.FullLoader)

    path_MPS_Template = doc['path_MPS_Template']
    path_MPS_Biologic = doc['path_MPS_Biologic']

    # Ask user the type of test they want to perform
    # Options: F(Formation), FC(Formation and Capacity Check)
    #          or CL(Cycle life)

    if protocol_type == 'F':
        file_MPS = 'Formation_Standard_Protocol-C-N.mps'
    elif protocol_type == 'FC':
        file_MPS = 'Formation-Cap-Check-Protocol-Template-C-N.mps'
    elif protocol_type == 'CL':
        file_MPS = 'Cycle_Life_Standard_Protocol-Template-C-N.mps'

    ##################################################
    ##################################################
    ##################################################

    # Import template Lines that need to be replaced #
    # with sample data ###############################
    mass_electrode_template = doc['mass_electrode_template']
    capacity_cell_template = doc['capacity_cell_template']
    current_limit_cp_step_template = doc['current_limit_cp_step_template']

    ############################################################
    # Import cam electrode min and max weight ##################
    ############################################################
    # Active material weight in electrode min value
    cam_min_value = float(doc['cam_min_value'])
    # Active material weight in electrode max value
    cam_max_value = float(doc['cam_max_value'])

    # Return as a dictionary
    return {
        "path_MPS_Template": path_MPS_Template,
        "path_MPS_Biologic": path_MPS_Biologic,
        "file_MPS": file_MPS,
        "mass_electrode_template": mass_electrode_template,
        "capacity_cell_template": capacity_cell_template,
        "current_limit_cp_step_template": current_limit_cp_step_template,
        "cam_min_value": cam_min_value,
        "cam_max_value": cam_max_value,
    }
