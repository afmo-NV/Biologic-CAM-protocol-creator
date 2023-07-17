from config_loader import load_config
from file_generator import create_schedule_files
from config_loader import load_config
import os
import sys
import logging


#######################################################
# Configuration of logging ############################
#######################################################
logging.basicConfig(filename='Biologic_CAM_creator_logging.log', filemode='a', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# create console handler and set level to debug
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# add formatter to console_handler
console_handler.setFormatter(formatter)

# add console_handler to logger
logging.getLogger('').addHandler(console_handler)
#####################################################
#####################################################
#####################################################


# Directory where the configuration file is located
base_directory = r'C:\Users\AndresMolinaOsorio\PycharmProjects\045_Biologic_Schedule_Creator'

#Load the configuration file
config_data = load_config(base_directory,'config.yaml')

# Check if the config_data is None, meaning there was an error
# in loading the configuration file loading
if config_data is None:
    sys.exit(1)

# Path where the protocol template is located
template_file_path = os.path.join(config_data['path_MPS_Template'], config_data['file_MPS'])

if not os.path.isfile(template_file_path):
    logging.error(f"Template file not found in {config_data['path_MPS_Template']}")
    sys.exit(1)
else:
    create_schedule_files(config_data)
    input("Press Enter to exit.")
    sys.exit(1)