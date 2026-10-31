# 📋 SQL Cheatsheet

```sql
-- Оконная функция: прирост к предыдущему значению
LAG(metric, 1) OVER (PARTITION BY user_id ORDER BY event_date)

-- Оконная функция: доля строки в разрезе группы
metric * 100.0 / SUM(metric) OVER (PARTITION BY category)

-- Безопасный расчет конверсии
ROUND(COUNT(DISTINCT converted_users) * 1.0 / NULLIF(COUNT(DISTINCT total_users), 0), 4)
```
