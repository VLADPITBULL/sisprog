import psycopg2
import pandas as pd
import re

# Настройки подключения к БД PostgreSQL
DB_PARAMS = {
    "dbname": "your_db_name",      # Название БД
    "user": "your_username",       # Имя пользователя
    "password": "your_password",   # Пароль
    "host": "localhost",           # Хост (оставь localhost если у тебя локально)
    "port": 5432                   # Порт (обычно 5432)
}


def clean_number(value):
    if pd.isna(value):
        return None
    value = str(value)
    value = re.sub(r"[^\d.,]", "", value).replace(",", ".")
    try:
        return float(value)
    except ValueError:
        return None

def clean_int(value):
    if pd.isna(value):
        return None
    digits = re.findall(r"\d+", str(value))
    return int(digits[0]) if digits else None

def load_materials(cursor, filepath):
    df = pd.read_csv(filepath, sep=";")
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO materials (name, type, image_url, cost, stock_qty, min_stock, units_per_pack, unit)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row["Наименование материала"],
            row["Тип материала"],
            None if "не указано" in str(row["Изображение"]).lower() else row["Изображение"],
            clean_number(row["Цена"]),
            clean_int(row["Количество на складе"]),
            clean_int(row["Минимальное количество"]),
            clean_int(row["Количество в упаковке"]),
            row["Единица измерения"]
        ))

def load_suppliers(cursor, filepath):
    df = pd.read_csv(filepath, header=0)
    for _, row in df.iterrows():
        score_match = re.search(r"\d+", str(row[" Рейтинг качества"]))
        score = int(score_match.group()) if score_match else None
        cursor.execute("""
            INSERT INTO suppliers (name, type, inn, quality_score)
            VALUES (%s, %s, %s, %s)
        """, (
            row["Наименование поставщика"].strip(),
            row[" Тип поставщика"].strip(),
            row[" ИНН"],
            score
        ))

def load_material_supplier_links(cursor, filepath):
    df = pd.read_excel(filepath)
    
    # Получаем соответствие названия → ID из базы
    cursor.execute("SELECT id, name FROM materials")
    material_map = {name: mid for mid, name in cursor.fetchall()}

    cursor.execute("SELECT id, name FROM suppliers")
    supplier_map = {name: sid for sid, name in cursor.fetchall()}

    for _, row in df.iterrows():
        material_name = row["Наименование материала"]
        supplier_name = row["Возможный поставщик"]
        mat_id = material_map.get(material_name)
        sup_id = supplier_map.get(supplier_name)
        if mat_id and sup_id:
            cursor.execute("""
                INSERT INTO material_supplier (material_id, supplier_id)
                VALUES (%s, %s)
                ON CONFLICT DO NOTHING
            """, (mat_id, sup_id))

def main():
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        conn.autocommit = True
        cursor = conn.cursor()

        print("Загрузка materials...")
        load_materials(cursor, "materials_k_import.csv")

        print("Загрузка suppliers...")
        load_suppliers(cursor, "supplier_k_import.txt")

        print("Загрузка связей material_supplier...")
        load_material_supplier_links(cursor, "materialsupplier_k_import.xlsx")

        print("Импорт завершён успешно!")

    except Exception as e:
        print("Ошибка:", e)
    finally:
        if conn:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    main()
