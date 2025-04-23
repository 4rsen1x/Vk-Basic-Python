# Считываем строку со стандартного ввода
input_string = input()

# Приводим строку к нижнему регистру и удаляем пробелы
filtered_chars = {ch for ch in input_string.lower() if ch != ' '}

# Сортируем уникальные символы в лексикографическом порядке
sorted_chars = sorted(filtered_chars)

# Выводим символы, разделенные пробелом
print(" ".join(sorted_chars))
