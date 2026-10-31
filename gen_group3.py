import os
import sys
sys.path.append(r"d:\vibe_app\main_data_analytics")
from notebook_helper import create_notebook

BASE = r"d:\vibe_app\main_data_analytics\course"

# ==========================================
# MODULE 06: BI & LOOKER STUDIO
# ==========================================
m06 = os.path.join(BASE, "module_06_bi_looker_studio")
os.makedirs(m06, exist_ok=True)

with open(os.path.join(m06, "README.md"), "w", encoding="utf-8") as f:
    f.write("""# 📊 Модуль 6: BI-аналитика и Looker Studio — Создание дашбордов

## 📌 О модуле
Дашборд — это рабочий инструмент топ-менеджеров и продуктовых команд. Looker Studio (Google) — один из самых доступных, мощных и облачных инструментов визуализации. Аналитик учится не просто «ставить графики», а проектировать экраны, отвечающие на вопросы принятия решений за 5 секунд.

## 🎯 Learning Outcomes
- **Apply**: Подключение источников данных (Google Sheets, BigQuery, CSV, базы данных).
- **Create**: Вычисляемые поля (`CASE WHEN`, математика), Blending (объединение таблиц в интерфейсе).
- **Evaluate**: Проектирование UI/UX дашборда по правилу F-паттерна и принципу Actionable Insights.
- **Analyze**: Настройка фильтров, диапазонов дат, параметров и Drill-Down срезов.

## 📚 Уроки
1. `lesson_01_looker_studio_setup_and_data_sources.ipynb` — Старт в Looker Studio: источники, типы полей, измерения vs показатели.
2. `lesson_02_calculated_fields_and_parameters.ipynb` — Вычисляемые поля: формулы, логика CASE WHEN.
3. `lesson_03_data_blending_joins_in_bi.ipynb` — Data Blending: соединение источников данных на лету.
4. `lesson_04_dashboard_ui_ux_for_executives.ipynb` — UX/UI принципы: иерархия внимания, KPI карточки.
5. `lesson_05_interactive_filters_controls.ipynb` — Интерактивность: кросс-фильтрация, параметры, drill-down.
6. `quiz.md` — Тест для самопроверки.
7. `cheatsheet.md` — Шпаргалка формул Looker Studio.
""")

create_notebook(os.path.join(m06, "lesson_01_looker_studio_setup_and_data_sources.ipynb"), [
    ("markdown", """# Модуль 6. Урок 1: Введение в Looker Studio

В BI-инструментах все поля делятся на два фундаментальных класса:
1. **Dimensions (Измерения, зеленые поля)**: Категориальные срезы, даты, сегменты (например, `City`, `Date`, `Category`). Они попадают в строки/группировки.
2. **Metrics (Показатели, синие поля)**: Числовые агрегируемые значения (например, `Revenue`, `Orders_Count`, `Avg_Check`).

## Подготовка данных для загрузки в Looker Studio
Перед импортом таблицы в Looker Studio создадим агрегированную плоскую выгрузку:
"""),
    ("code", """import pandas as pd
import sqlite3

# Экспорт готовой витрины для Looker Studio
conn = sqlite3.connect(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\ecommerce.db")
query = \"\"\"
SELECT 
    SUBSTR(o.order_date, 1, 10) AS order_date,
    c.city,
    c.acquisition_channel,
    c.device,
    p.category,
    p.product_name,
    oi.quantity,
    oi.unit_price,
    oi.total_amount AS revenue,
    (oi.total_amount - (p.cost * oi.quantity)) AS gross_profit
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
WHERE o.status = 'Completed';
\"\"\"
bi_export = pd.read_sql(query, conn)
bi_export.to_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\processed\\looker_studio_source.csv", index=False)
print(f"Витрина успешно сохранена! Строк: {len(bi_export)}")
print(bi_export.head(3))
""")
])

create_notebook(os.path.join(m06, "lesson_02_calculated_fields_and_parameters.ipynb"), [
    ("markdown", """# Модуль 6. Урок 2: Вычисляемые поля и синтаксис Looker Studio

Формулы в Looker Studio похожи на гибрид SQL и Excel:

### 1. Маржинальность в процентах:
```sql
SUM(gross_profit) / SUM(revenue)
```
*(Важно: делить именно сумму на сумму, а не брать среднее от частных!)*

### 2. Сегментация чека через CASE WHEN:
```sql
CASE 
  WHEN revenue >= 10000 THEN 'Крупный чек (>10k)'
  WHEN revenue >= 3000 THEN 'Средний чек (3k-10k)'
  ELSE 'Малый чек (<3k)'
END
```
""")
])

create_notebook(os.path.join(m06, "lesson_03_data_blending_joins_in_bi.ipynb"), [
    ("markdown", """# Модуль 6. Урок 3: Data Blending (Смешивание данных)

Когда факты лежат в разных таблицах (например, расходы на маркетинг из Google Sheets, а реальные продажи из базы заказов), в Looker Studio используется **Data Blending**.

### Правила надежного Blending:
1. Выбирайте единый ключ объединения (Join Key): например, `Date` + `Channel`.
2. Используйте **Left Outer Join**, чтобы не терять дни без расходов или без продаж.
3. Согласовывайте форматы дат (YYYY-MM-DD).
""")
])

create_notebook(os.path.join(m06, "lesson_04_dashboard_ui_ux_for_executives.ipynb"), [
    ("markdown", """# Модуль 6. Урок 4: UI/UX дизайн дашборда для руководителей

## Правило 5 секунд (5-Second Rule):
Руководитель должен за 5 секунд понять:
1. **Что происходит прямо сейчас?** (Главные KPI карточки в верхнем левом углу).
2. **Это хорошо или плохо?** (Сравнение с планом или предыдущим периодом $\\Delta\\%$).
3. **Где точка внимания?** (Цветовой акцент: зеленый/красный).

### Зонирование экрана (F-Pattern):
```
┌────────────────────────────────────────────────────────┐
│  [Logo / Название]   [Фильтр дат]  [Фильтр каналов]    │
├────────────────────────────────────────────────────────┤
│  [KPI: Выручка]   [KPI: Заказы]   [KPI: Средний чек]   │
├──────────────────────────┬─────────────────────────────┤
│  Тренд выручки (Line)    │  Структура по категориям   │
├──────────────────────────┴─────────────────────────────┤
│  Таблица лидеров / аутсайдеров (с условным выделением) │
└────────────────────────────────────────────────────────┘
```
""")
])

create_notebook(os.path.join(m06, "lesson_05_interactive_filters_controls.ipynb"), [
    ("markdown", """# Модуль 6. Урок 5: Интерактивность и Cross-Filtering

1. **Date Range Control**: Установка плавающих диапазонов («Последние 30 дней», «Текущий квартал»).
2. **Cross-filtering**: Клик по столбцу «Electronics» на диаграмме категорий автоматически фильтрует все остальные графики на странице.
3. **Drill-down**: Проваливание от уровня «Год» к «Месяцу» и «Дню» внутри одной диаграммы.
""")
])

with open(os.path.join(m06, "quiz.md"), "w", encoding="utf-8") as f:
    f.write("""# 🧠 Quiz: Самопроверка по Модулю 6 (Looker Studio)

### Вопрос 1
Как правильно рассчитать показатель конверсии (CR) в вычисляемом поле Looker Studio?
- [ ] `AVG(Conversions / Visitors)`
- [x] `SUM(Conversions) / SUM(Visitors)`
- [ ] `Conversions / Visitors`

### Вопрос 2
В чем разница между Dimension (Измерением) и Metric (Показателем)?
- [ ] Нет разницы
- [x] Dimension — это нечисловой срез или группировка (текст, дата, категория), а Metric — это агрегируемое числовое значение
- [ ] Metric всегда отображается зеленым цветом

### Вопрос 3
Что означает F-паттерн в дизайне дашбордов?
- [ ] Форматирование шрифтов в стиле Google
- [x] Привычка взгляда пользователя сканировать экран слева направо и сверху вниз; самые важные KPI размещают в левом верхнем углу
- [ ] Быстрое построение графиков за 5 минут
""")

with open(os.path.join(m06, "cheatsheet.md"), "w", encoding="utf-8") as f:
    f.write("""# 📋 Looker Studio Cheatsheet

```sql
-- Извлечение года-месяца
YEAR_MONTH(Date_Column)

-- Условная группировка
CASE 
  WHEN REGEXP_MATCH(Device, '.*Mobile.*') THEN 'Mobile' 
  ELSE 'Desktop' 
END

-- Безопасная маржа
(SUM(Revenue) - SUM(Cost)) / NULLIF(SUM(Revenue), 0)
```
""")

print("Module 06 created successfully.")

# ==========================================
# MODULE 07: A/B TESTING
# ==========================================
m07 = os.path.join(BASE, "module_07_ab_testing")
os.makedirs(m07, exist_ok=True)

with open(os.path.join(m07, "README.md"), "w", encoding="utf-8") as f:
    f.write("""# 🧪 Модуль 7: A/B-тестирование — Научный подход к изменениям в продукте

## 📌 О модуле
Бизнес не может полагаться на интуицию («мне кажется, эта синяя кнопка красивее»). A/B-тестирование — золотой стандарт проверки гипотез в продуктовых и маркетинговых компаниях (Яндекс, Авито, Ozon, Netflix, Uber).

## 🎯 Learning Outcomes
- **Understand**: Ошибки I рода ($\\alpha$, ложная тревога) и II рода ($\\beta$, упущенная выгода), статистическая мощность ($1 - \\beta$).
- **Apply**: Расчет размера выборки (Sample Size) и MDE (Minimum Detectable Effect) до старта теста.
- **Analyze**: Проверка корректности сплитования: A/A-тесты и Sample Ratio Mismatch (SRM).
- **Evaluate**: Проблема ранней остановки (Peeking Problem), множественное тестирование (поправка Бонферрони).
- **Create**: Полный Python-ноутбук анализа A/B-теста от валидации до решения о раскатке.

## 📚 Уроки
1. `lesson_01_ab_testing_framework_and_mde.ipynb` — Дизайн эксперимента: формулировка гипотезы, метрики OEC, расчет Sample Size & MDE.
2. `lesson_02_splitting_aa_tests_srm.ipynb` — Рандомизация, A/A-тестирование и проверка Sample Ratio Mismatch (Chi-Square).
3. `lesson_03_evaluating_metrics_proportions_means.ipynb` — Оценка результатов: тест пропорций для конверсий, t-тест / бутстрап для выручки.
4. `lesson_04_p_hacking_peeking_problem.ipynb` — Ловушки: p-hacking, peeking problem (почему нельзя подглядывать каждый день).
5. `lesson_05_business_decision_rollout.ipynb` — Принятие бизнес-решения: статистическая значимость vs экономическая целесообразность.
6. `quiz.md` — Тест для закрепления.
7. `cheatsheet.md` — Памятка формул A/B теста.
""")

create_notebook(os.path.join(m07, "lesson_01_ab_testing_framework_and_mde.ipynb"), [
    ("markdown", """# Модуль 7. Урок 1: Дизайн эксперимента и расчет выборки

Формула размера выборки для пропорции (конверсии):
$$n = \\frac{2 \\cdot (Z_{\\alpha/2} + Z_{\\beta})^2 \\cdot p(1-p)}{MDE^2}$$

Где:
- $\\alpha = 0.05$ (Уровень значимости, $Z_{0.025} \\approx 1.96$)
- $\\beta = 0.20$ (Мощность $80\\%$, $Z_{0.20} \\approx 0.84$)
- $p$ — базовая конверсия
- $MDE$ — минимальный детектируемый эффект в абсолютных долях
"""),
    ("code", """import statsmodels.stats.api as sms

# Расчет необходимого размера выборки на группу
baseline_cr = 0.080 # Базовая конверсия 8%
target_cr = 0.092   # Хотим заметить рост до 9.2% (MDE = 1.2% абс. / 15% отн.)

effect_size = sms.proportion_effectsize(baseline_cr, target_cr)
required_sample = sms.NormalIndPower().solve_power(
    effect_size=effect_size,
    power=0.80,
    alpha=0.05,
    ratio=1
)
print(f"Базовая конверсия: {baseline_cr*100}% | Ожидаемая: {target_cr*100}%")
print(f"Необходимо пользователей В КАЖДОЙ группе: {int(round(required_sample)):,}")
print(f"Всего участников теста: {int(round(required_sample))*2:,}")
""")
])

create_notebook(os.path.join(m07, "lesson_02_splitting_aa_tests_srm.ipynb"), [
    ("markdown", """# Модуль 7. Урок 2: Проверка сплитования: Sample Ratio Mismatch (SRM)

Если сплит 50/50, а пришло 5 200 против 4 800 пользователей — сломался ли сплиттер? Проверяем критерием $\\chi^2$.
"""),
    ("code", """import pandas as pd
from scipy.stats import chisquare

# Загружаем датасет A/B теста
ab_df = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\ab_test_checkout.csv")
counts = ab_df['test_group'].value_counts()
print("Фактическое распределение:")
print(counts)

# Хи-квадрат проверка SRM при ожидании 50 / 50
observed = [counts['A_Control'], counts['B_Variant']]
total = sum(observed)
expected = [total / 2, total / 2]

chi2_stat, p_val = chisquare(f_obs=observed, f_exp=expected)
print(f"\\nChi2 stat: {chi2_stat:.4f}, p-value: {p_val:.4f}")
if p_val < 0.01:
    print(" КРИТИЧЕСКАЯ ОШИБКА: Обнаружен SRM! Трафик распределился неравномерно, тест невалиден!")
else:
    print(" SRM не обнаружен. Сплитование корректное (50/50 соблюдено).")
""")
])

create_notebook(os.path.join(m07, "lesson_03_evaluating_metrics_proportions_means.ipynb"), [
    ("markdown", """# Модуль 7. Урок 3: Анализ конверсии и выручки в A/B тесте
"""),
    ("code", """import pandas as pd
from statsmodels.stats.proportion import proportions_ztest
from scipy import stats

ab_df = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\ab_test_checkout.csv")

group_a = ab_df[ab_df['test_group'] == 'A_Control']
group_b = ab_df[ab_df['test_group'] == 'B_Variant']

cr_a = group_a['converted'].mean()
cr_b = group_b['converted'].mean()
uplift = ((cr_b - cr_a) / cr_a) * 100

print(f"Конверсия Control (A): {cr_a*100:.2f}% ({group_a['converted'].sum()} / {len(group_a)})")
print(f"Конверсия Variant (B): {cr_b*100:.2f}% ({group_b['converted'].sum()} / {len(group_b)})")
print(f"Относительный прирост (Uplift): +{uplift:.2f}%")

# Z-test для конверсий
count = [group_b['converted'].sum(), group_a['converted'].sum()]
nobs = [len(group_b), len(group_a)]
z_stat, p_val = proportions_ztest(count, nobs)

print(f"Z-statistic: {z_stat:.4f}, p-value: {p_val:.5f}")
if p_val < 0.05:
    print(" Статистически значимый прирост конверсии!")
""")
])

create_notebook(os.path.join(m07, "lesson_04_p_hacking_peeking_problem.ipynb"), [
    ("markdown", """# Модуль 7. Урок 4: Peeking Problem (Почему нельзя останавливать тест раньше времени)

Если аналитик каждый день проверяет $p\\text{-value}$ и останавливает тест в момент $p < 0.05$, реальный уровень ошибки I рода возрастает с $5\\%$ до $30\\%+$!
"""),
    ("code", """# Симуляция Peeking Problem на пустом A/A тесте (где различий нет!)
import numpy as np
from scipy import stats

np.random.seed(123)
n_days = 30
users_per_day = 100

# Генерируем накопительные данные для одинаковых групп
a_users = np.random.binomial(1, 0.10, size=(n_days, users_per_day))
b_users = np.random.binomial(1, 0.10, size=(n_days, users_per_day))

peeking_false_alarms = 0
for day in range(5, n_days):
    sample_a = a_users[:day].flatten()
    sample_b = b_users[:day].flatten()
    _, p = stats.ttest_ind(sample_a, sample_b)
    if p < 0.05:
        peeking_false_alarms += 1
        print(f"День {day}: Подглядели! p-value={p:.4f} < 0.05. Ложное срабатывание!")
        break

if peeking_false_alarms == 0:
    print("Ложных срабатываний не было.")
""")
])

create_notebook(os.path.join(m07, "lesson_05_business_decision_rollout.ipynb"), [
    ("markdown", """# Модуль 7. Урок 5: Бизнес-решение о раскатке изменений

Чеклист перед раскаткой фичи на 100% пользователей:
1. Статистическая значимость основной целевой метрики ($p < 0.05$).
2. Отсутствие деградации guardrail-метрик (например, выросла конверсия, но упал средний чек или выросло число жалоб).
3. Экономическая окупаемость разработки (Cost-Benefit Analysis).
""")
])

with open(os.path.join(m07, "quiz.md"), "w", encoding="utf-8") as f:
    f.write("""# 🧠 Quiz: Самопроверка по Модулю 7 (A/B Testing)

### Вопрос 1
Что такое Sample Ratio Mismatch (SRM)?
- [ ] Ошибка в расчете среднего чека
- [x] Аномальное отклонение фактического соотношения пользователей в группах от запланированного (например, 45/55 вместо 50/50), указывающее на технический баг сплиттера
- [ ] Разница между конверсиями в группах

### Вопрос 2
Почему опасно завершать A/B-тест досрочно, как только p-value впервые упал ниже 0.05 (Peeking Problem)?
- [ ] Сервер зависнет
- [x] Это резко завышает вероятность ошибки I рода (ложноположительного результата), фиксируя случайный временный шум
- [ ] Теряются исторические логи

### Вопрос 3
Что такое Guardrail Metric?
- [ ] Метрика скорости загрузки кода
- [x] Защитная метрика, ухудшение которой недопустимо даже при росте целевой метрики (например: уровень возвратов, отток, жалобы в саппорт)
- [ ] Название кнопки на сайте
""")

with open(os.path.join(m07, "cheatsheet.md"), "w", encoding="utf-8") as f:
    f.write("""# 📋 A/B Testing Cheatsheet

| Понятие | Формула / Смысл |
|---|---|
| Ошибка I рода (Alpha) | Вероятность увидеть разницу там, где её нет (норма: 0.05) |
| Ошибка II рода (Beta) | Вероятность не заметить реальный эффект (норма: 0.20) |
| Мощность (Power) | $1 - \\beta = 0.80$ (шанс поймать реальное улучшение) |
| Поправка Бонферрони | $\\alpha_{new} = \\alpha / k$ (при проверке $k$ гипотез одновременно) |
""")

print("Module 07 created successfully.")

# ==========================================
# MODULE 08: PROMPT ENGINEERING FOR ANALYSTS
# ==========================================
m08 = os.path.join(BASE, "module_08_prompt_engineering")
os.makedirs(m08, exist_ok=True)

with open(os.path.join(m08, "README.md"), "w", encoding="utf-8") as f:
    f.write("""# 🤖 Модуль 8: Prompt Engineering для Data Analyst 2027

## 📌 О модуле
Промпт-инжиниринг в аналитике — это не просто вежливое обращение к ChatGPT. Это строгое инженерное искусство составления структурированных технических заданий для больших языковых моделей (LLM), позволяющее получать безошибочный код, корректную архитектуру данных и воспроизводимые инсайты.

## 🎯 Learning Outcomes
- **Understand**: Принципы работы LLM (токены, контекстное окно, вероятностное предсказание следующего слова).
- **Apply**: Архитектурные фреймворки составления промптов (RTCE: Role, Task, Context, Expectation).
- **Analyze**: Методологии Few-Shot Prompting, Chain-of-Thought (CoT) и ReAct в аналитических задачах.
- **Create**: Персональную библиотеку промптов для SQL, дебага Pandas и подготовки отчетов для C-level.

## 📚 Уроки
1. `lesson_01_prompt_engineering_fundamentals.ipynb` — Анатомия промпта аналитика: фреймворк RTCE, Zero-shot vs Few-shot.
2. `lesson_02_chain_of_thought_for_analytics.ipynb` — Рассуждение по шагам (Chain-of-Thought) для сложных математических задач.
3. `lesson_03_prompting_for_sql_and_python.ipynb` — Инженерия промптов для генерации SQL, оконных функций и Pandas-пайплайнов.
4. `lesson_04_debugging_and_root_cause_prompts.ipynb` — Промпты для дебага ошибок, анализа стектрейсов и оптимизации тяжелых запросов.
5. `prompt_library.md` — Готовая библиотека 25+ рабочих промптов аналитика данных.
6. `quiz.md` — Тест для самопроверки.
""")

create_notebook(os.path.join(m08, "lesson_01_prompt_engineering_fundamentals.ipynb"), [
    ("markdown", """# Модуль 8. Урок 1: Архитектурный фреймворк RTCE для аналитика

Любой надежный аналитический промпт должен содержать 4 компонента:
1. **R (Role)**: Роль эксперта (например: Lead PostgreSQL Database Administrator).
2. **T (Task)**: Четкое действие в повелительном наклонении (Напиши SQL-запрос...).
3. **C (Context)**: Схема базы, примеры данных, краевые условия (только клиенты 2026 года, статус Completed).
4. **E (Expectation / Format)**: Формат вывода (только чистый SQL в блоке кода без лишних приветствий, поясни логику).

### Плохой промпт:
> «Посчитай мне ретеншн в базе»

### Идеальный промпт:
> «Ты senior Product Analyst. База: PostgreSQL. Таблица `events(user_id INT, event_name TEXT, event_date TIMESTAMP)`. Напиши запрос расчета Day 1, Day 7, Day 30 Retention для когорт регистрации за январь 2026 года. Используй CTE. Обработай деление на ноль через NULLIF. Верни только код с комментариями.»
""")
])

create_notebook(os.path.join(m08, "lesson_02_chain_of_thought_for_analytics.ipynb"), [
    ("markdown", """# Модуль 8. Урок 2: Метод Chain-of-Thought (Цепочка рассуждений)

Когда LLM генерирует ответ сразу, вероятность логической ошибки высока. Добавление фразы:
> **«Рассуждай пошагово перед написанием формулы» (Think step by step)**

вынуждает модель сначала сгенерировать рассуждение в токенах, что повышает точность вычислений в разы.
""")
])

create_notebook(os.path.join(m08, "lesson_03_prompting_for_sql_and_python.ipynb"), [
    ("markdown", """# Модуль 8. Урок 3: Промпты для SQL и Python (Few-Shot Prompting)

Демонстрация техники Few-Shot (показ 1-2 эталонных примеров решения похожей задачи):
""")
])

create_notebook(os.path.join(m08, "lesson_04_debugging_and_root_cause_prompts.ipynb"), [
    ("markdown", """# Модуль 8. Урок 4: Промпты для отладки и поиска багов

## Шаблон промпта "Анализ стектрейса":
```text
У меня возникла ошибка при выполнении скрипта Pandas:
[ВСТАВИТЬ СТЕКТРЕЙС ОШИБКИ]

Фрагмент кода:
[ВСТАВИТЬ КОД]

Формат ответа:
1. Корневая причина ошибки (Root Cause).
2. Минимальный исправленный фрагмент кода.
3. Совет, как предотвратить подобные ошибки на стадии валидации данных.
```
""")
])

with open(os.path.join(m08, "prompt_library.md"), "w", encoding="utf-8") as f:
    f.write("""# 📚 Библиотека промптов аналитика данных 2027

### 1. Генерация когортного анализа на SQL
```text
РОЛЬ: Senior Data Engineer.
БД: SQLite / PostgreSQL.
СХЕМА: orders (order_id, customer_id, order_date, status, total_amount).
ЗАДАЧА: Напиши запрос, строящий классическую матрицу когортного ретеншна по месяцам.
УСЛОВИЯ: Включать только статус 'Completed'. Первый заказ пользователя определяет его когорту.
ФОРМАТ: Оформи через читаемые CTE (first_orders, monthly_activity, cohort_matrix).
```

### 2. Генерация отчета по бизнес-метрикам для CEO
```text
РОЛЬ: Chief Strategy Officer & Lead Analyst.
ДАННЫЕ: В текущем месяце выручка упала на 12%, при этом рекламный трафик вырос на 20%, а средний чек остался прежним.
ЗАДАЧА: Напиши аналитическую записку для Совета Директоров.
ФОРМАТ: Примени принцип Пирамиды Минто. Начни с ключевого вывода и рекомендуемого действия. Избегай технического жаргона.
```
""")

with open(os.path.join(m08, "quiz.md"), "w", encoding="utf-8") as f:
    f.write("""# 🧠 Quiz: Самопроверка по Модулю 8 (Prompt Engineering)

### Вопрос 1
Что дает метод Chain-of-Thought (рассуждение по шагам)?
- [ ] Уменьшает расход токенов
- [x] Повышает точность сложных аналитических расчетов за счет промежуточного вывода рассуждений
- [ ] Заставляет модель писать код на Java

### Вопрос 2
Что такое Few-Shot Prompting?
- [ ] Однократный запуск запроса
- [x] Передача модели одного или нескольких примеров «входные данные -> правильный результат» прямо в контексте промпта
- [ ] Быстрый ответ без рассуждений
""")

print("Module 08 created successfully.")
