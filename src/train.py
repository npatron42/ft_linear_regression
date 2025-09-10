# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    train.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: npatron <npatron@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/23 19:06:01 by npatron           #+#    #+#              #
#    Updated: 2025/09/10 11:26:01 by npatron          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils.linear_regression_utils import LinearRegressionUtils

import os
import sys

class LinearRegressionModel():
    def __init__(self, csv_path: str):
        self.linear_regression_utils = LinearRegressionUtils(csv_path=csv_path)
        self.x = []
        self.y = []
        self.m = 0
        self.learning_rate = 0

        self.linear_regression_utils.fill_x_and_y_from_dataset(x=self.x, y=self.y)
        self.m = len(self.x)
        return
    
    def normalized_values(self):
        return

    def cost_function(self):
        return

    def generate(self):
        return


def main():
    try:
        if (len(sys.argv) != 2):
            raise Exception("[ERROR] You need to use : \npython3 <path_to_train_program> <path_to_csv>")
        linear_regression_model = LinearRegressionModel(csv_path=sys.argv[1])
        print(linear_regression_model.x, linear_regression_model.y, linear_regression_model.m)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()