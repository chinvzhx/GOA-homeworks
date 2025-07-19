my_data = ["text", 5, 2.5, True, None]  # სხვადასხვა ტიპის მონაცემები ერთ სიაში

print(my_data)  # სიის დაბეჭდვა

# n2

foods = ["pizza", "burger", "salad"]  # საჭმლის სია

foods.append("khinkali")  # სიაში დამატება
foods.remove("burger")    # სიიდან წაშლა

print(foods)              # სიის დაბეჭდვა
print(len(foods))         # სიის სიგრძე

# n3

nums = [3, 7, 1, 9]  # რიცხვების სია

print(max(nums))     # მაქსიმუმი
print(min(nums))     # მინიმუმი
print(sum(nums))     # ჯამი

avg = sum(nums) # საშუალოს გამოთვლა
print(avg)# საშუალოს დაბეჭდვა

# n4

words = ["cat", "home", "apple", "car"]  # სიტყვების სია
short = []  # ცარიელი სია მოკლე სიტყვებისთვის

for w in words:
    if len(w) < 5:  # მხოლოდ 5-ზე ნაკლები ასოს მქონე სიტყვები
        short.append(w)

print(short)  # ფილტრირებული სია

# n5

names = ["Tiko", "Ana", "Luka"]  # სახელების სია

names.sort()  # სიის დალაგება
print(names)  # დალაგებული სია

names.reverse()  # სიის შებრუნება
print(names)     # შებრუნებული სია
