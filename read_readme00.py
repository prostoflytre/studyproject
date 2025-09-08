import re
import os

def list_readme_files():
    """Показывает список существующих README00{people} файлов в папке studyproject/Информация о пользователях"""
    folder_path = r'studyproject/Информация о пользователях'
    
    # Проверяем существование папки
    if not os.path.exists(folder_path):
        print(f"Папка '{folder_path}' не найдена!")
        return []
    
    print("\nСУЩЕСТВУЮЩИЕ ФАЙЛЫ:")
    print("-" * 30)
    
    readme_files = [f for f in os.listdir(folder_path) if f.startswith('README00') and f.endswith('.md')]
    
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
    
    return people, folder_path

people, folder_path = list_readme_files()

def add_new_user():
    new = int(people[-1]) + 1 if people else 1
    people.append(str(new))
    
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
    # Создаем папку, если она не существует
    os.makedirs(folder_path, exist_ok=True)
    
    file_path = os.path.join(folder_path, f'README00{new}.md')
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"\n✅ Файл README00{new}.md успешно создан в папке {folder_path}!")
    return college, course, name, group, id

def parse_readme(a):
    college = ""
    course = ""
    name = ""
    group = ""
    id = ""
    
    file_path = os.path.join(folder_path, f'README00{a}.md')
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
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

            print("✅ Информация успешно получена!")
            print()
            print("=" * 50)
            print(f"Здравствуйте, {name}!") 
            print(f"Приветствуем студента {college}")
            print(f"Курс: {course}")
            print(f"Команда: {group}")
            print(f"ID {id}")
            print("=" * 50)
            print()
            print("Желаем успехов в обучении! 🚀")
                
    except FileNotFoundError:
        b = input("Хотите добавить нового пользователя? (Да/Нет)\n") 
        if b.lower() in ['да', 'д', 'yes', 'y']:
            add_new_user()
        else:
            print("Возвращаемся назад.")
    
    return college, course, name, group, id


while True:
    print("\n" + "="*50)
    print("Чтобы завершить программу напишите 'end'")
    
    if people:
        a = input(f"Введите номер файла README00{people} или 'new' для ввода новых данных: ")
    else:
        a = input("Файлы не найдены. Введите 'new' для создания нового файла или 'end' для выхода: ")

    if a.lower() == "end":
        break
    elif a.lower() == "new":
        add_new_user()
    else:
        parse_readme(a)