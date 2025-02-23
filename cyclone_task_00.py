import re


def parse_text(text):
    pattern = r"\b[a-zA-Zа-яА-Я]{3,}\b"
    words = re.findall(pattern, text)
    unique_count = set([word.lower() for word in words])  # для всех регистров
    count_palindromes = sum(1 for word in words if word == word[::-1])
    return f"Total: {len(words)}, Unique: {len(unique_count)}, Palindrome: {count_palindromes}"


if __name__ == '__main__':
    try:
        with open("text_task_00.txt", "r", encoding="utf-8") as f:
            btext = f.read()
    except FileNotFoundError:
        print("Файл text_task_00.txt не найден. Проверьте путь к файлу.")
        exit(1)

    print(parse_text(btext))
