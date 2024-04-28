question=("what is temp today?" )
temp=int(input(question))
if temp >=30:
    print("Today is a hot day, drink planty of water!")
if temp < 30 and temp >= 15:
    print("it's a lovely day")
if temp < 15:
    print("it's a cold day, wear warm clothes")
