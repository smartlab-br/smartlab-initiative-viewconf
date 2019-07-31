import pandas as pd
import os

# Read the dictionary as a pandas dataset
dict_dataset = []

# Traverse the folder recursivelly, finding yaml templates to translate
path = "."
for root, d_names, f_names in os.walk("."):
    for f_name in f_names:
        if ".yaml" not in f_names: continue # Skips if not a YAML template
        # Translate each yaml using the dictionary
        template = open(f_name, 'r')
        # TODO Get the variables(row) from the template as an array

        for language in dict_dataset.column: # Creates a file for each language
            target = open(os.path.join('..', language, f_name), 'w')
            # TODO Get the values of the array of rows using the language definition
            # TODO Replace the values using the array
            target.write
        