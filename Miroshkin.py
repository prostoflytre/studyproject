import os
import re

def read_user_metrics_from_readme(readme_path='README003.md'):
    """
    Читает файл README.md и извлекает из него метрики пользователя.
    Ожидает найти строки в формате 'Ключ: Значение'.
    Возвращает словарь с найденными метриками.
    """
    metrics = {}
    try:
        with open(readme_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # Используем регулярное выражение для поиска шаблона "Ключ: Значение"
            pattern = r'^(\w+):\s*(.+)$'
            matches = re.finditer(pattern, content, re.MULTILINE)
            
            for match in matches:
                key = match.group(1).strip()   # Например, "Name"
                value = match.group(2).strip() # Например, "Алексей"
                metrics[key] = value
                
    except FileNotFoundError:
        print(f"Ошибка: Файл '{readme_path}' не найден в текущей директории.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
    
    return metrics

def generate_greeting(metrics):
    """
    Генерирует приветственное сообщение на основе извлеченных метрик.
    """
    # Основное приветствие по имени
    name = metrics.get('ФИ')
    if name:
        greeting = f"Привет, {name}!"
    else:
        greeting = "Привет!"
    
    # Добавляем дополнительную информацию, если она есть
    additional_info = []
    if 'Группа' in metrics:
        print('==========')
        additional_info.append(f"Группа — {metrics['Группа']}")
    if 'Команда' in metrics:
        additional_info.append(f"Команда: '{metrics['Команда']}'")
    if 'ID' in metrics:
        additional_info.append(f"ID: '{metrics['ID']}'")
    
    if additional_info:
        greeting += " " + ", ".join(additional_info) + "."
        
    
    return greeting

# Главная логика программы
if __name__ == "__main__":
    # Шаг 1: Извлекаем метрики из README.md
    user_metrics = read_user_metrics_from_readme()
    
    # Шаг 2: Если метрики найдены, генерируем и выводим приветствие
    if user_metrics:
        message = generate_greeting(user_metrics)
        for i in range(5):
            print(message)
    else:
        print("Не удалось найти метрики в файле README.md для приветствия.")