from config.config import *
import os
import matplotlib.pyplot as plt

if file_saving_enabled == True:
    try:
        os.makedirs('saved', exist_ok=True)
    except PermissionError:
        print('ERROR: Insufficient permissions, file saving disabled. Please run as adminstrator.')
        file_saving_enabled = False

def save_plot(target_star, file_suffix):
    """
    Streamlined way to save matplotlib plots to /saved_data
    """
    if file_saving_enabled == True:
        directory_name = 'saved/saved_data/' + target_star
        file_name = directory_name + '/' + target_star + file_suffix
        os.makedirs(directory_name, exist_ok=True)
        plt.savefig(file_name)
        print(f'Saving {target_star}{file_suffix}...')
        return 'saved'
    else:
        return 'saving is disabled'