import os
import sys
sys.path.append(r"d:\vibe_app\main_data_analytics")
from notebook_helper import create_notebook

BASE = r"d:\vibe_app\main_data_analytics\course"

# ==========================================
# MODULE 03: PYTHON & PANDAS (AI-ASSISTED)
# ==========================================
m03 = os.path.join(BASE, "module_03_python")
os.makedirs(m03, exist_ok=True)

with open(os.path.join(m03, "README.md"), "w", encoding="utf-8") as f:
    f.write("""# 🐍 Модуль 3: Python и Pandas — Анализ данных с AI-ассистентом

## 📌 Ключевая концепция 2027 года
> **Вам больше не нужно зубрить синтаксис наизусть.**
> Ваша задача — понимать структуру структур данных (Series, DataFrame), уметь декомпозировать преобразование на шаги, ставить точные ТЗ для Cursor / Copilot и проводить Code Review сгенерированного кода на предмет логических ошибок и утечек данных.

## 🎯 Learning Outcomes
- **Understand**: Ментальная модель DataFrame (строки, столбцы, индексы, векторизованные операции).
- **Apply**: Базовые операции Pandas (`read_csv`, `filter`, `groupby`, `merge`, `pivot_table`).
- **Analyze**: Поиск аномалий, сопоставление данных из нескольких источников.
- **AI Orchestration**: Написание точных комментариев-промптов в Cursor/Copilot для мгновенного получения рабочего кода.

## 📚 Уроки
1. `lesson_01_python_no_syntax_memorization.ipynb` — Ментальная модель Python и как формулировать задачи для AI.
2. `lesson_02_pandas_dataframes_indexing.ipynb` — Анатомия DataFrame: загрузка, срезы `.loc` / `.iloc`, фильтрация.
3. `lesson_03_pandas_aggregations_merge.ipynb` — Группировка (`groupby`), объединение (`merge`, `concat`), сводные таблицы.
4. `lesson_04_visualization_seaborn_matplotlib.ipynb` — Визуализация: Matplotlib, Seaborn и промпты для идеальных графиков.
5. `lesson_05_code_review_ai_validation.ipynb` — Практикум: ищем ошибки в коде, написанном LLM (Code Review).
6. `quiz.md` — Тест для самопроверки.
7. `cheatsheet.md` — Шпаргалка методов Pandas.
""")

create_notebook(os.path.join(m03, "lesson_01_python_no_syntax_memorization.ipynb"), [
    ("markdown", """# Модуль 3. Урок 1: Как аналитик пишет код в 2027 году

Забудьте учебники по синтаксису Python на 500 страниц. Аналитик оперирует концепциями:
1. **Input**: Какие данные на входе? (типы колонок, структура).
2. **Transformation**: Что математически/логически происходит со строками?
3. **Output**: Какой формат нужен на выходе?

## Демонстрация: Промпт-комментарий для Copilot
"""),
    ("code", """# ТЗ ДЛЯ AI: Создай синтетический датасет заказов с колонками user_id, order_date, amount
# и отфильтруй заказы с суммой выше медианной за последний квартал
import pandas as pd
import numpy as np

# Сгенерировано по ТЗ:
np.random.seed(42)
df = pd.DataFrame({
    'user_id': np.random.randint(100, 200, 20),
    'order_date': pd.date_range(start='2026-07-01', periods=20, freq='4D'),
    'amount': np.random.uniform(500, 15000, 20).round(2)
})

median_val = df['amount'].median()
filtered_df = df[df['amount'] > median_val].sort_values(by='amount', ascending=False)
print(f"Медианный чек: {median_val:.2f} руб")
print(filtered_df.head(5))
""")
])

create_notebook(os.path.join(m03, "lesson_02_pandas_dataframes_indexing.ipynb"), [
    ("markdown", """# Модуль 3. Урок 2: DataFrame: Загрузка, срезы и фильтрация

Работаем с реальным датасетом клиентов интернет-магазина.
"""),
    ("code", """import pandas as pd

# Загружаем реальный датасет курса
df_customers = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\customers.csv")

print("1. Форма датасета (строк, колонок):", df_customers.shape)
print("\\n2. Типы данных:")
print(df_customers.dtypes)

# Фильтрация: клиенты из Москвы или Казани с мобильных устройств
target_users = df_customers[
    (df_customers['city'].isin(['Moscow', 'Kazan'])) & 
    (df_customers['device'].str.contains('Mobile'))
]
print(f"\\n3. Найдено целевых пользователей: {len(target_users)}")
print(target_users.head(3))
""")
])

create_notebook(os.path.join(m03, "lesson_03_pandas_aggregations_merge.ipynb"), [
    ("markdown", """# Модуль 3. Урок 3: Агрегации и соединения данных (Merge)

Аналог `SQL JOIN` и `GROUP BY` в Pandas:
"""),
    ("code", """import pandas as pd

orders = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\orders.csv")
items = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\order_items.csv")
products = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\products.csv")

# Соединяем чеки с позициями и товарами
merged = items.merge(orders, on='order_id').merge(products, on='product_id')

# Анализ маржинальности по категориям
cat_summary = merged[merged['status'] == 'Completed'].groupby('category').agg(
    total_revenue=('total_amount', 'sum'),
    units_sold=('quantity', 'sum'),
    avg_price=('unit_price', 'mean'),
    margin_est=('total_amount', lambda x: (x * 0.35).sum()) # Оценочная маржа 35%
).reset_index()

cat_summary['revenue_share_%'] = (cat_summary['total_revenue'] / cat_summary['total_revenue'].sum() * 100).round(1)
print(cat_summary.sort_values(by='total_revenue', ascending=False))
""")
])

create_notebook(os.path.join(m03, "lesson_04_visualization_seaborn_matplotlib.ipynb"), [
    ("markdown", """# Модуль 3. Урок 4: Продвинутая визуализация с Seaborn
"""),
    ("code", """import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Загружаем SaaS-датасет
saas = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\saas_users.csv")

plt.figure(figsize=(10, 5))
sns.boxplot(data=saas, x='plan', y='nps_score', hue='is_churned', palette='Set2')
plt.title('Распределение NPS по тарифам и статусу оттока (Churn)', fontsize=13)
plt.xlabel('Тарифный план')
plt.ylabel('NPS (Оценка удовлетворенности)')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
""")
])

create_notebook(os.path.join(m03, "lesson_05_code_review_ai_validation.ipynb"), [
    ("markdown", """# Модуль 3. Урок 5: Code Review кода от ИИ (Поиск типичных багов)

### Кейс: Нейросеть написала код для расчета Retention Rate
Посмотрите на код ниже. В чем критическая логическая ошибка?
"""),
    ("code", """# КОД ОТ НЕЙРОСЕТИ С ОШИБКОЙ:
# "Посчитай процент вернувшихся клиентов"
# df.groupby('user_id')['order_date'].count() > 1 / len(df)  <-- ОШИБКА ЗДЕСЬ!

# ПРАВИЛЬНЫЙ АНАЛИТИЧЕСКИЙ КОД С ВАЛИДАЦИЕЙ:
import pandas as pd

orders = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\orders.csv")

# 1. Считаем уникальных пользователей всего
total_customers = orders['customer_id'].nunique()

# 2. Считаем тех, у кого > 1 завершенного заказа
repeat_buyers = orders[orders['status'] == 'Completed'].groupby('customer_id')['order_id'].nunique()
repeat_buyers_count = (repeat_buyers > 1).sum()

retention_rate = (repeat_buyers_count / total_customers) * 100
print(f"Всего пользователей: {total_customers}")
print(f"Повторных покупателей: {repeat_buyers_count}")
print(f"Repeat Purchase Rate: {retention_rate:.2f}%")
print("\\n Разбор ошибки AI: Нейросеть делила на общее число строк (заказов), а не на уникальных пользователей!")
""")
])

with open(os.path.join(m03, "quiz.md"), "w", encoding="utf-8") as f:
    f.write("""# 🧠 Quiz: Самопроверка по Модулю 3 (Python)

### Вопрос 1
Какой подход к коду на Python является правильным для аналитика 2027 года?
- [ ] Заучивать синтаксис методов наизусть
- [x] Понимать логику структур данных, формулировать задачи для AI-ассистентов и валидировать сгенерированный код
- [ ] Отказаться от Python в пользу калькулятора

### Вопрос 2
В чем разница между `.loc[]` и `.iloc[]` в Pandas?
- [ ] Разницы нет
- [x] `.loc` выбирает данные по текстовым меткам (колонкам/индексам), а `.iloc` — строго по целочисленным позициям (номерам строк/колонок)
- [ ] `.iloc` работает только с датами

### Вопрос 3
Какая главная опасность при слепом доверии коду от ChatGPT/Copilot?
- [ ] Компьютер перегреется
- [x] Логические ошибки в агрегациях (например, задвоение сумм или расчет среднего вместо взвешенного среднего), которые синтаксически работают без ошибок, но дают неверные бизнес-цифры
- [ ] Код сотрет жесткий диск
""")

with open(os.path.join(m03, "cheatsheet.md"), "w", encoding="utf-8") as f:
    f.write("""# 📋 Pandas Cheatsheet

```python
# Фильтрация нескольких условий
df[(df['col1'] > 10) & (df['col2'] == 'Target')]

# Группировка с именованными агрегациями
df.groupby('category').agg(
    orders=('order_id', 'nunique'),
    revenue=('amount', 'sum'),
    avg_check=('amount', 'mean')
)

# Проверка пропусков
df.isnull().sum()
```
""")

print("Module 03 created successfully.")

# ==========================================
# MODULE 04: DATA CLEANING & TRANSFORMATION
# ==========================================
m04 = os.path.join(BASE, "module_04_data_cleaning")
os.makedirs(m04, exist_ok=True)

with open(os.path.join(m04, "README.md"), "w", encoding="utf-8") as f:
    f.write("""# 🧹 Модуль 4: Очистка и трансформация данных (Data Cleaning)

## 📌 О модуле
«Garbage In — Garbage Out». Если данные грязные, любая нейросеть, дашборд или статистический тест дадут ложный результат. В этом модуле мы учимся автоматизировать обнаружение пропусков, выбросов, невалидных форматов и дублей.

## 🎯 Learning Outcomes
- **Understand**: Причины появления грязных данных (человеческий фактор, сетевые сбои, миграции БД).
- **Apply**: Методы заполнения пропусков (Forward Fill, медиана, моделирование), удаление дублей.
- **Analyze**: Детекция аномалий (Z-score, метод межквартильного размаха IQR).
- **Create**: Воспроизводимый пайплайн предобработки сырых данных на Python.

## 📚 Уроки
1. `lesson_01_dirty_data_types_missing_values.ipynb` — Работа с Missing Values (MCAR, MAR, MNAR) и приведение типов.
2. `lesson_02_duplicates_string_cleaning_regex.ipynb` — Нормализация строк, дедупликация, регулярные выражения (RegEx).
3. `lesson_03_outliers_anomaly_detection.ipynb` — Выбросы: когда их удалять, а когда исследовать как инсайт.
4. `lesson_04_automated_cleaning_pipelines.ipynb` — Построение автоматического пайплайна очистки сырого датасета.
5. `quiz.md` — Тест для самопроверки.
""")

create_notebook(os.path.join(m04, "lesson_01_dirty_data_types_missing_values.ipynb"), [
    ("markdown", """# Модуль 4. Урок 1: Пропущенные значения и трансформация типов
"""),
    ("code", """import pandas as pd
import numpy as np

# Имитация грязного фрагмента данных
raw_data = pd.DataFrame({
    'user_id': [1, 2, 3, 4, 5],
    'amount': ['1500', ' 2 300,50 ', np.nan, 'NULL', '4200'],
    'signup_date': ['2026-01-10', '15/01/2026', '2026-02-01', None, '2026-03-05']
})

print("Сырые грязные данные:")
print(raw_data)

# Шаг 1: Очистка строк и конвертация в float
def clean_currency(val):
    if pd.isna(val) or val == 'NULL':
        return np.nan
    val_str = str(val).replace(' ', '').replace(',', '.')
    return float(val_str)

raw_data['amount_cleaned'] = raw_data['amount'].apply(clean_currency)
# Заполняем пропуск медианой
raw_data['amount_imputed'] = raw_data['amount_cleaned'].fillna(raw_data['amount_cleaned'].median())

print("\\nОчищенные данные:")
print(raw_data[['user_id', 'amount_cleaned', 'amount_imputed']])
""")
])

create_notebook(os.path.join(m04, "lesson_02_duplicates_string_cleaning_regex.ipynb"), [
    ("markdown", """# Модуль 4. Урок 2: Дедупликация и стандартизация текста
"""),
    ("code", """import pandas as pd

contacts = pd.DataFrame({
    'name': ['Иван Иванов', 'иван  иванов', 'ПЕТР СИДОРОВ', 'Петр Сидоров '],
    'phone': ['+7 (999) 111-22-33', '89991112233', '+79992223344', '8 (999) 222-33-44']
})

# Очистка номера телефона регулярным выражением (оставляем только цифры, нормализуем +7)
contacts['phone_clean'] = contacts['phone'].str.replace(r'\\D', '', regex=True)
contacts['phone_clean'] = contacts['phone_clean'].apply(lambda x: '7' + x[1:] if x.startswith('8') else x)

# Нормализация ФИО
contacts['name_clean'] = contacts['name'].str.strip().str.title().str.replace(r'\\s+', ' ', regex=True)

# Удаление полных дублей
cleaned = contacts[['name_clean', 'phone_clean']].drop_duplicates()
print("Нормализованная база контактов:")
print(cleaned)
""")
])

create_notebook(os.path.join(m04, "lesson_03_outliers_anomaly_detection.ipynb"), [
    ("markdown", """# Модуль 4. Урок 3: Выявление выбросов (IQR и Z-Score)

Формула межквартильного размаха:
$$IQR = Q_3 - Q_1$$
$$\\text{Нижняя граница} = Q_1 - 1.5 \\times IQR$$
$$\\text{Верхняя граница} = Q_3 + 1.5 \\times IQR$$
"""),
    ("code", """import pandas as pd
import numpy as np

# Проверим чеки в заказах
orders = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\order_items.csv")

q1 = orders['total_amount'].quantile(0.25)
q3 = orders['total_amount'].quantile(0.75)
iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = orders[(orders['total_amount'] < lower_bound) | (orders['total_amount'] > upper_bound)]
print(f"Q1: {q1:.2f}, Q3: {q3:.2f}, IQR: {iqr:.2f}")
print(f"Границы нормы: [{lower_bound:.2f}, {upper_bound:.2f}]")
print(f"Количество выбросов: {len(outliers)} из {len(orders)} строк")
""")
])

create_notebook(os.path.join(m04, "lesson_04_automated_cleaning_pipelines.ipynb"), [
    ("markdown", """# Модуль 4. Урок 4: Автоматический пайплайн очистки (Pipeline Pattern)
"""),
    ("code", """import pandas as pd

def clean_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    df_clean = df.copy()
    # 1. Удаление полных дубликатов
    df_clean = df_clean.drop_duplicates()
    # 2. Обработка дат
    if 'order_date' in df_clean.columns:
        df_clean['order_date'] = pd.to_datetime(df_clean['order_date'])
    # 3. Фильтрация статусов
    if 'status' in df_clean.columns:
        df_clean = df_clean[df_clean['status'].isin(['Completed', 'Refunded'])]
    return df_clean

orders_raw = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\orders.csv")
orders_processed = clean_pipeline(orders_raw)
print(f"До очистки: {len(orders_raw)} строк, После: {len(orders_processed)} строк")
""")
])

with open(os.path.join(m04, "quiz.md"), "w", encoding="utf-8") as f:
    f.write("""# 🧠 Quiz: Самопроверка по Модулю 4 (Data Cleaning)

### Вопрос 1
Что делать с выбросами при подготовке данных для анализа среднего чека?
- [ ] Всегда сразу удалять любые выбросы
- [x] Исследовать причину: если это ошибка ввода — исправить/удалить; если реальные оптовые клиенты — сегментировать анализ (B2C отдельно, B2B отдельно)
- [ ] Заменить все выбросы на нули

### Вопрос 2
Какой метод заполнения пропусков наиболее нейтрален для числовых метрик с сильной асимметрией?
- [ ] Среднее арифметическое
- [x] Медиана (она устойчива к экстремальным значениям)
- [ ] Случайное число
""")

print("Module 04 created successfully.")

# ==========================================
# MODULE 05: STATISTICS & HYPOTHESIS TESTING
# ==========================================
m05 = os.path.join(BASE, "module_05_statistics")
os.makedirs(m05, exist_ok=True)

with open(os.path.join(m05, "README.md"), "w", encoding="utf-8") as f:
    f.write("""# 📐 Модуль 5: Статистика для аналитика — От описания к выводам

## 📌 О модуле
Математика, которая отличает настоящего аналитика от оператора таблиц. Без статистики невозможно проверить гипотезы, запустить A/B-тест, оценить риски или построить прогнозные регрессии. Вся теория подкреплена интерактивными Python-симуляциями.

## 🎯 Learning Outcomes
- **Understand**: Разница между генеральной совокупностью и выборкой, Central Limit Theorem (ЦПТ), закон больших чисел.
- **Apply**: Расчет доверительных интервалов, проверка гипотез через $p\\text{-value}$, проведение t-теста Стьюдента, критерия Манна-Уитни, хи-квадрат.
- **Analyze**: Корреляция vs Причинность, линейная и логистическая регрессия, интерпретация $R^2$ и коэффициентов.
- **Evaluate**: Статистические ловушки бизнеса (Survivorship Bias, Simpson's Paradox, Multiple Testing).

## 📚 Уроки
1. `lesson_01_descriptive_stats_outliers.ipynb` — Описательная статистика: Mean, Median, Mode, Variance, Std, IQR.
2. `lesson_02_probability_bayes_law_of_large_numbers.ipynb` — Теория вероятностей, условная вероятность, теорема Байеса.
3. `lesson_03_distributions_clt_confidence_intervals.ipynb` — Нормальное распределение, ЦПТ, 95% доверительные интервалы.
4. `lesson_04_hypothesis_testing_p_value_ttest_mann_whitney.ipynb` — Статистические гипотезы: $H_0$ vs $H_1$, ошибки I/II рода, t-тест, Mann-Whitney.
5. `lesson_05_correlation_and_regression_ols_logistic.ipynb` — Корреляционный анализ, OLS регрессия, предсказание оттока (логистическая).
6. `lesson_06_statistical_traps_in_business.ipynb` — Парадокс Симпсона и частые когнитивные ошибки при интерпретации данных.
7. `quiz.md` — 20 вопросов для подготовки к техническому собеседованию.
8. `cheatsheet.md` — Полная шпаргалка статистических критериев.
""")

create_notebook(os.path.join(m05, "lesson_01_descriptive_stats_outliers.ipynb"), [
    ("markdown", """# Модуль 5. Урок 1: Меры центральной тенденции и разброса

Когда среднее врет? Пример с зарплатами в комнате, куда зашел миллиардер:
"""),
    ("code", """import numpy as np
import pandas as pd

salaries = [50000, 60000, 55000, 65000, 70000, 52000, 58000] # Обычные сотрудники
salaries_with_vip = salaries + [100_000_000] # Пришел инвестор

print("БЕЗ ВЫБРОСА:")
print(f"Среднее: {np.mean(salaries):,.0f} руб | Медиана: {np.median(salaries):,.0f} руб")

print("\\nС ВЫБРОСОМ:")
print(f"Среднее: {np.mean(salaries_with_vip):,.0f} руб (Искажено!) | Медиана: {np.median(salaries_with_vip):,.0f} руб (Устойчива!)")
""")
])

create_notebook(os.path.join(m05, "lesson_02_probability_bayes_law_of_large_numbers.ipynb"), [
    ("markdown", """# Модуль 5. Урок 2: Вероятность и теорема Байеса в аналитике

Формула Байеса:
$$P(A|B) = \\frac{P(B|A) \\cdot P(A)}{P(B)}$$

Пример: Модель антифрода отметила платеж как подозрительный. Какова реальная вероятность мошенничества?
"""),
    ("code", """# Расчет апостериорной вероятности фрода
# P(Fraud) = 0.01 (1% транзакций мошеннические)
# Sensitivity (Recall) = 0.95 (если фрод, модель видит с шансом 95%)
# False Positive Rate = 0.05 (на честных срабатывает в 5% случаев)

p_fraud = 0.01
p_clean = 0.99
p_alert_given_fraud = 0.95
p_alert_given_clean = 0.05

# Полная вероятность срабатывания алерта
p_alert = (p_alert_given_fraud * p_fraud) + (p_alert_given_clean * p_clean)

# Истинная вероятность фрода при алерте
p_fraud_given_alert = (p_alert_given_fraud * p_fraud) / p_alert
print(f"Вероятность того, что отмеченная транзакция действительно фрод: {p_fraud_given_alert*100:.1f}%")
print("Инсайт: Несмотря на 95% точность, из-за редкого базового события более половины алертов — ложные!")
""")
])

create_notebook(os.path.join(m05, "lesson_03_distributions_clt_confidence_intervals.ipynb"), [
    ("markdown", """# Модуль 5. Урок 3: Центральная предельная теорема (ЦПТ) на практике

Даже если исходное распределение экспоненциальное или сильно скошенное, **распределение выборочных средних стремится к нормальному**!
"""),
    ("code", """import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
# Исходное скошенное распределение (чеки интернет-магазина)
population = np.random.exponential(scale=1000, size=50000)

sample_means = []
for _ in range(2000):
    sample = np.random.choice(population, size=50)
    sample_means.append(sample.mean())

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.hist(population, bins=50, color='orange', alpha=0.7)
plt.title('Исходная совокупность (Скошенная)')

plt.subplot(1, 2, 2)
plt.hist(sample_means, bins=40, color='blue', alpha=0.7)
plt.title('Выборочные средние (Нормальное ЦПТ!)')
plt.tight_layout()
plt.show()
""")
])

create_notebook(os.path.join(m05, "lesson_04_hypothesis_testing_p_value_ttest_mann_whitney.ipynb"), [
    ("markdown", """# Модуль 5. Урок 4: Проверка гипотез и p-value

Алгоритм проверки гипотез:
1. $H_0$: Разницы между группами нет.
2. $H_1$: Разница статистически значима.
3. Порог значимости $\\alpha = 0.05$.
4. Если $p\\text{-value} < \\alpha$ — отклоняем $H_0$.
"""),
    ("code", """from scipy import stats
import numpy as np

# Симулируем чеки двух версий сайта
np.random.seed(42)
revenue_a = np.random.normal(loc=3100, scale=800, size=500)
revenue_b = np.random.normal(loc=3250, scale=820, size=500)

# Двухвыборочный t-тест
t_stat, p_val = stats.ttest_ind(revenue_a, revenue_b)

print(f"Среднее группы А: {revenue_a.mean():.2f}")
print(f"Среднее группы B: {revenue_b.mean():.2f}")
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_val:.5f}")

if p_val < 0.05:
    print(" Результат статистически значим! Разница не случайна.")
else:
    print(" Не удалось отклонить H0. Разница может быть случайным шумом.")
""")
])

create_notebook(os.path.join(m05, "lesson_05_correlation_and_regression_ols_logistic.ipynb"), [
    ("markdown", """# Модуль 5. Урок 5: Линейная и логистическая регрессия
"""),
    ("code", """import pandas as pd
import statsmodels.api as sm

# На реальных данных SaaS исследуем связь использования фичей и NPS
saas = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\saas_users.csv")

X = saas[['active_seats', 'feature_a_usage']]
X = sm.add_constant(X)
y = saas['nps_score']

model = sm.OLS(y, X).fit()
print("Краткая сводка регрессии OLS:")
print(f"R-squared: {model.rsquared:.4f}")
print(f"Коэффициенты:\\n{model.params}")
""")
])

create_notebook(os.path.join(m05, "lesson_06_statistical_traps_in_business.ipynb"), [
    ("markdown", """# Модуль 5. Урок 6: Ловушки аналитика: Парадокс Симпсона
"""),
    ("code", """# Демонстрация Парадокса Симпсона
# В общем конверсия в группе А выше, но в разрезе каждого сегмента (Desktop/Mobile) группа B побеждает!
import pandas as pd

data = {
    'Variant': ['A', 'A', 'B', 'B'],
    'Device': ['Mobile', 'Desktop', 'Mobile', 'Desktop'],
    'Visitors': [800, 200, 200, 800],
    'Conversions': [80, 40, 24, 176]
}
simpson_df = pd.DataFrame(data)
simpson_df['CR_%'] = (simpson_df['Conversions'] / simpson_df['Visitors'] * 100).round(1)
print(simpson_df)
print("\\n Общий CR A: (80+40)/1000 = 12.0%")
print(" Общий CR B: (24+176)/1000 = 20.0%")
print(" Инсайт: Разбалансировка долей трафика меняет вывод на противоположный. Всегда сегментируйте данные!")
""")
])

with open(os.path.join(m05, "quiz.md"), "w", encoding="utf-8") as f:
    f.write("""# 🧠 Quiz: Самопроверка по Модулю 5 (Статистика)

### Вопрос 1
Что строго означает $p\\text{-value} = 0.03$?
- [ ] Вероятность того, что тестируемая гипотеза верна, равна 3%
- [x] Вероятность получить такое или еще более экстремальное различие случайно при условии, что нулевая гипотеза $H_0$ истинна, составляет 3%
- [ ] Вероятность ошибки ровно 97%

### Вопрос 2
Когда следует применять критерий Манна-Уитни вместо t-теста Стьюдента?
- [ ] Когда выборки очень большие
- [x] Когда данные имеют сильную асимметрию, тяжелые хвосты выбросов и не подчиняются нормальному распределению
- [ ] Всегда вместо t-теста

### Вопрос 3
Что показывает коэффициент детерминации $R^2$ в линейной регрессии?
- [ ] Точность предсказания в процентах
- [x] Долю дисперсии зависимой переменной, которая объясняется включенными в модель факторами
- [ ] Вероятность переобучения
""")

with open(os.path.join(m05, "cheatsheet.md"), "w", encoding="utf-8") as f:
    f.write("""# 📋 Statistics Cheatsheet

| Ситуация | Рекомендуемый тест / метод |
|---|---|
| Сравнение средних чеков (Нормальное распр.) | Двухвыборочный Two-Sample t-test |
| Сравнение чеков со скошенным распр. и выбросами | U-критерий Манна-Уитни (Mann-Whitney U) |
| Сравнение долей (Конверсия A/B) | Z-test для пропорций или Chi-Square (Хи-квадрат) |
| Взаимосвязь числовых величин | Коэффициент Пирсона (линейная) или Спирмена (ранговая) |
""")

print("Module 05 created successfully.")
