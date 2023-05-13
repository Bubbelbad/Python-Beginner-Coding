#Guide travelers:
def generate_trip_instructions(location):
  print("Looks like you are planning a trip to visit " + location)
  print("You can use the public tram system to get to " + location)
generate_trip_instructions("Göteborg Centralstation")

#Calculate costs for traveling:
def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = hotel_rate * trip_time - 10
  print(car_rental_total + hotel_total + plane_ticket_price)
calculate_expenses(200, 100, 100, 5)

#Budget program:
current_budget = 3500.75
def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))
print_remaining_budget(current_budget)
 
def deduct_expense(budget, expense):
  return budget - expense
shirt_expense = 9

new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)
print_remaining_budget(new_budget_after_shirt)

#To use multiple returns in a function: 
def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first, second, third

most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()
print(most_popular1)
print(most_popular2)
print(most_popular3)

def trip_planner_welcome(name):
  print(f"Welcome to tripplanner v1.0 {name}")
trip_planner_welcome("Victor")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time
estimate = estimated_time_rounded(2.5)

def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
  print("Your trip starts off in " + origin)
  print("And you are traveling to " + destination)
  print("You will be traveling by " + mode_of_transport)
  print("It will take approximately " + str(estimated_time) + " hours")
destination_setup("Göteborg", "Mazatlan", estimate, "Airplane")
