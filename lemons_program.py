def calculate_lemons_needed(current_lemons):
    total_lemons = 21
    lemons_needed = total_lemons - current_lemons
    if lemons_needed > 0:
        print(f"You need {lemons_needed} more lemons.")
    elif lemons_needed == 0:
        print("You already have exactly 21 lemons!")
    else:
        print(f"You have {abs(lemons_needed)} too many lemons. You should remove {abs(lemons_needed)} lemons.")

current_lemons = int(input("Enter the number of lemons you have: "))
calculate_lemons_needed(current_lemons) 
