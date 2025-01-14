"""
script to start the toolbox.
"""
import os
import sys
from src import executor
path = os.getcwd() # gets the current working directory
folder_name = os.path.basename(path) # gets the name of the current folder
sys.path.append(path) # add the whole directory to the path

# summarize all input setup in a dictionary
# available pre-defined scenarios: pv_gen, wind_gen, conventional_pp_gen, load, trafo_cap, line_cap, storage
input_setup = {
    'topology_path': './example/kerber_landnetz_fl2/topology.xlsx',
    'topology_name': 'Network',
    # (scenario name, scenario path, name of used pre-defined scenario, pre-defined scenario parameter)
    'scenario_setup': [('basic', './example/kerber_landnetz_fl2/scenarios/basic.xlsx', 'load', 0.9)]
                        # ('pv', './example/kerber_landnetz_fl2/scenarios/pv.xlsx', 'pv_gen', 1.5),
                        # ('pv_storage', './example/kerber_landnetz_fl2/scenarios/pv_storage.xlsx', '', 0),
                        # ('opf', './example/kerber_landnetz_fl2/scenarios/opf.xlsx', '', 0)]
    }

# summarize all output setups to a dictionary
output_setup = {
    # the Excel output will have topology and scenario name e.g. Results_Network01_Scenario01.xlsm
    'output_path': './result/',
    # all the scenarios will have the same plotting setings, however, time series scenarios will not be plotted
    'plot': { 'topology': True, # a plot with the network topology will be created and save as an image (just once)
              'interactive network': True, # a interactive map will be open in the default internet browser, and saved in the output_path
              'interactive heat map network': True # the interative map will include loading levels
            }
    }
# execute the toolbox
executor.executor(input_setup, output_setup)

