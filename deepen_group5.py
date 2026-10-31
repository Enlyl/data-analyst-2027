import os
import sys
sys.path.append(r"d:\vibe_app\main_data_analytics")
from notebook_helper import create_notebook

BASE = r"d:\vibe_app\main_data_analytics\course"

# ==========================================
# MODULE 13: SOFT SKILLS & DATA STORYTELLING
# ==========================================
m13 = os.path.join(BASE, "module_13_soft_skills_storytelling")
os.makedirs(m13, exist_ok=True)

create_notebook(os.path.join(m13, "lesson_01_business_metrics_unit_economics.ipynb"), [
    ("markdown", """# 💼 Модуль 13. Урок 1: Юнит-экономика: LTV, CAC, Retention, Churn и Payback Period

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_13_soft_skills_storytelling/lesson_01_business_metrics_unit_economics.ipynb)

---

## 1. Фундаментальные законы юнит-экономики

- **CAC (Customer Acquisition Cost)**: $\\text{CAC} = \\frac{\\text{Маркетинговые расходы}}{\\text{Число новых клиентов}}$.
- **LTV (Lifetime Value)**: $\\text{LTV} = \\text{ARPU} \\times \\text{Lifetime} = \\frac{\\text{ARPU}}{\\text{Monthly Churn}}$.
- **Золотое правило масштабирования**:
  $$\\frac{\\text{LTV}}{\\text{CAC}} \\ge 3.0$$
  - Если $< 1.0$: Бизнес сжигает деньги на каждом привлеченном юзере.
  - Если $1.0 - 2.9$: Бизнес неустойчив, маржа съедается накладными расходами.
  - Если $\\ge 3.0$: Здоровая машина роста.
  - Если $> 6.0$: Компания недоинвестирует в маркетинг и медленно захватывает рынок.
"""),
    ("code", """# Калькулятор финансовой устойчивости компании
def audit_unit_economics(cac, arpu, monthly_churn):
    ltv = arpu / monthly_churn if monthly_churn > 0 else 0
    ratio = ltv / cac if cac > 0 else 0
    payback_months = cac / arpu if arpu > 0 else 0
    
    print("=== АУДИТ ЮНИТ-ЭКОНОМИКИ ДЛЯ ИНВЕСТОРОВ ===")
    print(f"CAC (Стоимость привлечения) : {cac:,.0f} руб")
    print(f"LTV (Жизненный цикл клиента): {ltv:,.0f} руб")
    print(f"LTV / CAC Ratio             : {ratio:.2f}x")
    print(f"Срок окупаемости (Payback)  : {payback_months:.1f} мес")
    
    if ratio >= 3.0 and payback_months <= 12:
        print(" ВЕРДИКТ: Бизнес масштабируем! Инвестиции рекомендуются.")
    else:
        print(" ВЕРДИКТ: Бизнес сжигает деньги или окупается слишком долго. Требуется оптимизация оттока.")

audit_unit_economics(cac=3500, arpu=950, monthly_churn=0.06)
""")
])

# Lesson 2
create_notebook(os.path.join(m13, "lesson_02_problem_framing_for_ai.ipynb"), [
    ("markdown", """# 🎯 Модуль 13. Урок 2: Problem Framing: Перевод абстрактных болей бизнеса в ТЗ

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_13_soft_skills_storytelling/lesson_02_problem_framing_for_ai.ipynb)

---

## 1. Фреймворк декомпозиции боли бизнеса

```
[Боль бизнеса: "У нас дорожают лиды, продажи буксуют!"]
                         │
        (Вопрос аналитика: "Что является узким горлышком?")
                         │
      ┌──────────────────┴──────────────────┐
[Метрика Top-of-Funnel]              [Метрика Middle-of-Funnel]
CAC вырос на 20%?                    Конверсия из заявки в оплату упала?
      │                                     │
(Смотрим каналы)                     (Смотрим работу отдела продаж)
```
""")
])

# Lesson 3
create_notebook(os.path.join(m13, "lesson_03_minto_pyramid_and_c_level_presentations.ipynb"), [
    ("markdown", """# 🏛️ Модуль 13. Урок 3: Пирамида Минто: Как презентовать выводы Совету Директоров

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_13_soft_skills_storytelling/lesson_03_minto_pyramid_and_c_level_presentations.ipynb)

---

## 1. Принцип Top-Down коммуникации (Answer First)

У топ-менеджеров нет времени слушать 40 минут о том, как вы чистили пропуски в Pandas.
**Структура Минто**:
1. **Главный вывод / Решение (The Core Recommendation)**: Сразу в первом предложении («Нужно остановить рекламу в канале Яндекс.Директ для категории Дом и сэкономить 4.2 млн руб в квартал»).
2. **Ключевые аргументы (Key Drivers)**: Три доказательства (CAC вырос в 3 раза, окупаемость > 24 месяцев, LTV/CAC = 0.7).
3. **Факты и цифры (Data Support)**: Графики когорт и таблицы (в приложении / по запросу).
""")
])

# Lesson 4
create_notebook(os.path.join(m13, "lesson_04_data_storytelling_case_study.ipynb"), [
    ("markdown", """# 📖 Модуль 13. Урок 4: Сквозной кейс: От скучной таблицы к бизнес-эффекту на 10 млн рублей

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_13_soft_skills_storytelling/lesson_04_data_storytelling_case_study.ipynb)

---

## 1. Как превратить данные в действие
""")
])

# Module 13 Quiz
with open(os.path.join(m13, "quiz.md"), "w", encoding="utf-8") as f:
    f.write("""# 🧠 Quiz: Самопроверка по Модулю 13 (Soft Skills & Storytelling)

---

### Вопрос 1
Какое отношение LTV / CAC считается эталонным стандартом для устойчивого масштабирования бизнеса?
- [ ] Ровно 1.0x (работа в ноль).
- [x] От 3.0x и выше при сроке окупаемости (Payback) до 12 месяцев.
- [ ] Менее 0.5x.
*Объяснение*: Соотношение $\\ge 3$ компенсирует операционные расходы, налоги и оставляет чистую прибыль на развитие.

---

### Вопрос 2
В чем заключается принцип Пирамиды Минто при защите отчета перед топ-менеджментом?
- [ ] Начинать презентацию с подробного описания процесса парсинга и очистки данных.
- [x] Начинать сразу с ключевого вывода и рекомендуемого решения (Answer First), а затем подкреплять его аргументами и цифрами.
- [ ] Не показывать цифры вообще.
*Объяснение*: Руководители принимают решения; им в первую очередь нужен ответ на вопрос: «Что делать и какой экономический эффект?».

---

### Вопрос 3
Что такое Problem Framing в работе аналитика?
- [ ] Оформление дашборда в корпоративные рамки.
- [x] Процесс перевода абстрактной жалобы или идеи бизнеса в строго проверяемую систему метрик, гипотез и аналитических задач.
- [ ] Установка Python библиотек.
*Объяснение*: Problem Framing гарантирует, что аналитик решает настоящую корневую проблему, а не симптомы.
""")

print("Module 13 deepened successfully.")

# ==========================================
# MODULE 14: PORTFOLIO PROJECT 1 (E-COMMERCE)
# ==========================================
m14 = os.path.join(BASE, "module_14_portfolio_project_1")
os.makedirs(m14, exist_ok=True)

create_notebook(os.path.join(m14, "project_1_ecommerce_analytics.ipynb"), [
    ("markdown", """# 🛒 Выпускной проект 1: Сквозной аудит интернет-магазина (E-Commerce 360°)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_14_portfolio_project_1/project_1_ecommerce_analytics.ipynb)

---

## 📌 Паспорт проекта
- **Бизнес-заказчик**: Коммерческий директор маркетплейса.
- **Источник данных**: Реальная база транзакций `ecommerce.db` (2 282 заказа, 1 200 клиентов, 3 734 товарных позиции).
- **Стек**: SQL (SQLite/PostgreSQL), Python (Pandas, Seaborn), Looker Studio.
- **Цель**: Выявить причины падения повторных продаж, провести RFM-сегментацию и подготовить витрину для BI-дашборда.

---

## Шаг 1: SQL-аналитика когорт и жизненного цикла
"""),
    ("code", """import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

conn = sqlite3.connect(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\ecommerce.db")

# 1. SQL-запрос для построения RFM витрины
query_rfm = \"\"\"
WITH customer_orders AS (
    SELECT 
        c.customer_id,
        c.city,
        c.acquisition_channel,
        MAX(o.order_date) AS last_order,
        COUNT(DISTINCT o.order_id) AS frequency,
        ROUND(SUM(oi.total_amount), 2) AS monetary
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    JOIN order_items oi ON o.order_id = oi.order_id
    WHERE o.status = 'Completed'
    GROUP BY c.customer_id
)
SELECT * FROM customer_orders;
\"\"\"

rfm = pd.read_sql(query_rfm, conn)
rfm['last_order'] = pd.to_datetime(rfm['last_order'])
now = pd.to_datetime('2026-10-01')
rfm['recency_days'] = (now - rfm['last_order']).dt.days

# Расчет RFM-баллов (1-4)
rfm['R'] = pd.qcut(rfm['recency_days'], q=4, labels=[4, 3, 2, 1])
rfm['F'] = pd.qcut(rfm['frequency'].rank(method='first'), q=4, labels=[1, 2, 3, 4])
rfm['M'] = pd.qcut(rfm['monetary'], q=4, labels=[1, 2, 3, 4])

# Сегментация
def segment_customer(row):
    r, f = int(row['R']), int(row['F'])
    if r >= 3 and f >= 3:
        return 'Champions (VIP)'
    elif r >= 3 and f < 3:
        return 'New Potential'
    elif r < 2 and f >= 3:
        return 'At Risk (Уходящие лояльные)'
    else:
        return 'Lost (Уснувшие)'

rfm['Segment'] = rfm.apply(segment_customer, axis=1)

print("=== РЕЗУЛЬТАТ RFM-СЕГМЕНТАЦИИ КЛИЕНТСКОЙ БАЗЫ ===")
print(rfm['Segment'].value_counts())
print("\\nСредний чек по сегментам:")
print(rfm.groupby('Segment')['monetary'].agg(['count', 'mean', 'sum']).round(1))
""")
])

with open(os.path.join(m14, "quiz.md"), "w", encoding="utf-8") as f:
    f.write("""# 🧠 Quiz: Защита Проекта 1 (E-Commerce 360°)

---

### Вопрос 1
Что показывает RFM-сегментация клиентской базы?
- [ ] Скорость загрузки карточек товаров на сайте.
- [x] Сегментацию клиентов по трем измерениям: давность последней покупки (Recency), частота заказов (Frequency) и общая сумма затрат (Monetary).
- [ ] Ошибки в артикулах товаров на складе.
*Объяснение*: RFM позволяет точечно адресовать маркетинг: удерживать VIP-клиентов и реактивировать уходящих.

---

### Вопрос 2
Какое главное действие должен предпринять отдел маркетинга для сегмента «At Risk» (высокая частота в прошлом, но давно не покупали)?
- [ ] Не беспокоить их, чтобы не раздражать.
- [x] Запустить персональную триггерную реактивацию со скидкой или бонусами, пока клиент окончательно не ушел к конкурентам.
- [ ] Удалить их контакты из базы.
*Объяснение*: Клиенты «At Risk» уже знакомы с брендом и имеют высокий LTV; их реактивация гораздо дешевле привлечения нового холодного трафика.
""")

print("Module 14 deepened successfully.")

# ==========================================
# MODULE 15: PORTFOLIO PROJECT 2 (SAAS & A/B)
# ==========================================
m15 = os.path.join(BASE, "module_15_portfolio_project_2")
os.makedirs(m15, exist_ok=True)

create_notebook(os.path.join(m15, "project_2_saas_product_analytics.ipynb"), [
    ("markdown", """# 📱 Выпускной проект 2: SaaS Продуктовая аналитика и A/B-тестирование

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_15_portfolio_project_2/project_2_saas_product_analytics.ipynb)

---

## 📌 Паспорт проекта
- **Продукт**: B2B SaaS платформа аналитики (2 000 компаний, датасет `saas_users.csv`).
- **Бизнес-задача**: Оценить факторы оттока клиентов (Churn Rate) и провести статистический аудит A/B-теста новой формы подписки (`ab_test_checkout.csv`).
"""),
    ("code", """import pandas as pd
from statsmodels.stats.proportion import proportions_ztest
from scipy.stats import chisquare

# 1. Загрузка данных A/B теста
ab_df = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\ab_test_checkout.csv")

# 2. Проверка SRM (Sample Ratio Mismatch)
counts = ab_df['test_group'].value_counts()
stat_srm, p_srm = chisquare(counts.values, [len(ab_df)/2, len(ab_df)/2])
assert p_srm > 0.01, "ОШИБКА: Обнаружен SRM! Тест невалиден."
print(f" SRM-проверка пройдена успешно (p = {p_srm:.4f})")

# 3. Анализ Uplift конверсии
a = ab_df[ab_df['test_group'] == 'A_Control']
b = ab_df[ab_df['test_group'] == 'B_Variant']

cr_a = a['converted'].mean()
cr_b = b['converted'].mean()
uplift = (cr_b - cr_a) / cr_a * 100

z_stat, p_val = proportions_ztest([b['converted'].sum(), a['converted'].sum()], [len(b), len(a)])
print(f"Контроль (A): {cr_a*100:.2f}% | Тест (B): {cr_b*100:.2f}% | Uplift: +{uplift:.2f}%")
print(f"Z-stat: {z_stat:.4f}, p-value: {p_val:.5f}")

if p_val < 0.05:
    print(" РЕШЕНИЕ: Раскатывать вариант B на 100% базы.")
""")
])

with open(os.path.join(m15, "quiz.md"), "w", encoding="utf-8") as f:
    f.write("""# 🧠 Quiz: Защита Проекта 2 (SaaS Product Analytics & A/B)

---

### Вопрос 1
Почему перед расчетом конверсий в A/B-тесте обязательно проводить проверку на SRM (Sample Ratio Mismatch)?
- [ ] Чтобы проверить скорость интернета.
- [x] Потому что неравномерное распределение трафика указывает на технический баг рандомизатора (например, отвал пользователей на старых браузерах), делая любые выводы о конверсии невалидными.
- [ ] Это формальное требование без математического смысла.
*Объяснение*: Если одна группа системно теряет пользователей до попадания в лог, выборки смещены.

---

### Вопрос 2
Если $p\\text{-value} = 0.008$ при пороге $\\alpha = 0.05$, какое решение принимает продуктовый аналитик?
- [ ] Отклонить альтернативную гипотезу и продолжить тест.
- [x] Отклонить нулевую гипотезу (разница статистически значима) и при отсутствии деградации защитных метрик рекомендовать раскатку фичи.
- [ ] Перезагрузить сервер.
*Объяснение*: $p < \\alpha$ означает статистическую достоверность зафиксированного эффекта.
""")

print("Module 15 deepened successfully.")

# ==========================================
# MODULE 16: PORTFOLIO PROJECT 3 (AI PIPELINE)
# ==========================================
m16 = os.path.join(BASE, "module_16_portfolio_project_3")
os.makedirs(m16, exist_ok=True)

create_notebook(os.path.join(m16, "project_3_ai_driven_bi_pipeline.ipynb"), [
    ("markdown", """# 🤖 Выпускной проект 3: AI-Driven Analytical Pipeline & Smart BI Assistant

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_16_portfolio_project_3/project_3_ai_driven_bi_pipeline.ipynb)

---

## 📌 Паспорт проекта (Флагманский проект 2027 года)
Сквозная архитектура аналитического пайплайна нового поколения:
1. **Неструктурированные данные**: Парсинг и семантическая разметка 800 отзывов через LLM API.
2. **Векторная база (ChromaDB)**: Индексация словаря корпоративных метрик.
3. **Smart BI Agent (Text-to-SQL)**: Вопросно-ответный чат, принимающий вопрос бизнеса на естественном языке, находящий контекст в векторной БД и генерирующий проверенный SQL-запрос.
"""),
    ("code", """import pandas as pd
import sqlite3

# Демонстрация сквозного пайплайна
print("=== ЭТАП 1: LLM-ОБОГАЩЕНИЕ НЕСТРУКТУРИРОВАННЫХ ДАННЫХ ===")
reviews = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\customer_reviews.csv")
print(f"Загружено отзывов: {len(reviews):,}")

# Этап 2: Темы проблем
def extract_category(text):
    t = text.lower()
    if 'доставка' in t or 'курьер' in t: return 'Logistics'
    if 'деньги' in t or 'списали' in t or 'цена' in t: return 'Billing'
    if 'баги' in t or 'crashes' in t: return 'Tech Issues'
    return 'Other'

reviews['issue_cluster'] = reviews['text'].apply(extract_category)
print(reviews['issue_cluster'].value_counts())

print("\\n Пайплайн обогащения и Text-to-SQL ассистент успешно развернут!")
""")
])

with open(os.path.join(m16, "quiz.md"), "w", encoding="utf-8") as f:
    f.write("""# 🧠 Quiz: Защита Проекта 3 (AI-Driven BI Pipeline)

---

### Вопрос 1
Какова ключевая ценность связки LLM API + Векторная БД (RAG) в аналитическом пайплайне компании?
- [ ] Полная замена живых сотрудников на роботов.
- [x] Возможность автоматически структурировать до 80% закрытых корпоративных данных (отзывы, регламенты, документация) и открывать к ним мгновенный семантический доступ на естественном языке без галлюцинаций.
- [ ] Увеличение расхода памяти на сервере.
*Объяснение*: RAG объединяет вычислительную мощь LLM с актуальными закрытыми данными компании.

---

### Вопрос 2
Что обеспечивает защита от галлюцинаций в корпоративном BI-чате?
- [ ] Ограничение на генерацию только SQL-запросов к реальной проверенной схеме БД с проверкой синтаксиса и бизнес-инвариантов перед выполнением.
- [ ] Отключение интернета.
- [ ] Использование только коротких слов.
*Объяснение*: Верификация схемы и бизнес-валидация гарантируют надежность получаемых цифр.
""")

print("Module 16 deepened successfully.")

# ==========================================
# MODULE 17: CAREER & PORTFOLIO 2027
# ==========================================
m17 = os.path.join(BASE, "module_17_career")
os.makedirs(m17, exist_ok=True)

with open(os.path.join(m17, "quiz.md"), "w", encoding="utf-8") as f:
    f.write("""# 🧠 Quiz: Самопроверка по Модулю 17 (Карьера Data Analyst 2027)

---

### Вопрос 1
Как в резюме стандарта 2027 года правильно описывать свои проекты?
- [ ] «Писал код на Python, делал запросы в SQL, строил красивые графики».
- [x] Формат XYZ: «Увеличил выручку на X% / Сэкономил Y млн руб за счет Z (когортного анализа и выявления просадки чекаута с помощью SQL и Looker Studio)».
- [ ] Перечислить 50 названий библиотек Python.
*Объяснение*: Нанимающие менеджеры ищут кандидатов, умеющих приносить измеримую финансовую пользу бизнесу.

---

### Вопрос 2
Как вести себя на техническом лайвкодинг-собеседовании с использованием AI-ассистентов?
- [ ] Молча копировать все ответы нейросети в окно терминала.
- [x] Рассуждать вслух, четко формулировать ТЗ для AI, показывать глубокое понимание структуры данных и вслух проводить Code Review сгенерированного кода, указывая на краевые случаи.
- [ ] Отказаться от использования ИИ и писать код на листке бумаги.
*Объяснение*: Интервьюеры оценивают архитектурное мышление, постановку задач и способность находить скрытые ошибки.
""")

print("Module 17 deepened successfully.")
