# n 0

# my_list = ["baker ", "santa cruz", "thunder trucks", "playboy carti", "ken carson"]

# baker number 0 
# santa cruz 1 
# da ese miyveba atvla 0 idan iwyeba
# print(my_list)


# n1
my_list = ["baker ", "santa cruz", "thunder trucks", "playboy carti", "ken carson"]
print(my_list[-0]) 
print(my_list[-4]) 

# n2 
result = []


# Ask the user for 10 numbers
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 == 0:  
        result.append(num)

print("Even numbers:", result)


names = ["Gurami", "Gio", "Andria", "Mariami", "Dato"]

long_names = [name for name in names if len(name) > 5]

print(long_names)
