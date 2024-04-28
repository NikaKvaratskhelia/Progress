weight=float(input("Weight: "))
unit= input("Kg or lbs: ")
if unit== "Kg":
    converted = weight / 0.45
    print("weight in pounds is:" + str(converted))
if unit=="lbs":
    converted=weight * 0.45
    print ("weight in kgs: "  + str(converted))