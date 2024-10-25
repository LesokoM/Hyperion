
city_flight = {
    1:("Boksburg", 400),
    2:["Cape Town", 2500],
    3:["Durban", 1800],
    4: ["Bloemfontein", 2000],
    5: ["East London", 2200],
    6: ["Kimberley", 2100],
    7: ["Nelspruit", 1900],
    8 :["Polokowane", 1800]
    }

def readable():{
    print("----------------------------------------------------------------------")
}

def hotel_cost(num_nights):
    price_per_night = 800
    hotel_stay = num_nights*price_per_night
    return hotel_stay

def plane_cost(city_flight):

    for key, value in city_flight.items():
        print(f" {key}:City {value[0]}")
    readable()
    user_city = int(input("Please select which city you will be traveling to (ie 1,2 or 8): "))

    return city_flight[user_city][1]*2

def car_rental(rental_days):
    price_per_day_car = 450

    total_car_rental = 450 *rental_days

    return total_car_rental




def holiday_cost(hotel_cost,plane_cost,car_rental):
    readable()
    print(f"The total hotel stay costs R{hotel_cost}")
    print(f"The total cost of the flight is R{plane_cost}")
    print(f"The total cost to rent the car is R{car_rental}")

    readable()

    print(f"The total cost of the entire trip is: R{hotel_cost+plane_cost+car_rental} ")
    readable()


readable()
num_nights = int(input("How many nights will you be sleeping at the hotel?: "))

rental_days = int(input("How many days do you want to rent the car?: "))
readable()
hotel_costings = hotel_cost(num_nights)
plane_costings= plane_cost(city_flight)
car_rental_costings = car_rental(rental_days)

holiday_cost(hotel_costings, plane_costings, car_rental_costings)