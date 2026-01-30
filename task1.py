text = ''.join(s.lower() for s in input() if s.isalpha())
if text == text[::-1]:
    print("Строка является палиндромом")
else:
    print("Строка не является палиндромом")