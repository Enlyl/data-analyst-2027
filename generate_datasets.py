import os
import sqlite3
import random
import csv
from datetime import datetime, timedelta

DATASET_DIR = r"d:\vibe_app\main_data_analytics\course\datasets"
RAW_DIR = os.path.join(DATASET_DIR, "raw")
PROCESSED_DIR = os.path.join(DATASET_DIR, "processed")

os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)

# 1. Генерация E-Commerce Dataset (CSV + SQLite)
def generate_ecommerce_data():
    random.seed(42)
    categories = {
        "Electronics": ["Smartphone", "Laptop", "Wireless Earbuds", "Smartwatch", "Monitor", "Keyboard"],
        "Home & Kitchen": ["Coffee Maker", "Blender", "Air Fryer", "Vacuum Cleaner", "Toaster"],
        "Fashion": ["Sneakers", "Winter Jacket", "Jeans", "T-Shirt", "Backpack"],
        "Beauty": ["Skincare Set", "Perfume", "Hair Dryer", "Sunscreen"]
    }
    cities = ["Moscow", "Saint Petersburg", "Novosibirsk", "Yekaterinburg", "Kazan", "Nizhny Novgorod", "Samara"]
    channels = ["Organic Search", "Paid Ads", "Social Media", "Email Newsletter", "Referral", "Direct"]
    devices = ["Mobile iOS", "Mobile Android", "Desktop Web"]
    
    # Products
    products = []
    pid = 1
    for cat, items in categories.items():
        for item in items:
            base_price = round(random.uniform(15.0, 1200.0), 2)
            cost = round(base_price * random.uniform(0.4, 0.75), 2)
            products.append({
                "product_id": pid,
                "product_name": item,
                "category": cat,
                "price": base_price,
                "cost": cost
            })
            pid += 1

    # Customers
    customers = []
    start_date = datetime(2025, 1, 1)
    for cid in range(1, 1201):
        reg_date = start_date + timedelta(days=random.randint(0, 500))
        customers.append({
            "customer_id": cid,
            "first_name": f"User_{cid}",
            "city": random.choice(cities),
            "acquisition_channel": random.choice(channels),
            "registration_date": reg_date.strftime("%Y-%m-%d"),
            "device": random.choice(devices)
        })

    # Orders & Order Items
    orders = []
    order_items = []
    oid = 10001
    item_id = 1
    
    for cust in customers:
        reg_dt = datetime.strptime(cust["registration_date"], "%Y-%m-%d")
        num_orders = random.choices([0, 1, 2, 3, 5, 8, 12], weights=[20, 35, 20, 12, 8, 4, 1])[0]
        curr_dt = reg_dt
        for _ in range(num_orders):
            curr_dt += timedelta(days=random.randint(1, 45))
            if curr_dt > datetime(2026, 10, 1):
                break
            
            status = random.choices(["Completed", "Refunded", "Cancelled"], weights=[88, 7, 5])[0]
            orders.append({
                "order_id": oid,
                "customer_id": cust["customer_id"],
                "order_date": curr_dt.strftime("%Y-%m-%d %H:%M:%S"),
                "status": status,
                "payment_method": random.choice(["Credit Card", "Apple Pay / Mir Pay", "Fast Payment (SBP)", "Cash on Delivery"])
            })
            
            # items
            n_items = random.choices([1, 2, 3, 4], weights=[55, 30, 10, 5])[0]
            sampled_products = random.sample(products, n_items)
            for prod in sampled_products:
                qty = random.choices([1, 2, 3], weights=[80, 15, 5])[0]
                # small random discount
                discount = random.choice([0.0, 0.0, 0.05, 0.10, 0.20])
                item_price = round(prod["price"] * (1 - discount), 2)
                order_items.append({
                    "order_item_id": item_id,
                    "order_id": oid,
                    "product_id": prod["product_id"],
                    "quantity": qty,
                    "unit_price": item_price,
                    "total_amount": round(item_price * qty, 2)
                })
                item_id += 1
            oid += 1

    # Save to CSV
    def save_csv(path, data, keys):
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=keys)
            w.writeheader()
            w.writerows(data)

    save_csv(os.path.join(RAW_DIR, "products.csv"), products, ["product_id", "product_name", "category", "price", "cost"])
    save_csv(os.path.join(RAW_DIR, "customers.csv"), customers, ["customer_id", "first_name", "city", "acquisition_channel", "registration_date", "device"])
    save_csv(os.path.join(RAW_DIR, "orders.csv"), orders, ["order_id", "customer_id", "order_date", "status", "payment_method"])
    save_csv(os.path.join(RAW_DIR, "order_items.csv"), order_items, ["order_item_id", "order_id", "product_id", "quantity", "unit_price", "total_amount"])

    # Save to SQLite Database
    db_path = os.path.join(DATASET_DIR, "ecommerce.db")
    if os.path.exists(db_path):
        os.remove(db_path)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    cur.execute("""
    CREATE TABLE products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT,
        category TEXT,
        price REAL,
        cost REAL
    )""")
    cur.execute("""
    CREATE TABLE customers (
        customer_id INTEGER PRIMARY KEY,
        first_name TEXT,
        city TEXT,
        acquisition_channel TEXT,
        registration_date TEXT,
        device TEXT
    )""")
    cur.execute("""
    CREATE TABLE orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        order_date TEXT,
        status TEXT,
        payment_method TEXT,
        FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
    )""")
    cur.execute("""
    CREATE TABLE order_items (
        order_item_id INTEGER PRIMARY KEY,
        order_id INTEGER,
        product_id INTEGER,
        quantity INTEGER,
        unit_price REAL,
        total_amount REAL,
        FOREIGN KEY(order_id) REFERENCES orders(order_id),
        FOREIGN KEY(product_id) REFERENCES products(product_id)
    )""")
    
    for p in products:
        cur.execute("INSERT INTO products VALUES (?,?,?,?,?)", (p["product_id"], p["product_name"], p["category"], p["price"], p["cost"]))
    for c in customers:
        cur.execute("INSERT INTO customers VALUES (?,?,?,?,?,?)", (c["customer_id"], c["first_name"], c["city"], c["acquisition_channel"], c["registration_date"], c["device"]))
    for o in orders:
        cur.execute("INSERT INTO orders VALUES (?,?,?,?,?)", (o["order_id"], o["customer_id"], o["order_date"], o["status"], o["payment_method"]))
    for i in order_items:
        cur.execute("INSERT INTO order_items VALUES (?,?,?,?,?,?)", (i["order_item_id"], i["order_id"], i["product_id"], i["quantity"], i["unit_price"], i["total_amount"]))

    conn.commit()
    conn.close()
    print(f"E-commerce dataset generated: {len(products)} products, {len(customers)} customers, {len(orders)} orders, {len(order_items)} items.")

# 2. Генерация SaaS Subscription Dataset (для когорт, Churn, LTV)
def generate_saas_data():
    random.seed(101)
    plans = {"Starter": 29.0, "Professional": 99.0, "Enterprise": 299.0}
    industries = ["Fintech", "Healthtech", "Edtech", "E-commerce", "SaaS B2B", "Logistics", "Marketing Agency"]
    
    users = []
    start_date = datetime(2025, 1, 1)
    for uid in range(1, 2001):
        signup_dt = start_date + timedelta(days=random.randint(0, 480))
        plan = random.choices(["Starter", "Professional", "Enterprise"], weights=[60, 30, 10])[0]
        mrr = plans[plan]
        # Churn probability based on plan & usage
        churn_prob = 0.08 if plan == "Starter" else (0.04 if plan == "Professional" else 0.015)
        is_churned = random.random() < (churn_prob * 3) # over observation time
        
        churn_dt = None
        if is_churned:
            lifetime_days = random.randint(14, 300)
            churn_dt = signup_dt + timedelta(days=lifetime_days)
            if churn_dt > datetime(2026, 10, 1):
                is_churned = False
                churn_dt = None
                
        users.append({
            "user_id": uid,
            "company_name": f"Company_{uid}",
            "industry": random.choice(industries),
            "plan": plan,
            "mrr": mrr,
            "signup_date": signup_dt.strftime("%Y-%m-%d"),
            "is_churned": 1 if is_churned else 0,
            "churn_date": churn_dt.strftime("%Y-%m-%d") if churn_dt else "",
            "active_seats": random.randint(1, 25),
            "nps_score": random.choices([10, 9, 8, 7, 6, 5, 3], weights=[30, 30, 15, 10, 8, 4, 3])[0],
            "feature_a_usage": random.randint(5, 500),
            "feature_b_usage": random.randint(0, 80)
        })

    with open(os.path.join(RAW_DIR, "saas_users.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(users[0].keys()))
        w.writeheader()
        w.writerows(users)
    print(f"SaaS dataset generated: {len(users)} users.")

# 3. Генерация Unstructured Text / Reviews Dataset (для LLM API & RAG)
def generate_unstructured_reviews():
    random.seed(999)
    templates_pos = [
        "Отличный сервис, доставка пришла за 2 часа! Менеджер помог разобраться с настройками.",
        "Прекрасное качество товара. Пользуюсь каждый день уже месяц, нареканий ноль.",
        "Быстрая поддержка в чате, решили проблему за 5 минут. Рекомендую!",
        "Very intuitive dashboard and responsive UI. Loving the new export features.",
        "Супер! Интеграция с API прошла без запинки. Документация понятная."
    ]
    templates_neg = [
        "Ужасная доставка! Курьер опоздал на 4 часа, коробка помята, поддержка молчит.",
        "Деньги списали дважды, вернуть не могу уже неделю. Буду писать претензию.",
        "Постоянные баги при экспорте в CSV. Ничего не работает, верните подписку!",
        "App crashes whenever I load large datasets. Customer service gave generic replies.",
        "Интерфейс тормозит, цены подняли без предупреждения. Уходим к конкурентам."
    ]
    templates_neutral = [
        "Обычный продукт, ничего особенного. Работает нормально, но цена высоковата.",
        "Доставили вовремя. Пока тестирую, есть пара непонятных моментов в интерфейсе.",
        "Decent tool, does the job. Would appreciate more documentation on webhooks.",
        "Функционал стандартный. Хотелось бы больше шаблонов отчётов."
    ]
    
    reviews = []
    start_dt = datetime(2026, 1, 1)
    for rid in range(1, 801):
        dt = start_dt + timedelta(days=random.randint(0, 280))
        sentiment_true = random.choices(["Positive", "Negative", "Neutral"], weights=[55, 30, 15])[0]
        if sentiment_true == "Positive":
            text = random.choice(templates_pos)
            rating = random.choice([4, 5])
        elif sentiment_true == "Negative":
            text = random.choice(templates_neg)
            rating = random.choice([1, 2])
        else:
            text = random.choice(templates_neutral)
            rating = 3
            
        reviews.append({
            "review_id": rid,
            "date": dt.strftime("%Y-%m-%d"),
            "customer_id": random.randint(1, 1000),
            "rating": rating,
            "text": text,
            "sentiment_label": sentiment_true,
            "platform": random.choice(["App Store", "Google Play", "Trustpilot", "Internal Feedback"])
        })
        
    with open(os.path.join(RAW_DIR, "customer_reviews.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(reviews[0].keys()))
        w.writeheader()
        w.writerows(reviews)
    print(f"Unstructured reviews generated: {len(reviews)} reviews.")

# 4. Генерация A/B Testing Dataset
def generate_ab_test_data():
    random.seed(777)
    records = []
    # Test: New Checkout Button & Layout
    # Control: CR ~ 8.2%, Variant: CR ~ 9.6%
    n_users = 10000
    for uid in range(1, n_users + 1):
        group = "A_Control" if uid % 2 == 0 else "B_Variant"
        base_cr = 0.082 if group == "A_Control" else 0.096
        converted = 1 if random.random() < base_cr else 0
        revenue = round(random.uniform(20.0, 150.0), 2) if converted else 0.0
        device = random.choice(["Desktop", "Mobile Web", "Mobile App"])
        
        records.append({
            "user_id": uid,
            "test_group": group,
            "device": device,
            "converted": converted,
            "revenue": revenue
        })
        
    with open(os.path.join(RAW_DIR, "ab_test_checkout.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(records[0].keys()))
        w.writeheader()
        w.writerows(records)
    print(f"A/B test dataset generated: {len(records)} participants.")

if __name__ == "__main__":
    generate_ecommerce_data()
    generate_saas_data()
    generate_unstructured_reviews()
    generate_ab_test_data()
