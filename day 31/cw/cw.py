
# ფუნქციები გამოიყენება იმისთვის, რომ კოდი გავხადოთ უფრო ორგანიზებული და მარტივი.
# ისინი საშუალებას გვაძლევს ერთი და იგივე მოქმედება რამდენჯერმე გამოვიყენოთ 
# ისე, რომ ხელახლა არ დავწეროთ ერთი და იგივე კოდი.
def average_of_three(a, b, c):
    average = (a + b + c) / 3
    print("საშუალო არითმეტიკული არის:", average)

# magaliti
average_of_three(4, 7, 10)  # prints: 7.0


# Default value ფუნქციაში ნიშნავს იმას, რომ თუ არგუმენტი არ გადავეცით, მას ავტომატურად მიენიჭება ნაგულისხმევი მნიშვნელობა.


text = "   hello world   "

print(text.capitalize())
print(text.upper())
print(text.lower())
print(text.strip())
print(text.lstrip())
print(text.rstrip())
print(text.index("world"))
print(text.find("world"))
print(text.find("python"))
