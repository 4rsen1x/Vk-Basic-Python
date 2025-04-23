# Считываем три числа
num1 = int(input())
num2 = float(input())
num3 = int(input())

# Форматируем первое число: +000000102 (10 символов: знак + 9 цифр)
formatted_num1 = f"{num1:+010d}"

# Форматируем второе число: #######2.14 (10 символов: решетки + число)
# Вычисляем количество решеток
total_length = 10
num_str = f"{num2:.2f}"
hash_count = total_length - len(num_str)
formatted_num2 = "#" * hash_count + num_str

# Форматируем третье число: 1111_1111_1111_1111 (16 бит с разделителями)
binary_str = f"{num3:016b}"
formatted_num3 = "_".join([binary_str[i:i+4] for i in range(0, 16, 4)])

# Выводим результаты
print(formatted_num1)
print(formatted_num2)
print(formatted_num3)
