# Weather CLI

Python-проект для получения погоды через OpenWeather API и координат городов через Geoapify API. Вывод осуществляется напрямую в консоль.

## 🎯 Цели проекта

- Освоить некоторые паттерны ООП в Python
- Получить опыт работы с внешними API и HTTP-запросами
- Научиться работать с динамической типизацией
- Научиться структурировать проект с нуля
- Практика работы с git и командной строкой

---
## 🚀 Установка

1. Склонируйте репозиторий:
```bash
git clone https://github.com/rysel0/DA-Portfolio.git
cd weather
````

2. Создайте виртуальное окружение и установите зависимости:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

3. Задайте API-ключи через переменные окружения:

P.S. Предварительно необходимо зарегистрироваться и получить API ключи на сайтах https://openweathermap.org/ и https://www.geoapify.com/

```bash
export OPENWEATHER_API_KEY="твой_ключ"    # Linux/macOS
export GEOAPIFY_API_KEY="твой_ключ"       # Linux/macOS
```

> 🔒 Ключи не хранятся в коде.

---

## 💻 Запуск

Просто запусти скрипт

```bash
python -m src
```

Пример вывода:

```
Время и дата: 2025-08-25 18:43:01
Город: Москва
Температура: 16°C
Описание погоды: Облачно
Восход: 04:01
Закат: 19:15
```

## 📦 Структура проекта

```
src/
├── __main__.py
├── config.py
├── coordinates.py
├── exceptions.py
├── weather_api_service.py
└── weather_formatter.py
venv/
requirements.txt
```

## 🛠 Используемые библиотеки

* requests
