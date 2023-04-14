number = input("Nombre: ")
number = int(number)

numbers=[number]

while number != 0:
    number = input("Nombre: ")
    number = int(number)

    numbers.append(number)

print("Plus petit: " + str(min(numbers)))
print("Plus grand: " + str(max(numbers)))
