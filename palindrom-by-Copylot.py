def is_palindrome():
    # Шаг 1: Получение строки от пользователя
    original_str = input("Введите строку: ")

    # Шаг 2: Проверка на наличие не буквенных символов и пробелов
    if not all(c.isalpha() or c.isspace() for c in original_str):
        print("Ошибка: Строка должна содержать только буквы и пробелы. Пожалуйста, повторите ввод.")
        return

    # Шаг 3: Преобразование строки
    s = original_str.replace(" ", "").lower()

    # Шаг 4: Проверка на палиндром с использованием циклов и дополнительных переменных
    is_palindrome = True
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            is_palindrome = False
            break

    # Шаг 5: Вывод результата
    if is_palindrome:
        print(f'Строка "{original_str}" является палиндромом.')
    else:
        print(f'Строка "{original_str}" не является палиндромом.')

# Вызов функции для проверки
is_palindrome()
