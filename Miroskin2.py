import re

from UDIN import parse_readme_001
from SHABANOV import parse_readme_002
from Miroshkin import parse_readme_003
from Malinevskiy import parse_readme_004

def main():
    while True:
        print("\n" + "="*50)
        a = input("Введите номер README файла (1-4) или 'new' для ввода новых данных: ")
        print("Чтобы завершить программу напишите 'end'")
        
        if a.lower() == "end":
            break
        elif a.lower() == "new":
            input_new_data()
        else:
            output(a)

def input_new_data():
    """Функция для ввода новых данных пользователем"""
    print("\n" + "="*50)
    print("📝 Введите ваши данные:")
    print("="*50)
    
    college = input("Введите название учебного заведения: ")
    course = input("Введите название курса: ")
    name = input("Введите ваше ФИ: ")
    group = input("Введите название команды/группы: ")
    id = input("Введите ваш ID: ")
    
    # Выводим введенные данные
    print("\n✅ Ваши данные успешно сохранены!")
    output_custom_data(college, course, name, group, id)

def output_custom_data(college, course, name, group, id):
    """Функция для вывода пользовательских данных"""
    print("✅ Информация успешно получена!")
    print()
    
    # Выводим приветствие 5 раз
    for i in range(5):
        print("=" * 50)
        print(f"Здравствуйте, {name}!") 
        print(f"Приветствуем студента {college}")
        print(f"Курс: {course}")
        print(f"Команда: {group}")
        print(f"ID {id}")
        print("=" * 50)
        print()
    
    print("Желаем успехов в обучении! 🚀")

def output(profile):
    """Функция для вывода данных из README файлов"""
    def output_in():
        print("✅ Информация успешно получена!")
        print()
        
        # Выводим приветствие 5 раз
        for i in range(5):
            print("=" * 50)
            print(f"Здравствуйте, {name}!") 
            print(f"Приветствуем студента {college}")
            print(f"Курс: {course}")
            print(f"Команда: {group}")
            print(f"ID {id}")
            print("=" * 50)
            print()
        
        print("Желаем успехов в обучении! 🚀")
    
    # Получаем данные из соответствующего модуля
    if profile == "1":
        college, course, name, group, id = parse_readme_001()
        output_in()
    elif profile == "2":
        college, course, name, group, id = parse_readme_002()
        output_in()
    elif profile == "3":
        college, course, name, group, id = parse_readme_003()  
        output_in()
    elif profile == "4":
        college, course, name, group, id = parse_readme_004()
        output_in()
    else:
        print("❌ Неверный ввод! Введите число от 1 до 4 или 'new'")

if __name__ == "__main__":
    main()