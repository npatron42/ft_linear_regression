# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    train.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: npatron <npatron@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/23 19:06:01 by npatron           #+#    #+#              #
#    Updated: 2025/03/23 20:14:35 by npatron          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils import utils

import os
import sys

# Standard deviation --> 


class LinearRegressionModel():
    def __init__(self, csv_path):
        x, y = utils.fill_x_and_y_from_dataset(csv_path)
        m = len(x)
        alpha = None # Learning rate
        return
    
    def calculate

    def normalized_values(self):
        return

    def cost_function(self):
        return



    def generate(self):
        return


def main():
    
    if (len(sys.argv) != 2):
        print("Error.\npython3 train.py <path_to_csv>")
    model = LinearRegressionModel(csv_path=sys.argv[1])
    model.generate()
    return

main()