import re

def read_metrics_from_readme():
    """Читает файл README002.md и извлекает метрики."""
    metrics = {}
    try:
        with open('README002.md', 'r', encoding='utf-8') as file:
            content = file.read()
            
            # Используем регулярные выражения для поиска шаблона: **Ключ:** Значение
            pattern = r'\*\*(\w+)\*\*:\s*([^\n]+)'
            matches = re.findall(pattern, content)
            
            for key, value in matches:
                metrics[key.lower()] = value.strip() # Сохраняем в словарь в нижнем регистре
                
    except FileNotFoundError:
        print("Ошибка: Файл README.md не найден в корне проекта.")
    return metrics

def generate_greeting(metrics):
    """Генерирует приветствие на основе найденных метрик."""
    name = metrics.get('имя', 'Незнакомец')
    city = metrics.get('город', 'неизвестного города')
    course = metrics.get('курс', 'неизвестного курса')
    mood = metrics.get('настроение', 'загадочное')
    
    greeting = f"""
    Привет, {name}!
    Добро пожаловать с {city} на курс {course}!
    Рад видеть, что ваше настроение сегодня {mood}!
    """
    return greeting

if __name__ == "__main__":
    # Получаем метрики
    user_metrics = read_metrics_from_readme()
    
    # Генерируем и выводим приветствие
    if user_metrics: # Если метрики найдены
        message = generate_greeting(user_metrics)
        print(message)
    else:
        print("Не удалось извлечь метрики для приветствия.")