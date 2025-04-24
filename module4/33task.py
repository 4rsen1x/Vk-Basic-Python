import os

def write_and_read(text):
    with open("temp.txt", "w") as file:
        file.write(text)

    with open("temp.txt", "r") as file:
        return file.read()

text = input()
print(write_and_read(text))
