# 1
value = 10 + 5
print(value)
value = "Test"
print(value)




# 2
# password = input("Введите пароль >>>")
#
# original_password = "correct"
#
# if original_password == password:
#     print("Верно")
# else:
#     print("Неверно")
age = int(input("Введите ваш возраст >>>"))
if age >= 14:
    print("Паспорт можно получить")
    if 20 <= age < 45:
        print("Паспорт можно поменять")
elif age < 1:
        print("Custom")
else:
    print("Паспорт нельзя получить")




# 3
counter = 3
while counter > 0:
    print("Counter", counter)
    counter = counter - 1
else:
    print("Done!")




# 4
username = input("Укажите ваше имя:")
age = int(input("Укажите ваш возраст"))
# print(f"Привет, {username}! Тебе уже {age} лет!")
print("Привет, {}! Тебе уже {} лет!".format(username, age))




# 5
max_count = int(input("Максимальное число >>>"))
delimiter = int(input("Число для деления  >>>"))
current_count = 0
while True:
    if current_count == max_count:
        break

    current_count += 1

    if current_count % delimiter == 0:
        continue

    print(current_count)
