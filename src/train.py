# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    train.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: npatron <npatron@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/23 19:06:01 by npatron           #+#    #+#              #
#    Updated: 2025/09/12 13:12:46 by npatron          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import sys

from classes.linear_regression_model import LinearRegressionModel
from classes.linear_regression_accuracy import LinearRegressionAccuracy
from classes.linear_regression_vizualisation import LinearRegressionVizualisation

def main():
    try:
        if (len(sys.argv) != 2):
            raise Exception("[ERROR] You need to use : \npython3 <path_to_train_program> <path_to_csv>")
        linear_regression_model = LinearRegressionModel(csv_path=sys.argv[1])
        
        linear_regression_model.generate()
        linear_regression_accuracy = LinearRegressionAccuracy(X=linear_regression_model.X,
                                                              y=linear_regression_model.y,
                                                              m=linear_regression_model.m,
                                                              theta0=linear_regression_model.theta0,
                                                              theta1=linear_regression_model.theta1)
        
        linear_regression_vizualisation = LinearRegressionVizualisation(X=linear_regression_model.X, 
                                                                        y=linear_regression_model.y,
                                                                        x_label=linear_regression_model.x_label,
                                                                        y_label=linear_regression_model.y_label,
                                                                        theta0=linear_regression_model.theta0,
                                                                        theta1=linear_regression_model.theta1,
                                                                        linear_regression_accuracy=linear_regression_accuracy)
        linear_regression_accuracy.compute()
        linear_regression_vizualisation.show()
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()