import re
import os
# Main фаункция
def main():
    while True:
        print("\n" + "="*50)
        print("Чтобы завершить программу напишите 'end'")
        a = input(f"Введите номер файла READM00{people} или 'new' для ввода новых данных: ")
        
        # Проверка введённых пользователем данных
        if a.lower() == "end":
            break
        elif a.lower() == "new":
            add_new_user()
        else:
            parse_readme(a)
            
# Показывает список существующих README00* файлов
def list_readme_files():
    print("\nСУЩЕСТВУЮЩИЕ ФАЙЛЫ:")
    print("-" * 30)
    
    readme_files = [f for f in os.listdir('.') if f.startswith('README00') and f.endswith('.md')]
    
    if not readme_files:
        print("Файлы не найдены")
        return []
    
    # Сортируем файлы по номеру
    readme_files.sort()
    
    people = []
    for file in readme_files:
        # Извлекаем номер из имени файла
        number = file.replace('README00', '').replace('.md', '')
        if number.isdigit():
            number = int(number)
        else:
            number = number.lstrip('0')
        
        print(f"- {file} (номер: {number})")
        people.append(str(number))
    
    return people

people = list_readme_files()

# Создание нового пользователя
def add_new_user():
    new = people[-1] + 1
    people.append(new)
    college = input("Введите название колледжа: ") 
    course = input("Введите название курса: ") 
    name = input("Введите ваше ФИ (через пробел): ") 
    group = input("Введите название команды: ")
    id = input("Введите ваш ID: ")
    content =f"""
# studyproject
Колледж: {college}
Курс: {course}
ФИ: {name}
Команда: {group} 
ID: {id}
"""
    # Создание файла нового пользователя
    with open(f'README00{new}.md', 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"\n✅ Файл README00{new}.md успешно создан!")
    return college, course, name, group, id

# Получение значений из README файла и их вывод
def parse_readme(a):
    college = ""
    course = ""
    name = ""
    group = ""
    id = ""
    try:
        with open(f'README00{a}.md', 'r', encoding='utf-8') as file:
            content = file.read()
            
            # Извлекаем данные с помощью регулярных выражений
            college_match = re.search(r'Колледж:\s*(.+)', content)
            course_match = re.search(r'Курс:\s*(.+)', content)  
            name_match = re.search(r'ФИ:\s*(.+)', content)
            group_match = re.search(r'Команда:\s*(.+)', content) 
            id_match = re.search(r'ID:\s*(.+)', content) 
            
            if college_match:
                college = college_match.group(1).strip()
            if course_match:
                course = course_match.group(1).strip()
            if name_match:
                name = name_match.group(1).strip()
            if group_match:
                group = group_match.group(1).strip()
            if id_match:
                id = id_match.group(1).strip()

            # Вывод данных существующего пользователя
            print("✅ Информация успешно получена!")
            print()
            print("=" * 50)
            print(f"Здравствуйте, {name}!") 
            print(f"Приветствуем студента {college}")
            print(f"Курс: {course}")
            print(f"Команда: {group}")
            print(f"ID: {id}")
            print("=" * 50)
            print()
            print("Желаем успехов в обучении! 🚀")
    # Запрос на создание нового пользователя            
    except FileNotFoundError:
        b = input("Хотите добавить нового пользователя? (Да/Нет)\n") 
        if b.lower() in ['да', 'д', 'yes', 'y']:
            add_new_user()
        else:
            print("Возвращаемся назад.")
    
    return college, course, name, group, id

# Запуск main функции
if __name__ == "__main__":
    main()