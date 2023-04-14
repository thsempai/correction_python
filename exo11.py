from random import randint

n1 = randint(0, 100)
n2 = randint(0, 100)

user_anwser = input(str(n1) + "+" + str(n2) + "= ")
user_anwser = int(user_anwser)
errors = 0

while user_anwser != (n1 + n2):
    errors = errors + 1
    user_anwser = input(str(n1) + "+" + str(n2) + "= ")
    user_anwser = int(user_anwser)

print("Tu as commis " + str(errors) + " erreur(s).")

