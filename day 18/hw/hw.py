sum = 0

for i in range(1, 101):
    sum += i

print("ჯამი არის:", sum)

num = 1

while num <= 50:
    print(num)
    num += 2


sum = 0

for i in range(10):
    num = int(input(f"{i+1}-ე რიცხვი: "))
    sum += num

print("რიცხვების ჯამი არის:", sum)

import random

secret_number = random.randint(1, 10)
guess = 0

while guess != secret_number:
    guess = int(input("გამოიცანი რიცხვი 1-დან 10-მდე: "))
    if guess != secret_number:
        print("არასწორია, სცადე თავიდან!")

print("გილოცავ! სწორად გამოიცანი ")