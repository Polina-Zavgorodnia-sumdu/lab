# Ім'я файлу для спільної роботи
filename = 'students_questions.txt'

try:
    # Перевірка, чи існує файл, якщо так - читання останнього питання
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            prev_question = None
            for line in lines:
                if "Питання:" in line:
                    prev_question = line.strip()
            
            if prev_question:
                print(f"Попереднє питання: {prev_question.split('Питання: ')[1]}")
            else:
                print("Попереднього питання не знайдено.")
    except FileNotFoundError:
        print("Файл не знайдено, це перший запис.")
    
    # Введення інформації від студента
    name = input("Введіть ваше ім'я: ")
    
    if prev_question:
        answer = input("Введіть відповідь на попереднє питання: ")
    else:
        answer = "Немає попереднього питання, тому відповідь не потрібна."
    
    new_question = input("Введіть нове питання з програмування мовою Python, на яке відповість наступний студент: ")
    
    # Запис даних до файлу
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f"Ім'я: {name}\n")
        if prev_question:
            file.write(f"Відповідь: {answer}\n")
        file.write(f"Питання: {new_question}\n")
        file.write("Відповідь: \n")  # Місце для відповіді наступного студента
    
    print(f"Ваші дані та нове питання успішно записані до файлу {filename}.")
    
except IOError:
    print("Помилка: неможливо записати дані у файл.")
