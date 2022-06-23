import random

word_list = random.choice(["Monkey", "Ape", "Orangutan"]).lower()
print(word_list)
length = len(word_list)
display = []
for i in range(length):
    display.append("_")

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(length):
        letter = word_list[position]
        if letter == guess:
            display[position] = guess

    full = (f"\n{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("_____________")
        print("\nSuccess")

    print(full)
