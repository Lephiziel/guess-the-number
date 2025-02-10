import random
print("Здравствуйте, вы играете в игру 'Угадай число'")
print("Hello, you are playing 'Guess the number' game")
print()
print("Ваша задача угадать загаданное число(от 1 до 10)")
print("Your task is to guess the number(from 1 to 10)")
print()

random_number = random.randint(1, 10)

user_number = int(input("Введите любое число | Enter random number: "))

while user_number != random_number:
    if user_number != random_number:
        print("❌Вы не угадали, попробуйте снова❌")
        print("❌You're wrong, try again❌")
        user_number = int(input("Введите любое число | Enter random number: "))

print(f"✅Вы угадали, загаданное число было {random_number}✅")
print(f"✅You're right, the hidden number is {random_number}✅")
print(r"lephiziel@gmail.com - report about bugs")
