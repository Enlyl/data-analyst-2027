# 📊 Data Analyst 2027: Интерактивный курс в эпоху искусственного интеллекта

> **Комплексная программа подготовки Data Analyst нового поколения.**  
> Спроектирована на базе передовых педагогических практик (октябрь 2026): *Spaced Retrieval, Interleaving, Cognitive Load Theory, Learning by Prompting, Mastery-Based Progression*.

---

## 🧭 Архитектура программы

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ ФАЗА 0: ОНБОРДИНГ И АНАЛИТИЧЕСКОЕ МЫШЛЕНИЕ                                   │
│ └─ Module 00: Профессия 2027, Colab, GitHub, CRISP-DM, Problem Framing      │
├──────────────────────────────────────────────────────────────────────────────┤
│ ФАЗА 1: КЛАССИЧЕСКИЙ ХАРД-ФУНДАМЕНТ                                          │
│ ├─ Module 01: Excel / Google Sheets (Формулы, XLOOKUP, Pivot, AI Copilot)    │
│ ├─ Module 02: SQL Master (SELECT -> CTE -> Window Functions -> Text-to-SQL)  │
│ ├─ Module 03: Python & Pandas (Без заучивания синтаксиса, ТЗ для AI, Review)  │
│ ├─ Module 04: Data Cleaning (Пропуски, аномалии, дубли, валидационные пайплайны)│
│ └─ Module 05: Статистика & Гипотезы (ЦПТ, t-test, Mann-Whitney, OLS-регрессия) │
├──────────────────────────────────────────────────────────────────────────────┤
│ ФАЗА 2: ВИЗУАЛИЗАЦИЯ И ЭКСПЕРИМЕНТЫ                                         │
│ ├─ Module 06: Looker Studio (Вычисляемые поля, Blending, UI/UX дашбордов)    │
│ └─ Module 07: A/B-тестирование (Sample Size, MDE, SRM, Peeking Problem)      │
├──────────────────────────────────────────────────────────────────────────────┤
│ ФАЗА 3: AI-СТЕК АНАЛИТИКА 2027 (KEY DIFFERENTIATOR)                         │
│ ├─ Module 08: Prompt Engineering для аналитики (RTCE, CoT, Few-Shot)        │
│ ├─ Module 09: Ежедневный AI-воркфлоу (Cursor, Copilot, Zero Hallucination)   │
│ ├─ Module 10: LLM API & Неструктурированные данные (Sentiment, NER, Pydantic)│
│ ├─ Module 11: RAG & Векторные БД (ChromaDB, Semantic Search, Smart BI Chat) │
│ └─ Module 12: AI-агенты & LLM Evaluation (ReAct, LangChain, Ragas, Faithfulness)│
├──────────────────────────────────────────────────────────────────────────────┤
│ ФАЗА 4: SOFT SKILLS И БИЗНЕС (ГЛАВНЫЙ ЗАЩИТНИК ОТ АВТОМАТИЗАЦИИ)             │
│ └─ Module 13: Data Storytelling, Пирамида Минто, Юнит-экономика (LTV/CAC)   │
├──────────────────────────────────────────────────────────────────────────────┤
│ ФАЗА 5: ПОРТФОЛИО-ПРОЕКТЫ НА РЕАЛЬНЫХ ДАННЫХ                                │
│ ├─ Module 14: Project 1 — E-Commerce 360° (SQL витрина, RFM, Looker Studio) │
│ ├─ Module 15: Project 2 — SaaS Product Analytics & A/B-test (Churn, Uplift) │
│ └─ Module 16: Project 3 — AI-Driven Analytical Pipeline (LLM API + RAG)     │
├──────────────────────────────────────────────────────────────────────────────┤
│ ФАЗА 6: ТРУДОУСТРОЙСТВО И КАРЬЕРА                                            │
│ └─ Module 17: Резюме стандарта 2027, GitHub портфолио, Собеседования с AI    │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 📦 Данные курса (`datasets/`)
- `ecommerce.db` — Полноценная реляционная SQLite база интернет-магазина (заказы, клиенты, товары, чеки).
- `raw/saas_users.csv` — Датасет продуктовой аналитики B2B SaaS (активность, тарифы, Churn, NPS).
- `raw/customer_reviews.csv` — Неструктурированные отзывы пользователей для LLM API и RAG.
- `raw/ab_test_checkout.csv` — Данные эксперимента чекаута на 10 000 наблюдений.
- `processed/looker_studio_source.csv` — Готовая витрина для визуализации в Looker Studio.

---

## 🚀 Как проходить курс
1. Открывайте ноутбуки `.ipynb` локально в Jupyter / VS Code или загружайте в [Google Colab](https://colab.research.google.com).
2. Запускайте ячейки кода последовательно, выполняя интерактивные упражнения.
3. В конце каждого модуля проходите самопроверку `quiz.md` для закрепления через активное воспроизведение (*Active Recall*).
4. Готовые 3 проекта из модулей 14, 15, 16 публикуйте в личный GitHub по гайду из модуля 17.
