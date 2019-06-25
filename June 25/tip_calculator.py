def tip_calculator(total_amount, tip_percentage): 
    tip_multiplier = tip_percentage / 100 
    tip_amount = tip_multiplier * total_amount
    return tip_amount 

print(tip_calculator(150, 15))

