# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    linear_regression_accuracy.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: npatron <npatron@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/12 09:35:38 by npatron           #+#    #+#              #
#    Updated: 2025/09/12 14:22:09 by npatron          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from typing import List
from classes.utils.linear_regression_utils import LinearRegressionUtils

class LinearRegressionAccuracy():
    def __init__(self, X: List, y: List, m: int, theta0: float, theta1: float):
        self.X = X
        self.y = y
        self.m = m
        self.theta0 = theta0
        self.theta1 = theta1
        self.linear_regression_utils = LinearRegressionUtils()
        
        self.squared_error = 0.0
        self.mean_squared_error = 0.0
        self.root_mean_squared_error = 0.0
        self.absolute_error = 0.0
        self.mean_absolute_percentage_error = 0.0
        self.mean_absolute_error = 0.0

    def compute(self) -> None:
        self._compute_squared_error()
        self._compute_mean_squared_error()
        self._compute_root_mean_squared_error()
        self._compute_absolute_error()
        self._compute_mean_absolute_percentage_error()
        self._compute_mean_absolute_error()
        print(self.__dict__)
        self._save()
        return
    
    def _save(self):
        f = open("src/data/values/accuracy.txt", mode="w")
        f.write("------------------------- Squared ----------------------------\n\n")
        f.write(f"[SE] squared Error : {self.squared_error}\n")
        f.write(f"[MSE] Mean Squared Error : {self.mean_squared_error}\n")
        f.write(f"[RMSE] Root Mean Squared Error : {self.root_mean_squared_error}\n")
        f.write("------------------------- Absolute ----------------------------\n\n")
        f.write(f"[AE] Absolute Error : {self.absolute_error}\n")
        f.write(f"[MAPE] Mean Absolute Percentage Error : {self.mean_absolute_percentage_error}\n")
        f.write(f"[MAE] Mean Absolute Error : {self.mean_absolute_error}\n")
        return

    def _compute_squared_error(self):
        x_computed = self.linear_regression_utils.compute_x(X=self.X,
                                                            theta0=self.theta0,
                                                            theta1=self.theta1)
        self.squared_error = 0
        for i in range(self.m):
            self.squared_error += ((self.y[i] - x_computed[i]) ** 2)
        return
    
    def _compute_mean_squared_error(self):
        self.mean_squared_error = (self.squared_error / self.m)
        return
    
    def _compute_root_mean_squared_error(self):
        self.root_mean_squared_error = self.mean_squared_error ** 0.5
        return
    
    def _compute_absolute_error(self):
        x_computed = self.linear_regression_utils.compute_x(self.X, self.theta0, self.theta1)
        for i in range(self.m):
            self.absolute_error += (abs(self.y[i] - x_computed[i]))
        return
    
    def _compute_mean_absolute_percentage_error(self):
        x_computed = self.linear_regression_utils.compute_x(self.X, self.theta0, self.theta1)
        mape_sum = 0.0
        for i in range(self.m):
            if self.y[i] != 0:
                mape_sum += abs((self.y[i] - x_computed[i]) / self.y[i])
        self.mean_absolute_percentage_error = (mape_sum / self.m) * 100
        return
    
    def _compute_mean_absolute_error(self):
        self.mean_absolute_error = self.absolute_error / self.m
        return
    
    
    

