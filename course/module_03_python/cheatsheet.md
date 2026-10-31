# 📋 Pandas Cheatsheet

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
