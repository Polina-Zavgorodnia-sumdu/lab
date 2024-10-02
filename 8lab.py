# Словник з початковим списком студентів
students = {
    "Іванов Іван Іванович": {
        'Група': 101,
        'Курс': 2,
        'Предмети та оцінки': {
            "Математика": 85,
            "Фізика": 90,
            "Інформатика": 92,
            "Хімія": 88,
            "Біологія": 75,
            "Історія": 80
        }
    },
    "Петренко Петро Петрович": {
        'Група': 102,
        'Курс': 3,
        'Предмети та оцінки': {
            "Математика": 95,
            "Фізика": 88,
            "Інформатика": 91,
            "Хімія": 84,
            "Біологія": 77,
            "Історія": 79
        }
    }
}

# Список предметів, які будуть однаковими для всіх студентів
subjects = ["Математика", "Фізика", "Інформатика", "Хімія", "Біологія", "Історія"]

# Функція для додавання інформації про студента
def add_student(group_number, name, course, grades):
    if len(grades) != len(subjects):
        print("Кількість оцінок має відповідати кількості предметів!")
        return
    
    students[name] = {
        'Група': group_number,
        'Курс': course,
        'Предмети та оцінки': dict(zip(subjects, grades))  # Зв'язуємо предмети з оцінками
    }

# Функція для відображення всіх студентів
def show_students():
    if not students:
        print("Список студентів порожній.")
    else:
        for name, details in students.items():
            print(f"Студент: {name}")
            print(f"Номер групи: {details['Група']}")
            print(f"Курс: {details['Курс']}")
            print("Предмети та оцінки:")
            for subject, grade in details['Предмети та оцінки'].items():
                print(f"  {subject}: {grade}")
            print()

# Функція для введення даних студента з консолі
def input_student_data():
    name = input("Введіть прізвище, ім'я та по батькові студента: ")
    group_number = input("Введіть номер групи: ")
    course = input("Введіть курс: ")
    grades = []
    
    print("Введіть оцінки для наступних предметів:")
    for subject in subjects:
        grade = input(f"{subject}: ")
        grades.append(int(grade))  # Конвертуємо оцінку у ціле число
    
    add_student(group_number, name, course, grades)

# Основне меню для взаємодії з програмою
def menu():
    while True:
        print("\n1. Додати студента")
        print("2. Вивести список студентів")
        print("3. Вийти")
        choice = input("Оберіть дію (1/2/3): ")
        
        if choice == '1':
            input_student_data()
        elif choice == '2':
            show_students()
        elif choice == '3':
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

# Запуск меню
menu()
