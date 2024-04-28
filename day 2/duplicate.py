numbers=[1, 2, 5, 1, 2, 6, 9, 6, 0, 9, 7, 4, 5, 4]
uniques=[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)