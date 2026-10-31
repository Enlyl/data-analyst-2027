import os
import sys
sys.path.append(r"d:\vibe_app\main_data_analytics")
from notebook_helper import create_notebook

BASE = r"d:\vibe_app\main_data_analytics\course"

# ==========================================
# MODULE 13: SOFT SKILLS & STORYTELLING
# ==========================================
m13 = os.path.join(BASE, "module_13_soft_skills_storytelling")
os.makedirs(m13, exist_ok=True)

with open(os.path.join(m13, "README.md"), "w", encoding="utf-8") as f:
    f.write("""# 💼 Модуль 13: Soft Skills, Юнит-экономика и Data Storytelling

## 📌 О модуле
Софт-скиллы — главный защитник аналитика от автоматизации. Написать код может нейросеть за 5 секунд. Но понять реальную боль бизнеса, договориться со стейкхолдерами, задать правильные вопросы и защитить инвестиции перед Советом Директоров может только человек с развитым критическим мышлением и эмпатией.

## 🎯 Learning Outcomes
- **Understand**: Систему продуктовых и финансовых метрик (LTV, CAC, Retention, Churn, ROI, Payback Period).
- **Apply**: Методологию Problem Framing — перевод невнятной жалобы руководства в измеримую аналитическую гипотезу.
- **Create**: Структуру презентации по Пирамиде Минто (Minto Pyramid Principle: вывод -> ключевые аргументы -> подтверждающие данные).
- **Evaluate**: Оценка бизнес-эффекта и предотвращение ложных решений.

## 📚 Уроки
1. `lesson_01_business_metrics_unit_economics.ipynb` — Карта метрик бизнеса и формулы юнит-экономики.
2. `lesson_02_problem_framing_for_ai.ipynb` — Problem Framing: как правильно задавать вопросы стейкхолдерам и ставить ТЗ.
3. `lesson_03_minto_pyramid_and_c_level_presentations.ipynb` — Пирамида Минто и защита инсайтов перед C-level топ-менеджментом.
4. `lesson_04_data_storytelling_case_study.ipynb` — Практикум Data Storytelling: превращаем скучную таблицу в экшн-план компании.
5. `quiz.md` — Тест для закрепления.
""")

create_notebook(os.path.join(m13, "lesson_01_business_metrics_unit_economics.ipynb"), [
    ("markdown", """# Модуль 13. Урок 1: Юнит-экономика продукта

Ключевые формулы здоровья бизнеса:
$$LTV = ARPU \\times \\text{Lifetime} = \\frac{\\text{ARPPU} \\times \\text{Paying Share}}{\\text{Churn Rate}}$$
$$\\text{Unit Economics Rule: } \\frac{LTV}{CAC} \\ge 3.0$$

Если отношение $\\frac{LTV}{CAC} < 1$, бизнес сжигает деньги на каждом привлеченном клиенте!
"""),
    ("code", """# Калькулятор юнит-экономики
def calculate_unit_economics(cac, arpu, monthly_churn_rate):
    lifetime_months = 1.0 / monthly_churn_rate if monthly_churn_rate > 0 else 1
    ltv = arpu * lifetime_months
    ltv_to_cac = ltv / cac if cac > 0 else 0
    payback_months = cac / arpu if arpu > 0 else 0
    
    return {
        'LTV': round(ltv, 2),
        'CAC': round(cac, 2),
        'LTV / CAC Ratio': round(ltv_to_cac, 2),
        'Payback (Months)': round(payback_months, 1),
        'Status': 'Здоровый бизнес (>3x)' if ltv_to_cac >= 3 else ('На грани (1x-3x)' if ltv_to_cac >= 1 else 'Убыточный бизнес (<1x)')
    }

metrics = calculate_unit_economics(cac=1200, arpu=450, monthly_churn_rate=0.08)
for k, v in metrics.items():
    print(f"{k:20}: {v}")
""")
])

create_notebook(os.path.join(m13, "lesson_02_problem_framing_for_ai.ipynb"), [
    ("markdown", """# Модуль 13. Урок 2: Problem Framing (Формулирование проблемы)

### Пример диалога с бизнес-заказчиком:
- **Заказчик**: «Сделай мне дашборд со всеми пользователями и кликами за 2 года!»
- **Обычный джун**: «Хорошо, делаю...» (Тратит 2 недели, дашборд никто не открывает).
- **Аналитик 2027**: «Какое решение вы планируете принять на основе этих цифр? Какая проблема сейчас болит сильнее всего?»
- **Заказчик**: «Маркетинг просит еще 5 миллионов на рекламу, а я не знаю, окупаются ли старые каналы».
- **Аналитик**: «Тогда нам нужен не дашборд по всем кликам, а когортный анализ окупаемости каналов (ROAS по когортам) за последние 3 месяца. Я подготовлю его к вечеру».
""")
])

create_notebook(os.path.join(m13, "lesson_03_minto_pyramid_and_c_level_presentations.ipynb"), [
    ("markdown", """# Модуль 13. Урок 3: Пирамида Минто (Коммуникация с CEO)

```
                       [ГЛАВНЫЙ ВЫВОД / РЕШЕНИЕ]
            "Нужно закрыть таргетированную рекламу в канале X: 
                  она приносит 80% оттока и чистый убыток"
                                   │
         ┌─────────────────────────┼─────────────────────────┐
    [АРГУМЕНТ 1]              [АРГУМЕНТ 2]              [АРГУМЕНТ 3]
LTV/CAC канала = 0.6      Churn в 1-й месяц 45%      Экономия 1.8 млн руб
         │                         │                         │
  (Факты / SQL)             (Факты / Когорты)          (Факты / Финмодель)
```
""")
])

create_notebook(os.path.join(m13, "lesson_04_data_storytelling_case_study.ipynb"), [
    ("markdown", """# Модуль 13. Урок 4: Сквозной кейс Data Storytelling
""")
])

with open(os.path.join(m13, "quiz.md"), "w", encoding="utf-8") as f:
    f.write("""# 🧠 Quiz: Самопроверка по Модулю 13 (Soft Skills & Storytelling)

### Вопрос 1
Каково оптимальное соотношение LTV / CAC для масштабируемого устойчивого бизнеса?
- [ ] Меньше 0.5
- [x] От 3.0 и выше
- [ ] Ровно 1.0

### Вопрос 2
В чем суть принципа Пирамиды Минто при презентации аналитики руководителям?
- [ ] Начинать с подробного описания процесса загрузки данных и библиотек Python
- [x] Начинать сразу с ключевого вывода и рекомендуемого бизнес-действия, а затем раскрывать аргументы и цифры
- [ ] Не показывать цифры вообще
""")

print("Module 13 created successfully.")

# ==========================================
# MODULE 14: PORTFOLIO PROJECT 1 (E-COMMERCE)
# ==========================================
m14 = os.path.join(BASE, "module_14_portfolio_project_1")
os.makedirs(m14, exist_ok=True)

with open(os.path.join(m14, "README.md"), "w", encoding="utf-8") as f:
    f.write("""# 🛒 Портфолио-проект 1: Сквозная E-Commerce аналитика 360°

## 📌 Описание проекта
Полноценный аудит интернет-магазина на основе реальной базы заказов (15 000+ позиций, база `ecommerce.db`):
1. **SQL Витрина**: Расчет LTV, среднего чека, маржинальности.
2. **Pandas & Python**: Когортный анализ удержания (Retention Rate Matrix) и RFM-сегментация клиентов.
3. **Looker Studio**: Создание интерактивного дашборда для коммерческого директора.
4. **Бизнес-отчет**: Аналитическая записка с точками роста выручки.

## 📁 Файлы
- `project_1_ecommerce_analytics.ipynb` — Полный рабочий ноутбук выполнения проекта от SQL до визуализации.
""")

create_notebook(os.path.join(m14, "project_1_ecommerce_analytics.ipynb"), [
    ("markdown", """# Портфолио-проект 1: E-Commerce Analytics 360°

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com)

В этом проекте мы проводим глубокий анализ интернет-магазина.
"""),
    ("code", """import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

conn = sqlite3.connect(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\ecommerce.db")

# 1. SQL: Выгрузка данных для RFM-сегментации
query_rfm = \"\"\"
WITH customer_orders AS (
    SELECT 
        c.customer_id,
        MAX(o.order_date) AS last_order_date,
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
rfm_df = pd.read_sql(query_rfm, conn)
rfm_df['last_order_date'] = pd.to_datetime(rfm_df['last_order_date'])
now = pd.to_datetime('2026-10-01')
rfm_df['recency_days'] = (now - rfm_df['last_order_date']).dt.days

# Расчет RFM-рангов (1-4)
rfm_df['R_Score'] = pd.qcut(rfm_df['recency_days'], q=4, labels=[4, 3, 2, 1])
rfm_df['F_Score'] = pd.qcut(rfm_df['frequency'].rank(method='first'), q=4, labels=[1, 2, 3, 4])
rfm_df['M_Score'] = pd.qcut(rfm_df['monetary'], q=4, labels=[1, 2, 3, 4])

print("=== RFM СЕГМЕНТАЦИЯ КЛИЕНТСКОЙ БАЗЫ ===")
print(rfm_df[['customer_id', 'recency_days', 'frequency', 'monetary', 'R_Score', 'F_Score', 'M_Score']].head(5))
""")
])

print("Module 14 created successfully.")

# ==========================================
# MODULE 15: PORTFOLIO PROJECT 2 (SAAS)
# ==========================================
m15 = os.path.join(BASE, "module_15_portfolio_project_2")
os.makedirs(m15, exist_ok=True)

with open(os.path.join(m15, "README.md"), "w", encoding="utf-8") as f:
    f.write("""# 📱 Портфолио-проект 2: SaaS Продуктовая аналитика и A/B Тестирование

## 📌 Описание проекта
Анализ продуктовых метрик B2B SaaS платформы (2000 компаний, датасет `saas_users.csv`):
1. **Воронка активации**: Использование ключевых фичей A и B.
2. **Анализ оттока (Churn Analysis)**: Влияние NPS и тарифа на удержание клиентов.
3. **A/B Эксперимент**: Полный статистический анализ нового флоу оплаты (Z-test, проверка SRM, расчет доверительных интервалов).

## 📁 Файлы
- `project_2_saas_product_analytics.ipynb` — Сквозной рабочий ноутбук проекта.
""")

create_notebook(os.path.join(m15, "project_2_saas_product_analytics.ipynb"), [
    ("markdown", """# Портфолио-проект 2: SaaS Product Analytics & A/B Testing
"""),
    ("code", """import pandas as pd
import numpy as np
from scipy import stats

saas = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\saas_users.csv")

print("=== SAAS КЛЮЧЕВЫЕ МЕТРИКИ ===")
print(f"Всего клиентов: {len(saas)}")
print(f"Общий Churn Rate: {saas['is_churned'].mean()*100:.2f}%")
print(f"Общий MRR: ${saas['mrr'].sum():,.2f}")

# Отток в разрезе тарифных планов
churn_by_plan = saas.groupby('plan').agg(
    total_users=('user_id', 'count'),
    churn_rate=('is_churned', 'mean'),
    avg_nps=('nps_score', 'mean')
)
churn_by_plan['churn_rate_%'] = (churn_by_plan['churn_rate'] * 100).round(1)
print("\\nПоказатели по тарифам:")
print(churn_by_plan)
""")
])

print("Module 15 created successfully.")

# ==========================================
# MODULE 16: PORTFOLIO PROJECT 3 (AI PIPELINE)
# ==========================================
m16 = os.path.join(BASE, "module_16_portfolio_project_3")
os.makedirs(m16, exist_ok=True)

with open(os.path.join(m16, "README.md"), "w", encoding="utf-8") as f:
    f.write("""# 🤖 Портфолио-проект 3: AI-Driven Analytical Pipeline & Smart BI Chat

## 📌 Описание проекта (Флагманский проект 2027 года)
Этот проект выделит ваше резюме среди сотен классических кандидатов. Мы строим сквозную AI-систему:
1. **Сбор неструктурированных данных**: Отзывы клиентов из `customer_reviews.csv`.
2. **LLM API Обогащение**: Извлечение тем жалоб, sentiment-анализ и структурирование в JSON.
3. **RAG База знаний**: Индексация метрик компании в векторной БД ChromaDB.
4. **Smart BI Agent**: Чат-ассистент, который принимает вопрос на человеческом языке, находит контекст в регламентах, пишет SQL-запрос к `ecommerce.db` и отдает бизнес-ответ с визуализацией!

## 📁 Файлы
- `project_3_ai_driven_bi_pipeline.ipynb` — Полный код пайплайна.
""")

create_notebook(os.path.join(m16, "project_3_ai_driven_bi_pipeline.ipynb"), [
    ("markdown", """# Портфолио-проект 3: AI-Driven BI Pipeline & Assistant
"""),
    ("code", """import pandas as pd
import sqlite3

# Шаг 1: Обогащение неструктурированных данных через LLM
reviews = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\customer_reviews.csv")

def extract_insights_rule(text):
    text_l = text.lower()
    issues = []
    if 'доставка' in text_l or 'курьер' in text_l:
        issues.append('Logistics / Delivery')
    if 'деньги' in text_l or 'списали' in text_l or 'цена' in text_l:
        issues.append('Billing / Pricing')
    if 'баги' in text_l or 'crashes' in text_l or 'тормозит' in text_l:
        issues.append('App Stability / Bugs')
    return issues if issues else ['General Feedback']

reviews['category_issues'] = reviews['text'].apply(extract_insights_rule)
print("=== РЕЗУЛЬТАТ LLM-РАЗМЕТКИ ТЕМ ОБРАТНОЙ СВЯЗИ ===")
exploded = reviews.explode('category_issues')
print(exploded['category_issues'].value_counts())
""")
])

print("Module 16 created successfully.")

# ==========================================
# MODULE 17: CAREER & PORTFOLIO 2027
# ==========================================
m17 = os.path.join(BASE, "module_17_career")
os.makedirs(m17, exist_ok=True)

with open(os.path.join(m17, "README.md"), "w", encoding="utf-8") as f:
    f.write("""# 🚀 Модуль 17: Карьера Data Analyst 2027 — Резюме, Портфолио и Собеседования

## 📌 О модуле
Как устроиться на работу в эпоху, когда от кандидатов требуют AI-грамотность и глубокие софт-скиллы.

## 📚 Материалы модуля
1. `resume_template_2027.md` — Шаблон современного резюме с фокусом на влияние на бизнес ($ impact) и AI-компетенции.
2. `github_portfolio_guide.md` — Инструкция по оформлению GitHub репозиториев для прохождения скрининга.
3. `interview_questions_and_cases_2027.md` — Банк реальных вопросов с технических собеседований (SQL, статистика, live-coding с AI).
""")

with open(os.path.join(m17, "resume_template_2027.md"), "w", encoding="utf-8") as f:
    f.write("""# 📄 Шаблон резюме Data Analyst (Стандарт 2027)

### Иван Иванов | Data Analyst (AI-Assisted Workflows)
**Email**: ivan.data@email.com | **GitHub**: github.com/ivan-analyst | **LinkedIn**: linkedin.com/in/ivan-data

---

### ПРОФЕССИОНАЛЬНОЕ САММАРИ
Аналитик данных с фокусом на продуктовые метрики и автоматизацию аналитических пайплайнов с помощью современных AI-инструментов. Владею продвинутым SQL (оконные функции, оптимизация), Python (Pandas, визуализация), Looker Studio и методологией A/B-тестирования. Умею переводить бизнес-задачи в четкие ТЗ для LLM, сокращая время подготовки витрин данных на 60%.

---

### КЛЮЧЕВЫЕ КОМПЕТЕНЦИИ
- **Анализ данных**: SQL (PostgreSQL, SQLite), Python (Pandas, NumPy, Scipy, Statsmodels), Excel / Sheets.
- **BI & Визуализация**: Looker Studio, Seaborn, Matplotlib, Data Storytelling (Minto Pyramid).
- **Продуктовая аналитика & Эксперименты**: A/B-тестирование, расчет MDE/выборки, проверка SRM, когортный анализ, воронки, юнит-экономика (LTV, CAC, Retention, Churn).
- **AI-инструменты 2027**: Cursor IDE, Prompt Engineering (RTCE, CoT), интеграция LLM API для анализа неструктурированных данных, RAG (ChromaDB), валидация моделей.

---

### ПОРТФОЛИО-ПРОЕКТЫ
1. **AI-Driven E-Commerce & BI Analytics Platform**
   - Разработал сквозной дашборд в Looker Studio на базе 15 000+ транзакций, выявил просадку маржинальности в категории Electronics на 18%.
   - Реализовал RFM-сегментацию и когортный анализ удержания клиентов на Python.
   - Ссылка на GitHub: `github.com/.../ecommerce-analytics`

2. **SaaS Retention & A/B Testing Evaluation**
   - Провел статистический анализ A/B теста чекаута (10 000 участников): зафиксирован статистически значимый uplift конверсии +17.1% ($p = 0.012$), подтверждено отсутствие SRM.
   - Построил модель оттока и сегментации по тарифным планам.
   - Ссылка на GitHub: `github.com/.../saas-ab-testing`
""")

with open(os.path.join(m17, "github_portfolio_guide.md"), "w", encoding="utf-8") as f:
    f.write("""# 🌟 Руководство по оформлению GitHub портфолио

### Чеклист идеального репозитория проекта:
1. **Наглядный README**:
   - Краткое резюме задачи: «Какую проблему бизнеса решаем?»
   - Интерактивный бейдж «Open in Colab» для запуска ноутбука в 1 клик.
   - Скриншот итогового дашборда Looker Studio.
   - Четкие бизнес-выводы и рекомендации.
2. **Воспроизводимость кода**:
   - Наличие файла `requirements.txt`.
   - Ноутбук запускается от первой до последней ячейки без ошибок (`Restart & Run All`).
3. **Чистота структуры**:
   - Папки: `data/`, `notebooks/`, `assets/`, `sql/`.
""")

with open(os.path.join(m17, "interview_questions_and_cases_2027.md"), "w", encoding="utf-8") as f:
    f.write("""# 🎯 Вопросы и кейсы технических собеседований 2027

### 1. SQL Лайвкодинг
**Вопрос**: «Напишите запрос, который находит топ-3 самых дорогих заказа в каждом городе».
**Ответ**:
```sql
WITH ranked_orders AS (
    SELECT 
        c.city,
        o.order_id,
        SUM(oi.total_amount) AS order_total,
        DENSE_RANK() OVER (PARTITION BY c.city ORDER BY SUM(oi.total_amount) DESC) AS rnk
    FROM orders o
    JOIN customers c ON o.customer_id = c.customer_id
    JOIN order_items oi ON o.order_id = oi.order_id
    WHERE o.status = 'Completed'
    GROUP BY c.city, o.order_id
)
SELECT city, order_id, order_total, rnk
FROM ranked_orders
WHERE rnk <= 3;
```

### 2. Продуктовый бизнес-кейс
**Кейс**: «В A/B тесте конверсия в клик выросла на 15%, но общая выручка магазина упала на 5%. Что произошло и что вы будете рекомендовать?»
**Разбор**:
- Произошла оптимизация под кликбейтную локальную метрику.
- Пользователи чаще кликали, но покупали дешевые акционные товары, либо вырос процент отказов на этапе оплаты.
- Рекомендация: Отклонить раскатку, ориентироваться на целевую сквозную метрику (Revenue per User), а не на клики.
""")

print("Module 17 created successfully.")
