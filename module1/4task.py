s = input().strip()
has_a_or_o = ('a' in s) or ('o' in s)
no_i_and_e = ('i' not in s) and ('e' not in s)
is_correct = has_a_or_o and no_i_and_e
print(is_correct)
