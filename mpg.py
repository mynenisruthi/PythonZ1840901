#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
cost_per_gallon = float(input("Enter cost per gallon:\t\t"))

# calculate miles per gallon
mpg = miles_driven / gallons_used
mpg = round(mpg, 2)

# calculate gas cost total
gas_cost = gallons_used*cost_per_gallon
gas_cost = round(gas_cost,2)

#calculate cost per mile
cost_per_mile = gas_cost/miles_driven
cost_per_mile = round(cost_per_mile,2)
            
# format and display the result
print()
print("Miles Per Gallon:\t" + str(mpg))
print("Total Gas Cost:\t\t" +str(gas_cost))
print("Cost Per Mile:\t\t" +str(cost_per_mile))


