# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    linear_regression_model.py                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: npatron <npatron@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/10 11:29:50 by npatron           #+#    #+#              #
#    Updated: 2025/09/12 13:22:28 by npatron          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from typing import List

from classes.utils.linear_regression_utils import LinearRegressionUtils
from models.models import GenerateResponse

class LinearRegressionModel():
    X: List[int] = []
    y: List[int] = []
    
    x_label: str
    y_label: str
    
    cost: float
    learning_rate: float = 0.01
    mean_absolute_error: float
    m: int
    x_sum: int
    mean: float
    standard_deviation: float
    standardized_x: List[float]
    
    def __init__(self, csv_path: str):
        self.linear_regression_utils = LinearRegressionUtils()
        self.theta0 = 0
        self.theta1 = 0
        self.csv_path = csv_path

    def generate(self) -> GenerateResponse:
        computed_values = self.linear_regression_utils.generate_computed_values(csv_path=self.csv_path)
        self.__dict__.update(computed_values.model_dump())
        cost = self._compute_cost()
        while (abs(cost) >= 0.0000000001):
            tmp_theta0_normalized = self.learning_rate * sum(self._estimate_price(self.standardized_x[i]) - self.y[i] for i in range(self.m))
            tmp_theta1_normalized = self.learning_rate * sum((self._estimate_price(self.standardized_x[i]) - self.y[i]) * self.standardized_x[i] for i in range(self.m))            
            self.theta0 -= tmp_theta0_normalized
            self.theta1 -= tmp_theta1_normalized
            
            theta1_prime = self.theta1
            theta0_prime = self.theta0
            cost = self._compute_cost()
            
        self._denormalize_thetas(theta0_prime=theta0_prime, theta1_prime=theta1_prime)
        self._save_labels_and_thetas()
        return GenerateResponse(success=True)

    def _estimate_price(self, mileage: int) -> float:
        return (self.theta0 + (self.theta1 * mileage))

    def _save_labels_and_thetas(self):
        f = open("src/data/values/values.txt", mode="w")
        f.write(f"{self.x_label},{self.y_label}\n")
        f.write(f"{self.theta0},{self.theta1}")
        return

    def _denormalize_thetas(self, theta0_prime, theta1_prime):
        self.theta1 = theta1_prime / self.standard_deviation
        self.theta0 = theta0_prime - (theta1_prime * self.mean / self.standard_deviation)   

    def _compute_cost(self) -> float:
        cost = 0
        for i in range(self.m):
            cost += self._estimate_price(mileage=self.standardized_x[i]) - self.y[i]
        cost **= 2
        cost /= (self.m * 2)
        cost **= 0.5
        return cost

    

