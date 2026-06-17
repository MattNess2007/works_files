try:
    with open("resource/words.txt", "r", encoding="utf-8") as file:
        words = []
        for line in file:
            word = line.strip()
            if word:
                words.append(word)

    if len(words) == 0:
        print("Файл words.txt пуст!")
    else:
        alphabetical = sorted(words)

        by_length = sorted(words, key=len)

        reverse_alpha = sorted(words, reverse=True)

        with open("resource/sorted_alphabetically.txt", "w", encoding="utf-8") as f:
            for item in alphabetical:
                f.write(item + "\n")

        with open("resource/sorted_by_length.txt", "w", encoding="utf-8") as f:
            for item in by_length:
                f.write(item + "\n")

        with open("resource/sorted_reverse.txt", "w", encoding="utf-8") as f:
            for item in reverse_alpha:
                f.write(item + "\n")

except FileNotFoundError:
    print("Ошибка: Файл words.txt не найден!")
    print("Создайте файл words.txt в папке с программой")