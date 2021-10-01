""" Bubble sort without using the lib function.
        Takes filename as argument.
        Sorts the numbers in the file by extracting the data in the file and cleaning.
    """


import re
import os
pattern = re.compile("^(\-?\d+\s*)+$")

