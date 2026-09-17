text = input("Введите число или слово: ")

if len(text) > 20:
    print("Ошибка! Слишком большое число или длинное слово.")

elif text.isdigit():
    count = 0

    for i in text:
        count += 1

    print("Количество цифр:", count)

elif text.isalpha():
    result = ""
    i = len(text) - 1

    while i >= 0:
        result += text[i]
        i -= 1

    print("Перевернутое слово:", result)
else:
    print("Ошибка! Введите только число или только буквы.")