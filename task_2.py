try:
    search_word = input("Введите слово для поиска: ")

    with open("resource/text.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    found_lines = []
    count = 0

    for i in range(len(lines)):
        line = lines[i]
        words = line.split()
        if search_word in words:
            count += words.count(search_word)
            found_lines.append(i + 1)  
    if count > 0:
        print("Слово найдено!")
        print("Количество раз:", count)
        print("Строки:", found_lines)
    else:
        print("Слово не найдено")

    with open("resource/search_results.txt", "w", encoding="utf-8") as result_file:
        result_file.write("Искомое слово: " + search_word + "\n")
        result_file.write("Найдено: " + ("да" if count > 0 else "нет") + "\n")
        result_file.write("Количество: " + str(count) + "\n")
        result_file.write("Строки: " + str(found_lines) + "\n")

    print("Результат сохранен в search_results.txt")

except FileNotFoundError:
    print("Ошибка: Файл text.txt не найден!")
    print("Создайте файл text.txt в папке с программой")
