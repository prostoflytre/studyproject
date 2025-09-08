import re

from UDIN import parse_readme_001
from Malinevskiy import parse_readme_004
from Miroshkin import parse_readme_003
from SHABANOV import parse_readme_002

while True:
    a = input("Ввдите номер README файла: 00")
    print("Чтобы завршить программу напиши end")
    if a == "4":
        college, course, name, group, id = parse_readme_004()
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
    if a == "3":
        college, course, name, group, id = parse_readme_003()
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
    if a == "2":
        college, course, name, group, id = parse_readme_002()
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
    if a == "1":
        college, course, name, group, id = parse_readme_001()
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
    if a == "end":
       break