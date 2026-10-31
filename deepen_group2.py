import os
import sys
sys.path.append(r"d:\vibe_app\main_data_analytics")
from notebook_helper import create_notebook

BASE = r"d:\vibe_app\main_data_analytics\course"

# ==========================================
# MODULE 03: PYTHON & PANDAS DEEP DIVE
# ==========================================
m03 = os.path.join(BASE, "module_03_python")
os.makedirs(m03, exist_ok=True)

# Lesson 1
create_notebook(os.path.join(m03, "lesson_01_python_no_syntax_memorization.ipynb"), [
    ("markdown", """# 🐍 Модуль 3. Урок 1: Как аналитик пишет код на Python в 2027 году

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_03_python/lesson_01_python_no_syntax_memorization.ipynb)

---

## 1. Концепция: Векторизация против циклов for

Главная ментальная модель Python для данных: **мы никогда не перебираем строки таблицы циклом `for`**.
Векторизованные операции Pandas выполняются на оптимизированном коде C/C++ в сотни раз быстрее обычного цикла Python.

```
┌─────────────────────────────────┬─────────────────────────────────┐
│     ПЛОХОЙ МЕДЛЕННЫЙ КОД        │      ВЕКТОРИЗОВАННЫЙ PANDAS     │
├─────────────────────────────────┼─────────────────────────────────┤
│ for i in range(len(df)):        │ df['total'] =                   │
│     df.loc[i, 'total'] =        │     df['price'] * df['qty']     │
│         df.loc[i, 'price'] * ...│                                 │
│ (Работает 45 секунд)            │ (Работает 0.02 секунды)         │
└─────────────────────────────────┴─────────────────────────────────┘
```
"""),
    ("code", """# Практическое сравнение скорости: Векторизация vs Цикл for
import pandas as pd
import numpy as np
import time

n = 200_000
prices = np.random.uniform(100, 5000, n)
quantities = np.random.randint(1, 10, n)
df_perf = pd.DataFrame({'price': prices, 'quantity': quantities})

# 1. Векторизованный расчет
t0 = time.time()
df_perf['amount_vectorized'] = df_perf['price'] * df_perf['quantity']
t_vec = time.time() - t0

print(f"Векторизованный расчет на {n:,} строк занял: {t_vec:.4f} сек")
print("Это фундаментальный принцип высокопроизводительного анализа данных!")
""")
])

# Lesson 2
create_notebook(os.path.join(m03, "lesson_02_pandas_dataframes_indexing.ipynb"), [
    ("markdown", """# 📊 Модуль 3. Урок 2: Анатомия DataFrame: Индексация, срезы и фильтрация

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_03_python/lesson_02_pandas_dataframes_indexing.ipynb)

---

## 1. Разница между `.loc[]` и `.iloc[]`

- `.loc[label_indexer]` — обращение по **именам** (меткам) строк и названиям столбцов.
- `.iloc[position_indexer]` — обращение строго по **целочисленным номерам** позиций (0, 1, 2...).

### Булева фильтрация с несколькими условиями:
- `&` (логическое И), `|` (логическое ИЛИ), `~` (логическое НЕ).
- **Обязательно оборачивать каждое условие в круглые скобки**: `(df['A'] > 10) & (df['B'] == 'X')`!
"""),
    ("code", """import pandas as pd

# Загружаем реальный датасет клиентов курса
df_cust = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\customers.csv")

# Сложная сегментация: Мобильные пользователи из городов-миллионников, пришедшие с платной рекламы
target_segment = df_cust[
    (df_cust['city'].isin(['Moscow', 'Saint Petersburg', 'Kazan'])) &
    (df_cust['device'].str.contains('Mobile')) &
    (df_cust['acquisition_channel'] == 'Paid Ads')
]

print(f"Всего пользователей: {len(df_cust)}")
print(f"Пользователей в целевом сегменте: {len(target_segment)} ({len(target_segment)/len(df_cust)*100:.1f}%)")
print(target_segment[['customer_id', 'first_name', 'city', 'device']].head(4))
""")
])

# Lesson 3
create_notebook(os.path.join(m03, "lesson_03_pandas_aggregations_merge.ipynb"), [
    ("markdown", """# 🧩 Модуль 3. Урок 3: Агрегации, группировки и слияния таблиц (Merge / Concat)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_03_python/lesson_03_pandas_aggregations_merge.ipynb)

---

## 1. Реальный бизнес-кейс: Юнит-экономика товарных категорий

Объединяем продажи, себестоимость и данные клиентов для расчета чистой прибыли по категориям.
"""),
    ("code", """import pandas as pd

orders = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\orders.csv")
items = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\order_items.csv")
products = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\products.csv")

# Сквозной merge
full_df = items.merge(orders, on='order_id').merge(products, on='product_id')
full_df = full_df[full_df['status'] == 'Completed']

# Расчет валовой прибыли
full_df['gross_profit'] = full_df['total_amount'] - (full_df['cost'] * full_df['quantity'])

# Группировка с несколькими метриками
cat_pnl = full_df.groupby('category').agg(
    revenue=('total_amount', 'sum'),
    gross_profit=('gross_profit', 'sum'),
    orders_count=('order_id', 'nunique'),
    avg_order_value=('total_amount', 'mean')
).reset_index()

cat_pnl['margin_pct'] = (cat_pnl['gross_profit'] / cat_pnl['revenue'] * 100).round(1)
print("UNIT-ЭКОНОМИКА КАТЕГОРИЙ:")
print(cat_pnl.sort_values(by='revenue', ascending=False))
""")
])

# Lesson 4
create_notebook(os.path.join(m03, "lesson_04_visualization_seaborn_matplotlib.ipynb"), [
    ("markdown", """# 📊 Модуль 3. Урок 4: Визуализация данных в Python (Matplotlib & Seaborn)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_03_python/lesson_04_visualization_seaborn_matplotlib.ipynb)

---

## 1. Когда какой график использовать в бизнесе?

- **Boxplot (Ящик с усами)**: Сравнение медианы и разброса метрики между сегментами (выявление аномалий).
- **Lineplot (Линия)**: Динамика во времени, сезонность.
- **Barplot (Столбцы)**: Сравнение дискретных категорий.
- **Heatmap (Тепловая карта)**: Корреляционная матрица, когортные сетки.
"""),
    ("code", """import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

saas = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\saas_users.csv")

plt.figure(figsize=(10, 5))
sns.violinplot(data=saas, x='plan', y='nps_score', hue='is_churned', split=True, palette='Blues_r')
plt.title('Распределение NPS по тарифам и факту оттока клиентов', fontsize=13, pad=12)
plt.xlabel('Тарифный план')
plt.ylabel('Оценка NPS')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
""")
])

# Lesson 5
create_notebook(os.path.join(m03, "lesson_05_code_review_ai_validation.ipynb"), [
    ("markdown", """# 🕵️ Модуль 3. Урок 5: Code Review кода от ИИ: Поиск скрытых математических багов

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_03_python/lesson_05_code_review_ai_validation.ipynb)

---

## 1. Классические галлюцинации LLM при написании аналитического кода

1. **Среднее от процентов (Averaging Averages)**: ИИ берет конверсию филиала 1 (10%) и филиала 2 (2%) и считает: `(10 + 2) / 2 = 6%`. Но в филиале 1 было 10 посетителей, а в филиале 2 — 10 000! Реальная конверсия будет около 2.01%, а не 6%!
2. **Утечка будущего (Data Leakage)**: Использование данных из будущего при фильтрации когорт.
3. **Замена NaN на 0 без предупреждения**: Искажает медиану и стандартное отклонение.
"""),
    ("code", """# Демонстрация критической ошибки "Среднее от процентов"
import pandas as pd

branch_data = pd.DataFrame({
    'Филиал': ['Точка А (Маленькая)', 'Точка Б (Флагман)'],
    'Посетители': [10, 10000],
    'Покупки': [1, 200]
})
branch_data['CR'] = branch_data['Покупки'] / branch_data['Посетители']

# ОШИБКА НЕЙРОСЕТИ:
bad_cr = branch_data['CR'].mean()

# ПРАВИЛЬНЫЙ РАСЧЕТ АНАЛИТИКА:
true_cr = branch_data['Покупки'].sum() / branch_data['Посетители'].sum()

print(f"Ошибка ИИ (Среднее от процентов): {bad_cr*100:.2f}% (ОШИБКА В 3 РАЗА!)")
print(f"Истинная сквозная конверсия: {true_cr*100:.2f}%")
""")
])

# Module 03 Quiz
with open(os.path.join(m03, "quiz.md"), "w", encoding="utf-8") as f:
    f.write("""# 🧠 Quiz: Самопроверка по Модулю 3 (Python & Pandas)

---

### Вопрос 1
Почему в Pandas категорически рекомендуется использовать векторизованные операции вместо циклов `for`?
- [ ] Циклы for запрещены создателями Python.
- [x] Векторизованные операции транслируются в оптимизированный C-код и выполняются в десятки и сотни раз быстрее.
- [ ] Векторизованные операции не расходуют память.
*Объяснение*: Pandas оперирует низкоуровневыми массивами C через NumPy, выполняя расчеты над всей колонкой единым блоком инструкций процессора (SIMD).

---

### Вопрос 2
В чем заключается ошибка при расчете общего CR компании через `df['conversion_rate'].mean()`?
- [ ] Ошибки нет, среднее всегда корректно.
- [x] Это математическая ошибка усреднения процентов без учета разницы в объемах трафика между филиалами/сегментами.
- [ ] Метод .mean() не умеет работать с числами с плавающей точкой.
*Объяснение*: Чтобы получить истинную конверсию, необходимо разделить суммарное число целевых действий на суммарный трафик (`total_actions / total_traffic`).

---

### Вопрос 3
Какой результат вернет операция `df.loc[0:2]` vs `df.iloc[0:2]`?
- [ ] Одинаковый результат.
- [x] `.loc[0:2]` включит строки с метками 0, 1 и 2 (включая правый конец), а `.iloc[0:2]` вернет строго первые 2 строки с индексами 0 и 1 (не включая правый конец).
- [ ] Выдаст ошибку синтаксиса.
*Объяснение*: В `.loc` правая граница включается, так как поиск идет по именам/меткам. В `.iloc` правая граница исключается по стандартному правилу срезов Python.
""")

print("Module 03 deepened successfully.")

# ==========================================
# MODULE 04: DATA CLEANING DEEP DIVE
# ==========================================
m04 = os.path.join(BASE, "module_04_data_cleaning")
os.makedirs(m04, exist_ok=True)

create_notebook(os.path.join(m04, "lesson_01_dirty_data_types_missing_values.ipynb"), [
    ("markdown", """# 🧹 Модуль 4. Урок 1: Missing Values: MCAR, MAR, MNAR и приведение типов

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_04_data_cleaning/lesson_01_dirty_data_types_missing_values.ipynb)

---

## 1. Теория пропусков в данных: Три типа Missing Values

Нельзя просто так брать и заполнять все пропуски средним. В статистике выделяют 3 природы отсутствия данных:
1. **MCAR (Missing Completely at Random)**: Пропуск абсолютно случаен (например, случайный сбой датчика сети). Удаление строк не смещает оценку.
2. **MAR (Missing at Random)**: Вероятность пропуска зависит от других наблюдаемых полей (например, женщины реже указывают возраст в анкете, но чаще указывают образование).
3. **MNAR (Missing Not at Random)**: Пропуск зависит от самого ненаблюдаемого значения (например, люди с экстремально высоким или нулевым доходом скрывают свой доход). Заполнение медианой приведет к катастрофическому смещению!
"""),
    ("code", """import pandas as pd
import numpy as np

# Реальный кейс: Обработка пропусков в зависимости от природы данных
dirty_users = pd.DataFrame({
    'user_id': range(1, 6),
    'income': [50000, np.nan, 75000, np.nan, 120000],
    'is_employed': [1, 0, 1, 0, 1], # Если человек не работает, доход пропущен осмысленно!
    'age': [25, 42, np.nan, 31, 55]
})

print("СЫРЫЕ ДАННЫЕ С ПРОПУСКАМИ:")
print(dirty_users)

# Умная импутация:
# 1. Если не трудоустроен — ставим 0
dirty_users.loc[dirty_users['is_employed'] == 0, 'income'] = dirty_users.loc[dirty_users['is_employed'] == 0, 'income'].fillna(0)
# 2. Для возраста берем медиану
dirty_users['age'] = dirty_users['age'].fillna(dirty_users['age'].median())

print("\\nОЧИЩЕННЫЕ ДАННЫЕ БЕЗ СМЕЩЕНИЯ ВЫБОРКИ:")
print(dirty_users)
""")
])

# Lesson 2
create_notebook(os.path.join(m04, "lesson_02_duplicates_string_cleaning_regex.ipynb"), [
    ("markdown", """# 🔤 Модуль 4. Урок 2: Дедупликация и нормализация текста с RegEx

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_04_data_cleaning/lesson_02_duplicates_string_cleaning_regex.ipynb)

---

## 1. Регулярные выражения (RegEx) для аналитика

Регулярные выражения — суперсила для очистки грязных телефонов, email, промокодов и артикулов:
- `\\d+` — одна или более цифр.
- `[A-Za-z]+` — латинские буквы.
- `^...$` — начало и конец строки.
"""),
    ("code", """import pandas as pd

raw_logistics = pd.DataFrame({
    'tracking_number': ['RU-123456-X', 'ru_123456_x ', 'RU123456X', 'Order #999999-Y'],
    'customer_phone': ['+7 (999) 123-45-67', '89991234567', '79991234567', '+7 999 123 45 67']
})

# Нормализуем трек-номера: удаляем пробелы, переводим в верхний регистр, убираем знаки препинания
raw_logistics['tracking_clean'] = raw_logistics['tracking_number'].str.upper().str.replace(r'[^A-Z0-9]', '', regex=True)

# Нормализуем телефон в стандартный формат E.164: +7XXXXXXXXXX
digits = raw_logistics['customer_phone'].str.replace(r'\\D', '', regex=True)
raw_logistics['phone_clean'] = digits.apply(lambda x: '+7' + x[1:] if x.startswith('8') else '+' + x)

print("РЕЗУЛЬТАТ REGEX-ОЧИСТКИ:")
print(raw_logistics[['tracking_clean', 'phone_clean']])
""")
])

# Lesson 3
create_notebook(os.path.join(m04, "lesson_03_outliers_anomaly_detection.ipynb"), [
    ("markdown", """# 🚨 Модуль 4. Урок 3: Детекция аномалий и выбросов: IQR, Z-Score, Isolation

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_04_data_cleaning/lesson_03_outliers_anomaly_detection.ipynb)

---

## 1. Когда выброс — это ошибка, а когда — ключевой инсайт бизнеса?

- **Выброс-ошибка**: Сумма заказа = -100 руб или возраст клиента = 200 лет. Удаляем или исправляем.
- **Выброс-инсайт**: Заказ на 5 000 000 руб при среднем чеке 3 000 руб. Это оптовый B2B-клиент. Если вы просто удалите его из базы, вы исказите выручку на 30%!
"""),
    ("code", """import pandas as pd
import numpy as np

items = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\order_items.csv")

# Расчет Z-score: z = (x - mean) / std
mean_amt = items['total_amount'].mean()
std_amt = items['total_amount'].std()
items['z_score'] = (items['total_amount'] - mean_amt) / std_amt

# Аномалии с Z-score > 3 (вероятность при нормальном распределении < 0.3%)
anomalies = items[items['z_score'].abs() > 3]
print(f"Средняя сумма позиции: ${mean_amt:.2f} | Std: ${std_amt:.2f}")
print(f"Обнаружено статистических аномалий (|z| > 3): {len(anomalies)} строк")
print(anomalies[['order_item_id', 'total_amount', 'z_score']].head(5))
""")
])

# Lesson 4
create_notebook(os.path.join(m04, "lesson_04_automated_cleaning_pipelines.ipynb"), [
    ("markdown", """# ⚙️ Модуль 4. Урок 4: Построение продакшен-пайплайна валидации данных

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_04_data_cleaning/lesson_04_automated_cleaning_pipelines.ipynb)

---

## 1. Концепция Data Contracts и Assert-валидации

В зрелых командах аналитики пишут проверки-утверждения (`assert`), предотвращающие попадание битых данных в витрины.
"""),
    ("code", """import pandas as pd

def validate_and_clean_orders(raw_df: pd.DataFrame) -> pd.DataFrame:
    df = raw_df.copy()
    
    # Инвариант 1: Уникальность первичного ключа
    assert df['order_id'].nunique() == len(df), "КРИТИЧЕСКИЙ СБОЙ: Дубликаты в order_id!"
    
    # Очистка
    df = df.dropna(subset=['order_id', 'customer_id'])
    df['order_date'] = pd.to_datetime(df['order_date'])
    
    # Инвариант 2: Статусы только из белого списка
    valid_statuses = {'Completed', 'Refunded', 'Cancelled'}
    df = df[df['status'].isin(valid_statuses)]
    
    return df

orders_raw = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\orders.csv")
orders_clean = validate_and_clean_orders(orders_raw)
print(f"Пайплайн валидации успешно пройден! Валидных заказов: {len(orders_clean):,}")
""")
])

# Module 04 Quiz
with open(os.path.join(m04, "quiz.md"), "w", encoding="utf-8") as f:
    f.write("""# 🧠 Quiz: Самопроверка по Модулю 4 (Очистка и качество данных)

---

### Вопрос 1
Что означает пропуск типа MNAR (Missing Not at Random)?
- [ ] Данные потерялись из-за случайного обрыва связи Wi-Fi.
- [x] Вероятность отсутствия значения напрямую связана с самим этим скрытым значением (например, люди с очень низким доходом отказываются его называть).
- [ ] Ошибка в формате даты.
*Объяснение*: При MNAR нельзя просто удалять строки или заменять их на среднее, так как это системно исказит распределение.

---

### Вопрос 2
Что делать, если в транзакциях интернет-магазина обнаружен заказ на сумму в 50 раз выше среднего чека?
- [ ] Немедленно удалить этот заказ как выброс.
- [x] Проверить контекст: если это реальный оптовый покупатель, сохранить его в базе, но при расчете розничного среднего чека выделить в отдельный B2B-сегмент.
- [ ] Заменить сумму на медиану.
*Объяснение*: Выбросы в коммерческих данных часто представляют наиболее ценный сегмент клиентов (B2B, киты), который требует отдельного анализа.

---

### Вопрос 3
Какое регулярное выражение (RegEx) извлечет только цифры из строки `Order #4592-A`?
- [ ] `[A-Z]+`
- [x] `\\d+`
- [ ] `\\s+`
*Объяснение*: `\\d` обозначает digit (любую цифру от 0 до 9), а квантификатор `+` означает одно или более вхождений.
""")

print("Module 04 deepened successfully.")

# ==========================================
# MODULE 05: STATISTICS DEEP DIVE
# ==========================================
m05 = os.path.join(BASE, "module_05_statistics")
os.makedirs(m05, exist_ok=True)

# Lesson 1
create_notebook(os.path.join(m05, "lesson_01_descriptive_stats_outliers.ipynb"), [
    ("markdown", """# 📐 Модуль 5. Урок 1: Описательная статистика: Мода, Медиана, Дисперсия и Квартили

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_05_statistics/lesson_01_descriptive_stats_outliers.ipynb)

---

## 1. Почему среднее врет в 80% задач бизнеса?

В реальной жизни большинство продуктовых и финансовых метрик (чеки, зарплаты, время сессии в приложении) подчиняются **скошенным распределениям с тяжелыми правыми хвостами** (Log-normal, Pareto).

- **Среднее (Mean)**: Чувствительно к единичным крупным выбросам.
- **Медиана (Median, 50-й перцентиль)**: Робастная метрика, делящая выборку ровно пополам.
"""),
    ("code", """import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Симулируем распределение доходов пользователей (Парето)
np.random.seed(42)
incomes = np.random.pareto(a=2.5, size=5000) * 40000 + 25000

mean_val = np.mean(incomes)
median_val = np.median(incomes)
q75 = np.percentile(incomes, 75)
q90 = np.percentile(incomes, 90)

print(f"Средний доход: {mean_val:,.0f} руб (Искажен длинным хвостом)")
print(f"Медианный доход: {median_val:,.0f} руб (Отражает реальный средний класс)")
print(f"75% пользователей зарабатывают меньше: {q75:,.0f} руб")
print(f"90% пользователей зарабатывают меньше: {q90:,.0f} руб")
""")
])

# Lesson 2
create_notebook(os.path.join(m05, "lesson_02_probability_bayes_law_of_large_numbers.ipynb"), [
    ("markdown", """# 🎲 Модуль 5. Урок 2: Теория вероятностей и Теорема Байеса в Финтехе

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_05_statistics/lesson_02_probability_bayes_law_of_large_numbers.ipynb)

---

## 1. Реальный кейс Банка: Антифрод-система и Базовая ставка (Base Rate Fallacy)

Формула Байеса связывает априорную вероятность с новыми свидетельствами:
$$P(\\text{Fraud} | \\text{Alert}) = \\frac{P(\\text{Alert} | \\text{Fraud}) \\cdot P(\\text{Fraud})}{P(\\text{Alert})}$$
"""),
    ("code", """# Кейс: Модель антифрода с точностью 98%
# P(Fraud) = 0.005 (0.5% транзакций мошеннические)
# Sensitivity = 0.98 (поймает 98% мошенников)
# False Positive Rate = 0.02 (на 2% честных операций ложно сработает)

p_fraud = 0.005
p_clean = 0.995
p_alert_fraud = 0.98
p_alert_clean = 0.02

# Полная вероятность срабатывания алерта
p_alert = (p_alert_fraud * p_fraud) + (p_alert_clean * p_clean)

# Истинная вероятность фрода при сработавшем алерте
p_true_fraud = (p_alert_fraud * p_fraud) / p_alert

print(f"Вероятность того, что заблокированный платеж реально мошеннический: {p_true_fraud*100:.1f}%")
print("ШОК-ВЫВОД ДЛЯ РУКОВОДСТВА: Почти 80% заблокированных операций — ЧЕСТНЫЕ КЛИЕНТЫ!")
""")
])

# Lesson 3
create_notebook(os.path.join(m05, "lesson_03_distributions_clt_confidence_intervals.ipynb"), [
    ("markdown", """# 🔔 Модуль 5. Урок 3: Центральная предельная теорема (ЦПТ) и 95% Доверительные интервалы

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_05_statistics/lesson_03_distributions_clt_confidence_intervals.ipynb)

---

## 1. Смысл 95% Доверительного интервала (Confidence Interval)

Формула для среднего значения:
$$CI = \\bar{X} \\pm 1.96 \\cdot \\frac{\\sigma}{\\sqrt{n}}$$

> **Что это значит простыми словами?** Если мы повторим наш эксперимент 100 раз и построим 100 интервалов, ровно 95 из них накроют истинное среднее генеральной совокупности.
"""),
    ("code", """import numpy as np
from scipy import stats

np.random.seed(42)
sample_checks = np.random.exponential(scale=2500, size=400) # 400 чеков клиентов

mean = np.mean(sample_checks)
sem = stats.sem(sample_checks) # Стандартная ошибка среднего
ci = stats.t.interval(0.95, df=len(sample_checks)-1, loc=mean, scale=sem)

print(f"Выборочное среднее: {mean:.2f} руб")
print(f"95% Доверительный интервал: [{ci[0]:.2f}, {ci[1]:.2f}] руб")
print(f"Бизнес-интерпретация: Мы на 95% уверены, что истинный средний чек бизнеса лежит в диапазоне от {ci[0]:.0f} до {ci[1]:.0f} руб.")
""")
])

# Lesson 4
create_notebook(os.path.join(m05, "lesson_04_hypothesis_testing_p_value_ttest_mann_whitney.ipynb"), [
    ("markdown", """# ⚖️ Модуль 5. Урок 4: Проверка гипотез: $p$-value, t-тест Стьюдента и критерий Манна-Уитни

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_05_statistics/lesson_04_hypothesis_testing_p_value_ttest_mann_whitney.ipynb)

---

## 1. Решающее дерево выбора статистического критерия

```
                          [Какая метрика?]
                                 │
           ┌─────────────────────┴─────────────────────┐
     [Качественная (Доли / CR)]              [Количественная (Чеки, Время)]
           │                                           │
  Z-test пропорций / Хи-квадрат            [Нормальное распределение?]
                                                       │
                                   ┌───────────────────┴───────────────────┐
                                 [ДА]                                    [НЕТ]
                             t-тест Стьюдента                   U-тест Манна-Уитни / Бутстрап
```
"""),
    ("code", """from scipy import stats
import numpy as np

# Сравнение времени загрузки двух версий приложения
np.random.seed(101)
time_v1 = np.random.normal(loc=1.8, scale=0.4, size=300) # Старая версия
time_v2 = np.random.normal(loc=1.65, scale=0.38, size=300) # Новая оптимизированная версия

# Двухвыборочный t-тест (H0: разницы нет, H1: время отличается)
t_stat, p_val = stats.ttest_ind(time_v1, time_v2)

print(f"Среднее время V1: {time_v1.mean():.3f} сек")
print(f"Среднее время V2: {time_v2.mean():.3f} сек (Ускорение на 150 мс)")
print(f"p-value: {p_val:.6f}")

if p_val < 0.05:
    print(" Результат статистически значим (p < 0.05)! Новая версия приложения реально быстрее.")
""")
])

# Lesson 5
create_notebook(os.path.join(m05, "lesson_05_correlation_and_regression_ols_logistic.ipynb"), [
    ("markdown", """# 📈 Модуль 5. Урок 5: Корреляция vs Причинность и Регрессионный анализ (OLS)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_05_statistics/lesson_05_correlation_and_regression_ols_logistic.ipynb)

---

## 1. Уравнение множественной линейной регрессии

$$Y = \\beta_0 + \\beta_1 X_1 + \\beta_2 X_2 + \\dots + \\epsilon$$

### Главные метрики качества модели:
- **$R^2$ (Коэффициент детерминации)**: Какую долю дисперсии целевой переменной объясняет наша модель ($0.0 \\dots 1.0$).
- **p-value коэффициента $\\beta_i$**: Если $p > 0.05$, фактор статистически незначим и должен быть исключен.
"""),
    ("code", """import pandas as pd
import statsmodels.api as sm

saas = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\saas_users.csv")

# Исследуем, какие факторы влияют на отток (MRR компании)
X = saas[['active_seats', 'feature_a_usage', 'nps_score']]
X = sm.add_constant(X)
y = saas['mrr']

model = sm.OLS(y, X).fit()
print("РЕЗУЛЬТАТЫ РЕГРЕССИОННОГО АНАЛИЗА:")
print(f"R-squared: {model.rsquared:.3f}")
print("\\nКоэффициенты модели:")
print(model.params.round(3))
print("\\np-values факторов:")
print(model.pvalues.apply(lambda x: f"{x:.4f}"))
""")
])

# Lesson 6
create_notebook(os.path.join(m05, "lesson_06_statistical_traps_in_business.ipynb"), [
    ("markdown", """# ⚠️ Модуль 5. Урок 6: Статистические ловушки бизнеса: Парадокс Симпсона и Ошибка выжившего

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_05_statistics/lesson_06_statistical_traps_in_business.ipynb)

---

## 1. Классические когнитивные искажения при анализе данных

1. **Парадокс Симпсона**: Направление тренда меняется на противоположное при объединении групп. Решение: Всегда исследовать данные в срезах!
2. **Ошибка выжившего (Survivorship Bias)**: Анализ только тех клиентов, кто остался в сервисе 6 месяцев, полностью игнорируя 80% отвалившихся в первую неделю.
3. **Регрессия к среднему (Regression to the Mean)**: Экстремальный всплеск продаж в понедельник естественным образом сменится спадом во вторник без всякого вмешательства менеджмента.
""")
])

# Module 05 Quiz
with open(os.path.join(m05, "quiz.md"), "w", encoding="utf-8") as f:
    f.write("""# 🧠 Quiz: Самопроверка по Модулю 5 (Статистика & Гипотезы)

---

### Вопрос 1
Что в строгом математическом смысле показывает $p\\text{-value} = 0.02$?
- [ ] Вероятность того, что альтернативная гипотеза верна, равна 98%.
- [x] Вероятность получить такое же или еще более сильное различие случайно, если нулевая гипотеза (об отсутствии эффекта) на самом деле верна, составляет 2%.
- [ ] Ошибка в расчете доверительного интервала.
*Объяснение*: $p$-value — это условная вероятность наблюдаемых данных при истинности нулевой гипотезы $P(\\text{Data} | H_0)$.

---

### Вопрос 2
В каких случаях следует отдать предпочтение U-критерию Манна-Уитни перед t-тестом Стьюдента?
- [ ] Когда выборка идеально подчиняется нормальному распределению Гаусса.
- [x] Когда данные имеют сильную асимметрию, тяжелые хвосты и не подчиняются нормальному распределению (например, доходы или чеки).
- [ ] Когда сравниваются доли конверсий.
*Объяснение*: Манна-Уитни — непараметрический ранговый критерий, он сравнивает распределение рангов и устойчив к экстремальным выбросам.

---

### Вопрос 3
Что описывает Парадокс Симпсона?
- [ ] Ошибку округления при делении на ноль.
- [x] Ситуацию, когда тренд, наблюдаемый в отдельных подгруппах данных, полностью исчезает или меняет знак на противоположный при объединении этих групп.
- [ ] Корреляцию двух не связанных случайных величин.
*Объяснение*: Парадокс возникает из-за неравномерного распределения скрытой переменной (confounding variable), например, перекоса трафика между десктопом и мобайлом.
""")

print("Module 05 deepened successfully.")
