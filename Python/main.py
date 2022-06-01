from cmath import acos
from car import Car
from account import Account

if __name__ == "__main__":
    car = Car("AFS342", Account("Manolo Tercero", "WDf56"))
    print(vars(car))
    print(vars(car.driver))