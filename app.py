import os

clear = lambda: os.system('cls')

def tip_calculator():
    clear()
    print("\n*** Tip and Bill Calculator ***")
    print(f"Your bill is: ${bill_subtotal:.2f}")
    print(f"You have chosen to tip: {tip_amount}%")
    print(f"The tip total is: ${tip_total:.2f}")
    if num_of_parties == 1:
        print(f"The total you owe: ${bill_total:.2f}")
    else:
        print(f"There are {num_of_parties} parties splitting the bill.")
        print(f"Each party should pay: ${split_bill_total:.2f}")

print("*** Tip and Bill Calculator ***")
bill_subtotal = float(input("What is the total of your bill? "))
tip_amount = int(input("What percentage tip would you like to give? [Popular tip amounts =  15% / 18% / 20% / 22% / 25%] "))
tip_percent = float(tip_amount / 100)
tip_total = float(bill_subtotal * tip_percent)
num_of_parties = int(input("How many parties are splitting the bill? "))
bill_total = float(bill_subtotal + tip_total)
split_bill_total = bill_total / num_of_parties
tip_calculator()

