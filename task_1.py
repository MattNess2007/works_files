try:
    with open("resource/input.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    line_count = len(lines)

    word_count = 0
    for line in lines:
        words = line.split()
        word_count += len(words)

    with open("resource/statistics.txt", "w", encoding="utf-8") as result_file:
        result_file.write("Количество строк: " + str(line_count) + "\n")
        result_file.write("Количество слов: " + str(word_count) + "\n")

    print("Готово! Результат в файле statistics.txt")
    print("Строк:", line_count)
    print("Слов:", word_count)

except FileNotFoundError:
    print("Ошибка: Файл input.txt не найден!")
    print("Создайте файл input.txt в папке с программой")