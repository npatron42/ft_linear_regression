# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    train.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: npatron <npatron@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/23 19:06:01 by npatron           #+#    #+#              #
#    Updated: 2025/09/10 13:00:51 by npatron          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from services.linear_regression_service import LinearRegressionService

import os
import sys

def main():
    try:
        if (len(sys.argv) != 2):
            raise Exception("[ERROR] You need to use : \npython3 <path_to_train_program> <path_to_csv>")
        linear_regression_model = LinearRegressionService(csv_path=sys.argv[1])
        linear_regression_model.generate()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()