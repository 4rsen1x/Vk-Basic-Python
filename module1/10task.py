# Считываем строку со стандартного ввода
text = input()

# Разбиваем строку на слова (разделитель - пробел) и приводим каждое слово к нижнему регистру
words = text.lower().split()

# Создаем словарь для подсчета количества вхождений каждого слова
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Находим слово с максимальной частотой
most_frequent_word = max(word_count, key=word_count.get)
frequency = word_count[most_frequent_word]

# Выводим результат
print(most_frequent_word, frequency)
