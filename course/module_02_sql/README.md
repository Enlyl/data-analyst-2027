# 🗃️ Модуль 2: SQL — От первых запросов до аналитических оконных функций

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
