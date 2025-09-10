# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    linear_regression_utils.py                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: npatron <npatron@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/10 09:58:01 by npatron           #+#    #+#              #
#    Updated: 2025/09/10 11:19:54 by npatron          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import csv
from typing import List

class LinearRegressionUtils():
    def __init__(self, csv_path):
        self.csv_path = csv_path
        
    ## Public implementation ##

    def fill_x_and_y_from_dataset(self, x: List, y: List) -> None:
        try:
            with open(self.csv_path, newline='') as f:
                reader = csv.reader(f)
                csv_lines = list(reader)

            for line in csv_lines:
                x.append(line[0])
                y.append(line[1])
        except csv.Error as e:
            print(f"[ERROR] Error during 'fill_x_and_y_from_dataset': {e}")
    

    ## Private implementation 

    #TODO
    
    

    