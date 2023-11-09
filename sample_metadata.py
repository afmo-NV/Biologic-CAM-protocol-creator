import pandas as pd
import os
import glob
import logging


def rename_latest_coin_cell_records_file(download_dir):
    """ This function removes duplicated Coin_Cell_QC_Data_V1_2022.xlsx files.
     Duplicates need to be removed in order to read information from the most updated
     records file """

    logging.debug('SAMPLE_METADATA. Searching for Coin_Cell_QC_Data_V1_2022 files')
    # Define the desired name for the file
    desired_file = os.path.join(download_dir, 'Coin_Cell_QC_Data_V1_2022.xlsx')

    # Get list of all 'Coin_Cell_QC_Data_V1_2022.xlsx' files
    files = glob.glob(os.path.join(download_dir, 'Coin_Cell_QC_Data_V1_2022*.xlsx'))

    logging.debug(f'SAMPLE_METADATA. Found {len(files)} Coin Cell Record files in the folder')

    if len(files) == 0:
        logging.debug(f'SAMPLE_METADATA. No Coin Cell Records file found in {download_dir}. Please download a copy of the file')
        return None
    else:
        pass

    # If there are more than 1 files
    if len(files) > 1:
        # Find the most recently downloaded file
        latest_file = max(files, key=os.path.getctime)

        logging.debug(f'SAMPLE_METADATA. {latest_file} found as the latest Coin Cell Records file')

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

        logging.debug('SAMPLE_METADATA. Coin Cell Records files renamed')

    else:
        logging.debug('SAMPLE_METADATA. Only one Coin Cell Records file found, no renaming done')


def get_sample_info(file_path, sample_id):
    """
    This function collects the active material weight for the coin cells tested
        from the Coin_Cell_QC_Data_V1_2022.xlsx file

    Args:
        file_path (str): path where the Excel coin cell records file is
        sample_id (str): sample ID in the Excel coin cell records file

    Returns:
        sample_names_list (list): list that contains all sample names in a sample ID
        repetition_number_listv (list): list repetition number in a sample ID
        mass_active_material_list (list): list of active material weight in a sample ID

    """

    # Columns to import from the Excel coin cell records
    cols_to_import = ['Sample Ticket ID', 'Sample name', ' Repetition #', 'Active material weight (g)']
    logging.debug('SAMPLE_METADATA. Extracting information about the sample from Coin Cell Records file')

    try:
        # Load the data from the spreadsheet
        data = pd.read_excel(file_path, sheet_name='CCCV_Data', usecols=cols_to_import)

    except PermissionError:
        logging.error("SAMPLE_METADATA. Unable to read the Coin Cell Records file. Please close the file if it is open and try again.")
        return None

    except FileNotFoundError:
        logging.error(f"SAMPLE_METADATA. Coin Cell Records file not found: {file_path}. Please download a copy of the file")
        return None

    # Filter the data for the given sample ID
    sample_data = data[data['Sample Ticket ID'] == sample_id]

    # Check if sample_data is empty
    if sample_data.empty:
        logging.error("SAMPLE_METADATA. No data found for the provided sample ID.")
        return None

    # Get sample names
    sample_names_series = sample_data['Sample name']
    # This line replaces spaces and underscores with dashes
    sample_names_series = sample_names_series.apply(lambda x: x.replace(' ', '-').replace('_', '-'))
    sample_names_list = sample_names_series.to_list()

    # Get repetition number
    repetition_number_series = sample_data[' Repetition #']
    repetition_number_list = repetition_number_series.to_list()

    # Get mass of active material rounded to 5 decimals
    mass_active_material_series = sample_data['Active material weight (g)']
    mass_active_material_list = mass_active_material_series.round(5).to_list()

    # Check if the mass_active_material_list is empty or contains negative values
    if not mass_active_material_list or any(value < 0 for value in mass_active_material_list):
        logging.debug('SAMPLE_METADATA. mass_active_material_list is empty or contains negative values')
        return None

    logging.debug('SAMPLE_METADATA. Information about the sample extracted sucessfully')
    # return cc_number, mass_active_material_list, sample_names_list
    return sample_names_list, repetition_number_list, mass_active_material_list