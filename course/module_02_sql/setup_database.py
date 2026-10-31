"""
setup_database.py — Создание учебной базы данных ecommerce.db

Скрипт создаёт SQLite базу данных интернет-магазина с реалистичными данными.
Таблицы: customers (500), products (100), orders (5000), order_items (15000).
Включает "грязные" данные: NULL, дубликаты, аномалии — для практики очистки.

Использование:
    python setup_database.py
    # или в Colab:
    # !python setup_database.py
"""

import sqlite3
import random
import string
from datetime import datetime, timedelta

# --- Конфигурация ---
DB_NAME = "ecommerce.db"
SEED = 42  # Фиксированный seed для воспроизводимости
random.seed(SEED)

# --- Справочные данные ---

FIRST_NAMES_MALE = [
    "Александр", "Дмитрий", "Максим", "Сергей", "Андрей",
    "Алексей", "Артём", "Илья", "Кирилл", "Михаил",
    "Никита", "Матвей", "Роман", "Егор", "Арсений",
    "Иван", "Денис", "Евгений", "Даниил", "Тимофей",
    "Владислав", "Игорь", "Владимир", "Павел", "Руслан",
    "Марк", "Константин", "Тимур", "Олег", "Ярослав",
    "Антон", "Николай", "Глеб", "Данил", "Савелий",
    "Вадим", "Степан", "Юрий", "Богдан", "Артур"
]

FIRST_NAMES_FEMALE = [
    "Анна", "Мария", "Елена", "Дарья", "Алина",
    "Ирина", "Екатерина", "Ольга", "Татьяна", "Наталья",
    "Юлия", "Виктория", "Полина", "Анастасия", "Кристина",
    "Светлана", "Валерия", "Софья", "Вера", "Александра",
    "Маргарита", "Людмила", "Марина", "Ксения", "Диана",
    "Надежда", "Лариса", "Оксана", "Галина", "Елизавета",
    "Варвара", "Милана", "Алиса", "Ева", "Арина",
    "Карина", "Яна", "Злата", "Нина", "Таисия"
]

LAST_NAMES_MALE = [
    "Иванов", "Петров", "Сидоров", "Козлов", "Новиков",
    "Морозов", "Волков", "Алексеев", "Лебедев", "Семёнов",
    "Егоров", "Павлов", "Кузнецов", "Степанов", "Николаев",
    "Орлов", "Андреев", "Макаров", "Никитин", "Захаров",
    "Зайцев", "Соловьёв", "Борисов", "Яковлев", "Григорьев",
    "Романов", "Воробьёв", "Сергеев", "Кузьмин", "Фролов",
    "Александров", "Дмитриев", "Королёв", "Гусев", "Киселёв",
    "Ильин", "Максимов", "Поляков", "Сорокин", "Виноградов"
]

LAST_NAMES_FEMALE = [
    "Иванова", "Петрова", "Сидорова", "Козлова", "Новикова",
    "Морозова", "Волкова", "Алексеева", "Лебедева", "Семёнова",
    "Егорова", "Павлова", "Кузнецова", "Степанова", "Николаева",
    "Орлова", "Андреева", "Макарова", "Никитина", "Захарова",
    "Зайцева", "Соловьёва", "Борисова", "Яковлева", "Григорьева",
    "Романова", "Воробьёва", "Сергеева", "Кузьмина", "Фролова",
    "Александрова", "Дмитриева", "Королёва", "Гусева", "Киселёва",
    "Ильина", "Максимова", "Полякова", "Сорокина", "Виноградова"
]

CITIES = [
    "Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург",
    "Казань", "Нижний Новгород", "Челябинск", "Самара",
    "Омск", "Ростов-на-Дону", "Уфа", "Красноярск",
    "Воронеж", "Пермь", "Волгоград", "Краснодар",
    "Тюмень", "Саратов", "Тольятти", "Ижевск",
    "Барнаул", "Иркутск", "Ульяновск", "Хабаровск",
    "Владивосток", "Ярославль", "Махачкала", "Томск",
    "Оренбург", "Кемерово"
]

# Веса городов — крупные города чаще
CITY_WEIGHTS = [
    20, 15, 5, 5, 5, 4, 3, 3, 3, 4,
    3, 3, 3, 3, 3, 4, 3, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2, 2, 2
]

EMAIL_DOMAINS = [
    "gmail.com", "yandex.ru", "mail.ru", "outlook.com",
    "rambler.ru", "inbox.ru", "bk.ru", "list.ru"
]

# Категории и товары
CATEGORIES = {
    "Электроника": [
        ("Смартфон Samsung Galaxy S24", 79990),
        ("Смартфон iPhone 15", 89990),
        ("Ноутбук ASUS VivoBook", 54990),
        ("Ноутбук Lenovo IdeaPad", 47990),
        ("Планшет iPad Air", 59990),
        ("Планшет Samsung Tab S9", 49990),
        ("Наушники Sony WH-1000XM5", 29990),
        ("Наушники Apple AirPods Pro", 24990),
        ("Умные часы Apple Watch", 39990),
        ("Умные часы Samsung Galaxy Watch", 27990),
        ("Портативная колонка JBL", 7990),
        ("Фитнес-браслет Xiaomi", 4990),
        ("Электронная книга Kindle", 12990),
        ("Веб-камера Logitech C920", 8990),
        ("Внешний аккумулятор 20000 mAh", 2990),
    ],
    "Одежда": [
        ("Куртка зимняя мужская", 12990),
        ("Куртка зимняя женская", 14990),
        ("Джинсы классические", 4990),
        ("Платье летнее", 3990),
        ("Футболка хлопковая", 1490),
        ("Рубашка деловая", 3490),
        ("Свитер шерстяной", 5990),
        ("Спортивный костюм", 6990),
        ("Пальто демисезонное", 15990),
        ("Шорты летние", 1990),
        ("Толстовка с капюшоном", 3490),
        ("Юбка миди", 2990),
        ("Брюки классические", 4490),
        ("Кроссовки беговые", 7990),
        ("Ботинки зимние", 9990),
    ],
    "Книги": [
        ("Python для начинающих", 890),
        ("SQL за 10 минут", 690),
        ("Чистый код", 1290),
        ("Думай медленно, решай быстро", 790),
        ("Атомные привычки", 690),
        ("Sapiens: Краткая история", 890),
        ("1984 (Оруэлл)", 390),
        ("Мастер и Маргарита", 490),
        ("Гарри Поттер (коллекция)", 3990),
        ("Data Science с нуля", 1190),
        ("Искусство войны", 290),
        ("Маленький принц", 390),
        ("Психология влияния", 790),
        ("Финансовая грамотность", 590),
        ("Алгоритмы. Руководство", 1490),
    ],
    "Дом и сад": [
        ("Кофемашина DeLonghi", 34990),
        ("Робот-пылесос Xiaomi", 24990),
        ("Набор кастрюль (6 шт)", 8990),
        ("Постельное бельё сатин", 4990),
        ("Настольная лампа LED", 2490),
        ("Увлажнитель воздуха", 5990),
        ("Набор полотенец (4 шт)", 1990),
        ("Электрочайник стальной", 3490),
        ("Блендер погружной", 4490),
        ("Набор для сада (инструменты)", 3990),
        ("Ваза декоративная", 1490),
        ("Подушка ортопедическая", 3990),
        ("Одеяло бамбуковое", 5490),
        ("Сковорода антипригарная", 2990),
        ("Органайзер для хранения", 1290),
    ],
    "Спорт": [
        ("Гантели разборные 20 кг", 6990),
        ("Коврик для йоги", 1490),
        ("Велосипед горный", 29990),
        ("Самокат электрический", 34990),
        ("Рюкзак туристический 50л", 5990),
        ("Палатка 3-местная", 8990),
        ("Спальный мешок зимний", 4990),
        ("Теннисная ракетка", 3990),
        ("Мяч футбольный", 1990),
        ("Скакалка скоростная", 790),
        ("Эспандер набор", 1490),
        ("Ролик для пресса", 990),
        ("Шлем велосипедный", 2990),
        ("Бутылка спортивная", 690),
        ("Перчатки боксёрские", 2490),
    ],
    "Красота": [
        ("Набор косметики (подарочный)", 4990),
        ("Крем для лица увлажняющий", 1490),
        ("Шампунь профессиональный", 890),
        ("Парфюм мужской (50 мл)", 5990),
        ("Парфюм женский (50 мл)", 6990),
        ("Фен с ионизацией", 4490),
        ("Утюжок для волос", 3490),
        ("Набор кистей для макияжа", 2490),
        ("Тушь для ресниц", 990),
        ("Гель для душа (набор)", 690),
    ],
    "Продукты": [
        ("Кофе в зёрнах 1 кг", 1290),
        ("Чай коллекция (набор)", 890),
        ("Шоколад ручной работы", 590),
        ("Оливковое масло Extra Virgin", 790),
        ("Мёд натуральный 500г", 490),
        ("Орехи ассорти 500г", 690),
        ("Паста итальянская (набор)", 590),
        ("Соус соевый 500мл", 290),
        ("Специи набор (12 шт)", 990),
        ("Джем ягодный (3 шт)", 490),
    ],
}

# Статусы заказов с вероятностями
ORDER_STATUSES = [
    ("delivered", 0.70),
    ("shipped", 0.10),
    ("processing", 0.08),
    ("cancelled", 0.07),
    ("returned", 0.05),
]

# Способы оплаты
PAYMENT_METHODS = ["card", "cash", "online_wallet", "bank_transfer"]
PAYMENT_WEIGHTS = [50, 15, 25, 10]


def transliterate(name: str) -> str:
    """Простая транслитерация для email."""
    mapping = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
        'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i',
        'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
        'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
        'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch',
        'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '',
        'э': 'e', 'ю': 'yu', 'я': 'ya',
    }
    result = ""
    for ch in name.lower():
        result += mapping.get(ch, ch)
    return result


def generate_phone() -> str:
    """Генерирует российский номер телефона."""
    code = random.choice(["903", "905", "906", "909", "910", "915",
                           "916", "917", "918", "920", "925", "926",
                           "927", "929", "950", "951", "960", "961",
                           "962", "963", "964", "965", "966", "967",
                           "968", "977", "980", "981", "982", "983",
                           "985", "987", "988", "989", "995", "996",
                           "999"])
    number = ''.join([str(random.randint(0, 9)) for _ in range(7)])
    return f"+7{code}{number}"


def random_date(start: datetime, end: datetime) -> datetime:
    """Случайная дата между start и end."""
    delta = end - start
    random_seconds = random.randint(0, int(delta.total_seconds()))
    return start + timedelta(seconds=random_seconds)


def create_database():
    """Создаёт базу данных и заполняет её данными."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # --- Удаляем старые таблицы если есть ---
    cursor.executescript("""
        DROP TABLE IF EXISTS order_items;
        DROP TABLE IF EXISTS orders;
        DROP TABLE IF EXISTS products;
        DROP TABLE IF EXISTS customers;
    """)

    # =========================================
    # 1. Создаём таблицы
    # =========================================
    cursor.executescript("""
        CREATE TABLE customers (
            customer_id   INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name    TEXT,
            last_name     TEXT,
            email         TEXT,
            phone         TEXT,
            city          TEXT,
            registration_date TEXT,
            age           INTEGER
        );

        CREATE TABLE products (
            product_id    INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name  TEXT NOT NULL,
            category      TEXT NOT NULL,
            price         REAL NOT NULL,
            stock         INTEGER DEFAULT 0
        );

        CREATE TABLE orders (
            order_id      INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id   INTEGER,
            order_date    TEXT NOT NULL,
            status        TEXT NOT NULL,
            payment_method TEXT,
            total_amount  REAL,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        );

        CREATE TABLE order_items (
            item_id       INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id      INTEGER NOT NULL,
            product_id    INTEGER NOT NULL,
            quantity      INTEGER NOT NULL,
            unit_price    REAL NOT NULL,
            discount      REAL DEFAULT 0,
            FOREIGN KEY (order_id) REFERENCES orders(order_id),
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        );
    """)

    # =========================================
    # 2. Заполняем customers (500 записей)
    # =========================================
    print("Создаём клиентов...")
    customers_data = []
    used_emails = set()

    reg_start = datetime(2023, 1, 1)
    reg_end = datetime(2025, 10, 30)

    for i in range(500):
        is_male = random.random() < 0.48
        if is_male:
            first_name = random.choice(FIRST_NAMES_MALE)
            last_name = random.choice(LAST_NAMES_MALE)
        else:
            first_name = random.choice(FIRST_NAMES_FEMALE)
            last_name = random.choice(LAST_NAMES_FEMALE)

        city = random.choices(CITIES, weights=CITY_WEIGHTS, k=1)[0]
        age = random.choices(
            range(18, 71),
            weights=[1 if a < 22 else 3 if a < 35 else 2 if a < 50 else 1 for a in range(18, 71)],
            k=1
        )[0]

        # Email (с возможными дубликатами для "грязных" данных)
        base_email = transliterate(first_name) + "." + transliterate(last_name)
        domain = random.choice(EMAIL_DOMAINS)
        email = f"{base_email}{random.randint(1, 999)}@{domain}"

        # Телефон (некоторые NULL — "грязные" данные)
        phone = generate_phone() if random.random() > 0.05 else None

        # Некоторые клиенты без email (NULL)
        if random.random() < 0.03:
            email = None

        # Некоторые без города
        if random.random() < 0.02:
            city = None

        # Некоторые без возраста
        if random.random() < 0.04:
            age = None

        reg_date = random_date(reg_start, reg_end).strftime("%Y-%m-%d")

        customers_data.append((first_name, last_name, email, phone, city, reg_date, age))

    # Добавляем несколько дубликатов (те же имена, разные email)
    for _ in range(10):
        orig = random.choice(customers_data)
        dup = (orig[0], orig[1],
               f"{transliterate(orig[0])}.dup{random.randint(1,99)}@{random.choice(EMAIL_DOMAINS)}",
               generate_phone(), orig[4],
               random_date(reg_start, reg_end).strftime("%Y-%m-%d"), orig[6])
        customers_data.append(dup)

    # Обрезаем до 500
    customers_data = customers_data[:500]

    cursor.executemany("""
        INSERT INTO customers (first_name, last_name, email, phone, city, registration_date, age)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, customers_data)

    # =========================================
    # 3. Заполняем products (100 записей)
    # =========================================
    print("Создаём товары...")
    products_data = []
    for category, items in CATEGORIES.items():
        for name, base_price in items:
            # Немного варьируем цену
            price = round(base_price * random.uniform(0.9, 1.1), 2)
            stock = random.randint(0, 500)
            # Некоторые товары с нулевым остатком
            if random.random() < 0.08:
                stock = 0
            products_data.append((name, category, price, stock))

    cursor.executemany("""
        INSERT INTO products (product_name, category, price, stock)
        VALUES (?, ?, ?, ?)
    """, products_data)

    # Получаем ID товаров для дальнейшего использования
    cursor.execute("SELECT product_id, price, category FROM products")
    products_info = cursor.fetchall()
    product_ids = [p[0] for p in products_info]
    product_prices = {p[0]: p[1] for p in products_info}
    product_categories = {p[0]: p[2] for p in products_info}

    # Категории с разной популярностью
    category_popularity = {
        "Электроника": 30,
        "Одежда": 25,
        "Книги": 15,
        "Дом и сад": 12,
        "Спорт": 8,
        "Красота": 6,
        "Продукты": 4,
    }

    product_weights = [category_popularity.get(product_categories[pid], 5) for pid in product_ids]

    # =========================================
    # 4. Заполняем orders (5000) и order_items (15000)
    # =========================================
    print("Создаём заказы...")
    order_start = datetime(2024, 1, 1)
    order_end = datetime(2025, 10, 30)

    customer_ids = list(range(1, 501))
    # Некоторые клиенты покупают чаще (Парето: 20% клиентов = 80% заказов)
    active_customers = random.sample(customer_ids, 100)  # 20% активных
    passive_customers = [c for c in customer_ids if c not in active_customers]

    # Некоторые клиенты вообще не покупают (для задач на LEFT JOIN)
    never_bought = random.sample(passive_customers, 30)
    passive_customers = [c for c in passive_customers if c not in never_bought]

    orders_data = []
    order_items_data = []
    order_counter = 0

    for _ in range(5000):
        # Выбираем клиента (активные чаще)
        if random.random() < 0.80:
            cust_id = random.choice(active_customers)
        else:
            cust_id = random.choice(passive_customers)

        # Дата заказа (больше заказов в ноябре-декабре и марте)
        order_dt = random_date(order_start, order_end)
        # Сезонность
        if order_dt.month in [11, 12]:
            # Больше шансов сохранить эту дату
            pass
        elif order_dt.month in [1, 2, 7, 8]:
            # Немного сдвигаем — но оставим для простоты
            pass

        order_date_str = order_dt.strftime("%Y-%m-%d %H:%M:%S")

        # Статус
        status = random.choices(
            [s[0] for s in ORDER_STATUSES],
            weights=[s[1] for s in ORDER_STATUSES],
            k=1
        )[0]

        # Способ оплаты
        payment = random.choices(PAYMENT_METHODS, weights=PAYMENT_WEIGHTS, k=1)[0]
        # Некоторые NULL
        if random.random() < 0.02:
            payment = None

        order_counter += 1

        # Товары в заказе (1-5 позиций)
        num_items = random.choices([1, 2, 3, 4, 5], weights=[40, 30, 15, 10, 5], k=1)[0]
        selected_products = random.choices(product_ids, weights=product_weights, k=num_items)
        # Убираем дубликаты товаров в одном заказе
        selected_products = list(set(selected_products))

        total = 0.0
        for pid in selected_products:
            qty = random.choices([1, 2, 3, 4, 5], weights=[60, 20, 10, 7, 3], k=1)[0]
            unit_price = product_prices[pid]

            # Скидка (0-20%, часто 0)
            discount = 0.0
            if random.random() < 0.25:
                discount = random.choice([0.05, 0.10, 0.15, 0.20])

            item_total = unit_price * qty * (1 - discount)
            total += item_total

            order_items_data.append((order_counter, pid, qty, unit_price, discount))

        total = round(total, 2)

        # Аномалия: некоторые заказы с total_amount = 0 или NULL
        if random.random() < 0.01:
            total = 0.0
        if random.random() < 0.005:
            total = None

        orders_data.append((cust_id, order_date_str, status, payment, total))

    cursor.executemany("""
        INSERT INTO orders (customer_id, order_date, status, payment_method, total_amount)
        VALUES (?, ?, ?, ?, ?)
    """, orders_data)

    cursor.executemany("""
        INSERT INTO order_items (order_id, product_id, quantity, unit_price, discount)
        VALUES (?, ?, ?, ?, ?)
    """, order_items_data)

    # =========================================
    # 5. Создаём индексы
    # =========================================
    print("Создаём индексы...")
    cursor.executescript("""
        CREATE INDEX idx_orders_customer_id ON orders(customer_id);
        CREATE INDEX idx_orders_order_date ON orders(order_date);
        CREATE INDEX idx_orders_status ON orders(status);
        CREATE INDEX idx_order_items_order_id ON order_items(order_id);
        CREATE INDEX idx_order_items_product_id ON order_items(product_id);
        CREATE INDEX idx_products_category ON products(category);
        CREATE INDEX idx_customers_city ON customers(city);
        CREATE INDEX idx_customers_registration_date ON customers(registration_date);
    """)

    conn.commit()

    # =========================================
    # 6. Проверка
    # =========================================
    print("\n=== База данных создана ===")
    for table in ["customers", "products", "orders", "order_items"]:
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = cursor.fetchone()[0]
        print(f"  {table}: {count} записей")

    # Проверяем NULL
    cursor.execute("SELECT COUNT(*) FROM customers WHERE email IS NULL")
    print(f"\n  Клиенты без email (NULL): {cursor.fetchone()[0]}")
    cursor.execute("SELECT COUNT(*) FROM customers WHERE phone IS NULL")
    print(f"  Клиенты без телефона (NULL): {cursor.fetchone()[0]}")
    cursor.execute("SELECT COUNT(*) FROM customers WHERE city IS NULL")
    print(f"  Клиенты без города (NULL): {cursor.fetchone()[0]}")
    cursor.execute("SELECT COUNT(*) FROM orders WHERE total_amount IS NULL OR total_amount = 0")
    print(f"  Заказы с проблемным total (NULL/0): {cursor.fetchone()[0]}")

    conn.close()
    print(f"\nФайл {DB_NAME} сохранён в текущей директории.")


if __name__ == "__main__":
    create_database()
