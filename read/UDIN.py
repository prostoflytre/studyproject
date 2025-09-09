import re
import os
def parse_readme_001():
    """
    Функция читает и анализирует файл README001.md, чтобы извлечь информацию.
    """
    college = None
    course = None
    name = None
    group = None
    id = None
    date = None
    
    try:
        folder_path = "c:/Users/Student/gihub 21is/studyproject/read/"
        file_path = os.path.join(folder_path, 'README001.md')
        
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
            # Извлекаем данные с помощью регулярных выражений
            college_match = re.search(r'Колледж:\s*(.+)', content)
            course_match = re.search(r'Курс:\s*(.+)', content)  # Обратите внимание на опечатку в "Курc"
            name_match = re.search(r'ФИ:\s*(.+)', content)
            group_match = re.search(r'Команда:\s*(.+)', content)  # И здесь "Команда"
            id_match = re.search(r'ID:\s*(.+)', content)  # И здесь "ID"
            update_match = re.search(r'Изменение:\s*(.+)', content)
            
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
            if update_match:
                date = update_match.group(1).strip()

                
    except FileNotFoundError:
        print("Ошибка: Файл README001.md не найден в текущей директории.")
    
    return college, course, name, group, id, date

def main():
    """
    Главная функция программы.
    """
    print("👋 Добро пожаловать в программу приветствия!")
    print("Читаю информацию из README001.md...")
    print()
    
    # Парсим данные из README001
    college, course, name, group, id, date = parse_readme_001()
    
    # Проверяем, что данные найдены
    if not all([college, course, name, group, id, date]):
        print("❌ В README001.md не найдена вся необходимая информация.")
        print("Пожалуйста, проверьте формат файла.")
        return
    for i in range(5):
        # Выводим приветствие с использованием данных из README001
        print("✅ Информация успешно получена!")
        print()
        print("=" * 50)
        print(f"Здравствуйте, {name}!") 
        print(f"Приветствуем студента {college}")
        print(f"Курс: {course}")
        print(f"Команда: {group}")
        print(f"ID: {id}")
        print(f"Изменение: {date}")
        print("=" * 50)
        print()
        print("Желаем успехов в обучении! 🚀")

# Запуск программы
if __name__ == "__main__":
    main()