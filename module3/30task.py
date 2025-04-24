class Dictionary:
    def __init__(self, dictionary):
        self._dict = dictionary  # сохраняем словарь как атрибут

    def __call__(self, key):
        return self._dict.get(key)  # возвращаем значение по ключу
code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
