# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    predict.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: npatron <npatron@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/10 10:52:26 by npatron           #+#    #+#              #
#    Updated: 2025/09/12 13:32:48 by npatron          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Predict:
    x_label = "None"
    y_label = "None"
    theta0 = 0
    theta1 = 0
    
    def __init__(self):
        self._fill_labels_and_thetas()
    
    def work(self, x: float | int) -> float | int:
        return (self.theta0 + (self.theta1 * x))
        
    def _fill_labels_and_thetas(self) -> None:
        f = open("src/data/values/values.txt", "r")
        values = f.read().split(sep="\n")

        labels = values[0].split(sep=",")
        thetas = values[1].split(sep=",")

        self.x_label = labels[0]
        self.y_label = labels[1]           
        self.theta0 = float(thetas[0])
        self.theta1 = float(thetas[1])
        

def main():
    try:
        predict = Predict()
        x = float(input(f"Enter a {predict.x_label} : "))
        if (x < 0):
            return
        predicted_value = predict.work(x=x)
        if predicted_value < 0:
            predicted_value = 0
        print(f"Your {predict.y_label}: {predicted_value}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()