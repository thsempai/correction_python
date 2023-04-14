from random import randint

numbers = []

for _ in range(3):
    numbers.append(randint(1, 6))
    
print(str(numbers[0]) + " - " + str(numbers[1]) +  " - " + str(numbers[2]))

while numbers[0] != numbers[1] or numbers[0] != numbers[2]:
    for index in range(3):
        numbers[index] = randint(1, 6)
    print(str(numbers[0]) + " - " + str(numbers[1]) +  " - " + str(numbers[2]))

