# 🎯 Вопросы и кейсы технических собеседований 2027

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
