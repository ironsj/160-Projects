#Inputs
name = input("Enter your name:")

num_pizzas = int(input("Enter the number of pizza you want to order:"))

print("Pizza Size and Cost", "- Small (10 inch, $7.95), Medium (12 inch, $9.95), and Large (14 inch, $11.95)", sep="\n")
pizza_size = input("Enter the size of your pizzas:")

print("Available Topping and Cost Per Topping")
print("- Ham, Mushrooms, Onions, Green Peppers, Black Olives, Tomatoes, Pineapple, Spinach")
print("- $0.75 each for Small Pizza, $0.95 each for Medium Pizza, and $1.15 each for Large Pizza")

num_toppings = int(input("Enter the number of topping on your pizzas:"))
toppings_choice = input("Enter your choices of toppings:")

#Outputs
print("Order Summary")
print("Customer name:\t", name)
print(num_pizzas, pizza_size, "Pizzas with", toppings_choice)

subtotal = 0
if pizza_size == "Small":
    subtotal = (num_pizzas * 7.95) + (num_toppings * 0.75)
elif pizza_size == "Medium":
    subtotal = (num_pizzas * 9.95) + (num_toppings * 0.95)
else:
    subtotal = (num_pizzas * 11.95) + (num_toppings * 1.15)
print("Subtotal:", "${:,.2f}".format(subtotal))

tax = subtotal * 0.06
print("Sales Tax(6.0%):", "${:,.2f}".format(tax))

total = subtotal + tax
print("Total Cost:", "${:,.2f}".format(subtotal + tax))

