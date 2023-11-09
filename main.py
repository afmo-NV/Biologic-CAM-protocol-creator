from file_generator import *
from config_loader import load_config
import sys
from sample_metadata import *
import warnings
import datetime

# Directory where the configuration file is located
base_directory = '/Users/andresmolina/Documents/Python_Projects/06_CAM_Biologic_Protocol_Creator'

#######################################################
# Configuration of logging ############################
#######################################################
# Specify the log directory folder, if there is no folder, create it.
log_dir = os.path.join(base_directory, 'logs')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
# Specify the timestamp
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

# Specify the log file name
log_filename = f'Biologic_CAM_creator_logging_{timestamp}.log'

# create logger
logging.basicConfig(filename=os.path.join(log_dir, log_filename), filemode='w', level=logging.DEBUG,
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

# Get sample ID
sample_ID = get_sample_id()

logging.debug(f'MAIN. BIOLOGIC CAM PROTOCOL GENERATOR STARTED FOR SAMPLE {sample_ID}')

# Filter out the specific warning
warnings.filterwarnings("ignore", message="Data Validation extension is not supported and will be removed")

# When finding multiple Coin Cell Record files in the local PC, delete the old versions
# and keep the latest and most updated version.
rename_latest_coin_cell_records_file(
                                '/Users/andresmolina/Documents/Python_Projects/06_CAM_Biologic_Protocol_Creator/data')

# Path to the coin cell records
coin_cell_records_path = ('/Users/andresmolina/Documents/Python_Projects/06_CAM_Biologic_Protocol_Creator'
                          '/data/Coin_Cell_QC_Data_V1_2022.xlsx')

# Get number of coin cells per sample and mass of electrodes
# cc_number, mass_electrodes = get_sample_info(coin_cell_records_path, sample_ID)
sample_names_list, repetition_number_list, mass_active_material_list = get_sample_info(coin_cell_records_path,
                                                                                       sample_ID)

# Get the protocol type (Formation (F), Formation + Capacity Check (FC)
# or Cycle Life (CL))
protocol_type = get_cycling_protocol()

# Load the configuration file
config_data = load_config(base_directory, 'config.yaml', protocol_type)

# Check if the config_data is None, meaning there was an error
# in loading the configuration file loading
if config_data is None:
    sys.exit(1)

# Path where the protocol template is located
template_file_path = os.path.join(config_data['path_MPS_Template'], config_data['file_MPS'])

if not os.path.isfile(template_file_path):
    logging.error(f"SAMPLE_METADATA. Template file not found in {config_data['path_MPS_Template']}")
    sys.exit(1)
else:
    if protocol_type == 'F':
        create_formation_schedule_files(config_data, sample_ID, sample_names_list, repetition_number_list,
                                        mass_active_material_list)
        input("Press Enter to exit.")
        sys.exit(1)
    elif protocol_type == 'CL':
        create_cycle_life_schedule_files(config_data, sample_ID, sample_names_list, repetition_number_list,
                                         mass_active_material_list)
        input("Press Enter to exit.")
        sys.exit(1)
    elif protocol_type == 'FC':
        create_formation_capacity_check_schedule_files(config_data, sample_ID, sample_names_list,
                                                       repetition_number_list, mass_active_material_list)
        input("Press Enter to exit.")
        sys.exit(1)
