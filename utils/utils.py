# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    utils.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: npatron <npatron@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/23 19:06:13 by npatron           #+#    #+#              #
#    Updated: 2025/03/23 20:03:28 by npatron          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import csv

def fill_x_and_y_from_dataset(path_to_csv) -> None:

    x = []
    y = []

    with open(path_to_csv, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    for element in data:
        x.append(element[0])
        y.append(element[1])

    return x, y
