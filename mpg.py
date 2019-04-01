#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon application")
print()

while True:

# get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_per_gallon = float(input("Enter cost per gallon:      "))

    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    else:
    # calculate and display miles per gallon
        mpg = round((miles_driven / gallons_used), 2)
        gas_cost = round((gallons_used*cost_per_gallon),2)
        cost_per_mile = round((gas_cost/miles_driven),1)

        print()
        print("Miles Per Gallon:          ", mpg)
        print("Total Gas Cost:            ", gas_cost)
        print("Cost Per Mile:             ",cost_per_mile)

    print()
    yes_or_no = (input("Get entries for another trip (y/n)? "))

    if yes_or_no=='n':
        break

