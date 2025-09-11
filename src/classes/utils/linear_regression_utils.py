# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    linear_regression_utils.py                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: npatron <npatron@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/10 09:58:01 by npatron           #+#    #+#              #
#    Updated: 2025/09/11 16:21:38 by npatron          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import csv
from typing import List

from models.models import ComputedValues, XAndYSetGenerated

class LinearRegressionUtils():
    def __init__(self, csv_path):
        self.csv_path = csv_path
        
    ## Public implementation ##

    def fill_x_and_y_from_dataset(self) -> XAndYSetGenerated | None:
        try:
            X, y = [], []
            with open(self.csv_path, newline='') as f:
                reader = csv.reader(f)
                
                # Récupère la première ligne comme header
                header = next(reader, None)
                if header is None or len(header) < 2:
                    raise ValueError("SV file is empty or bad")
                
                x_label, y_label = header[0], header[1]

                for row in reader:
                    if len(row) < 2:
                        continue
                    X.append(int(row[0]))
                    y.append(int(row[1]))

            return XAndYSetGenerated(X=X, y=y, x_label=x_label, y_label=y_label)
        except (csv.Error, ValueError) as e:
            print(f"[ERROR] Error during 'fill_x_and_y_from_dataset': {e}")
            return None
    
    def generate_computed_values(self) -> ComputedValues:
            generate_computed_values_response = self.fill_x_and_y_from_dataset()
   
            X = generate_computed_values_response.X
            y = generate_computed_values_response.y
            x_sum = self._compute_sum(list=X)
            m = len(X)
            mean = x_sum / m
            standard_deviation = self._compute_standard_deviation(X=X, mean=mean, m=m)
            standardized_values = self._standardize_values(X=X, mean=mean, standard_deviation=standard_deviation)
            return ComputedValues(
                X=X,
                y=y,
                x_sum=x_sum,
                m=m,
                mean=mean,
                standard_deviation=standard_deviation,
                standardized_x=standardized_values
            )

    ## Private implementation 

    def _compute_sum(self, list: List) -> int:
        x_sum = 0
        for element in list:
            x_sum += int(element)
        return x_sum

    def _compute_standard_deviation(self, X: List, mean: float, m: int) -> float:
        standard_deviation: float = sum((int(x) - mean) ** 2 for x in X) / m
        standard_deviation **= 0.5
        return standard_deviation

    def _standardize_values(self, X: List, mean: float, standard_deviation: float) -> List[int]:
        standardized_values: List[float] = []
        for x in X:
            x_p = (x - mean) / standard_deviation
            standardized_values.append(x_p)
        return standardized_values