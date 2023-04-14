password = "Pyth0n007"

input_user = None
tries = 3

while input_user != password and tries > 0:
    input_user = input("Mot de passe: ")
    tries = tries - 1

if password == input_user:
    print("Mot de passe valide.")
else:
    print("Mot de passe incorrect.")

