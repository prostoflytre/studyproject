import re

from UDIN import parse_readme_001
from SHABANOV import parse_readme_002
from Miroshkin import parse_readme_003
from Malinevskiy import parse_readme_004

def main():

    while True:
        a = input("Ввдите номер README файла: 00")
        print("Чтобы завршить программу напиши end")
        if a == "end":
            break
        else:
              output(a)


def output(profile):
            
            def output_in():
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

            def input_new():
                    Kollej = input("Введите название колледжа: ") 
                    Kurs = input("Введите название курса: ") 
                    FI = input("Введите ваше ФИ (через пробел): ") 
                    Team = input("Введите название команды: ")
                    ID = input("Введите ваш ID: ")
                    content =f"""
# studyproject
Колледж: {Kollej}
Курc: {Kurs}
ФИ: {FI}
Команда: {Team} 
ID: {ID}
                    """
                    with open('REDMEENEW.md', 'w', encoding='utf-8') as file:
                        file.write(content)
                    return Kollej, Kurs, FI, Team, ID
                
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
                b = input("Хотите добавить нового пользователя? (Да/Нет)\n") 
                if b == "Да":
                    college, course, name, group, id = input_new()
                    output_in()
        
if __name__ == "__main__":
    main()