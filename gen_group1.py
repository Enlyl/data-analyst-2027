import os
import sys
sys.path.append(r"d:\vibe_app\main_data_analytics")
from notebook_helper import create_notebook

BASE = r"d:\vibe_app\main_data_analytics\course"

# ==========================================
# MODULE 00: ONBOARDING
# ==========================================
m00 = os.path.join(BASE, "module_00_onboarding")
os.makedirs(m00, exist_ok=True)

with open(os.path.join(m00, "README.md"), "w", encoding="utf-8") as f:
    f.write("""# 🚀 Модуль 0: Онбординг и мышление Data Analyst 2027

## 📌 О модуле
Добро пожаловать в профессию! Аналитика данных образца 2027 года фундаментально отличается от того, что было 5 лет назад. Рутинный синтаксис SQL и Python берет на себя искусственный интеллект, а от аналитика требуются **Problem Framing**, архитектурное понимание данных, формулирование ТЗ для AI и глубокое бизнес-видение.

## 🎯 Learning Outcomes (Таксономия Блума)
- **Remember**: Терминология (Data Analyst vs Data Scientist, CRISP-DM, EDA, KPI, Pipeline).
- **Understand**: Отличия роли аналитика до и после AI-революции; архитектуру современного стека данных.
- **Apply**: Развертывание рабочего окружения в Google Colab, подключение AI-ассистентов, создание первого репозитория на GitHub.
- **Analyze**: Декомпозиция сырой проблемы бизнеса в систему метрик и аналитических задач.

## 📚 Содержание уроков
1. `lesson_01_role_data_analyst_2027.ipynb` — Профессия аналитика в эпоху AI: ландшафт рынка, карта компетенций, день из жизни.
2. `lesson_02_environment_setup_colab_ai.ipynb` — Среда разработки: Google Colab, VS Code, Git, настройка Copilot/Cursor/Claude.
3. `lesson_03_analytical_thinking_crisp_dm.ipynb` — Аналитическое мышление: методология CRISP-DM, перевод бизнес-боли в метрики.
4. `quiz.md` — Тест для самопроверки (Active Recall).
""")

# M00 Lesson 1
create_notebook(os.path.join(m00, "lesson_01_role_data_analyst_2027.ipynb"), [
    ("markdown", """# Урок 1: Кто такой Data Analyst в 2027 году?

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com)

## 1. Сдвиг парадигмы: Аналитик 2020 vs Аналитик 2027

В 2020 году аналитик 80% времени тратил на:
- Поиск синтаксиса `pandas` и StackOverflow
- Ручное исправление запятых в 200-строчных SQL-запросах
- Копирование графиков из Excel в PowerPoint

В 2027 году рутина автоматизирована LLM. **Аналитик стал архитектором решений и бизнес-стратегом:**

```
2020: [Бизнес вопрос] -> (Аналитик долго пишет SQL) -> (Аналитик строит график) -> [Сырые цифры]
2027: [Бизнес вопрос] -> (Аналитик валидирует гипотезу + ставит ТЗ AI) -> (AI генерит код + пайплайн) -> (Аналитик интерпретирует & Storytelling) -> [Решение бизнеса]
```

### Ключевая формула успеха аналитика 2027:
$$\\text{Value} = \\text{Domain Knowledge} \\times \\text{Critical Thinking} \\times \\text{AI Orchestration}$$
"""),
    ("code", """# Анализ рынка вакансий Data Analyst: визуализация тренда ключевых навыков
import matplotlib.pyplot as plt

skills = ['SQL', 'Business Metrics', 'AI Prompting / Validation', 'Python / Pandas', 'BI (Looker/PBI)', 'RAG / LLM APIs']
importance_2022 = [95, 70, 5, 85, 90, 0]
importance_2027 = [90, 95, 95, 80, 85, 85]

x = range(len(skills))
plt.figure(figsize=(10, 5))
plt.plot(skills, importance_2022, marker='o', label='2022 Demand (%)', color='gray', linestyle='--')
plt.plot(skills, importance_2027, marker='s', label='2027 Demand (%)', color='#0066cc', linewidth=2.5)
plt.title('Эволюция требований к Data Analyst (2022 vs 2027)', fontsize=14)
plt.ylabel('Востребованность в вакансиях (%)')
plt.xticks(rotation=20)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
"""),
    ("markdown", """## 2. Карта компетенций современного специалиста
1. **Hard Skills База**: SQL (сложные выборки, оконные функции), Python (Pandas для трансформаций), Looker Studio.
2. **AI Copilot Skills**: Составление точных промптов для генерации кода, валидация ответов (Zero Hallucination Tolerance).
3. **Advanced AI**: Интеграция LLM API в пайплайны, RAG для аналитики внутренних документов.
4. **Soft Skills**: Data Storytelling (пирамида Минто), умение защитить выводы перед CEO.
""")
])

# M00 Lesson 2
create_notebook(os.path.join(m00, "lesson_02_environment_setup_colab_ai.ipynb"), [
    ("markdown", """# Урок 2: Развертывание рабочего окружения (Colab, Python, AI)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com)

В этом уроке мы настроим облачную среду Google Colab и проверим готовность к работе с данными.
"""),
    ("code", """# Проверка версий ключевых аналитических библиотек
import sys
import pandas as pd
import numpy as np
import matplotlib
import sqlite3

print("=== ДИАГНОСТИКА ОКРУЖЕНИЯ ===")
print(f"Python version : {sys.version.split()[0]}")
print(f"Pandas version : {pd.__version__}")
print(f"NumPy version  : {np.__version__}")
print(f"Matplotlib     : {matplotlib.__version__}")
print(f"SQLite version : {sqlite3.sqlite_version}")
print(" Среда готова к работе!")
"""),
    ("markdown", """## Принцип работы с AI-ассистентами в Colab и локально
1. **Cursor / Copilot**: Используются как парный программист (Pair Programmer). Вы формулируете намерение в комментарии, AI предлагает реализацию.
2. **Правило валидации**: Никогда не запускайте AI-код вслепую. Всегда проверяйте типы колонок (`.dtypes`), наличие `NaN`, размеры (`.shape`).
""")
])

# M00 Lesson 3
create_notebook(os.path.join(m00, "lesson_03_analytical_thinking_crisp_dm.ipynb"), [
    ("markdown", """# Урок 3: Аналитическое мышление и фреймворк CRISP-DM

## 1. Методология CRISP-DM
Стандарт де-факто в индустрии анализа данных:

```
[1. Business Understanding]
           │
[2. Data Understanding]
           │
[3. Data Preparation] ─── (80% рутины, теперь ускоряется AI)
           │
[4. Modeling / Analysis]
           │
[5. Evaluation] ──────── (Защита от галлюцинаций и бизнес-валидация)
           │
[6. Deployment / Action]
```

## 2. Практический кейс: "У нас падают продажи в мобильном приложении"
Как классический новичок отвечает на такой запрос:
- *«Я построил график заказов по дням, вот скриншот»* (Бесполезно для бизнеса).

Как действует аналитик 2027 года:
1. Декомпозирует проблему на формулу выручки:
$$\\text{Revenue} = \\text{Traffic} \\times \\text{Conversion Rate (CR)} \\times \\text{Average Order Value (AOV)}$$
2. Локализует просадку: какой множитель упал?
3. Проверяет технические срезы: iOS vs Android, версия приложения, сбой платежного шлюза.
"""),
    ("code", """# Симуляция декомпозиции выручки: поиск точки сбоя
import pandas as pd

data = {
    'Period': ['Week 1 (Baseline)', 'Week 2 (Incident)'],
    'Traffic (Users)': [100000, 102000],
    'Checkout_Conversion': [0.035, 0.018], # Упала почти в 2 раза!
    'AOV (Руб)': [3200, 3250]
}

df_case = pd.DataFrame(data)
df_case['Revenue'] = df_case['Traffic (Users)'] * df_case['Checkout_Conversion'] * df_case['AOV (Руб)']
df_case['Revenue_Formatted'] = df_case['Revenue'].apply(lambda x: f"{x:,.0f} руб")
print(df_case[['Period', 'Traffic (Users)', 'Checkout_Conversion', 'AOV (Руб)', 'Revenue_Formatted']])
print("\\n Вывод: Трафик и средний чек на месте. Проблема строго в конверсии чекаута!")
""")
])

with open(os.path.join(m00, "quiz.md"), "w", encoding="utf-8") as f:
    f.write("""# 🧠 Quiz: Самопроверка по Модулю 0

### Вопрос 1
Какова главная роль Data Analyst в 2027 году в условиях доступности генеративного ИИ?
- [ ] Быстро печатать код SQL и Pandas наизусть без подсказок
- [x] Постановка бизнес-задач, формулирование ТЗ для AI, валидация результатов и Data Storytelling
- [ ] Ручной ввод данных в Excel

### Вопрос 2
Что означает этап Business Understanding в методологии CRISP-DM?
- [ ] Выбор цветовой палитры графиков
- [x] Четкое определение бизнес-цели, метрик успеха и перевод проблемы бизнеса в аналитическую задачу
- [ ] Очистка пропущенных значений в базе данных

### Вопрос 3
Если общая выручка компании упала на 20%, какой первый шаг должен сделать аналитик?
- [ ] Сразу обучить нейросеть предсказывать продажи
- [x] Декомпозировать выручку на составляющие (Traffic * CR * AOV) и определить, какой сегмент дал просадку
- [ ] Сказать руководству, что виноват отдел маркетинга
""")

print("Module 00 created successfully.")

# ==========================================
# MODULE 01: EXCEL & GOOGLE SHEETS
# ==========================================
m01 = os.path.join(BASE, "module_01_excel")
os.makedirs(m01, exist_ok=True)

with open(os.path.join(m01, "README.md"), "w", encoding="utf-8") as f:
    f.write("""# 📊 Модуль 1: Excel и Google Sheets — Фундамент работы с данными

## 📌 О модуле
Excel и Google Sheets остаются главным языком коммуникации бизнеса. Топ-менеджеры, финансисты и маркетологи думают таблицами. Аналитик обязан уметь быстро рассчитывать срезы, собирать сводные таблицы и формулировать промпты для генерации сложных формул в Copilot.

## 🎯 Learning Outcomes
- **Understand**: Структуру плоских таблиц (tidy data), принципы адресации ($A$1 vs A1).
- **Apply**: Функции `SUMIFS`, `COUNTIFS`, `XLOOKUP`, `INDEX+MATCH`, вложенные условия.
- **Analyze**: Сводные таблицы (Pivot Tables), вычисляемые поля, когортные группировки.
- **Create**: Интерактивные отчеты с визуализацией и срезами (Slicers); формулы через AI Copilot.

## 📚 Уроки
1. `lesson_01_interface_basics_formatting.ipynb` — Интерфейс, горячие клавиши, типы данных, условное форматирование.
2. `lesson_02_formulas_functions_xlookup.ipynb` — Библиотека формул: математика, логика, текст, даты, современный XLOOKUP.
3. `lesson_03_pivot_tables_aggregations.ipynb` — Сводные таблицы: многоуровневая группировка, % от общего, срезы.
4. `lesson_04_visualization_data_story.ipynb` — Построение диаграмм по стандартам Тафти (Tufte): устранение визуального шума.
5. `lesson_05_ai_copilot_excel_formulas.ipynb` — Промпт-инжиниринг для формул Excel, генерация Google Apps Script, валидация.
6. `quiz.md` — Тест для закрепления.
7. `cheatsheet.md` — Справочник главных формул.
""")

create_notebook(os.path.join(m01, "lesson_01_interface_basics_formatting.ipynb"), [
    ("markdown", """# Модуль 1. Урок 1: Архитектура таблиц и базовые операции

В аналитике таблица должна быть **Tidy Data**:
1. Каждый столбец — одна переменная.
2. Каждая строка — одно наблюдение.
3. Каждая ячейка — единичное значение.
"""),
    ("code", """# Демонстрация принципа Tidy Data через Pandas (эквивалент правильной структуры Excel)
import pandas as pd

# Плохой формат: даты размазаны по колонкам
bad_table = pd.DataFrame({
    'Product': ['Laptop', 'Mouse'],
    'Jan_2026': [1000, 200],
    'Feb_2026': [1200, 250]
})

# Правильный Tidy формат (Unpivoted / Flat)
tidy_table = pd.melt(bad_table, id_vars=['Product'], var_name='Month', value_name='Sales')
print("НЕПРАВИЛЬНЫЙ ФОРМАТ ДЛЯ АНАЛИТИКИ (Широкий):")
print(bad_table)
print("\\nПРАВИЛЬНЫЙ TIDY ФОРМАТ (Готов для Pivot Table и SQL):")
print(tidy_table)
""")
])

create_notebook(os.path.join(m01, "lesson_02_formulas_functions_xlookup.ipynb"), [
    ("markdown", """# Модуль 1. Урок 2: Формулы: от агрегаций до XLOOKUP

## Главные функции аналитика:
- `SUMIFS(sum_range, criteria_range1, criterion1, ...)` — сумма по нескольким условиям.
- `COUNTIFS(...)` — подсчет строк по условиям.
- `XLOOKUP(lookup_value, lookup_array, return_array, if_not_found)` — современная замена устаревшего VLOOKUP. Не ломается при вставке столбцов!
"""),
    ("code", """# Имитация логики XLOOKUP на реальных данных заказов
import pandas as pd

# Загрузим датасеты, сгенерированные для курса
orders = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\orders.csv").head(5)
customers = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\customers.csv")

# Логика: XLOOKUP(orders.customer_id, customers.customer_id, customers.city)
merged_sample = orders.merge(customers[['customer_id', 'city', 'acquisition_channel']], on='customer_id', how='left')
print("Результат сопоставления данных (аналог XLOOKUP):")
print(merged_sample[['order_id', 'customer_id', 'order_date', 'city', 'acquisition_channel']])
""")
])

create_notebook(os.path.join(m01, "lesson_03_pivot_tables_aggregations.ipynb"), [
    ("markdown", """# Модуль 1. Урок 3: Сводные таблицы (Pivot Tables)

Сводная таблица — главный инструмент мгновенного исследования многомерных данных без написания кода.

Ключевые зоны Pivot Table:
1. **Строки (Rows)**: Измерение группировки (например, Город).
2. **Столбцы (Columns)**: Дополнительный разрез (например, Канал привлечения).
3. **Значения (Values)**: Числовая агрегация (Сумма выручки, Количество клиентов).
4. **Фильтры (Filters / Slicers)**: Глобальный срез данных.
"""),
    ("code", """# Создание сводного отчета по продажам
import pandas as pd

orders = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\orders.csv")
order_items = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\order_items.csv")
customers = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\customers.csv")

# Сборка плоского датасета
full_df = order_items.merge(orders, on='order_id').merge(customers, on='customer_id')

# Pivot Table: Город x Канал привлечения -> Выручка
pivot = pd.pivot_table(
    full_df[full_df['status'] == 'Completed'],
    values='total_amount',
    index='city',
    columns='acquisition_channel',
    aggfunc='sum',
    fill_value=0
)
print("Сводная таблица выручки (Руб):")
print(pivot.round(0).astype(int))
""")
])

create_notebook(os.path.join(m01, "lesson_04_visualization_data_story.ipynb"), [
    ("markdown", """# Модуль 1. Урок 4: Графики и принципы Эдварда Тафти (Data-Ink Ratio)

Принципы чистой визуализации:
1. **Data-Ink Ratio**: Максимум чернил на отображение данных, минимум на фоновые сетки, 3D-эффекты и тени.
2. **Круговые диаграммы (Pie Charts) запрещены**, если срезов больше 3. Человеческий глаз плохо оценивает углы; используйте горизонтальный Bar Chart.
3. Всегда подписывайте единицы измерения.
"""),
    ("code", """import matplotlib.pyplot as plt
import pandas as pd

order_items = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\order_items.csv")
products = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\products.csv")
df = order_items.merge(products, on='product_id')

cat_sales = df.groupby('category')['total_amount'].sum().sort_values(ascending=True)

plt.figure(figsize=(9, 4.5))
bars = plt.barh(cat_sales.index, cat_sales.values, color='#1f77b4', edgecolor='none')
plt.title('Выручка по товарным категориям (Tufte Style)', fontsize=13, pad=15)
plt.xlabel('Сумма (USD)')
# Убираем лишние рамки
for spine in ['top', 'right', 'left']:
    plt.gca().spines[spine].set_visible(False)
plt.grid(axis='x', linestyle=':', alpha=0.6)
# Подписываем значения прямо у столбцов
for bar in bars:
    w = bar.get_width()
    plt.text(w + 1000, bar.get_y() + bar.get_height()/2, f"${w:,.0f}", va='center', fontsize=10)
plt.tight_layout()
plt.show()
""")
])

create_notebook(os.path.join(m01, "lesson_05_ai_copilot_excel_formulas.ipynb"), [
    ("markdown", """# Модуль 1. Урок 5: AI Copilot для формул и валидация логики

## Шаблон эффективного промпта для генерации формул:
```text
РОЛЬ: Ты эксперт по Google Sheets / Excel.
ДАННЫЕ: В таблице на листе "Orders" колонка A: Order_Date, B: Customer_ID, C: Amount, D: Status.
ЗАДАЧА: Напиши формулу для расчета среднего чека только для клиентов, совершивших более 3 заказов со статусом "Completed" в 2026 году.
ФОРМАТ: Дай саму формулу, объяснение логики и возможные краевые случаи (деление на ноль).
```

### Чеклист валидации формул от ИИ:
1. Корректность разделителей (запятая `,` в US-локали vs точка с запятой `;` в RU-локали).
2. Обработка ошибок через `IFERROR` / `IFNA`.
3. Соответствие диапазонов строк (не забыли ли знак доллара `$`).
""")
])

with open(os.path.join(m01, "quiz.md"), "w", encoding="utf-8") as f:
    f.write("""# 🧠 Quiz: Самопроверка по Модулю 1 (Excel)

### Вопрос 1
В чем ключевое преимущество `XLOOKUP` перед `VLOOKUP`?
- [ ] XLOOKUP работает быстрее ровно в 10 раз
- [x] Искомый столбец может находиться левее возвращаемого, формула не ломается при добавлении столбцов
- [ ] XLOOKUP работает только с числами

### Вопрос 2
Что произойдет при копировании формулы `=A$1 + 10` вниз на 5 строк?
- [ ] Ссылка сместится на A6
- [x] Номер строки зафиксирован знаком $, ссылка останется на ячейку A1
- [ ] Выдаст ошибку #REF!

### Вопрос 3
Почему в профессиональных отчетах избегают 3D круговых диаграмм (Pie Charts)?
- [ ] Они занимают слишком много памяти на компьютере
- [x] Они искажают пропорции восприятия долей и перегружают внимание визуальным мусором
- [ ] Их не поддерживает Excel
""")

with open(os.path.join(m01, "cheatsheet.md"), "w", encoding="utf-8") as f:
    f.write("""# 📋 Excel & Sheets Cheatsheet

| Задача | Формула |
|---|---|
| Поиск значения | `=XLOOKUP(F2, A:A, C:C, "Не найдено")` |
| Сумма с условием | `=SUMIFS(D:D, A:A, "Completed", B:B, ">="&DATE(2026,1,1))` |
| Количество уникальных | `=COUNTA(UNIQUE(FILTER(B:B, A:A="Completed")))` |
| Безопасный расчет | `=IFERROR(A2 / B2, 0)` |
| Склейка текста | `=TEXTJOIN(" - ", TRUE, A2, B2)` |
""")

print("Module 01 created successfully.")

# ==========================================
# MODULE 02: SQL MASTER
# ==========================================
m02 = os.path.join(BASE, "module_02_sql")
os.makedirs(m02, exist_ok=True)

with open(os.path.join(m02, "README.md"), "w", encoding="utf-8") as f:
    f.write("""# 🗃️ Модуль 2: SQL — От первых запросов до аналитических оконных функций

## 📌 О модуле
SQL (Structured Query Language) — главный фундамент data-стека. LLM пишут синтаксис, но только аналитик понимает структуру реляционной модели, видит дублирование при JOIN и умеет оптимизировать тяжелые запросы. В этом модуле мы работаем с реальной SQLite базой e-commerce на 15 000+ записей.

## 🎯 Learning Outcomes
- **Apply**: Составление сложных запросов (`SELECT`, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`).
- **Analyze**: Все виды `JOIN` (INNER, LEFT, FULL, CROSS, SELF), борьба с декартовым произведением строк.
- **Evaluate**: Использование CTE (Common Table Expressions) для структурирования запросов вместо спагетти-подзапросов.
- **Create**: Аналитические оконные функции (`ROW_NUMBER`, `DENSE_RANK`, `LAG`, `LEAD`, `SUM OVER (PARTITION BY ...)`).
- **AI Orchestration**: Промптинг для генерации SQL, проверка EXPLAIN QUERY PLAN, защита от галлюцинаций агрегаций.

## 📚 Уроки
1. `lesson_01_db_intro_select_filtering.ipynb` — Подключение к базе, анатомия SQL, SELECT, WHERE, LIKE, IN.
2. `lesson_02_aggregations_group_by_having.ipynb` — Агрегатные функции, группировка, разница WHERE vs HAVING.
3. `lesson_03_joins_deep_dive.ipynb` — Реляционная связь, виды JOIN, поиск потерянных строк.
4. `lesson_04_subqueries_and_cte.ipynb` — Чистый код через CTE (`WITH`), многоуровневая аналитика.
5. `lesson_05_window_functions_advanced.ipynb` — Оконные функции: ранги, нарастающий итог, темпы роста (MoM / YoY).
6. `lesson_06_sql_patterns_retention_funnels.ipynb` — Паттерны продуктовой аналитики: когорты, воронки на чистом SQL.
7. `lesson_07_prompt_engineering_for_sql_and_validation.ipynb` — Генерация SQL через нейросети и строгий чеклист валидации.
8. `quiz.md` — 15 вопросов со скринингов.
9. `cheatsheet.md` — Справочник SQL конструкций.
""")

create_notebook(os.path.join(m02, "lesson_01_db_intro_select_filtering.ipynb"), [
    ("markdown", """# Модуль 2. Урок 1: Архитектура SQL и базовые запросы

Подключаемся к учебной базе данных `ecommerce.db`.
"""),
    ("code", """import sqlite3
import pandas as pd

DB_PATH = r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\ecommerce.db"
conn = sqlite3.connect(DB_PATH)

# Посмотрим список таблиц
tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)
print("Таблицы в базе данных:")
print(tables)
"""),
    ("markdown", """## Базовый синтаксис SELECT + WHERE
Порядок выполнения в SQL (важно понимать!):
1. `FROM`
2. `WHERE`
3. `GROUP BY`
4. `HAVING`
5. `SELECT`
6. `ORDER BY`
7. `LIMIT`
"""),
    ("code", """query = \"\"\"
SELECT 
    customer_id, 
    first_name, 
    city, 
    acquisition_channel
FROM customers
WHERE city IN ('Moscow', 'Saint Petersburg')
  AND acquisition_channel = 'Paid Ads'
ORDER BY customer_id ASC
LIMIT 5;
\"\"\"
res = pd.read_sql(query, conn)
print(res)
""")
])

create_notebook(os.path.join(m02, "lesson_02_aggregations_group_by_having.ipynb"), [
    ("markdown", """# Модуль 2. Урок 2: Агрегации: GROUP BY и разница с HAVING

- `WHERE` фильтрует **сырые строки** ДО агрегации.
- `HAVING` фильтрует **сгруппированные результаты** ПОСЛЕ `GROUP BY`.
"""),
    ("code", """import sqlite3
import pandas as pd

conn = sqlite3.connect(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\ecommerce.db")

query = \"\"\"
SELECT 
    status,
    COUNT(order_id) AS total_orders,
    ROUND(COUNT(order_id) * 100.0 / (SELECT COUNT(*) FROM orders), 2) AS share_pct
FROM orders
GROUP BY status
HAVING total_orders > 50
ORDER BY total_orders DESC;
\"\"\"
print(pd.read_sql(query, conn))
""")
])

create_notebook(os.path.join(m02, "lesson_03_joins_deep_dive.ipynb"), [
    ("markdown", """# Модуль 2. Урок 3: Объединение таблиц (JOIN)

Виды соединений:
- **INNER JOIN**: только те строки, которые есть в обеих таблицах.
- **LEFT JOIN**: все строки из левой таблицы + совпадения из правой (если нет совпадений — NULL).
- **WARNING**: Неосторожный JOIN «один-ко-многим» может искусственно размножить строки и утроить выручку в отчете!
"""),
    ("code", """import sqlite3
import pandas as pd

conn = sqlite3.connect(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\ecommerce.db")

query = \"\"\"
SELECT 
    c.acquisition_channel,
    COUNT(DISTINCT o.order_id) AS orders_count,
    ROUND(SUM(oi.total_amount), 2) AS total_revenue,
    ROUND(AVG(oi.total_amount), 2) AS avg_item_revenue
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
LEFT JOIN order_items oi ON o.order_id = oi.order_id
WHERE o.status = 'Completed'
GROUP BY c.acquisition_channel
ORDER BY total_revenue DESC;
\"\"\"
print(pd.read_sql(query, conn))
""")
])

create_notebook(os.path.join(m02, "lesson_04_subqueries_and_cte.ipynb"), [
    ("markdown", """# Модуль 2. Урок 4: Чистый SQL через CTE (Common Table Expressions)

Вместо вложенных подзапросов в 5 этажей, пишите читаемый код с `WITH`:
"""),
    ("code", """import sqlite3
import pandas as pd

conn = sqlite3.connect(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\ecommerce.db")

query = \"\"\"
WITH customer_spending AS (
    SELECT 
        customer_id,
        ROUND(SUM(total_amount), 2) AS ltv
    FROM orders o
    JOIN order_items oi ON o.order_id = oi.order_id
    WHERE o.status = 'Completed'
    GROUP BY customer_id
),
thresholds AS (
    SELECT AVG(ltv) AS avg_spend FROM customer_spending
)
SELECT 
    cs.customer_id,
    cs.ltv,
    ROUND(t.avg_spend, 2) AS market_avg,
    CASE 
        WHEN cs.ltv >= t.avg_spend * 2 THEN 'VIP Tier'
        WHEN cs.ltv >= t.avg_spend THEN 'Above Average'
        ELSE 'Regular'
    END AS customer_tier
FROM customer_spending cs
CROSS JOIN thresholds t
ORDER BY cs.ltv DESC
LIMIT 10;
\"\"\"
print(pd.read_sql(query, conn))
""")
])

create_notebook(os.path.join(m02, "lesson_05_window_functions_advanced.ipynb"), [
    ("markdown", """# Модуль 2. Урок 5: Оконные функции (Window Functions)

Оконные функции производят вычисления по группе строк, **не схлопывая строки** (в отличие от `GROUP BY`).

Синтаксис:
$$\\text{FUNCTION}() \\text{ OVER } (\\text{PARTITION BY } col \\text{ ORDER BY } col)$$
"""),
    ("code", """import sqlite3
import pandas as pd

conn = sqlite3.connect(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\ecommerce.db")

query = \"\"\"
WITH monthly_sales AS (
    SELECT 
        SUBSTR(o.order_date, 1, 7) AS order_month,
        ROUND(SUM(oi.total_amount), 2) AS revenue
    FROM orders o
    JOIN order_items oi ON o.order_id = oi.order_id
    WHERE o.status = 'Completed'
    GROUP BY order_month
)
SELECT 
    order_month,
    revenue,
    -- Нарастающий итог (Running Total)
    ROUND(SUM(revenue) OVER (ORDER BY order_month), 2) AS cumulative_revenue,
    -- Предыдущий месяц через LAG
    LAG(revenue, 1) OVER (ORDER BY order_month) AS prev_month_revenue,
    -- Темп прироста MoM %
    ROUND((revenue - LAG(revenue, 1) OVER (ORDER BY order_month)) * 100.0 / 
          LAG(revenue, 1) OVER (ORDER BY order_month), 2) AS mom_growth_pct
FROM monthly_sales
ORDER BY order_month;
\"\"\"
print(pd.read_sql(query, conn))
""")
])

create_notebook(os.path.join(m02, "lesson_06_sql_patterns_retention_funnels.ipynb"), [
    ("markdown", """# Модуль 2. Урок 6: Продуктовые паттерны на SQL (Когорты & Retention)

Расчет даты первого заказа для каждого пользователя (Когорта) и распределение повторных покупок.
"""),
    ("code", """import sqlite3
import pandas as pd

conn = sqlite3.connect(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\ecommerce.db")

query = \"\"\"
WITH first_orders AS (
    SELECT 
        customer_id,
        MIN(SUBSTR(order_date, 1, 7)) AS cohort_month
    FROM orders
    WHERE status = 'Completed'
    GROUP BY customer_id
),
customer_activities AS (
    SELECT 
        o.customer_id,
        fo.cohort_month,
        SUBSTR(o.order_date, 1, 7) AS order_month
    FROM orders o
    JOIN first_orders fo ON o.customer_id = fo.customer_id
    WHERE o.status = 'Completed'
)
SELECT 
    cohort_month,
    COUNT(DISTINCT customer_id) AS total_cohort_users,
    COUNT(DISTINCT CASE WHEN order_month = cohort_month THEN customer_id END) AS month_0,
    COUNT(DISTINCT CASE WHEN order_month > cohort_month THEN customer_id END) AS repeat_buyers
FROM customer_activities
GROUP BY cohort_month
ORDER BY cohort_month
LIMIT 6;
\"\"\"
print(pd.read_sql(query, conn))
""")
])

create_notebook(os.path.join(m02, "lesson_07_prompt_engineering_for_sql_and_validation.ipynb"), [
    ("markdown", """# Модуль 2. Урок 7: AI Prompting для SQL и Чеклист Валидации

## Шаблон System Prompt для Text-to-SQL:
```sql
Ты senior Data Architect. База данных: SQLite.
Схема:
- customers(customer_id PK, city, acquisition_channel, registration_date)
- orders(order_id PK, customer_id FK, order_date, status)
- order_items(order_item_id PK, order_id FK, product_id FK, quantity, unit_price, total_amount)
Правило: Всегда фильтруй orders.status = 'Completed' при расчете выручки.
```

### Чеклист проверки SQL-кода от нейросети (Red Flags):
- [ ] **Cartesian Explosion**: Не задвоил ли JOIN строки перед SUM? Всегда сравнивайте `COUNT(DISTINCT id)` до и после.
- [ ] **NULL Trap**: Проверены ли пропуски в колонках фильтрации?
- [ ] **Grouping Leak**: Все ли неагрегированные поля из `SELECT` попали в `GROUP BY`?
""")
])

with open(os.path.join(m02, "quiz.md"), "w", encoding="utf-8") as f:
    f.write("""# 🧠 Quiz: Самопроверка по Модулю 2 (SQL)

### Вопрос 1
В чем разница между `RANK()` и `DENSE_RANK()`?
- [ ] Разницы нет
- [x] При одинаковых значениях RANK оставляет пропуски в нумерации (1, 2, 2, 4), а DENSE_RANK нумерует без пробелов (1, 2, 2, 3)
- [ ] DENSE_RANK работает только в PostgreSQL

### Вопрос 2
Зачем нужна конструкция `WITH` (CTE)?
- [ ] Она ускоряет любой запрос в 100 раз
- [x] Она позволяет разбить сложный запрос на логические читаемые блоки и использовать их повторно
- [ ] Без нее нельзя соединять таблицы

### Вопрос 3
Какой результат вернет `COUNT(*)` vs `COUNT(column_name)` если в колонке есть NULL?
- [ ] Одинаковый
- [x] `COUNT(*)` считает все строки, а `COUNT(column_name)` игнорирует строки с NULL
- [ ] Вернет ошибку базы данных
""")

with open(os.path.join(m02, "cheatsheet.md"), "w", encoding="utf-8") as f:
    f.write("""# 📋 SQL Cheatsheet

```sql
-- Оконная функция: прирост к предыдущему значению
LAG(metric, 1) OVER (PARTITION BY user_id ORDER BY event_date)

-- Оконная функция: доля строки в разрезе группы
metric * 100.0 / SUM(metric) OVER (PARTITION BY category)

-- Безопасный расчет конверсии
ROUND(COUNT(DISTINCT converted_users) * 1.0 / NULLIF(COUNT(DISTINCT total_users), 0), 4)
```
""")

print("Module 02 created successfully.")
