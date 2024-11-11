import csv
import json

# Функція для створення початкового CSV файлу з даними
def create_initial_csv(filename='data.csv'):
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
            fieldnames = ['id', 'name', 'age']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # Запис заголовка та початкових рядків даних
            writer.writeheader()
            writer.writerow({'id': '1', 'name': 'Alice', 'age': '25'})
            writer.writerow({'id': '2', 'name': 'Bob', 'age': '30'})
            writer.writerow({'id': '3', 'name': 'Charlie', 'age': '22'})

        print("Початковий CSV файл створено.")
    except IOError as e:
        print(f"Помилка при створенні файлу CSV: {e}")

# Функція для показу вмісту CSV файлу
def show_csv(filename='data.csv'):
    try:
        with open(filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                print(row)
    except IOError as e:
        print(f"Помилка при читанні файлу CSV: {e}")

# Створення початкового CSV файлу для тестування
create_initial_csv()

# Показ початкового CSV файлу
print("Початковий CSV файл:")
show_csv()

# Меню для редагування CSV
fieldnames = ['id', 'name', 'age']
while True:
    print("\nМеню:")
    print("1. Додати запис")
    print("2. Видалити запис за ID")
    print("3. Показати CSV файл")
    print("4. Завершити та конвертувати у JSON")
    choice = input("Виберіть опцію (1-4): ")

    if choice == '1':
        new_id = input("Введіть ID: ")
        new_name = input("Введіть ім'я: ")
        new_age = input("Введіть вік: ")
        try:
            with open('data.csv', mode='a', newline='', encoding='utf-8') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writerow({'id': new_id, 'name': new_name, 'age': new_age})
            print("Запис додано.")
        except IOError as e:
            print(f"Помилка при записі у файл CSV: {e}")

    elif choice == '2':
        delete_id = input("Введіть ID для видалення: ")
        try:
            rows = []
            with open('data.csv', mode='r', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)
                rows = [row for row in reader if row['id'] != delete_id]

            with open('data.csv', mode='w', newline='', encoding='utf-8') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)
            print("Запис видалено.")
        except IOError as e:
            print(f"Помилка при обробці файлу CSV: {e}")

    elif choice == '3':
        print("Поточний вміст CSV файлу:")
        show_csv()

    elif choice == '4':
        # Конвертація CSV у JSON
        try:
            with open('data.csv', mode='r', encoding='utf-8') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                data = [row for row in csv_reader]

            with open('data.json', mode='w', encoding='utf-8') as json_file:
                json.dump(data, json_file, indent=4)

            print("Конвертація у JSON виконана успішно.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Помилка при роботі з файлами: {e}")
        break

    else:
        print("Неправильний вибір. Спробуйте ще раз.")