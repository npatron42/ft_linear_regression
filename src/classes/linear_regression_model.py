# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    linear_regression_model.py                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: npatron <npatron@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/10 11:29:50 by npatron           #+#    #+#              #
#    Updated: 2025/09/11 11:49:06 by npatron          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils.linear_regression_utils import LinearRegressionUtils
from models.models import GenerateResponse, Stats
from typing import List

class LinearRegressionModel():
    X: List[int] = []
    y: List[int] = []
    
    x_label: str
    y_label: str
    
    stats: Stats
    
    thetas: tuple[float, float]
    learning_rate: float
    mean_absolute_error: float
    
    def __init__(self, csv_path: str):
        self.linear_regression_utils = LinearRegressionUtils(csv_path=csv_path)

    ## Public implementation ##

    def generate(self) -> GenerateResponse:
        try:
            computed_values = self.linear_regression_utils.generate_computed_values()
            self.__dict__.update(computed_values.model_dump())
            
            return GenerateResponse(success=True)
        except Exception as e:
            return GenerateResponse(success=False)

    ## Private implementation ##

    def _compute_cost(self) -> None:
        
        return

