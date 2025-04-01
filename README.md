# 📘 Проект управления производственной системой

## 🧾 Содержание

1. [Описание проекта](#описание-проекта)
2. [Структура репозитория](#структура-репозитория)
3. [Установка и настройка](#установка-и-настройка)
4. [Часть 1: Структура БД и импорт данных](#часть-1-структура-бд-и-импорт-данных)
5. [Часть 2: Подсистема материалов (PyQt)](#часть-2-подсистема-материалов-pyqt)
6. [Часть 3: Интерфейс работы с партнёрами (PyQt)](#часть-3-интерфейс-работы-с-партнёрами-pyqt)
7. [Тестирование](#тестирование)

## 📌 Описание проекта

Проект предназначен для автоматизации производственного учета: управление материалами, партнёрами и заявками. Реализован с использованием Python, PostgreSQL и PyQt5.

## 📁 Структура репозитория

```
├── init_db.sql                # SQL-структура базы PostgreSQL
├── import_data.py            # Импорт данных из CSV/XLSX/TXT
├── materials_subsystem/      # Подсистема материалов
│   ├── main.py
│   ├── db.py
│   ├── models.py
│   ├── views.py
│   ├── controllers.py
│   ├── calculation.py
│   └── tests/
│       └── test_calculation.py
├── partners_module/          # Подсистема партнёров
│   ├── main.py
│   ├── views.py
│   ├── controllers.py
│   ├── models.py
│   └── partner_dialog.py
├── requirements.txt
└── README.md
```

## ⚙️ Установка и настройка

### Установка зависимостей

```bash
pip install -r requirements.txt
```

### PostgreSQL

1. Установите PostgreSQL
2. Создайте базу:

```bash
createdb your_db_name
```

3. Примените SQL-структуру:

```bash
psql -U your_username -d your_db_name -f init_db.sql
```

## 🔹 Часть 1: Структура БД и импорт данных

### 📂 Файлы импорта:
- `materials_k_import.csv`
- `supplier_k_import.txt`
- `materialsupplier_k_import.xlsx`

### 🐍 Запуск импорта:

```bash
python import_data.py
```

> Убедись, что параметры подключения в `import_data.py` указаны верно.

## 🔹 Часть 2: Подсистема материалов (PyQt)

### 📦 Возможности:
- Просмотр всех материалов
- Поиск по названию
- Поставщики и остатки
- Метод `get_quantity_for_product`

### ▶️ Запуск:

```bash
cd materials_subsystem
python main.py
```

## 🔹 Часть 3: Интерфейс работы с партнёрами (PyQt)

### 📦 Возможности:
- Просмотр партнёров
- Добавление, редактирование, удаление (CRUD)
- Пагинация
- Обработка ошибок (ввод, пустые поля, ошибки БД)

### ▶️ Запуск:

```bash
cd partners_module
python main.py
```

## ✅ Тестирование

В папке `materials_subsystem/tests`:

```bash
pytest test_calculation.py
```

## 📦 requirements.txt

```txt
PyQt5
psycopg2
SQLAlchemy
pandas
openpyxl
pytest
```

## 🧠 Автор

**Тестовое задание для производственной системы «Мастер пол»**
