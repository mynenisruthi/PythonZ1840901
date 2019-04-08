
def get_int(prompt,min_value,max_value):
    while "True":
        years = int(input(prompt))
        if years > min_value and years <= max_value:
            break
        else:
            print("Entry must be greater than "+ str(min_value)+" and less than or equal to "+str(max_value))
    return years

def get_float(prompt,min_value,max_value):
    while "True":
        money_value = float(input(prompt))
        if money_value>min_value and  money_value <=max_value:
            break
        else:
            print("Entry must be greater than "+ str(min_value)+" and less than or equal to "+str(max_value))
    return money_value