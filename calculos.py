# Creating values for the vector x and printing it
import random

t = int(input("Type the vectors size: "))
x = [0] * t

for i in range(0, len(x)):
    x[i] = random.randint(0, 50)

print("[", end="")  
for i in range(0, len(x)):
    print(x[i], end=" ")
    if(i < len(x) - 1):
        print(", ", end="") 
print("]")

# Printing vector's values inverted (from end to start)
print("[", end"")
for i in range(len(x)-1, -1, -1):
    print(exe1[i], end=" ")
    if(i < len(exe1) - 1):
        print(", ", end="")
print("]", end="")

# Sum of all the vector's values
s = 0
for i in range(0, len(x)):
    s += x[i]
print(f"The sum of the vector x is equal to: {s}")

# Sum of the odd vector's values
s = 0
for i in range(0, len(x)):
    if(x[i] % 2 == 1):
        s += x[i]
print(f"The sum of odd numbers in the vector x is: {s}")

# Count of even numbers 
even = 0
for i in range(0, len(x)):
    if(x[i] % 2 == 0):
        even += 1
print(f"The total of even numbers in the vector x ix: {even}")

# Calcule of the average
s = 0
for i in range(0, len(x)):
    s += x[i]
print(f"The calcule of the average is: {s} / {len(x)}")
media = s / len(x)
print(f"The average of the vector x values is: {media}")

# Average of the even numbers
somap = 0
for i in range(0, len(x)):
    if(x[i] % 2 == 0):
        somap += x
media = somap / len(x)
print(f"A media dos numeros pares é: {media}")
