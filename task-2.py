from collections import deque


def is_palindrome(s):
    # Видалення пробілів і приведення в нижній регістр
    sanitized_chars = ''.join(c for c in s if c.isalnum()).lower()
    chars_deque = deque(sanitized_chars)

    while len(chars_deque) > 1:
        if chars_deque.popleft() != chars_deque.pop():
            return False

    return True


# Перевірка
phrases = ["radar", "Level", "noon", "Hannah", "book",
           "Race fast, safe car.", "No lemon, no melon.", "Not a palindrome"]
for phrase in phrases:
    result_string = 'is' if is_palindrome(phrase) else 'is not'
    print(f'"{phrase}" {result_string} a palindrom')
