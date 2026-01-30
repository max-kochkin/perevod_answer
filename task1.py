def is_palindrome(s: str) -> bool:
    text = ''.join(c.lower() for c in s if c.isalpha() or c.isdigit())     # Проверяет, является ли строка палиндромом
    return text == text[::-1]                                  # Регистр букв, пробелы и знаки препинания не учитываются


def run_examples() -> None:
    examples = [
        "Я иду с мечем судия",
        "А роза упала на лапу Азора",
        "Hello, world!",
        "Не палиндром"
    ]

    for s in examples:
        if is_palindrome(s):
            print(f"'{s}' - Строка является палиндромом")
        else:
            print(f"'{s}' - Строка не является палиндромом")


def run_tests() -> None:
    assert is_palindrome("Я иду с мечем судия")
    assert is_palindrome("А роза упала на лапу Азора")
    assert is_palindrome("Tenet")

    assert not is_palindrome("Привет")
    assert not is_palindrome("12345")
    assert not is_palindrome("Это не палиндром")

    print("Все тесты пройдены успешно!")


if __name__ == "__main__":
    run_examples()
    print()
    run_tests()
