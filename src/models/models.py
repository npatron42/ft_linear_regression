# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    models.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: npatron <npatron@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/10 13:14:03 by npatron           #+#    #+#              #
#    Updated: 2025/09/12 13:14:45 by npatron          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from typing import List
from pydantic import BaseModel

class XAndYSetGenerated(BaseModel):
    X: List
    y: List
    x_label: str
    y_label: str

    
class GenerateResponse(BaseModel):
    success: bool

class ComputedValues(BaseModel):
    X: List
    y: List
    x_label: str
    y_label: str
    m: int = None
    x_sum: float = None
    mean: float = None
    standard_deviation: float = None
    standardized_x: List[float] = []
