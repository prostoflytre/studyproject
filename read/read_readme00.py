import re
import os
from pathlib import Path
import time

# Получение абсолютного пути к папке с README файлами (текущая директория скрипта)
def get_readme_folder():
    # Получаем путь к директории, где находится скрипт
    return str(Path(__file__).parent)

# Main функция
def main():
    global people
    global last_file_check
    global folder_path
    
    folder_path = get_readme_folder()
    people, last_file_check = list_readme_files()
    
    while True:
        print("\n" + "="*50)
        print("Чтобы завершить программу напишите 'end'")
        a = input(f"Введите номер файла README00{people} или 'new' для ввода новых данных: ")
        
        # Проверка введённых пользователем данных
        if a.lower() == "end":
            break
        elif a.lower() == "new":
            add_new_user()
        else:
            parse_readme(a)
            
# Показывает список существующих README00* файлов
def list_readme_files():
    global folder_path
    print("\nСУЩЕСТВУЮЩИЕ ФАЙЛЫ:")
    print("-" * 30)
    print(f"Путь к папке: {folder_path}")
    
    readme_files = [f for f in os.listdir(folder_path) if f.startswith('README00') and f.endswith('.md')]
    
    if not readme_files:
        print("Файлы не найдены в папке.")
        return [], time.time()
    
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
    
    return people, time.time()

# Проверка изменений в файловой системе
def check_for_file_changes(previous_files, previous_check_time):
    global folder_path
    
    # Получаем текущий список файлов
    current_files = [f for f in os.listdir(folder_path) if f.startswith('README00') and f.endswith('.md')]
    current_files.sort()
    
    # Проверяем новые файлы
    new_files = [f for f in current_files if f not in [f"README00{x}.md" for x in previous_files]]
    
    # Проверяем удаленные файлы
    deleted_files = [f for f in [f"README00{x}.md" for x in previous_files] if f not in current_files]
    
    # Выводим сообщения об изменениях
    if new_files:
        print(f"\n⚠️  Обнаружены новые файлы: {', '.join(new_files)}")
    
    if deleted_files:
        print(f"\n⚠️  Файлы были удалены: {', '.join(deleted_files)}")
    
    return current_files != [f"README00{x}.md" for x in previous_files]

# Проверка существования файла
def check_file_exists(file_number):
    global folder_path
    file_path = os.path.join(folder_path, f"README00{file_number}.md")
    return os.path.exists(file_path)

# Получение следующего доступного номера файла
def get_next_available_number():
    global folder_path
    
    readme_files = [f for f in os.listdir(folder_path) if f.startswith('README00') and f.endswith('.md')]
    
    if not readme_files:
        return 1
    
    # Извлекаем номера из всех файлов
    numbers = []
    for file in readme_files:
        number_str = file.replace('README00', '').replace('.md', '')
        if number_str.isdigit():
            numbers.append(int(number_str))
    
    if numbers:
        return max(numbers) + 1
    else:
        return 1

# Создание нового пользователя
def add_new_user():
    global people, last_file_check, folder_path
    
    # Проверяем изменения в файловой системе перед созданием
    if check_for_file_changes(people, last_file_check):
        print("⚠️  Обнаружены изменения в файловой системе! Обновляю список файлов...")
        people, last_file_check = list_readme_files()
    
    # Получаем следующий доступный номер
    new_number = get_next_available_number()
    
    # Двойная проверка, что файл не существует
    if check_file_exists(new_number):
        print(f"⚠️ Файл README00{new_number}.md уже существует!")
        # Обновляем список файлов
        people, last_file_check = list_readme_files()
        return None
    
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
    file_path = os.path.join(folder_path, f'README00{new_number}.md')
    
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"\n✅ Файл README00{new_number}.md успешно создан!")
        print(f"Путь: {file_path}")
        
        # Проверяем, не появился ли вдруг такой файл во время создания
        time.sleep(0.1)  # небольшая задержка для файловой системы
        if check_for_file_changes(people, last_file_check):
            print("⚠️  Обнаружены изменения во время создания файла!")
            people, last_file_check = list_readme_files()
        else:
            people.append(str(new_number))
            
        return college, course, name, group, id
        
    except Exception as e:
        print(f"❌ Ошибка при создании файла: {e}")
        return None

# Получение значений из README файла и их вывод
def parse_readme(a):
    global people, last_file_check, folder_path
    
    # Проверяем изменения в файловой системе перед чтением
    if check_for_file_changes(people, last_file_check):
        print("⚠️  Обнаружены изменения в файловой системе! Обновляю список файлов...")
        people, last_file_check = list_readme_files()
    
    college = ""
    course = ""
    name = ""
    group = ""
    id = ""
    
    file_path = os.path.join(folder_path, f'README00{a}.md')
    
    # Проверяем, существует ли файл
    if not os.path.exists(file_path):
        print(f"❌ Файл README00{a}.md не найден!")
        print(f"Путь: {file_path}")
        
        # Проверяем, был ли этот файл в исходном списке
        if a in people:
            print(f"⚠️  Файл README00{a}.md был удален!")
        
        b = input("Хотите добавить нового пользователя? (Да/Нет)\n") 
        if b.lower() in ['да', 'д', 'yes', 'y']:
            add_new_user()
        else:
            print("Возвращаемся назад.")
        return None, None, None, None, None
    
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
    
    except Exception as e:
        print(f"❌ Ошибка при чтении файла: {e}")
    
    return college, course, name, group, id

# Запуск main функции
if __name__ == "__main__":
    main()