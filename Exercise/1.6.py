#Exercise 1 : Mailing Address

print("Muhamad Yusuf Hidayat")
print("Departement of Computer Science")
print("National Institute Technology Bandung")
print("2500 National Institute Technology Bandung")
print("40291, Bandung")
print("Indonesia")

#Exercise 2 : Hello

name = input("What is your name ?")
print (f"Hello {name}", "Good Morning")

#Exercise 3 : Area of Room

#Give user input
lenth = input ("Lenth of Room")
width = input("Width of Room")

#Type convertion from str to floating point numbers
l_convert = float (lenth)
w_convert = float(width)

#Calculate area l * w
area = w_convert * l_convert

#Display output
print (f"{area}", "meters")

#Exercise 4 : Area of a Field

#Value that convert from square feet to acre
SQFT_PER_ACRE = 43560

#Length user input
length = input("Lenth of Area ?")

#Width user input
width = input("Width of Area ?")

#Type conversion from string to float number
length_cov = float(length)
width_cov = float(width)

#Calculate total area in acre
total_area = length_cov * width_cov / SQFT_PER_ACRE

#Print the calculation result
output = print(f"There are {total_area} square feet in an acres")

#Exercise 5 : Bottle Deposits

#Compute the refund amount for a collection of bottles
LESS_DEPOSITE = 0.10
MORE_DEPOSITE = 0.25

# Read the number of containers of each size from the user
less = input("How many containers 1 litre or less?" " ")
more = input("How many containers more that 1 litre?" " ")

# Type conversion
less_int = int(less)
more_int = int(more)

# Calculate refund amount
refund = LESS_DEPOSITE * less_int + MORE_DEPOSITE * more_int

# Display output
print("Your total refund will be $%.2f." % refund)

#Exercise 6 : Tax & Tip

#User cost input
meal_cost = input("Cost of a meal?" " " "Rp.")

#Type convert
meal_cost_conv = float(meal_cost)
# In this case, I use restaurant tax
#Tax & Tip Rate
Tax = 0.10
Tip = 0.18

#Tax calculation
tax = meal_cost_conv * Tax
#Tip calculation
tip = meal_cost_conv * Tip

#Total bill calculation (Tip, Tax and Food cost)
total_bill = tip + tax + meal_cost_conv
output = "The tax is Rp.%.2f and the tip is Rp.%.2f, making the total Rp.%.2f" % (
    tax,
    tip,
    total_bill,
)

#Display output
print(output)