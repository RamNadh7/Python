print('Welcome to Tip Calculator!!')
total_bill=float(input('What was the total Bill? : Rs. '))
tip=int(input('How much tip would you like to give? 10,12, 15 ?' ))
split=int(input('How many people to split the bill? '))
each_final_amount=round((total_bill*(1+(tip/100)))/split,2)
print(f'Each person should pay Rs.{each_final_amount}')