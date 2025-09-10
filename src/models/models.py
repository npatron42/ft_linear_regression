# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    models.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: npatron <npatron@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/10 13:14:03 by npatron           #+#    #+#              #
#    Updated: 2025/09/10 15:01:37 by npatron          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from typing import List
from pydantic import BaseModel

class ParseCSVDatasetResponse(BaseModel):
    X: List
    y: List
    x_label: str
    y_label: str

class GenerateComputedValuesResponse(BaseModel):
    X: List
    y: List
    standardized_x: List
    x_sum: int
    m: int
    mean: float
    standard_deviation: float
    
class GenerateResponse(BaseModel):
    success: bool
