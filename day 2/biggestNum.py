numbers= [1, 4, 5, 6, 8, 24, 13, 17, 19, 43, 45, 58, 23, 90, 61,83 ,54, 68 ,12 , 43 ,58]
max = numbers[0]
for number in numbers:
    if number > max:
        max=number
print(max)