# function to return the hotel cost
def hotel_cost(nights):
    return nights * 875
# function to return the plane cost
def plane_cost(city):
    ticket = 0
    if city == "1":
        ticket = 750
    elif city == "2":
        ticket = 850
    elif city == "3":
        ticket = 600
    else:
        print('invalid option')

    return ticket
# returns the number of days the car_rental is to be paid 
def car_rental(days):
    return days * 275
# returns the total holiday cost for the night depending on that particular city and the the number of days
def holiday_cost(nights, city, days):
    nights = hotel_cost(nights)
    city = plane_cost(city)
    days = car_rental(days)
    return nights + city + days
#Declares the user to enter the number of nights they will be spending, the destination of their choice so to calculate the number of nights they will be using it and total cost will then be printed at the end
nights =hotel_cost(int(input('How many nights will you be staying? ')))
city = 0
while city== 0:# function will return invalid for every wrong choice
 city = plane_cost(input('1. O R Tambo International ,\n2.Capetown International\n 3. King Shaka International \nwhere are you flying to? '))
days = car_rental(int(input('How many days do you need the car for?: ')))
total = holiday_cost(nights, city, days)
print(holiday_cost(nights, city, days)) # total cost to be printed out