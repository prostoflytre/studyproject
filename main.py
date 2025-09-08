import re

from UDIN import parse_readme_001
from Malinevskiy import parse_readme_004
from Miroshkin import parse_readme_003
from SHABANOV import parse_readme_002

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
                
            if profile == "1":
                college, course, name, group, id = parse_readme_001()
                output_in()
            if profile == "2":
                college, course, name, group, id = parse_readme_002()
                output_in()
            if profile == "3":
                college, course, name, group, id = parse_readme_003()  
                output_in()
            if profile == "4":
                college, course, name, group, id = parse_readme_004()
                output_in()
            else:
                 print("Введите иное значение")

            

        
if __name__ == "__main__":
    main()