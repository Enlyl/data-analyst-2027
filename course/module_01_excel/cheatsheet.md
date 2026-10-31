# 📋 Excel & Sheets Cheatsheet

| Задача | Формула |
|---|---|
| Поиск значения | `=XLOOKUP(F2, A:A, C:C, "Не найдено")` |
| Сумма с условием | `=SUMIFS(D:D, A:A, "Completed", B:B, ">="&DATE(2026,1,1))` |
| Количество уникальных | `=COUNTA(UNIQUE(FILTER(B:B, A:A="Completed")))` |
| Безопасный расчет | `=IFERROR(A2 / B2, 0)` |
| Склейка текста | `=TEXTJOIN(" - ", TRUE, A2, B2)` |
