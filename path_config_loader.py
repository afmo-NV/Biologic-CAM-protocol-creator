import os
import yaml
import logging


def load_path_config(config_directory, directory_config_filename):
    """
    Loads the path configuration file that contains the directories for all the necessary files.

    :param config_directory: string, the directory where the configuration file is located.
    :param directory_config_filename: string, the name of the protocol configuration file.
    :return: dictionary, the configuration data.
    """
    config_file_path = os.path.join(config_directory, directory_config_filename)

    # Check if the directory and the file exist
    if not os.path.isdir(config_directory):
        logging.error(f"CONFIG_LOADER. Path configuration directory not found: {config_directory}")
        return None
    if not os.path.isfile(config_file_path):
        logging.error(f"CONFIG_LOADER. Path configuration file not found: {config_file_path}")
        return None

    with open(os.path.join(config_directory, directory_config_filename)) as file:
        doc = yaml.load(file, Loader=yaml.FullLoader)

    path_Coin_Cell_Records_File = doc['path_Coin_Cell_Records_File']
    cc_records_filename = doc['cc_records_filename']
    path_MPS_Template = doc['path_MPS_Template']
    path_MPS_Biologic = doc['path_MPS_Biologic']

    logging.debug(f"CONFIG_LOADER. Path configuration file loaded successfully")

    # Return as a dictionary
    return {
        "path_MPS_Template": path_MPS_Template,
        "path_MPS_Biologic": path_MPS_Biologic,
        "path_Coin_Cell_Records_File": path_Coin_Cell_Records_File,
        "cc_records_filename": cc_records_filename,
    }
