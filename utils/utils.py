##
# Copyright (c) 2024 - Indigen Solutions
# Authors:
#   - Nicolas Patron <nicolas.patron@indigen.com>
# NOTICE: All information contained herein is, and remains
# the property of Indigen Solutions and its suppliers, if any.
# Dissemination of this information or reproduction of this material
# is strictly forbidden unless prior written permission is obtained
# from Indigen Solutions.
#

import csv
import pandas as pd

def fill_x_and_y_from_dataset(path_to_csv) -> None:

    x = []
    y = []

    with open(path_to_csv, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    for element in data:
        x.append(element[0])
        y.append(element[1])

    return x, y
