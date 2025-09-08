import re

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
            parse_readme(a)


def input_new(profile):
                    
                    Kollej = input("Введите название колледжа: ") 
                    Kurs = input("Введите название курса: ") 
                    FI = input("Введите ваше ФИ (через пробел): ") 
                    Team = input("Введите название команды: ")
                    ID = input("Введите ваш ID: ")
                    content =f"""
# studyproject
Колледж: {Kollej}
Курс: {Kurs}
ФИ: {FI}
Команда: {Team} 
ID: {ID}
                    """
                    with open(f'README00{profile}.md', 'w', encoding='utf-8') as file:
                        file.write(content)
                    return Kollej, Kurs, FI, Team, ID

def parse_readme(number):
    """
    Функция читает и анализирует файл READMEE.md, чтобы извлечь информацию.
    """
    college = None
    course = None
    name = None
    group = None
    id = None
    
    try:
        with open(f'README00{number}.md', 'r', encoding='utf-8') as file:
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
        if b == "Да":
            input_new(number)
    
    return college, course, name, group, id


        
if __name__ == "__main__":
    main()