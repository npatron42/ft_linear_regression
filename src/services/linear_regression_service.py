# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    linear_regression_service.py                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: npatron <npatron@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/10 11:29:50 by npatron           #+#    #+#              #
#    Updated: 2025/09/10 15:02:15 by npatron          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils.linear_regression_utils import LinearRegressionUtils
from models.models import GenerateResponse
from typing import List

class LinearRegressionService():
    def __init__(self, csv_path: str):
        self.linear_regression_utils = LinearRegressionUtils(csv_path=csv_path)
        
        self.X = []
        self.y = []
        
        self.x_label = "None"
        self.y_label = "None"

        self.m = 0
        self.x_sum = 0
        self.mean = 0
        
        self.standardized_x = []
        self.standard_deviation = 0
        
        self.learning_rate = 0
        return

    ## Public implementation

    def generate(self) -> GenerateResponse:
        try:
            computed_values = self.linear_regression_utils.generate_computed_values()
            self.__dict__.update(computed_values.model_dump())
            self._print_values()
            return GenerateResponse(success=True)
        except Exception as e:
            return GenerateResponse(success=False)
        return

    ## Private implementation

    def _print_values(self):
        print("[DEBUG] x :", self.X)
        print("[DEBUG] y :", self.y)
        print("[DEBUG] standardized_x :", self.standardized_x)
        print("[DEBUG] x_sum :", self.x_sum)
        print("[DEBUG] m :", self.m)
        print("[DEBUG] learning_rate :", self.learning_rate)
        print("[DEBUG] standard_deviation :", self.standard_deviation)
        print("[DEBUG] mean :", self.mean)




    def _compute_cost(self) -> None:
        return

