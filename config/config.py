version = '2.1.4'
# ENABLE/DISABLE FUNCTIONALITY BELOW
masking_enabled = False # enable/disable cadence masking
sound_enabled = False # enable/disable sound effects
file_saving_enabled = True # recommended enabled (saves plots to saved_data/{starsystem})
attempt_wikipedia_pull = True
# DEFAULTS
periodogram_lower_bound_default = 0.5
periodogram_upper_bound_default = 30
selected_bins = 700 # default: 700
rounding_decimal_places = 4 # decimal places to round to
file_saving_format = 'svg' # supports png, jpeg, pdf, svg (recommended)
# TELESCOPE DATA
selected_telescope = 'Kepler' # options are Kepler, K2, Tess (recommend Kepler)
selected_cadence = 'long' # long or short
# commonly used print statements for easy editing
prompt_periodogram_upper_bound = f'Please input periodogram upper bound (if blank, default {periodogram_upper_bound_default}): '
prompt_periodogram_lower_bound = f'Please input periodogram lower bound (if blank, default {periodogram_lower_bound_default}): '
prompt_input_not_recognized = 'Input not recognized. Please try again.'
# do not edit below
import string
user_flags = ['masking_enabled', masking_enabled, 'sound_enabled', sound_enabled, 'file_saving_enabled', file_saving_enabled, 'attempt_wikipedia_pull', attempt_wikipedia_pull] # add any user vars to this list. First name in str, then variable itself
list_of_tools = ['Star Pixelfile Retrieval', 'Star Light Curve Analysis', 'Exoplanet Radius Calculator', 'Star Habitable Zone Calculator', 'Stefan-Boltzmann Star Temperature Calculator', 'Kepler Orbital Radius Calculator', 'Inverse-Square Exoplanet Stellar Energy Calculator', 'Blackbody Exoplanet Temperature Calculator', 'Generate Full Report']
alphabet_list = list(string.ascii_uppercase) # list of every individual letter from the alphabet, uppercase
list_of_functions_index = []
