weight=float(input("Enter your weight: "))
unit=input("kilograms or pounds ? (K or L): ")

if(unit=="K"):
    weight=weight * 2.205
    unit="Lps."
    print(f"your weight is: {round(weight, 3)}{unit}")
elif(unit=="L"):
    weight=weight / 2.205
    unit="Kgs."
    print(f"your weight is: {round(weight, 3)}{unit}")
else:
    print(f"{unit} is not valid")
