# Считываем строку со стандартного ввода
input_string = input()

# Приводим строку к нижнему регистру
lower_string = input_string.lower()

# Заменяем указанные символы на пустую строку и подсчитываем замены
chars_to_replace = {'!', '%', '#', '@'}
replaced_count = 0
result_string = []

for char in lower_string:
    if char in chars_to_replace:
        replaced_count += 1
    else:
        result_string.append(char)

# Собираем итоговую строку
result_string = ''.join(result_string)

# Выводим результаты
print(replaced_count)
print(result_string)
