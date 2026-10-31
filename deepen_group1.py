import os
import sys
sys.path.append(r"d:\vibe_app\main_data_analytics")
from notebook_helper import create_notebook

BASE = r"d:\vibe_app\main_data_analytics\course"

# ==========================================
# MODULE 00: ONBOARDING & ANALYTICAL THINKING
# ==========================================
m00 = os.path.join(BASE, "module_00_onboarding")
os.makedirs(m00, exist_ok=True)

# Lesson 1: Role of Data Analyst 2027
create_notebook(os.path.join(m00, "lesson_01_role_data_analyst_2027.ipynb"), [
    ("markdown", """# 📊 Модуль 0. Урок 1: Профессия Data Analyst в эпоху генеративного ИИ (2027)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_00_onboarding/lesson_01_role_data_analyst_2027.ipynb)

---

## 1. Фундаментальный сдвиг роли: от «SQL-машиниста» к Архитектору решений

В 2018–2022 годах 80% рабочего времени аналитика данных уходило на техническую рутину:
- Написание однотипных запросов `SELECT ... JOIN ... GROUP BY`;
- Ручная замена точек на запятые в Excel;
- Бесконечный поиск синтаксиса Pandas на StackOverflow;
- Построение простых графиков по просьбе менеджеров («построй мне диаграмму продаж по регионам к обеду»).

**К осени 2026 — 2027 года этот рынок закрылся.** Модели уровня Claude 3.7 Sonnet, OpenAI o3 и Gemini 2.5 генерируют идеальный синтаксический код за секунды. Классический «джуниор», знавший только базовый SQL и пару функций Pandas, стал экономически нецелесообразен для найма.

### Кем стал Data Analyst нового поколения?
Современный аналитик — это **переводчик между болью бизнеса и данными**:
1. **Problem Framing (Постановка задачи)**: Бизнес приходит с туманной фразой: *«Кажется, у нас что-то не то с мобильным приложением»*. Аналитик переводит это в дерево измеримых метрик, формулирует проверяемые гипотезы и ставит техническое задание AI-ассистентам.
2. **AI Orchestration (Управление ансамблем инструментов)**: Написание точных системных промптов для генерации пайплайнов, использование Cursor и Copilot для мгновенного прототипирования.
3. **Data Verification & Zero Hallucination (Валидация и защита от ошибок)**: Нейросеть не несет финансовой ответственности за галлюцинацию в отчете. Аналитик владеет чеклистами верификации математических инвариантов и логики агрегаций.
4. **Data Storytelling & Influence (Влияние на бизнес)**: Цифры сами по себе не имеют ценности. Ценность имеет решение CEO/CPO, принятое на их основе.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       АНАТОМИЯ СТОИМОСТИ АНАЛИТИКА 2027                     │
├─────────────────────────────────────────────────────────────────────────────┤
│  5%   │ Синтаксис (написание базового кода вручную)                          │
│  25%  │ AI-оркестрация и архитектура витрин данных                          │
│  30%  │ Валидация, фактчекинг и защита от галлюцинаций                       │
│  40%  │ Data Storytelling, юнит-экономика и защита решений перед бизнесом    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Реальный бизнес-кейс: "Загадочное падение продаж в Black Friday"

### Контекст компании
Крупный омниканальный ритейлер электроники (500 000 MAU). В Черную пятницу коммерческий директор в панике: *«Выручка на 15% ниже прогноза, хотя бюджет на рекламу удвоен! Маркетологи говорят, что трафик рекордный. Разберитесь!»*

### Как действует слабый аналитик (подход 2020 года):
- Строит график выручки по часам.
- Пишет в чат: *«Да, действительно, выручка упала на 15%. Вот график»*.
- Тратит 2 дня на ручное ковыряние логов, бизнес теряет миллионы рублей прямо сейчас.

### Как действует современный аналитик (AI-Assisted Workflow):
1. Мгновенно раскладывает выручку на множители верхнего уровня:
   $$\\text{Revenue} = \\text{Traffic} \\times \\text{CR (Conversion Rate)} \\times \\text{AOV (Average Order Value)}$$
2. Пишет короткое ТЗ для AI: *«Сгенерируй скрипт для расчета динамики Traffic, CR и AOV по 15-минутным интервалам с разбивкой по платформам (iOS, Android, Web) и платежным шлюзам»*.
3. Валидирует код и запускает.
4. Обнаруживает: трафик вырос на 45%, AOV стабилен, но **конверсия на iOS версии 18.2 упала с 3.8% до 0.2%** из-за сбоя авторизации в SDK СБП (Системы быстрых платежей).
5. Через 12 минут после запроса баг передан разработчикам, хотфикс выкачен, компания спасла 28 млн рублей выручки.
"""),
    ("code", """# Практическая симуляция кейса Black Friday: декомпозиция сбоя
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Симулируем 15-минутные интервалы Черной пятницы
np.random.seed(42)
time_slots = pd.date_range("2026-11-27 08:00", "2026-11-27 14:00", freq="15min")

data = []
for t in time_slots:
    # Базовый трафик растет к полудню
    traffic_web = np.random.randint(1200, 1800)
    traffic_android = np.random.randint(2000, 2600)
    traffic_ios = np.random.randint(2500, 3200)
    
    # Нормальная конверсия 3.5%
    cr_web = np.random.normal(0.035, 0.002)
    cr_android = np.random.normal(0.036, 0.002)
    
    # В 10:15 на iOS выкатили сбойный билд SDK платежей!
    if t >= pd.Timestamp("2026-11-27 10:15"):
        cr_ios = np.random.normal(0.003, 0.001) # Просадка в 10 раз!
    else:
        cr_ios = np.random.normal(0.038, 0.002)
        
    data.append({'timestamp': t, 'platform': 'Desktop Web', 'traffic': traffic_web, 'cr': cr_web, 'aov': 4200})
    data.append({'timestamp': t, 'platform': 'Android App', 'traffic': traffic_android, 'cr': cr_android, 'aov': 3900})
    data.append({'timestamp': t, 'platform': 'iOS App', 'traffic': traffic_ios, 'cr': cr_ios, 'aov': 4800})

df_incident = pd.DataFrame(data)
df_incident['orders'] = (df_incident['traffic'] * df_incident['cr']).round(0)
df_incident['revenue'] = df_incident['orders'] * df_incident['aov']

# Сводный анализ по платформам до и после 10:15
df_incident['incident_phase'] = np.where(df_incident['timestamp'] < '2026-11-27 10:15', 'До инцидента', 'Во время инцидента')

summary = df_incident.groupby(['incident_phase', 'platform']).agg(
    avg_cr=('cr', lambda x: f"{x.mean()*100:.2f}%"),
    total_revenue=('revenue', lambda x: f"{x.sum():,.0f} руб")
).unstack(level=0)

print("=== РЕЗУЛЬТАТ ЛОКАЛИЗАЦИИ ПРОБЛЕМЫ АНАЛИТИКОМ ===")
print(summary)
"""),
    ("markdown", """## 3. Типичные ловушки новичков (Red Flags)
1. **Ловушка агрегированных данных**: Смотреть на среднюю конверсию по всей компании. В общем котле просадка iOS выглядит как «легкое колебание», но внутри сегмента — катастрофа. Всегда сегментируйте!
2. **Синдром курьера**: Принести график без ответа на вопрос: *«И что нам с этим делать?»*. Аналитик всегда должен давать **Action Item** (рекомендацию к действию).
3. **Слепая вера коду AI**: Попросить ИИ посчитать среднюю конверсию, не проверив, посчитал ли он среднее от процентов (математическая ошибка!) или разделил сумму заказов на сумму сессий.

---

## 4. Практическое задание (Hands-on Practice)
1. Измените в коде выше время начала инцидента на 11:30.
2. Добавьте проверку: сколько недополученной выручки (Lost Revenue) принес сбой за время инцидента по сравнению с базовым сценарием?
""")
])

# Lesson 2: Environment & Modern AI Tools
create_notebook(os.path.join(m00, "lesson_02_environment_setup_colab_ai.ipynb"), [
    ("markdown", """# 🛠️ Модуль 0. Урок 2: Развертывание рабочего окружения и AI-стека аналитика

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_00_onboarding/lesson_02_environment_setup_colab_ai.ipynb)

---

## 1. Архитектура рабочего места 2027: Cloud First + Local AI IDE

Современный специалист использует гибридную инфраструктуру:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        РАБОЧАЯ СРЕДА АНАЛИТИКА                         │
├──────────────────────────────────┬─────────────────────────────────────┤
│      ОБЛАЧНАЯ СРЕДА (CLOUD)      │     ЛОКАЛЬНАЯ СРЕДА (LOCAL IDE)     │
├──────────────────────────────────┼─────────────────────────────────────┤
│ • Google Colab (Zero Config)     │ • Cursor IDE (AI-native редактор)   │
│ • Облачные GPU/TPU при нужде     │ • VS Code + GitHub Copilot          │
│ • Google Drive / BigQuery        │ • Git + GitHub (версионирование)    │
│ • Looker Studio (BI)             │ • Локальный SQLite / DuckDB         │
└──────────────────────────────────┴─────────────────────────────────────┘
```

---

## 2. Реальный бизнес-кейс: "Воспроизводимость отчета для инвесторов"

### Ситуация
Стартап закрывает раунд финансирования Series A на \$5 млн. Венчурный фонд просит предоставить когортный анализ за 2 года с кодом расчета Retention Rate.
- Аналитик отправляет Jupyter ноутбук, сохраненный локально.
- Партнер фонда открывает ноутбук: падает ошибка `FileNotFoundError: C:/Users/Vasya/Downloads/data_final_v2_NEW.csv`, версии Pandas не совпадают, функции устарели.
- Сделка под угрозой: инвесторы сомневаются в технической зрелости команды.

### Стандарт индустрии 2027:
1. Ноутбук должен открываться в **1 клик в Google Colab**.
2. Данные загружаются либо из облачного хранилища, либо генерируются/выгружаются скриптом автоматически.
3. В начале каждого файла — блок фиксации версий зависимостей (`requirements.txt`).
4. Все выводы сформулированы в Markdown-ячейках с четкой структурой.
"""),
    ("code", """# Демонстрация полностью автономного и воспроизводимого блока данных
import sys
import pandas as pd
import numpy as np

# Проверка версий
assert sys.version_info >= (3, 9), "Требуется Python 3.9 или выше"

print(" Среда верифицирована:")
print(f"- Python: {sys.version.split()[0]}")
print(f"- Pandas: {pd.__version__}")
print(f"- NumPy : {np.__version__}")

# Создание демо-когорты, не зависящей от локального диска
dates = pd.date_range('2026-01-01', periods=12, freq='ME')
cohort_mock = pd.DataFrame({
    'Cohort': [d.strftime('%Y-%m') for d in dates],
    'New_Users': np.random.randint(1500, 3000, 12),
    'Month_1_Retention': np.random.uniform(0.35, 0.45, 12).round(3),
    'Month_3_Retention': np.random.uniform(0.20, 0.28, 12).round(3)
})

print("\\nПример воспроизводимого артефакта когорт:")
print(cohort_mock.head(4))
"""),
    ("markdown", """## 3. Чеклист готовности рабочего окружения
- [ ] Аккаунт в Google (для Google Colab и Looker Studio).
- [ ] Аккаунт на GitHub (для портфолио и контроля версий).
- [ ] Настроенный редактор (Cursor или VS Code).
- [ ] Доступ к LLM-ассистенту (ChatGPT Plus / Claude Pro / Cursor Agent).
""")
])

# Lesson 3: Analytical Thinking & CRISP-DM
create_notebook(os.path.join(m00, "lesson_03_analytical_thinking_crisp_dm.ipynb"), [
    ("markdown", """# 🧠 Модуль 0. Урок 3: Аналитическое мышление и индустриальный стандарт CRISP-DM

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_00_onboarding/lesson_03_analytical_thinking_crisp_dm.ipynb)

---

## 1. Методология CRISP-DM в деталях

CRISP-DM (*Cross-Industry Standard Process for Data Mining*) — главный международный стандарт жизненного цикла работы с данными:

```
[1. Business Understanding] ─── "Какую проблему бизнеса мы решаем и сколько денег это принесет?"
           │
[2. Data Understanding]     ─── "Какие данные есть, где они лежат, насколько они полны и достоверны?"
           │
[3. Data Preparation]       ─── "Очистка, джойны, обработка пропусков, фильтрация выбросов"
           │
[4. Modeling & Analysis]    ─── "Построение срезов, когорт, статтестов, регрессий или прогнозов"
           │
[5. Evaluation]             ─── "Ответил ли анализ на бизнес-вопрос? Нет ли ошибки в данных?"
           │
[6. Deployment & Action]    ─── "Внедрение дашборда, принятие решения о раскатке фичи, регламент"
```

---

## 2. Реальный бизнес-кейс: "Сеть кофеен у дома: почему падает повторная посещаемость?"

### Business Understanding
Сеть из 45 кофеен фиксирует падение выручки со второго квартала на 12%. Руководство считает, что «надо запустить рекламу у блогеров».
Аналитик проводит Problem Framing:
- **Целевая бизнес-метрика**: 30-Day Repeat Purchase Rate (доля гостей, вернувшихся в течение 30 дней).
- **Гипотеза бизнеса**: «О нас мало знают новые клиенты».
- **Контргипотеза аналитика**: «Мы теряем уже пришедших клиентов из-за падения качества сервиса или вкуса кофе».

### Data Understanding & Preparation
Аналитик объединяет кассовые чеки с данными программы лояльности и отзывами на картах (Яндекс Карты, 2ГИС).
"""),
    ("code", """import pandas as pd
import numpy as np

# Симуляция исследования сети кофеен
np.random.seed(10)
locations = [f"Кофейня_{i}" for i in range(1, 11)]

coffee_data = []
for loc in locations:
    guests = np.random.randint(800, 1500)
    repeat_rate = np.random.uniform(0.18, 0.48)
    avg_speed_sec = np.random.randint(90, 320) # Время ожидания кофе
    complaints = int(guests * np.random.uniform(0.01, 0.08))
    
    coffee_data.append({
        'location': loc,
        'monthly_guests': guests,
        'repeat_rate': repeat_rate,
        'avg_wait_seconds': avg_speed_sec,
        'complaints_count': complaints
    })

df_coffee = pd.DataFrame(coffee_data)

# Считаем корреляцию между скоростью отдачи кофе и повторными визитами
corr_wait = df_coffee['avg_wait_seconds'].corr(df_coffee['repeat_rate'])
print(f"Корреляция между временем ожидания и Retention гостей: {corr_wait:.3f}")
print("Вывод: Сильная отрицательная связь! Чем дольше гость ждет напиток, тем ниже вероятность возврата.")

# Топ-3 проблемные точки
worst_locations = df_coffee.sort_values(by='avg_wait_seconds', ascending=False).head(3)
print("\\nТОП-3 ТОЧКИ С КРИТИЧЕСКИМ ВРЕМЕНЕМ ОЖИДАНИЯ:")
print(worst_locations[['location', 'avg_wait_seconds', 'repeat_rate', 'complaints_count']])
""")
    ,
    ("markdown", """## 3. Бизнес-решение (Deployment / Action)
Вместо слива 3 000 000 рублей на блогеров:
1. Выявлена реальная причина: на точках с ожиданием > 4 минут гости уходят в кофейни конкурентов за углом.
2. Закуплены скоростные темперы и настроен дополнительный бариста в утренний час-пик.
3. Время ожидания снизилось до 110 секунд, возвратность гостей выросла на 7 п.п., выручка восстановилась за 3 недели.
""")
])

# Module 00 Quiz
with open(os.path.join(m00, "quiz.md"), "w", encoding="utf-8") as f:
    f.write("""# 🧠 Quiz: Самопроверка по Модулю 0 (Онбординг & Аналитическое мышление)

---

### Вопрос 1
В чем заключается фундаментальное отличие роли Data Analyst 2027 года от роли 2020 года?
- [ ] В 2027 году аналитики больше не используют базы данных и SQL.
- [x] В 2027 году рутинное написание кода автоматизировано AI, а фокус сместился на Problem Framing, постановку ТЗ для LLM, фактчекинг и Data Storytelling.
- [ ] В 2027 году аналитик обязан обучать собственные нейросети на суперкомпьютере.
*Объяснение*: Рутинный синтаксис генерируют LLM. Главная ценность человека — перевод бизнес-проблем в метрики, критический аудит кода и коммуникация решений с топ-менеджментом.

---

### Вопрос 2
Руководство компании жалуется: *«В этом месяце выручка упала на 10%, срочно удвойте расходы на маркетинг»*. Каково первое действие профессионального аналитика?
- [ ] Сразу согласовать бюджет и запустить рекламу.
- [x] Декомпозировать выручку на метрики Traffic * CR * AOV, сегментировать данные по платформам/каналам и локализовать причину падения.
- [ ] Построить круговую диаграмму продаж.
*Объяснение*: Если просадка вызвана техническим багом в чекауте или падением среднего чека, заливка нового рекламного трафика лишь сожжет деньги компании без роста продаж.

---

### Вопрос 3
Какой этап методологии CRISP-DM является первым и самым важным для успеха проекта?
- [ ] Data Preparation (Очистка данных).
- [ ] Modeling (Построение моделей).
- [x] Business Understanding (Понимание бизнес-контекста и целей).
*Объяснение*: Не поняв экономический смысл задачи и решение, которое будет приниматься, аналитик рискует построить идеальный технический отчет, который окажется бесполезен бизнесу.
""")

print("Module 00 deepened successfully.")

# ==========================================
# MODULE 01: EXCEL & SHEETS DEEP DIVE
# ==========================================
m01 = os.path.join(BASE, "module_01_excel")
os.makedirs(m01, exist_ok=True)

# Lesson 1: Formatting & Tidy Data
create_notebook(os.path.join(m01, "lesson_01_interface_basics_formatting.ipynb"), [
    ("markdown", """# 📊 Модуль 1. Урок 1: Архитектура таблиц и принципы Tidy Data в Excel / Sheets

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_01_excel/lesson_01_interface_basics_formatting.ipynb)

---

## 1. Ментальная модель: Почему 90% таблиц в бизнесе "сломаны"?

В корпоративном мире финансисты и менеджеры часто создают таблицы для **человеческих глаз**, а не для машинного анализа:
- Объединенные ячейки (Merged Cells) — злейший враг аналитика;
- Итоги посреди данных;
- Пустые строки для «красоты»;
- Даты, размазанные по столбцам вправо.

### Стандарт Хэдли Уикхема: Tidy Data (Аккуратные данные)
1. **Каждая переменная образует столбец**.
2. **Каждое наблюдение образует строку**.
3. **Каждый тип сущности образует отдельную таблицу**.
"""),
    ("code", """# Демонстрация трансформации плохой сводки в Tidy Data
import pandas as pd

# Типичный "директорский" отчет (Wide format с объединенными смыслами)
ugly_report = pd.DataFrame({
    'Менеджер': ['Алексей', 'Мария', 'Иван'],
    'Янв_План': [100000, 150000, 120000],
    'Янв_Факт': [95000, 160000, 110000],
    'Фев_План': [110000, 150000, 130000],
    'Фев_Факт': [115000, 140000, 135000]
})

print("СЫРОЙ ВИД (Не пригоден для SQL и BI):")
print(ugly_report)

# Переводим в Tidy формат через Pandas (в Excel это делается через Power Query Unpivot)
tidy_df = pd.melt(
    ugly_report, 
    id_vars=['Менеджер'], 
    var_name='Период_Метрика', 
    value_name='Сумма'
)
tidy_df[['Месяц', 'Тип']] = tidy_df['Период_Метрика'].str.split('_', expand=True)
tidy_df = tidy_df.drop(columns=['Период_Метрика'])

print("\\nИДЕАЛЬНЫЙ TIDY DATA ВИД (Готов для сводных таблиц, SQL и Looker Studio):")
print(tidy_df.head(6))
""")
])

# Lesson 2: Formulas & XLOOKUP
create_notebook(os.path.join(m01, "lesson_02_formulas_functions_xlookup.ipynb"), [
    ("markdown", """# 🧮 Модуль 1. Урок 2: Библиотека формул: от агрегаций до XLOOKUP

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_01_excel/lesson_02_formulas_functions_xlookup.ipynb)

---

## 1. Смерть VLOOKUP: Почему в 2027 году используют XLOOKUP?

Классический `VLOOKUP` (ВПР) имел 3 фатальных недостатка:
1. **Жесткий номер столбца**: Если коллега вставил столбец в середину справочника — формула с номерами столбцов выдает неверные данные.
2. **Поиск только вправо**: Нельзя искать значение, если ключ находится правее возвращаемого результата.
3. **Медленная работа**: На таблицах от 50 000 строк VLOOKUP зависает.

### Синтаксис XLOOKUP:
```excel
=XLOOKUP(искомое_значение; диапазон_поиска; возвращаемый_диапазон; [если_не_найдено]; [режим_сопоставления])
```
"""),
    ("code", """# Практический кейс: Склейка транзакций с себестоимостью через аналог XLOOKUP
import pandas as pd

# Загружаем реальные датасеты курса
orders = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\order_items.csv").head(10)
products = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\products.csv")

# В Excel: =XLOOKUP(orders!C2; products!A:A; products!E:E; 0)
merged = orders.merge(products[['product_id', 'product_name', 'cost', 'category']], on='product_id', how='left')
merged['profit'] = merged['total_amount'] - (merged['cost'] * merged['quantity'])

print("РЕЗУЛЬТАТ РАСЧЕТА МАРЖИ С ПОМОЩЬЮ XLOOKUP-ЛОГИКИ:")
print(merged[['order_id', 'product_name', 'quantity', 'unit_price', 'cost', 'total_amount', 'profit']])
""")
])

# Lesson 3: Pivot Tables
create_notebook(os.path.join(m01, "lesson_03_pivot_tables_aggregations.ipynb"), [
    ("markdown", """# 📑 Модуль 1. Урок 3: Сводные таблицы (Pivot Tables) и срезы данных

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_01_excel/lesson_03_pivot_tables_aggregations.ipynb)

---

## 1. Анатомия многомерного анализа без кода

Сводная таблица (Pivot Table) агрегирует тысячи строк сырых логов за доли секунды.
Ключевые приемы профессионалов:
- **Вычисляемые поля (Calculated Fields)**: Расчет среднего чека и маржи прямо внутри сводной таблицы.
- **Отображение значений как % от строки / % от столбца**: Мгновенное выявление структуры продаж.
- **Группировка дат**: Схлопывание ежедневных записей по Месяцам, Кварталам и Годам.
"""),
    ("code", """# Построение сложной сводной таблицы по реальной базе e-commerce
import pandas as pd

orders = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\orders.csv")
items = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\order_items.csv")
customers = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\customers.csv")

df = items.merge(orders, on='order_id').merge(customers, on='customer_id')
df = df[df['status'] == 'Completed']

# Сводный отчет: Город x Канал привлечения с суммами и средними
pivot = pd.pivot_table(
    df,
    values='total_amount',
    index='city',
    columns='acquisition_channel',
    aggfunc=['sum', 'count'],
    fill_value=0
)

print("СВОДНЫЙ ОТЧЕТ ПО ВЫРУЧКЕ И ЗАКАЗАМ:")
print(pivot['sum'].round(0).astype(int))
""")
])

# Lesson 4: Visualizations
create_notebook(os.path.join(m01, "lesson_04_visualization_data_story.ipynb"), [
    ("markdown", """# 📈 Модуль 1. Урок 4: Визуализация данных и принципы Эдварда Тафти

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_01_excel/lesson_04_visualization_data_story.ipynb)

---

## 1. Принцип Data-Ink Ratio

Эдвард Тафти, классик теории визуализации данных, сформулировал закон:
$$\\text{Data-Ink Ratio} = \\frac{\\text{Чернила, отображающие данные}}{\\text{Все использованные чернила на графике}} \\to 1.0$$

### Что нужно нещадно удалять с диаграмм:
- Тяжелые фоновые сетки темных цветов;
- 3D-эффекты и тени;
- Повторяющиеся подписи осей;
- Круговые диаграммы с более чем 3 сегментами (человеческий мозг плохо оценивает соотношение площадей и углов).
"""),
    ("code", """# Демонстрация принципа минимализма Тафти на реальных данных
import matplotlib.pyplot as plt
import pandas as pd

items = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\order_items.csv")
products = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\products.csv")
df = items.merge(products, on='product_id')

sales_by_cat = df.groupby('category')['total_amount'].sum().sort_values(ascending=True)

fig, ax = plt.subplots(figsize=(9, 4))
bars = ax.barh(sales_by_cat.index, sales_by_cat.values, color='#0284c7', height=0.55)

# Убираем рамки
for s in ['top', 'right', 'left']:
    ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#94a3b8')

# Добавляем подписи данных прямо к столбцам
for bar in bars:
    w = bar.get_width()
    ax.text(w + 2000, bar.get_y() + bar.get_height()/2, f"${w:,.0f}", va='center', fontsize=10, color='#0f172a', weight='600')

ax.set_title('Выручка по категориям за отчетный период (Tufte Clean Style)', fontsize=12, pad=15, loc='left')
ax.xaxis.grid(True, linestyle='--', alpha=0.4, color='#cbd5e1')
plt.tight_layout()
plt.show()
""")
])

# Lesson 5: AI Copilot for Excel
create_notebook(os.path.join(m01, "lesson_05_ai_copilot_excel_formulas.ipynb"), [
    ("markdown", """# 🤖 Модуль 1. Урок 5: Генерация сложных формул и макросов через AI Copilot

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_01_excel/lesson_05_ai_copilot_excel_formulas.ipynb)

---

## 1. Промпт-инжиниринг для Excel / Google Sheets

Чтобы нейросеть написала формулу без ошибок, используйте архитектуру **T-C-O (Task, Context, Output)**:
1. **Context**: «Таблица 'Sales', колонка A — Order_Date (YYYY-MM-DD), колонка B — Customer_ID, колонка C — Status ('Done', 'Cancelled'), колонка D — Revenue (число)».
2. **Task**: «Посчитай сумму выручки только для повторных клиентов (у которых больше 1 заказа со статусом 'Done') за последние 90 дней».
3. **Output**: «Напиши формулу для Google Sheets. Учти деление на ноль и русскую локаль (разделитель точка с запятой ;)».

---

## 2. Чеклист валидации формул от нейросети
- [ ] **Локализация разделителей**: US-локаль использует запятую `,`, европейская/российская — точку с запятой `;`.
- [ ] **Фиксация диапазонов**: Проставлены ли знаки доллара `$A$2:$A$1000`, чтобы формула не съехала при протяжке.
- [ ] **Обработка ошибок**: Обернута ли формула в `IFERROR(..., 0)`?
""")
])

print("Module 01 deepened successfully.")

# ==========================================
# MODULE 02: SQL MASTER DEEP DIVE
# ==========================================
m02 = os.path.join(BASE, "module_02_sql")
os.makedirs(m02, exist_ok=True)

# Lesson 1: DB intro & SELECT
create_notebook(os.path.join(m02, "lesson_01_db_intro_select_filtering.ipynb"), [
    ("markdown", """# 🗃️ Модуль 2. Урок 1: Реляционная модель данных и логический порядок выполнения SQL

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_02_sql/lesson_01_db_intro_select_filtering.ipynb)

---

## 1. Главный секрет SQL: Порядок написания vs Порядок выполнения

Почему новички пишут неработающие запросы? Потому что SQL **пишется** в одном порядке, а СУБД **выполняет** его совершенно в другом!

```
┌─────────────────────────────────┬─────────────────────────────────┐
│     КАК ВЫ ПИШЕТЕ ЗАПРОС        │      КАК ЕГО ВЫПОЛНЯЕТ СУБД     │
├─────────────────────────────────┼─────────────────────────────────┤
│ 1. SELECT                       │ 1. FROM (откуда берем данные)   │
│ 2. FROM                         │ 2. ON / JOIN (как связываем)    │
│ 3. WHERE                        │ 3. WHERE (фильтруем сырые строки)│
│ 4. GROUP BY                     │ 4. GROUP BY (схлопываем группы) │
│ 5. HAVING                       │ 5. HAVING (фильтруем группы)    │
│ 6. ORDER BY                     │ 6. SELECT (выбираем поля/алиасы)│
│ 7. LIMIT                        │ 7. DISTINCT                     │
│                                 │ 8. ORDER BY (сортируем)         │
│                                 │ 9. LIMIT / OFFSET (отрезаем)    │
└─────────────────────────────────┴─────────────────────────────────┘
```

> **Инсайт собеседований**: Вы не можете использовать алиас из `SELECT` внутри секции `WHERE`, потому что на момент выполнения `WHERE` секция `SELECT` еще даже не запускалась!
"""),
    ("code", """import sqlite3
import pandas as pd

conn = sqlite3.connect(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\ecommerce.db")

# Запрос с правильной фильтрацией и строгим порядком
query = \"\"\"
SELECT 
    customer_id,
    first_name,
    city,
    acquisition_channel,
    registration_date
FROM customers
WHERE city IN ('Moscow', 'Saint Petersburg', 'Kazan')
  AND acquisition_channel != 'Direct'
  AND registration_date >= '2025-06-01'
ORDER BY registration_date DESC
LIMIT 5;
\"\"\"

print("РЕЗУЛЬТАТ ЗАПРОСА К E-COMMERCE БАЗЕ:")
print(pd.read_sql(query, conn))
""")
])

# Lesson 2: Group By & Having
create_notebook(os.path.join(m02, "lesson_02_aggregations_group_by_having.ipynb"), [
    ("markdown", """# 📊 Модуль 2. Урок 2: Агрегатные функции и жесткая разница WHERE vs HAVING

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_02_sql/lesson_02_aggregations_group_by_having.ipynb)

---

## 1. Разница между WHERE и HAVING на реальном кейсе

- **WHERE**: Фильтрует отдельные строки **до того**, как они объединятся в группы. Не может содержать агрегатные функции (`SUM`, `AVG`, `COUNT`).
- **HAVING**: Фильтрует уже готовые сгруппированные строки **после** группировки.
"""),
    ("code", """import sqlite3
import pandas as pd

conn = sqlite3.connect(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\ecommerce.db")

# Кейс: Найти города, где совершено более 150 успешных заказов, 
# исключив тестовые и отмененные заказы ДО агрегации
query = \"\"\"
SELECT 
    c.city,
    COUNT(o.order_id) AS completed_orders,
    ROUND(SUM(oi.total_amount), 2) AS city_revenue,
    ROUND(AVG(oi.total_amount), 2) AS avg_item_amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
WHERE o.status = 'Completed'                      -- WHERE: отсекаем строки до расчета
GROUP BY c.city
HAVING completed_orders > 150                      -- HAVING: фильтруем агрегированный результат
ORDER BY city_revenue DESC;
\"\"\"

print("ГОРОДА-ЛИДЕРЫ С БОЛЕЕ ЧЕМ 150 УСПЕШНЫМИ ЗАКАЗАМИ:")
print(pd.read_sql(query, conn))
""")
])

# Lesson 3: Joins deep dive
create_notebook(os.path.join(m02, "lesson_03_joins_deep_dive.ipynb"), [
    ("markdown", """# 🔗 Модуль 2. Урок 3: Все виды JOIN и защита от Cartesian Explosion (Задвоения данных)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_02_sql/lesson_03_joins_deep_dive.ipynb)

---

## 1. Опасность дублирования строк при JOIN

Самая частая ошибка, из-за которой компании увольняют аналитиков: **случайное размножение строк при связи «один-ко-многим»**.

Если у одного клиента 3 заказа, а у каждого заказа по 2 товара:
- `customers` JOIN `orders` -> 3 строки;
- `orders` JOIN `order_items` -> 6 строк.
Если вы после этого сделаете `SUM(orders.delivery_cost)`, стоимость доставки посчитается **дважды для каждого заказа**!
"""),
    ("code", """import sqlite3
import pandas as pd

conn = sqlite3.connect(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\ecommerce.db")

# Запрос с правильным подсчетом уникальных заказов и суммы без задвоения
query = \"\"\"
SELECT 
    c.acquisition_channel,
    COUNT(DISTINCT c.customer_id) AS unique_customers,
    COUNT(DISTINCT o.order_id) AS total_orders,
    ROUND(SUM(oi.total_amount), 2) AS total_revenue,
    ROUND(SUM(oi.total_amount) / COUNT(DISTINCT o.order_id), 2) AS real_aov
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id AND o.status = 'Completed'
LEFT JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY c.acquisition_channel
ORDER BY total_revenue DESC;
\"\"\"

print("АККУРАТНЫЙ РАСЧЕТ БЕЗ ДУБЛИРОВАНИЯ МЕТРИК:")
print(pd.read_sql(query, conn))
""")
])

# Lesson 4: CTE
create_notebook(os.path.join(m02, "lesson_04_subqueries_and_cte.ipynb"), [
    ("markdown", """# 🧱 Модуль 2. Урок 4: Чистая архитектура SQL через CTE (WITH)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_02_sql/lesson_04_subqueries_and_cte.ipynb)

---

## 1. Принцип модульности: Common Table Expressions (CTE)

В реальной работе запросы на 200 строк с 5 уровнями вложенных подзапросов невозможно поддерживать.
Конструкция `WITH` превращает спагетти-код в последовательный пайплайн:
"""),
    ("code", """import sqlite3
import pandas as pd

conn = sqlite3.connect(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\ecommerce.db")

query = \"\"\"
-- Шаг 1: Агрегация на уровне клиента
WITH customer_stats AS (
    SELECT 
        customer_id,
        COUNT(DISTINCT order_id) AS orders_count,
        SUM(total_amount) AS total_spent
    FROM orders o
    JOIN order_items oi ON o.order_id = oi.order_id
    WHERE o.status = 'Completed'
    GROUP BY customer_id
),
-- Шаг 2: Расчет порогов для сегментации
benchmark AS (
    SELECT 
        AVG(total_spent) AS avg_ltv,
        AVG(orders_count) AS avg_orders
    FROM customer_stats
)
-- Шаг 3: Финальный отчет с присвоением бизнес-сегментов
SELECT 
    cs.customer_id,
    cs.orders_count,
    ROUND(cs.total_spent, 2) AS total_spent,
    CASE 
        WHEN cs.total_spent > b.avg_ltv * 2 THEN 'VIP Client'
        WHEN cs.orders_count > b.avg_orders THEN 'Loyal Client'
        ELSE 'Regular Client'
    END AS segment
FROM customer_stats cs
CROSS JOIN benchmark b
ORDER BY cs.total_spent DESC
LIMIT 8;
\"\"\"

print("КЛИЕНТСКАЯ СЕГМЕНТАЦИЯ ЧЕРЕЗ CTE:")
print(pd.read_sql(query, conn))
""")
])

# Lesson 5: Window Functions
create_notebook(os.path.join(m02, "lesson_05_window_functions_advanced.ipynb"), [
    ("markdown", """# 🪟 Модуль 2. Урок 5: Оконные функции (Window Functions) в деталях

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_02_sql/lesson_05_window_functions_advanced.ipynb)

---

## 1. Главные оконные функции аналитика данных

1. `ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...)`: Уникальная нумерация строк внутри группы (идеально для дедупликации).
2. `DENSE_RANK() OVER (...)`: Ранжирование без пропусков (Топ-3 товара в каждой категории).
3. `LAG(col, 1) OVER (...)` и `LEAD(col, 1) OVER (...)`: Доступ к предыдущей или следующей строке (расчет темпов роста MoM / YoY).
4. `SUM(col) OVER (ORDER BY ...)`: Расчет нарастающего итога (Cumulative Revenue).
"""),
    ("code", """import sqlite3
import pandas as pd

conn = sqlite3.connect(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\ecommerce.db")

query = \"\"\"
WITH monthly_revenue AS (
    SELECT 
        SUBSTR(o.order_date, 1, 7) AS ym,
        ROUND(SUM(oi.total_amount), 2) AS revenue
    FROM orders o
    JOIN order_items oi ON o.order_id = oi.order_id
    WHERE o.status = 'Completed'
    GROUP BY ym
)
SELECT 
    ym,
    revenue,
    -- Нарастающий итог с начала года
    ROUND(SUM(revenue) OVER (ORDER BY ym), 2) AS running_total,
    -- Доход за предыдущий месяц
    LAG(revenue, 1) OVER (ORDER BY ym) AS prev_month,
    -- Относительный прирост месяц-к-месяцу (MoM %)
    ROUND((revenue - LAG(revenue, 1) OVER (ORDER BY ym)) * 100.0 / 
          LAG(revenue, 1) OVER (ORDER BY ym), 2) AS mom_growth_pct
FROM monthly_revenue
ORDER BY ym;
\"\"\"

print("ФИНАНСОВАЯ АНАЛИТИКА ЧЕРЕЗ ОКОННЫЕ ФУНКЦИИ:")
print(pd.read_sql(query, conn))
""")
])

# Lesson 6: Retention & Funnels SQL
create_notebook(os.path.join(m02, "lesson_06_sql_patterns_retention_funnels.ipynb"), [
    ("markdown", """# 🔄 Модуль 2. Урок 6: Паттерны продуктовой аналитики: Воронки и Когорты на SQL

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_02_sql/lesson_06_sql_patterns_retention_funnels.ipynb)

---

## 1. Помесячный когортный анализ Retention Rate на чистом SQL

Когортный анализ отвечает на ключевой вопрос: *«Удерживаем ли мы клиентов, привлеченных в разные месяцы, или они разово покупают и исчезают?»*
"""),
    ("code", """import sqlite3
import pandas as pd

conn = sqlite3.connect(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\ecommerce.db")

query = \"\"\"
WITH cohorts AS (
    SELECT 
        customer_id,
        MIN(SUBSTR(order_date, 1, 7)) AS first_order_month
    FROM orders
    WHERE status = 'Completed'
    GROUP BY customer_id
),
activities AS (
    SELECT 
        o.customer_id,
        c.first_order_month,
        SUBSTR(o.order_date, 1, 7) AS order_month
    FROM orders o
    JOIN cohorts c ON o.customer_id = c.customer_id
    WHERE o.status = 'Completed'
)
SELECT 
    first_order_month AS cohort,
    COUNT(DISTINCT customer_id) AS cohort_size,
    COUNT(DISTINCT CASE WHEN order_month = first_order_month THEN customer_id END) AS m0_active,
    COUNT(DISTINCT CASE WHEN order_month > first_order_month THEN customer_id END) AS repeat_buyers,
    ROUND(COUNT(DISTINCT CASE WHEN order_month > first_order_month THEN customer_id END) * 100.0 / 
          COUNT(DISTINCT customer_id), 1) AS repeat_buyer_pct
FROM activities
GROUP BY first_order_month
ORDER BY first_order_month
LIMIT 6;
\"\"\"

print("КОГОРТНАЯ МАТРИЦА УДЕРЖАНИЯ:")
print(pd.read_sql(query, conn))
""")
])

# Lesson 7: Prompt Engineering for SQL
create_notebook(os.path.join(m02, "lesson_07_prompt_engineering_for_sql_and_validation.ipynb"), [
    ("markdown", """# 🛡️ Модуль 2. Урок 7: Text-to-SQL промптинг и строгий чеклист валидации

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_02_sql/lesson_07_prompt_engineering_for_sql_and_validation.ipynb)

---

## 1. Архитектура надежного промпта для Text-to-SQL

Когда вы просите нейросеть написать SQL, передавайте ей:
1. **Диалект СУБД** (PostgreSQL / SQLite / BigQuery / ClickHouse — у всех разный синтаксис работы с датами и строками).
2. **Точные DDL схемы таблиц** с первичными и внешними ключами.
3. **Бизнес-правила фильтрации** («Всегда отсекай статус != Completed»).

### Чеклист проверки SQL-кода от нейросети:
- [ ] Не использовал ли ИИ агрегат внутри WHERE?
- [ ] Все ли неагрегированные поля из SELECT попали в GROUP BY?
- [ ] Проверено ли деление на ноль через `NULLIF(..., 0)`?
- [ ] Проверена ли уникальность ключей при JOIN во избежание декартова произведения?
""")
])

print("Module 02 deepened successfully.")
