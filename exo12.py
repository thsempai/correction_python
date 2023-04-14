number = input("Nombre: ")
number = int(number)

last_number = None
sum_number = number

while number != last_number:
    last_number = number
    
    number = input("Nombre: ")
    number = int(number)

    sum_number = sum_number + number

print("Somme: " +str(sum_number))
