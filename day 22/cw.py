# მომხმარებლის მონაცემების შეყვანა
name = input("შეიყვანეთ თქვენი სახელი: ")
age = int(input("შეიყვანეთ თქვენი ასაკი: "))
experience = int(input("შეიყვანეთ თქვენი სამუშაო გამოცდილება წლებში: "))

if age > 22 and experience > 2:
    print("Hired")
elif age > 25 and experience > 1:
    print("Hired")
elif age > 20 and experience > 3:
    print("Hired")
elif name == "გურამ":
    print("Hired")
else:
    print("Not hired")



Names = ["Levan", "Guram", "David", "Mariam", "Giorgi", 30, 7, 54321, 8.8, False]
Nums = [25, 40, 5, 95, 10, 100]

print(len(Names))
print(sum(Nums))
print(min(Nums))
print(max(Nums))

Nums.append(77)
Nums.reverse()
Nums.remove(40)

print(Nums)
