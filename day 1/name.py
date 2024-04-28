name=input("what is your name? ")
charachters=len(name)
if charachters < 3:
    print("name must contain at least 3 charachters")
if charachters > 50:
    print("name must contain less than 50 charachters")
if charachters > 3 and charachters < 50:
    print("name looks good!")
 