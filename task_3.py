files = ["file1.txt", "file2.txt", "file3.txt"]
all_exist = True

for file_name in files:
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            pass
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_name} не найден!")
        all_exist = False

if all_exist:
    with open("resource/combined.txt", "w", encoding="utf-8") as combined:
        for i, file_name in enumerate(files):
            with open(file_name, "r", encoding="utf-8") as f:
                content = f.read()
            combined.write(f"\n=== Содержимое {file_name} ===\n")
            combined.write(content)