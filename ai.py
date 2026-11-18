import random

print("AI NUMBER GUESSER")
print("חשב על מספר בין 1 ל-10")

number = random.randint(1, 10)

guess = int(input("מה המספר שאני חושב עליו? "))

if guess == number:
    print("צדקת! כל הכבוד!")
else:
    print("לא נכון! המספר היה:", number)