def process_line(s):
    if s.startswith("!"):
        s = s.upper()
    else:
        s = s.lower()
    chars_to_remove = "!@#%"
    for ch in chars_to_remove:
        s = s.replace(ch, "")
    return s

while True:
    try:
        line = input()
    except EOFError:
        break
    print(process_line(line))
