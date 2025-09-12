# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    linear_regression_vizualisation.py                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: npatron <npatron@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/11 16:40:23 by npatron           #+#    #+#              #
#    Updated: 2025/09/12 12:18:59 by npatron          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from typing import List
import matplotlib.pyplot as plt

from classes.utils.linear_regression_utils import LinearRegressionUtils
from classes.linear_regression_accuracy import LinearRegressionAccuracy

class LinearRegressionVizualisation():

    def __init__(self, X: List, y: List, theta0: float, theta1: float, linear_regression_accuracy: LinearRegressionAccuracy):
        self.linear_regression_utils = LinearRegressionUtils()
        self.X = X
        self.y = y
        self.theta0 = theta0
        self.theta1 = theta1
        self.linear_regression_accuracy = linear_regression_accuracy

    def show(self):
        fig1, ax1 = plt.subplots()
        ax1.set_title("Car mileage vs Price")
        ax1.scatter(self.X, self.y)
        ax1.set_xlabel("Mileage")
        ax1.set_ylabel("Price")
        y_computed = self.linear_regression_utils.compute_x(X=self.X, theta0=self.theta0, theta1=self.theta1)
        ax1.plot(self.X, y_computed, color="pink")

        fig2, ax2 = plt.subplots()
        ax2.axis('off')
        column_labels = ["Squarred Error", "Mean Squarred Error", "Root mean squared error", "Absolute error", "Mean Absolute Error"]
        table_data = [
            [
                self.linear_regression_accuracy.squared_error, 
                self.linear_regression_accuracy.mean_absolute_error,
                self.linear_regression_accuracy.root_mean_squared_error, 
                self.linear_regression_accuracy.absolute_error, 
                self.linear_regression_accuracy.mean_absolute_error
            ]
        ]
        table = ax2.table(
            cellText=table_data,
            colLabels=column_labels,
            cellLoc='center',
            loc='center'
        )
        table.scale(1, 3)

        plt.show()

    