# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    linear_regression_vizualisation.py                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: npatron <npatron@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/11 16:40:23 by npatron           #+#    #+#              #
#    Updated: 2025/09/11 17:50:19 by npatron          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from typing import List
import matplotlib.pyplot as plt


class LinearRegressionVizualisation():
    def show(self, X: List, y: List, theta0: float, theta1: float):
        y_computed = self.compute_y(X=X, theta0=theta0, theta1=theta1)
        plt.title("Car mileage vs Price")
        plt.scatter(X, y)
        plt.xlabel("Mileage")
        plt.ylabel("Price")
        
        plt.plot(X, y_computed, color="pink")

        plt.show()
        
    def compute_y(self, X: List, theta0: float, theta1: float) -> List[float]:
        y_computed = []
        for x in X:
            value = (theta1 * x) + theta0
            y_computed.append(value)
        return y_computed
    