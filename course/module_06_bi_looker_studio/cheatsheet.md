# 📋 Looker Studio Cheatsheet

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
