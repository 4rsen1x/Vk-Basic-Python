denominator, numerator = int(input()), int(input())

def changed_div(numerator, denominator):
    try:
        return denominator / numerator
    except ZeroDivisionError:
        return denominator

print(changed_div(numerator, denominator))
