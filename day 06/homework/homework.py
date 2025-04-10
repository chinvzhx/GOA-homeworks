# 1) მომხმარებლისგან რიცხვის მიღება და კონსოლში გამოტანა, როგორც მთელი რიცხვი.

number_str = input("Enter a number: ")  # მომხმარებლისგან შეყვანის მიღება, როგორც სტრინგი.
number_int = int(number_str)  # სტრინგის მთელ რიცხვად გადაყვანა.
print("Your entered number as an integer:", number_int)  # მთელი რიცხვის კონსოლში გამოტანა.

# 2) მომხმარებლისგან ინფორმაციის მიღება და მისი მონაცემთა ტიპის შემოწმება.

information = input("Enter some information: ")  # მომხმარებლისგან შეყვანის მიღება.
data_type = type(information)  # შეყვანის მონაცემთა ტიპის შემოწმება.
print("The data type of your entered information:", data_type)  # მონაცემთა ტიპის კონსოლში გამოტანა.

# 3) რიცხვის შენახვა სტრინგის ცვლადში ('15') და შემდეგ ამ სტრინგის მთელ რიცხვად გადაყვანა.

number_str = '15'  # რიცხვის შენახვა, როგორც სტრინგი.
number_int = int(number_str)  # სტრინგის მთელ რიცხვად გადაყვანა.
print("The number converted from string to integer:", number_int)  # მთელი რიცხვის კონსოლში გამოტანა.

# 4) type() ფუნქციის დანიშნულების ახსნა კომენტარებში.

# type() ფუნქცია გამოიყენება ცვლადის ან მნიშვნელობის მონაცემთა ტიპის განსასაზღვრად.
# ის აბრუნებს ტიპის ობიექტს, რომელიც მიუთითებს ცვლადის ან მნიშვნელობის ტიპზე.
# მაგალითად, თუ ცვლადი შეიცავს მთელ რიცხვს, type() დააბრუნებს <class 'int'>.
# თუ ცვლადი შეიცავს სტრინგს, type() დააბრუნებს <class 'str'>.

# 5) input() ფუნქციის დანიშნულების ახსნა კომენტარებში.

# input() ფუნქცია გამოიყენება კონსოლიდან მომხმარებლის შეყვანის მისაღებად.
# ის აჩვენებს მოთხოვნას (სტრინგი, რომელიც გადაეცემა, როგორც არგუმენტი) და ელოდება მომხმარებლის შეყვანას.
# მომხმარებლის შეყვანა ბრუნდება, როგორც სტრინგი.
# თუ შეყვანა რიცხვად უნდა დამუშავდეს, დაბრუნებული სტრინგი უნდა გადაკეთდეს მთელ ან წილად რიცხვად.