# 2. Пользователь вводит время в секундах...
time = int(input("Введите время в секундах >>> "))
h = time // 3600
m = (time // 60) % 60
s = time % 60
if m < 10:
    m = str('0' + str(m))
else:
    m = str(m)
if s < 10:
    s = str('0' + str(s))
else:
    s = str(s)
print("{}:{}:{}".format(h, m, s))
print(f"{h}:{m}:{s}")
print(str(h) + ':' + str(m) + ':' + str(s))

# 3. Узнайте у пользователя число n...
number = int(input("Введите любое число >>> "))
n = number
nn = n + n
nnn = n + n + n
print(n + nn + nnn)

# 4. Пользователь вводит целое положительное число...
positive_number = int(input("Введите любое целое положительное число >>> "))
m = positive_number % 10
a = positive_number//10
while positive_number > 0:
    if positive_number % 10 > m:
        m = positive_number % 10
    positive_number = positive_number//10
print("Самая большая цифра в числе: {}".format(m))

# 5. Запросите у пользователя значения выручки и издержек фирмы...
proceeds = int(input("Введите выручку >>> "))
costs = int(input("Введите издержки >>> "))
if proceeds < costs:
    print("Фирма работает в минус")
if proceeds > costs:
    print("Фирма работает в плюс")
    profitability = proceeds // costs
    print("Фирма работает с рентабельностью {}".format(profitability))
    employees = int(input("Введите количество сотрудников >>> "))
    proceed_per_employee = profitability // employees
    print("Прибыль на одного сотрудника {}".format(proceed_per_employee))

# 6. Спортсмен занимается ежедневными пробежками...
start = int(input("Укажите количество километров в первый день >>> "))
finish = int(input("Укажите нужное количество километров >>> "))
count = 0
while finish > start:
    start = start * 1.1
    count = count + 1
    if finish < start:
        print("Спортсмен пробежит {} км на {} день".format(finish, count))
