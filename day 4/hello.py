import random

print("Welcome to Hangman")

word=["apple", "car", "laptop", "house","sister", "television" ]

secret = random.choice(word)
display=[]
for letter in secret:
    display += "_"
print (display)
print("You only have 5 guesses!")

guessc = 0


game_over = False
while not game_over:
    x = input("Guess the letter: ").lower()
    for position in range(len(secret)):
        letter = secret[position]
        if letter == x:
             display[position] = letter
    print(display)
    if x not in secret:
        guessc += 1
        guessl = 5 - guessc
        print(f"Guesses left - {guessl}")
        if guessc >= 5:
            game_over = True 
            print("Loser")
    if "_" not in display:
            print("You won!")
            game_over = True


