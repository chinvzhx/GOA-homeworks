# n0
# print:
# + გამოსაყენებელია შედეგის პირდაპირ ტერმინალში გამოსატანად
# + სასარგებლოა დებაგინგისთვის
# - არ აბრუნებს მნიშვნელობას ამიტომ ვერ გამოიყენება სხხვა გამოთვლებში
# - ფუნქციამ შედეგი მხოლოდ ბეჭდავს და ვერ ვიყენებთ შემდეგ

# return:
# + აბრუნებს მნიშვნელობას რომლითაც შეგვიძლია მერე ვიმუშაოთ
# + ფუნქციას ხდის მრავალჯერად გამოსადეგს
# + საშუალებას გვაძლევს შედეგი შევინახოთ ცვლადში
# - შედეგი ეკრანზე არ ჩანს თუ print არ გამოვიყენეთ
# - ახალბედებისთვის შეიძლება ნაკლებად გასაგები იყოს

# n1
def check_age(age):
    if age >= 18:
        print("Access Granted")
    else:
        print("Access Denied")

# n2
def user_info(name, surname, address):
    return f"users name: {name}\nusers surname: {surname}\nusers address: {address}"

# n3
def power(num1, num2):
    return num1 ** num2

# n4
def arithmetic_average(numbers):
    return sum(numbers) / len(numbers)
