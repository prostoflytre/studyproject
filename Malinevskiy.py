import re

def parse_readme():
    """
    Функция читает и анализирует файл ID207621431.md, чтобы извлечь информацию.
    """
    college = None
    course = None
    name = None
    group = None
    
    try:
        with open('ID207621431.md', 'r', encoding='utf-8') as file:
            content = file.read()
            
            # Извлекаем данные с помощью регулярных выражений
            college_match = re.search(r'Колледж:\s*(.+)', content)
            course_match = re.search(r'Курс:\s*(.+)', content)  # Обратите внимание на опечатку в "Курc"
            name_match = re.search(r'ФИ:\s*(.+)', content)
            group_match = re.search(r'Команда:\s*(.+)', content)  # И здесь "Команда"
            id_match = re.search(r'ID:\s*(.+)', content)  # И здесь "Команда"
            
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
                
    except FileNotFoundError:
        print("Ошибка: Файл ID207621431.md не найден в текущей директории.")
    
    return college, course, name, group, id

def main():
    """
    Главная функция программы.
    """
    print("👋 Добро пожаловать в программу приветствия!")
    print("Читаю информацию из ID207621431.md...")
    print()
    
    # Парсим данные из README
    college, course, name, group, id = parse_readme()
    
    # Проверяем, что данные найдены
    if not all([college, course, name, group, id]):
        print("❌ В README.md не найдена вся необходимая информация.")
        print("Пожалуйста, проверьте формат файла.")
        return
    
    
    # Выводим приветствие с использованием данных из README
    for i in range(5):
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

# Запуск программы

if __name__ == "__main__":
    main()