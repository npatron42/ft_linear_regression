# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    predict.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: npatron <npatron@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/10 10:52:26 by npatron           #+#    #+#              #
#    Updated: 2025/09/11 17:58:03 by npatron          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class PredictCarPriceByMileage:
    theta0 = 0
    theta1 = 0
    
    def __init__(self, mileage: int):
        self.mileage = mileage
        self._fill_thetas()
    
    def estimate_price(self) -> float | int:
        return (self.theta0 + (self.theta1 * self.mileage))
        
    def _fill_thetas(self) -> None:
        f = open("src/data/values/values.txt", "r")
        values = f.read().split(sep=",")
        self.theta0 = float(values[0])
        self.theta1 = float(values[1])
        
    
def main():
    try:
        mileage = float(input("Give me a mileage : "))
        if (mileage < 0):
            print("Impossible.\n Mileages inputs must be >= 0")
            return
        predict_car_price_by_mileage = PredictCarPriceByMileage(mileage=mileage)
        price = predict_car_price_by_mileage.estimate_price()
        if price < 0:
            price = 0
        print(f"Your price: {price}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()