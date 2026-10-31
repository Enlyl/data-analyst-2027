import os
import sys
sys.path.append(r"d:\vibe_app\main_data_analytics")
from notebook_helper import create_notebook

BASE = r"d:\vibe_app\main_data_analytics\course"

# ==========================================
# MODULE 06: LOOKER STUDIO & BI
# ==========================================
m06 = os.path.join(BASE, "module_06_bi_looker_studio")
os.makedirs(m06, exist_ok=True)

create_notebook(os.path.join(m06, "lesson_01_looker_studio_setup_and_data_sources.ipynb"), [
    ("markdown", """# 📊 Модуль 6. Урок 1: Подключение источников данных и архитектура витрин в Looker Studio

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_06_bi_looker_studio/lesson_01_looker_studio_setup_and_data_sources.ipynb)

---

## 1. Ментальная модель BI: Измерения (Dimensions) vs Показатели (Metrics)

В Looker Studio и любом современном BI-инструменте данные жестко разделяются:
- **Dimensions (Зеленые поля)**: Категориальные срезы, по которым данные группируются (Город, Категория, Дата, Канал привлечения).
- **Metrics (Синие поля)**: Числовые агрегируемые величины (Выручка, Количество клиентов, Средний чек).

### Золотое правило витрины данных для BI:
Никогда не подключайте «сырые» ненормализованные логи напрямую в отчеты, если в них миллионы строк. Сначала подготовьте денормализованную витрину (Data Mart) на уровне SQL/Python.
"""),
    ("code", """# Экспорт оптимизированной витрины для Looker Studio
import sqlite3
import pandas as pd

conn = sqlite3.connect(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\ecommerce.db")

query_bi = \"\"\"
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

bi_data = pd.read_sql(query_bi, conn)
bi_data.to_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\processed\\looker_studio_source.csv", index=False)
print(" ВИТРИНА ДЛЯ LOOKER STUDIO ГОТОВА:")
print(f"Строк: {len(bi_data):,} | Колонок: {len(bi_data.columns)}")
print(bi_data.head(3))
""")
])

# Lesson 2
create_notebook(os.path.join(m06, "lesson_02_calculated_fields_and_parameters.ipynb"), [
    ("markdown", """# ⚙️ Модуль 6. Урок 2: Вычисляемые поля и логика CASE WHEN в Looker Studio

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_06_bi_looker_studio/lesson_02_calculated_fields_and_parameters.ipynb)

---

## 1. Топ-3 формулы в Looker Studio

### 1. Маржинальность бизнеса (% Margin):
```sql
SUM(gross_profit) / SUM(revenue)
```
*(Ошибочно писать: `AVG(gross_profit / revenue)` — это усреднит проценты без весов).*

### 2. Динамическая сегментация чека:
```sql
CASE 
  WHEN revenue >= 15000 THEN '1. Крупный чек (>15k)'
  WHEN revenue >= 5000 THEN '2. Средний чек (5k-15k)'
  ELSE '3. Малый чек (<5k)'
END
```

### 3. Нормализация каналов рекламы:
```sql
CASE 
  WHEN REGEXP_MATCH(acquisition_channel, '.*(Paid|Ads).*') THEN 'Платный трафик'
  ELSE 'Органический трафик'
END
```
""")
])

# Lesson 3
create_notebook(os.path.join(m06, "lesson_03_data_blending_joins_in_bi.ipynb"), [
    ("markdown", """# 🔗 Модуль 6. Урок 3: Data Blending: Склейка фактов разных уровней гранулярности

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_06_bi_looker_studio/lesson_03_data_blending_joins_in_bi.ipynb)

---

## 1. Проблема разных уровней детализации (Granularity Mismatch)

Кейс:
- **Таблица 1 (Маркетинг)**: Расходы по дням и рекламным кампаниям (Google Sheets, 1 строка на день).
- **Таблица 2 (Продажи)**: Транзакции по каждому отдельному чеку (База данных, 500 строк на день).
Если вы наивно соедините их в BI без предварительной агрегации, рекламный бюджет дня продублируется 500 раз!

### Правило безопасного Blending:
Перед объединением в Looker Studio агрегируйте обе таблицы к **единому ключу** (например: `Дата` + `Канал`).
""")
])

# Lesson 4
create_notebook(os.path.join(m06, "lesson_04_dashboard_ui_ux_for_executives.ipynb"), [
    ("markdown", """# 📱 Модуль 6. Урок 4: UI/UX дизайн дашбордов для C-Level руководителей

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_06_bi_looker_studio/lesson_04_dashboard_ui_ux_for_executives.ipynb)

---

## 1. Принцип Actionable Dashboard: Ответ за 5 секунд

Топ-менеджер не должен разгадывать дашборд как ребус.
Экран делится на 3 смысловых яруса:
1. **Верхний ярус (Карточки Scorecard)**: Выручка, Количество заказов, Средний чек, LTV/CAC с динамикой к прошлому периоду ($\Delta\%$).
2. **Средний ярус (Тренды)**: Линейный график динамики за 90 дней и столбчатая диаграмма структуры по категориям.
3. **Нижний ярус (Детализация)**: Таблица лидеров и аутсайдеров с условным цветовым форматированием (Heatmap).
""")
])

# Lesson 5
create_notebook(os.path.join(m06, "lesson_05_interactive_filters_controls.ipynb"), [
    ("markdown", """# 🎛️ Модуль 6. Урок 5: Интерактивные фильтры, параметры и Drill-down

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_06_bi_looker_studio/lesson_05_interactive_filters_controls.ipynb)

---

## 1. Превращение статического отчета в инструмент исследователя

- **Cross-filtering (Кросс-фильтрация)**: Клик по столбцу категории на одной диаграмме мгновенно пересчитывает все остальные графики страницы.
- **Drill-down**: Иерархия уровней (`Год -> Квартал -> Месяц -> День`).
- **Срезы по устройствам (Device Slicers)**: Выбор Desktop / Mobile.
""")
])

# Module 06 Quiz
with open(os.path.join(m06, "quiz.md"), "w", encoding="utf-8") as f:
    f.write("""# 🧠 Quiz: Самопроверка по Модулю 6 (Looker Studio & BI)

---

### Вопрос 1
Как правильно рассчитать конверсию (Conversion Rate) в вычисляемом поле Looker Studio?
- [ ] `AVG(Purchases / Sessions)`
- [x] `SUM(Purchases) / SUM(Sessions)`
- [ ] `Purchases / Sessions`
*Объяснение*: Нельзя усреднять частные (`AVG(...)`). Необходимо вычислить отношение суммы всех покупок к сумме всех сессий.

---

### Вопрос 2
Что такое Granularity Mismatch при Data Blending?
- [ ] Ошибка в названии столбца.
- [x] Несоответствие уровня детализации таблиц (например, расходы сгруппированы по дням, а продажи — по конкретным секундам чеков), приводящее к задвоению метрик.
- [ ] Нехватка оперативной памяти в браузере.
*Объяснение*: Для корректного соединения обе таблицы должны быть приведены к одинаковому составному ключу группировки.

---

### Вопрос 3
Каково правило «5 секунд» в дизайне бизнес-дашбордов?
- [ ] Дашборд должен загружаться не более 5 секунд.
- [x] Руководитель должен за 5 секунд понять текущий статус ключевых KPI и наличие отклонений от плана.
- [ ] Графики должны обновляться каждые 5 секунд.
*Объяснение*: Главные карточки метрик с индикаторами отклонения должны считываться моментально в верхнем левом углу.
""")

print("Module 06 deepened successfully.")

# ==========================================
# MODULE 07: A/B TESTING DEEP DIVE
# ==========================================
m07 = os.path.join(BASE, "module_07_ab_testing")
os.makedirs(m07, exist_ok=True)

# Lesson 1
create_notebook(os.path.join(m07, "lesson_01_ab_testing_framework_and_mde.ipynb"), [
    ("markdown", """# 🧪 Модуль 7. Урок 1: Дизайн эксперимента: Метрики OEC, Sample Size и MDE

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_07_ab_testing/lesson_01_ab_testing_framework_and_mde.ipynb)

---

## 1. Математика планирования A/B-эксперимента

Никогда не запускайте тест со словами: *«Покрутим пару дней, а там посмотрим»*.
До запуска теста аналитик обязан рассчитать **минимальный размер выборки (Sample Size)**.

Формула необходимого размера выборки на группу:
$$n = \\frac{2 \\cdot (Z_{\\alpha/2} + Z_{\\beta})^2 \\cdot p(1-p)}{MDE^2}$$

Где:
- $\\alpha = 0.05$ (Ошибка I рода, вероятность ложной тревоги 5%);
- $\\beta = 0.20$ (Ошибка II рода, мощность $1 - \\beta = 80\\%$);
- $MDE$ (Minimum Detectable Effect) — минимальный эффект, который экономически имеет смысл обнаружить.
"""),
    ("code", """import statsmodels.stats.api as sms

# Расчет выборки для интернет-магазина
baseline_cr = 0.082  # Текущая конверсия 8.2%
target_cr = 0.095    # Ожидаемый рост до 9.5% (MDE = +1.3% абс.)

effect_size = sms.proportion_effectsize(baseline_cr, target_cr)
required_n = sms.NormalIndPower().solve_power(
    effect_size=effect_size,
    power=0.80,
    alpha=0.05,
    ratio=1
)

print(f"Базовая конверсия: {baseline_cr*100:.1f}% | Целевая: {target_cr*100:.1f}%")
print(f"Необходимо пользователей В КАЖДОЙ группе: {int(round(required_n)):,}")
print(f"Всего пользователей в тесте: {int(round(required_n))*2:,}")
""")
])

# Lesson 2
create_notebook(os.path.join(m07, "lesson_02_splitting_aa_tests_srm.ipynb"), [
    ("markdown", """# ⚖️ Модуль 7. Урок 2: Проверка честности сплитования: Sample Ratio Mismatch (SRM)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_07_ab_testing/lesson_02_splitting_aa_tests_srm.ipynb)

---

## 1. Sample Ratio Mismatch (SRM) — Убийца A/B-тестов

Если вы планировали тест 50/50, а в группу А пришло 5 200 пользователей, а в группу B — 4 800 пользователей:
- Это не «случайная погрешность».
- Это технический сбой системы сплитования (например, на iOS вариант B не загружался и пользователи отваливались до попадания в лог).
- **Результаты такого теста нельзя анализировать! Они полностью невалидны.**
"""),
    ("code", """import pandas as pd
from scipy.stats import chisquare

# Загружаем реальный датасет эксперимента чекаута
ab_df = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\ab_test_checkout.csv")
counts = ab_df['test_group'].value_counts()
print("ФАКТИЧЕСКИЙ СПЛИТ ПОЛЬЗОВАТЕЛЕЙ:")
print(counts)

# Проверка критерием Хи-квадрат
obs = [counts['A_Control'], counts['B_Variant']]
exp = [len(ab_df)/2, len(ab_df)/2]
stat, p_val = chisquare(obs, exp)

print(f"\\nChi2-statistic: {stat:.4f}, p-value: {p_val:.4f}")
if p_val < 0.01:
    print(" АВАРИЯ: Обнаружен SRM! Тест бракованный.")
else:
    print(" SRM не обнаружен! Сплитование 50/50 корректно.")
""")
])

# Lesson 3
create_notebook(os.path.join(m07, "lesson_03_evaluating_metrics_proportions_means.ipynb"), [
    ("markdown", """# 📊 Модуль 7. Урок 3: Полный статистический анализ A/B-теста на Python

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_07_ab_testing/lesson_03_evaluating_metrics_proportions_means.ipynb)

---

## 1. Z-test для конверсий и оценка Uplift
"""),
    ("code", """import pandas as pd
from statsmodels.stats.proportion import proportions_ztest

ab_df = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\ab_test_checkout.csv")

a = ab_df[ab_df['test_group'] == 'A_Control']
b = ab_df[ab_df['test_group'] == 'B_Variant']

cr_a = a['converted'].mean()
cr_b = b['converted'].mean()
uplift = (cr_b - cr_a) / cr_a * 100

count = [b['converted'].sum(), a['converted'].sum()]
nobs = [len(b), len(a)]
z_stat, p_val = proportions_ztest(count, nobs)

print(f"Контроль (A): CR = {cr_a*100:.2f}% | Вариант (B): CR = {cr_b*100:.2f}%")
print(f"Относительный прирост (Uplift): +{uplift:.2f}%")
print(f"Z-stat: {z_stat:.4f}, p-value: {p_val:.5f}")

if p_val < 0.05:
    print(" РЕШЕНИЕ: Изменение статистически значимо! Выкатываем вариант B на 100% аудитории.")
""")
])

# Lesson 4
create_notebook(os.path.join(m07, "lesson_04_p_hacking_peeking_problem.ipynb"), [
    ("markdown", """# 🛑 Модуль 7. Урок 4: Peeking Problem и p-hacking: Почему нельзя подглядывать в результаты

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_07_ab_testing/lesson_04_p_hacking_peeking_problem.ipynb)

---

## 1. Механика ложного срабатывания при Peeking

Если вы каждый день заглядываете в дашборд теста и решаете остановить его в первый момент, когда $p < 0.05$, вероятность ложноположительного результата (**False Positive**) возрастает с нормальных $5\\%$ до $35-40\\%$!
Вы гарантированно выкатите на прод бесполезную или вредную фичу, приняв случайное колебание за победу.
""")
])

# Lesson 5
create_notebook(os.path.join(m07, "lesson_05_business_decision_rollout.ipynb"), [
    ("markdown", """# 🚀 Модуль 7. Урок 5: Принятие бизнес-решения о раскатке: Guardrail метрики

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_07_ab_testing/lesson_05_business_decision_rollout.ipynb)

---

## 1. Guardrail Metrics (Защитные метрики)

Даже если целевая метрика (CR) статистически значимо выросла на 15%, тест **нельзя** раскатывать, если:
1. Выросло число возвратов товаров (Refund Rate);
2. Упал средний чек (AOV);
3. Увеличилось время ответа саппорта или выросла нагрузка на серверы.
""")
])

# Module 07 Quiz
with open(os.path.join(m07, "quiz.md"), "w", encoding="utf-8") as f:
    f.write("""# 🧠 Quiz: Самопроверка по Модулю 7 (A/B-тестирование)

---

### Вопрос 1
Что происходит с реальным уровнем ошибки I рода ($\\alpha$), если аналитик каждый день проверяет тест и останавливает его при первом $p < 0.05$ (Peeking Problem)?
- [ ] Ошибка остается строго 5%.
- [x] Реальная вероятность ложноположительного результата подскакивает до 30-40%, фиксируя случайный шум.
- [ ] Ошибка уменьшается до нуля.
*Объяснение*: Непрерывный мониторинг накапливает вероятность случайного пересечения порога 0.05.

---

### Вопрос 2
Что показывает Sample Ratio Mismatch (SRM)?
- [ ] Разницу в конверсиях между группами.
- [x] Нарушение запланированного соотношения объемов трафика в группах (например, 48/52 вместо 50/50), указывающее на технический сбой рандомизатора.
- [ ] Ошибку в расчете выручки.
*Объяснение*: При наличии SRM результаты сравнения метрик между группами математически невалидны.

---

### Вопрос 3
Зачем нужны Guardrail-метрики в эксперименте?
- [ ] Чтобы ускорить расчет p-value.
- [x] Чтобы предотвратить раскатку фичи, которая вырастила локальную метрику за счет разрушения глобального здоровья бизнеса (например, рост кликов ценой падения выручки).
- [ ] Для шифрования данных.
*Объяснение*: Guardrail-метрики защищают ключевые бизнес-показатели от деградации.
""")

print("Module 07 deepened successfully.")

# ==========================================
# MODULE 08: PROMPT ENGINEERING DEEP DIVE
# ==========================================
m08 = os.path.join(BASE, "module_08_prompt_engineering")
os.makedirs(m08, exist_ok=True)

create_notebook(os.path.join(m08, "lesson_01_prompt_engineering_fundamentals.ipynb"), [
    ("markdown", """# 🤖 Модуль 8. Урок 1: Архитектурные фреймворки промптинга: RTCE и Few-Shot

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_08_prompt_engineering/lesson_01_prompt_engineering_fundamentals.ipynb)

---

## 1. Фреймворк RTCE в аналитике

1. **R (Role)**: «Ты Principal Database Architect в FinTech компании с 15-летним опытом оптимизации PostgreSQL».
2. **T (Task)**: «Напиши запрос для расчета 30-дневного скользящего среднего Retention Rate».
3. **C (Context)**: Схема таблицы, типы полей, объем (50 млн строк, нужны индексы).
4. **E (Expectation)**: «Используй только стандартный SQL, CTE и оконные функции. Добавь пояснения логики».
""")
])

# Lesson 2
create_notebook(os.path.join(m08, "lesson_02_chain_of_thought_for_analytics.ipynb"), [
    ("markdown", """# 🧠 Модуль 8. Урок 2: Метод Chain-of-Thought (Рассуждение по шагам)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_08_prompt_engineering/lesson_02_chain_of_thought_for_analytics.ipynb)

---

## 1. Почему нейросети ошибаются в математике без CoT?

LLM — это авторегрессионные языковые модели. Они не вычисляют формулу в скрытом процессоре, они предсказывают следующее слово (токен).
Если заставить модель сразу выдать число — шанс ошибки велик.
Если заставить модель расписать каждый шаг формулы вслух — вероятность правильного ответа превышает 98%.
""")
])

# Lesson 3
create_notebook(os.path.join(m08, "lesson_03_prompting_for_sql_and_python.ipynb"), [
    ("markdown", """# 💻 Модуль 8. Урок 3: Промпты для генерации сложного SQL и Pandas пайплайнов

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_08_prompt_engineering/lesson_03_prompting_for_sql_and_python.ipynb)

---

## 1. Шаблоны промптов для когортного анализа и воронок
""")
])

# Lesson 4
create_notebook(os.path.join(m08, "lesson_04_debugging_and_root_cause_prompts.ipynb"), [
    ("markdown", """# 🔍 Модуль 8. Урок 4: Поиск багов, оптимизация планов запросов (EXPLAIN) и аудит кода

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_08_prompt_engineering/lesson_04_debugging_and_root_cause_prompts.ipynb)

---

## 1. Промпт для анализа EXPLAIN QUERY PLAN
""")
])

# Module 08 Quiz
with open(os.path.join(m08, "quiz.md"), "w", encoding="utf-8") as f:
    f.write("""# 🧠 Quiz: Самопроверка по Модулю 8 (Prompt Engineering)

---

### Вопрос 1
Что дает добавление инструкции «Рассуждай по шагам» (Chain-of-Thought) в промпте для аналитика?
- [ ] Уменьшает количество затраченных токенов.
- [x] Позволяет модели сформировать промежуточные логические выводы перед финальным расчетом, резко снижая процент математических ошибок.
- [ ] Переводит код на язык C++.
*Объяснение*: CoT принуждает LLM использовать контекст генерируемых токенов как рабочую память.

---

### Вопрос 2
В чем заключается техника Few-Shot Prompting?
- [ ] Однократный запрос без контекста.
- [x] Предоставление модели в тексте промпта 1-3 готовых примеров «входные данные -> ожидаемый результат» перед постановкой основной задачи.
- [ ] Написание кода без использования библиотек.
*Объяснение*: Few-Shot задает точный шаблон структуры ответа и логики рассуждений.

---

### Вопрос 3
Какой компонент фреймворка RTCE отвечает за формат и ограничения вывода?
- [ ] R (Role).
- [ ] T (Task).
- [x] E (Expectation).
*Объяснение*: В Expectation задаются ограничения (например, «только валидный JSON без пояснений», «обработать деление на ноль»).
""")

print("Module 08 deepened successfully.")
