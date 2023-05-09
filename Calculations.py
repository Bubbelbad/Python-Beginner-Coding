#Why does this zip thing not work?
products = ["DynaVap", "O-rings", "Torch", "Wooden_box"]
prices = [1399, 79, 69, 199]
mixed_list = zip(products, prices)
print(mixed_list)

print("I would like to buy the " + products[0] + ", but it's really expensive!"
      """

I think it might be worth it in the long run tho?""")

Costs = 2000
Years_left = 40

Yearly_Costs = Costs / Years_left
print(f"It would costs me {int(Yearly_Costs)} SEK per year to use it, if I live for {Years_left} more that is. My lungs will probably thank me. ")

#Now some calulus: 
income = input("Skriv din årsinkomst (utan mellanslag): ")
income = float(income)
tax = 0.3
if income > 20000: 
  lefties = income - 20000
  tax = lefties * tax
  
print(income)
print(tax)

#Some word(len) stuff:
word2 = input("Skriv ett ord: ")
word3 = input("Skriv ett till ord: ")
if len(word2) >= 3 or len(word3) >= 3:
  level = 1
elif len(word2) >= 3 and len(word3) >= 3:
  level = 2
else: 
  print("Ta bladet från munnen, pojkvasker!")
print(level)

#Password-Check:
user = input("Användarnamn: ")
password = input("Lösenord: ")
if user == "vatten" and password == "lavemang":
  message = "Välkommen!"
elif user =="vatten" or password == "lavemang":
  message = "Försök igen"
else:
  message = "Haha, helt fel!!"



#Program for calculating the costs at a barberer:
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price = 0

#Calculating total price:
for price in prices: 
  total_price =+ price

#Calculating the avarage price:
avarage_price = total_price // len(prices)
print("""Avarage Haircut Price: 
"""+ str(avarage_price) + " $")

#Raising the cost by 5$:
new_prices = [price - 5 for price in prices]
print(new_prices)

#Renevues, weekly & daily:
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total revenue: " + str(total_revenue))

avarage_daily_revenue = total_revenue // 7
print(avarage_daily_revenue)

#Getting the hairstyles from under 30 $ for advertising: 
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]

print(cuts_under_30)
