#!/usr/bin/env python3

import validation

def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = validation.get_float("Enter monthly investment:\t",0,1000)
        yearly_interest_rate = validation.get_float("Enter yearly interest rate:\t",0,15)
        years = validation.get_int("Enter number of years:\t\t",0,50)

        # get and display future value
        monthly_interest_rate = yearly_interest_rate / 12 / 100
        months = years * 12

    # calculate future value
        future_value = 0.0
        for i in range(0, months):
            future_value += monthly_investment
            monthly_interest = future_value * monthly_interest_rate
            future_value += monthly_interest

        print("Future value:\t\t\t" + str(round(future_value, 2)))
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()
    
if __name__ == "__main__":
    main()