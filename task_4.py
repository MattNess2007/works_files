def encrypt(text):
    result = ""
    for char in text:
        if 'а' <= char <= 'я' or 'А' <= char <= 'Я':
            if char.islower():
                result += chr((ord(char) - ord('а') + 3) % 32 + ord('а'))
            else:
                result += chr((ord(char) - ord('А') + 3) % 32 + ord('А'))
        else:
            result += char
    return result


def decrypt(text):
    result = ""
    for char in text:
        if 'а' <= char <= 'я' or 'А' <= char <= 'Я':
            if char.islower():
                result += chr((ord(char) - ord('а') - 3) % 32 + ord('а'))
            else:
                result += chr((ord(char) - ord('А') - 3) % 32 + ord('А'))
        else:
            result += char
    return result


try:
    with open("resource/secret.txt", "r", encoding="utf-8") as file:
        secret_text = file.read()

    encrypted_text = encrypt(secret_text)

    with open("resource/encrypted.txt", "w", encoding="utf-8") as enc_file:
        enc_file.write(encrypted_text)

    print("Шифрование выполнено!")
    print("Оригинальный текст:", secret_text)
    print("Зашифрованный текст:", encrypted_text)

    with open("resource/encrypted.txt", "r", encoding="utf-8") as enc_file:
        encrypted_text = enc_file.read()

    decrypted_text = decrypt(encrypted_text)

    with open("resource/decrypted.txt", "w", encoding="utf-8") as dec_file:
        dec_file.write(decrypted_text)

    print("Расшифровка выполнена!")
    print("Расшифрованный текст:", decrypted_text)
    print("Созданы файлы: encrypted.txt и decrypted.txt")

except FileNotFoundError:
    print("Ошибка: Файл secret.txt не найден!")
    print("Создайте файл secret.txt в папке с программой")