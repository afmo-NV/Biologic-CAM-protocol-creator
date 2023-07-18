# Biologic-CAM-protocol-creator
Python project for automatically generating multiple Biologic protocol files for formation tests @ C/10

Biologic Cyclers are used in CAM-NV to run different protocols (mainly) in coin cells. 
Every experiment in a Biologic cycler requires a .mps file that contains multiple settings such as charge/discharge current or voltage limits. 
Since the .mps file is a text file, the Biologic-CAM-protocol-creator is a project that aims to automatize the creation of these files by
modifying multiple lines in a template  mps file ('Formation_Standard_Protocol-C-N.mps'), with specific information from the sample. These 
information includes mass of the cathode active material in each coin cell and specific capacity of the sample. 

With the information entered by the user, the electrical current used to charge and discharge the coin cells is automatically calculated. 

The template file must be created initially using the Biologic software BT-Lab. For this project, the template was designed to run one Constant Current Constant 
Voltage (CCCV) charge discharge cycle at a c-rate of C/10. 

The project is divided into the following files:

user_input_functions.py: Contains functions that prompts the user to input the following information about the sampple:
                        - Sample ID
                        - Number of coin cells per sample ID
                        - Mass of the Cathode active material in each coin cell 
                        - Specific capacity of the sample
                        

config_loader.py: Contains the function load_config that loads the information contained in a yaml configuration file.


file_generator.py: Contains the create_schedule_files function that creates and exports the protocol files based on the information
                  saved in the configuration file.


main.py: Calls all the functions and sets up the logging configuration.

# **Example:**
5 coin cells are tested for the sample 'cam-active-material-14585'. 
The user will be prompted to enter the following info:
-sample ID: cam-active-material-14585
-number of coin cells: 5
-mass of the active material in each electrode in grams: 0.01502,0.01485,0.01505,0.01495,0.01520
-specific capacity of the sample in mAh.g-1: 210

With this information, 5 mps files will be created in the folder 'cam-active-material-14585' with the following filenames:
Formation-Protocol_cam-active-material-14585-CC-1.mps
Formation-Protocol_cam-active-material-14585-CC-2.mps
Formation-Protocol_cam-active-material-14585-CC-3.mps
Formation-Protocol_cam-active-material-14585-CC-4.mps
Formation-Protocol_cam-active-material-14585-CC-5.mps

In addition, the file 'cam-active-material-14585-Filenames.txt' will be created. This file contains the systematic names for each experiment
that should be entered in the BT-Lab software when starting each coin cell. For this example, the file will contain the following filenames:
cam-active-material-14585-CC-1_0.01502_Mass
cam-active-material-14585-CC-1_0.01485_Mass
cam-active-material-14585-CC-1_0.01505_Mass
cam-active-material-14585-CC-1_0.01495_Mass
cam-active-material-14585-CC-1_0.01520_Mass

The previous sytematic filenames are useful for performing calculations with the results from each test. For example, by including the mass in each filename,
the experimental specific capacity calculation can also be automated once each experiment is finished. 

