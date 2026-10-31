"""Генерация практического датасета для Module 01: Excel"""
import csv
import random
import datetime

random.seed(42)

# Справочные данные
products = {
    "Электроника": [
        ("Смартфон Samsung Galaxy", 29990), ("Наушники Sony WH-1000XM5", 24990),
        ("Планшет iPad Air", 54990), ("Ноутбук ASUS VivoBook", 45990),
        ("Умные часы Apple Watch", 32990), ("Портативная колонка JBL", 5990),
        ("Зарядное устройство Anker", 1990), ("Кабель USB-C", 490),
        ("Чехол для смартфона", 890), ("Внешний аккумулятор Xiaomi", 2490),
    ],
    "Одежда": [
        ("Футболка базовая", 1290), ("Джинсы классические", 3990),
        ("Куртка зимняя", 8990), ("Кроссовки Nike Air", 7990),
        ("Шапка вязаная", 990), ("Рубашка офисная", 2490),
        ("Свитер шерстяной", 3490), ("Носки набор 5 пар", 690),
    ],
    "Дом и сад": [
        ("Кофемашина De'Longhi", 19990), ("Набор полотенец", 1890),
        ("Подушка ортопедическая", 2990), ("Лампа настольная LED", 1490),
        ("Набор кастрюль", 4990), ("Ваза керамическая", 1290),
        ("Плед флисовый", 1990), ("Коврик для ванной", 790),
    ],
    "Книги": [
        ("Python для начинающих", 890), ("Thinking Fast and Slow", 690),
        ("Sapiens: Краткая история", 790), ("Atomic Habits", 590),
        ("Мастер и Маргарита", 490), ("1984 Джордж Оруэлл", 390),
        ("Гарри Поттер и философский камень", 690), ("Код да Винчи", 490),
    ],
    "Продукты": [
        ("Кофе молотый Lavazza 250г", 590), ("Чай Ahmad Earl Grey 100п", 390),
        ("Шоколад Lindt 100г", 290), ("Мёд натуральный 500г", 490),
        ("Оливковое масло 500мл", 690), ("Паста Barilla 500г", 190),
        ("Орехи кешью 200г", 390), ("Гранола 400г", 290),
    ],
}

cities = [
    "Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань",
    "Нижний Новгород", "Челябинск", "Самара", "Ростов-на-Дону", "Уфа",
    "Краснодар", "Воронеж", "Пермь", "Волгоград", "Красноярск",
]

payment_methods = ["Карта Visa", "Карта MasterCard", "СБП", "Наличные", "Apple Pay", "Google Pay"]

# Весовые коэффициенты городов (Москва и СПб чаще)
city_weights = [25, 18, 8, 7, 7, 5, 5, 4, 5, 4, 5, 3, 3, 3, 3]

start_date = datetime.date(2026, 1, 1)
end_date = datetime.date(2026, 9, 30)
date_range = (end_date - start_date).days

rows = []
customer_ids = [f"CUST-{i:04d}" for i in range(1, 301)]

for i in range(1, 1001):
    order_id = f"ORD-{i:05d}"
    order_date = start_date + datetime.timedelta(days=random.randint(0, date_range))
    customer_id = random.choice(customer_ids)
    
    category = random.choices(list(products.keys()), weights=[30, 20, 15, 15, 20])[0]
    product_name, base_price = random.choice(products[category])
    
    quantity = random.choices([1, 2, 3, 4, 5], weights=[50, 25, 15, 7, 3])[0]
    
    # Вариация цены ±10%
    price = round(base_price * random.uniform(0.9, 1.1), 2)
    
    city = random.choices(cities, weights=city_weights)[0]
    payment = random.choice(payment_methods)
    
    # === Внедряем "грязные" данные ===
    r = random.random()
    
    # ~3% пустые customer_id
    if r < 0.03:
        customer_id = ""
    
    # ~2% цена = 0 или отрицательная
    if 0.03 <= r < 0.05:
        price = random.choice([0, -price, ""])
    
    # ~2% дублированный order_id (повтор предыдущего)
    if 0.05 <= r < 0.07 and len(rows) > 0:
        order_id = rows[-1][0]
    
    # ~2% несогласованный формат города
    if 0.07 <= r < 0.09:
        city = random.choice(["москва", "МОСКВА", " Москва ", "Мск", "С-Петербург", "спб"])
    
    # ~2% пропущенная категория
    if 0.09 <= r < 0.11:
        category = ""
    
    # ~1% некорректная дата (как строка)
    if 0.11 <= r < 0.12:
        order_date = random.choice(["31/13/2026", "not_a_date", "2026.13.01"])
    else:
        order_date = order_date.strftime("%Y-%m-%d")
    
    # ~1% quantity как текст
    if 0.12 <= r < 0.13:
        quantity = random.choice(["два", "N/A", ""])
    
    rows.append([order_id, order_date, customer_id, product_name, category, quantity, price, city, payment])

# Записываем CSV
output_path = r"d:\vibe_app\main_data_analytics\course\module_01_excel\exercises\practice_dataset.csv"
with open(output_path, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["order_id", "date", "customer_id", "product", "category", "quantity", "price", "city", "payment_method"])
    writer.writerows(rows)

print(f"Generated {len(rows)} rows -> {output_path}")
