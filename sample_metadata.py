import pandas as pd
import os
import glob
import logging


def rename_latest_coin_cell_records_file(download_dir):

    """ This function removes duplicated Coin_Cell_QC_Data_V1_2022.xlsx files.
     Duplicates are necessary to remove to read information from the latest and most updated
     records file """

    logging.debug('Searching for Coin_Cell_QC_Data_V1_2022 files')
    # Define the desired name for the file
    desired_file = os.path.join(download_dir, 'Coin_Cell_QC_Data_V1_2022.xlsx')

    # Get list of all 'Coin_Cell_QC_Data_V1_2022.xlsx' files
    files = glob.glob(os.path.join(download_dir, 'Coin_Cell_QC_Data_V1_2022*.xlsx'))

    logging.debug(f'Found {len(files)} Coin Cell Record files in the folder')

    if len(files) == 0:
        logging.debug(f'No Coin Cell Records file found in {download_dir}. Please download a copy of the file')
        return None
    else:
        pass

    # If there are more than 1 files
    if len(files) > 1:
        # Find the most recently downloaded file
        latest_file = max(files, key=os.path.getctime)

        logging.debug(f'{latest_file} found as the latest Coin Cell Records file')

        # Delete all files except the latest
        for file in files:
            if file != latest_file:
                os.remove(file)
                logging.debug(f'{file} deleted')

        # Check if the file already exists, if yes, delete it
        if os.path.exists(desired_file):
            os.remove(desired_file)

        # Rename the latest file to 'test.xlsx'
        os.rename(latest_file, desired_file)

        logging.debug('Coin Cell Records files renamed')

    else:
        logging.debug('Only one Coin Cell Records file found, no renaming done')


def get_sample_info(file_path, sample_id):

    """ This function collects the active material weight for the coin cells tested
        from the Coin_Cell_QC_Data_V1_2022.xlsx file"""

    # Columns to import
    cols_to_import = ['Sample Ticket ID', 'Sample name', 'Active material weight (g)']

    logging.debug('Extracting information about the sample from Coin Cell Records file')

    try:
        # Load the data from the spreadsheet
        data = pd.read_excel(file_path, sheet_name= 'CCCV_Data', usecols= cols_to_import)

    except PermissionError:
        logging.error("Unable to read the Coin Cell Records file. Please close the file if it is open and try again.")
        return None

    except FileNotFoundError:
        logging.error(f"Coin Cell Records file not found: {file_path}. Please download a copy of the file")
        return None

    # Filter the data for the given sample ID
    sample_data = data[data['Sample Ticket ID'] == sample_id]

    # Check if sample_data is empty
    if sample_data.empty:
        logging.error("No data found for the provided sample ID.")
        return None

        # Get number of coin cells
    cc_number = len(sample_data)

    # Get mass of active material rounded to 5 decimals
    mass_active_material_series = sample_data['Active material weight (g)']
    mass_active_material_list = mass_active_material_series.round(5).to_list()

    # Check if the mass_active_material_list is empty or contains negative values
    if not mass_active_material_list or any(value < 0 for value in mass_active_material_list):
        logging.debug('mass_active_material_list is empty or contains negative values')
        return None

    logging.debug('Information about the sample extracted sucessfully')
    return cc_number, mass_active_material_list