# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    models.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: npatron <npatron@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/10 13:14:03 by npatron           #+#    #+#              #
#    Updated: 2025/09/11 11:36:49 by npatron          ###   ########.fr        #
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

class Stats(BaseModel):
    m: int = None
    x_sum: int = None
    mean: float = None
    standard_deviation: float = None
    standardized_x: List[float] = []

class ComputedValues(BaseModel):
    X: List
    y: List
    stats: Stats
