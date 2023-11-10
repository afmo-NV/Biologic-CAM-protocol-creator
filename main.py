from file_generator import *from config_loader import load_protocol_configfrom path_config_loader import load_path_configimport sysfrom sample_metadata import *import warningsfrom logger_config import setup_logging# Directory where the configuration file is locatedbase_directory = os.path.dirname(os.path.abspath(__file__))# Setup the logging configurationsetup_logging(base_directory)# Load the path configuration filepath_config_data = load_path_config(base_directory, 'directory_configuration_file.yaml')# Get sample IDsample_ID = get_sample_id()logging.debug(f'MAIN. BIOLOGIC CAM PROTOCOL GENERATOR STARTED FOR SAMPLE {sample_ID}')# Filter out the specific warningwarnings.filterwarnings("ignore", message="Data Validation extension is not supported and will be removed")# Rename the latest coin cell records file when multiple coin cell files are foundrename_latest_coin_cell_records_file(path_config_data['path_Coin_Cell_Records_File'],                                     path_config_data['cc_records_filename'])# Path to the coin cell recordscoin_cell_records_path = os.path.join(path_config_data['path_Coin_Cell_Records_File'],                                      path_config_data['cc_records_filename'])# Get the sample names, repetition numbers and mass of active materialsample_names_list, repetition_number_list, mass_active_material_list = get_sample_info(coin_cell_records_path,                                                                                       sample_ID)# Get the protocol type (Formation (F), Formation + Capacity Check (FC), Cycle Life (CL) or DCIRprotocol_type = get_cycling_protocol()# Load the configuration file based on the protocol typeconfig_data = load_protocol_config(base_directory, 'config.yaml', protocol_type)# Check if the config_data is None, meaning there was an error in loading the configuration file loadingif config_data is None:    sys.exit(1)# Path where the protocol template is locatedtemplate_file_path = os.path.join(path_config_data['path_MPS_Template'], config_data['file_MPS'])if not os.path.isfile(template_file_path):    logging.error(f"SAMPLE_METADATA. Template file not found in {config_data['path_MPS_Template']}")    sys.exit(1)else:    if protocol_type == 'F':        create_formation_schedule_files(config_data,                                        path_config_data,                                        sample_ID,                                        sample_names_list,                                        repetition_number_list,                                        mass_active_material_list)        input("Press Enter to exit.")        sys.exit(1)    elif protocol_type == 'CL':        create_cycle_life_schedule_files(config_data,                                         path_config_data,                                         sample_ID,                                         sample_names_list,                                         repetition_number_list,                                         mass_active_material_list)        input("Press Enter to exit.")        sys.exit(1)    elif protocol_type == 'FC':        create_formation_capacity_check_schedule_files(config_data,                                                       path_config_data,                                                       sample_ID,                                                       sample_names_list,                                                       repetition_number_list,                                                       mass_active_material_list)        input("Press Enter to exit.")        sys.exit(1)