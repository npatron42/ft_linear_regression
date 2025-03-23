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

from utils import utils
import os


class LinearRegressionModel():
    def __init__(self, csv_path):
        x, y = utils.fill_x_and_y_from_dataset(csv_path)
        m = len(x)
        alpha = None # Learning rate
        return
    
    def cost_function():
        return



    def generate():
        return



def main():
    model = LinearRegressionModel()
    model.generate()
    return

main()