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
