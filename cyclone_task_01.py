lang_map = {"rus": ("а", "А", 32),
            'eng': ("a", "A", 26)}
SHIFT = ord('м') - ord('д')


def decrypt_caesar(message, lang):
    """Функция для дешифрования. Если результат не читаемый, дешифруй его повторно."""
    decrypted_message = ""
    language = lang_map.get(lang)
    if not language:
        return {"message": "Такого языка в системе нет"}
    lower_letter, upper_letter, alphabet_length = language[0], language[1], language[2]
    for char in message:
        if char.isalpha():
            char_code = ord(char) - SHIFT
            if char.islower():
                if char_code < ord(lower_letter):
                    char_code += alphabet_length
            elif char.isupper():
                if char_code < ord(upper_letter):
                    char_code += alphabet_length
            decrypted_message += chr(char_code)
        else:
            decrypted_message += char
    return decrypted_message


if __name__ == "__main__":
    try:
        with open("text_task_01_caesar.txt", "r", encoding="utf-8") as f:
            encrypted_message = f.read()
    except FileNotFoundError:
        print("Файл text_task_01_caesar.txt не найден. Проверьте путь к файлу.")
        exit(1)

    input_lang = input('Введите язык шифра, rus или eng: ').strip().lower()
    original_message = decrypt_caesar(encrypted_message, input_lang)
    print(original_message)
    task_phrase = ''  # Вставьте сюда шифр на латинице для повторного дешифрования
    if task_phrase:
        original_phrase = decrypt_caesar(task_phrase, input_lang)
        print(original_phrase)
