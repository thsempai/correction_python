number = input("Nombre: ")
number = int(number)

min_number = number
max_number = number

while number != 0:
    number = input("Nombre: ")
    number = int(number)

    if number < min_number:
        min_number = number
    elif number > max_number:
        max_number = number

print("Plus petit: " + str(min_number))
print("Plus grand: " + str(max_number))
