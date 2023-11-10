import logging
import os
import datetime


def setup_logging(base_directory):
    """
    This function sets up the logging configuration.
    :param base_directory: string, the base directory of the program.
    :return: None
    """

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
