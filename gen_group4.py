import os
import sys
sys.path.append(r"d:\vibe_app\main_data_analytics")
from notebook_helper import create_notebook

BASE = r"d:\vibe_app\main_data_analytics\course"

# ==========================================
# MODULE 09: AI IN DAILY WORK
# ==========================================
m09 = os.path.join(BASE, "module_09_ai_tools_daily")
os.makedirs(m09, exist_ok=True)

with open(os.path.join(m09, "README.md"), "w", encoding="utf-8") as f:
    f.write("""# 🛠️ Модуль 9: AI в ежедневной работе аналитика (Cursor, Copilot, ChatGPT)

## 📌 О модуле
Разница между джуном и мидлом в 2027 году: джун пишет скрипт 3 дня, а специалист новой формации решает ту же задачу за 2 часа с помощью AI-инструментов, гарантируя нулевой процент галлюцинаций.

## 🎯 Learning Outcomes
- **Apply**: Использование Cursor IDE и GitHub Copilot для парного программирования.
- **Analyze**: Code Interpreter (Advanced Data Analysis) для быстрого разведочного анализа (EDA).
- **Evaluate**: 5-уровневый фреймворк валидации ответов ИИ: от синтаксиса до краевых бизнес-кейсов.

## 📚 Уроки
1. `lesson_01_cursor_vs_copilot_workflows.ipynb` — Настройка рабочего места: Cursor, Copilot, индексация кодовой базы.
2. `lesson_02_claude_chatgpt_data_interpreter.ipynb` — Работа с веб-ассистентами (Claude 3.7 / ChatGPT): быстрый EDA, генерация гипотез.
3. `lesson_03_ai_validation_framework_hallucinations.ipynb` — Архитектура валидации: как защитить бизнес от галлюцинаций ИИ.
4. `quiz.md` — Тест для самопроверки.
""")

create_notebook(os.path.join(m09, "lesson_01_cursor_vs_copilot_workflows.ipynb"), [
    ("markdown", """# Модуль 9. Урок 1: Воркфлоу с Cursor и Copilot

### Три режима работы с AI в редакторе:
1. **Tab Autocomplete**: Автодополнение следующей строки или блока кода.
2. **Inline Edit (Cmd+K / Ctrl+K)**: Рефакторинг выделенного участка («перепиши через векторизованную операцию Pandas»).
3. **Project Chat (Cmd+L / Ctrl+L)**: Запрос с контекстом всего репозитория («найди, где в проекте рассчитывается LTV и добавь фильтр по статусу»).
""")
])

create_notebook(os.path.join(m09, "lesson_02_claude_chatgpt_data_interpreter.ipynb"), [
    ("markdown", """# Модуль 9. Урок 2: Разведочный анализ (EDA) в Code Interpreter

Как за 10 минут получить предварительную картину любого неизвестного датасета с помощью AI:
"""),
    ("code", """# Демонстрация скрипта автоматического EDA, который генерируют современные Code Interpreter
import pandas as pd

df = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\saas_users.csv")

def automated_eda_summary(data: pd.DataFrame):
    print("=== АВТОМАТИЧЕСКАЯ СВОДКА ДАТАСЕТА ===")
    print(f"Строк: {data.shape[0]}, Колонок: {data.shape[1]}")
    print("\\nПропуски в данных:")
    print(data.isnull().sum()[data.isnull().sum() > 0])
    print("\\nЧисловые показатели (Ключевые квантили):")
    print(data.describe().T[['mean', '50%', 'std', 'min', 'max']])

automated_eda_summary(df)
""")
])

create_notebook(os.path.join(m09, "lesson_03_ai_validation_framework_hallucinations.ipynb"), [
    ("markdown", """# Модуль 9. Урок 3: Фреймворк валидации ИИ (Zero Hallucination)

```
             [Входной ответ от LLM]
                        │
    1. Синтаксическая валидация (Код запускается?)
                        │
    2. Проверка размерностей (shape, dtypes, nulls)
                        │
    3. Бизнес-инварианты (Выручка >= 0, CR <= 100%)
                        │
    4. Сверка с контрольными бенчмарками
                        │
             [Одобрено в прод]
```
""")
])

with open(os.path.join(m09, "quiz.md"), "w", encoding="utf-8") as f:
    f.write("""# 🧠 Quiz: Самопроверка по Модулю 9 (AI в ежедневной работе)

### Вопрос 1
Что делать, если ChatGPT написал сложный SQL-запрос, который выполнился без ошибок?
- [ ] Сразу отправить результаты финансовому директору
- [x] Провести ручную валидацию: проверить результат на известных тестовых пользователях, проверить отсутствие задвоения строк при JOIN и соответствие бизнес-логике
- [ ] Закрыть проект

### Вопрос 2
Что такое бизнес-инвариант при валидации кода?
- [ ] Название корпоративной почты
- [x] Фундаментальное правило предметной области, которое ни при каких обстоятельствах не может быть нарушено (например: отток не может быть отрицательным, конверсия не может превышать 100%)
- [ ] Количество пробелов в строке
""")

print("Module 09 created successfully.")

# ==========================================
# MODULE 10: LLM API & UNSTRUCTURED DATA
# ==========================================
m10 = os.path.join(BASE, "module_10_llm_api")
os.makedirs(m10, exist_ok=True)

with open(os.path.join(m10, "README.md"), "w", encoding="utf-8") as f:
    f.write("""# 🧠 Модуль 10: Работа с LLM API и анализ неструктурированных данных

## 📌 О модуле
До 80% данных компании — неструктурированные: отзывы клиентов, переписки в саппорте, тикеты, расшифровки звонков, договоры. Классический SQL бессилен перед текстом. Аналитик 2027 года подключает LLM API (OpenAI, Anthropic, Gemini, локальные модели), чтобы извлекать сущности, оценивать сентимент и формировать структурированные витрины.

## 🎯 Learning Outcomes
- **Understand**: Принципы вызова LLM API (temperature, max_tokens, system vs user messages).
- **Apply**: Автоматическая разметка текста: Sentiment Analysis, определение тем тикетов, извлечение именованных сущностей (NER).
- **Create**: Использование Structured Outputs (Pydantic / JSON Mode) для надежного получения гарантированной схемы JSON без сбоев.
- **Analyze**: Расчет стоимости API (Token Economics), оптимизация батчами и кэширование.

## 📚 Уроки
1. `lesson_01_calling_llm_apis_python.ipynb` — Подключение и первые вызовы современных LLM API из Python.
2. `lesson_02_parsing_unstructured_data.ipynb` — Анализ реального датасета отзывов клиентов (`customer_reviews.csv`).
3. `lesson_03_structured_outputs_pydantic_json.ipynb` — Гарантированный JSON и валидация через Pydantic.
4. `lesson_04_batch_processing_and_costs.ipynb` — Пакетная обработка 10 000 строк: Rate Limits, ретраи, контроль бюджета.
5. `quiz.md` — Тест для закрепления.
6. `cheatsheet.md` — Шаблоны Python-кода для работы с LLM API.
""")

create_notebook(os.path.join(m10, "lesson_01_calling_llm_apis_python.ipynb"), [
    ("markdown", """# Модуль 10. Урок 1: Архитектура вызова LLM API

Базовый шаблон для аналитического запроса к API (универсальный интерфейс):
"""),
    ("code", """# Демонстрационный мок вызова LLM API для анализа тональности
def mock_llm_sentiment_analyzer(text: str) -> dict:
    \"\"\"Имитация вызова современной LLM через API\"\"\"
    text_lower = text.lower()
    if any(w in text_lower for w in ['отличный', 'прекрасно', 'супер', 'быстро', 'loving', 'intuitive']):
        sentiment = 'Positive'
        score = 0.95
    elif any(w in text_lower for w in ['ужасно', 'баги', 'списали', 'тормозит', 'crashes', 'верните']):
        sentiment = 'Negative'
        score = 0.10
    else:
        sentiment = 'Neutral'
        score = 0.50
        
    return {
        'sentiment': sentiment,
        'confidence': score,
        'tokens_used': len(text.split()) * 2
    }

sample_review = "Ужасная доставка! Курьер опоздал на 4 часа, а приложение крашится."
response = mock_llm_sentiment_analyzer(sample_review)
print("Входной отзыв:", sample_review)
print("Результат LLM API:", response)
""")
])

create_notebook(os.path.join(m10, "lesson_02_parsing_unstructured_data.ipynb"), [
    ("markdown", """# Модуль 10. Урок 2: Разметка неструктурированных данных на масштабе

Применим логику извлечения инсайтов на датасете реальных отзывов `customer_reviews.csv`:
"""),
    ("code", """import pandas as pd

# Загружаем реальный датасет отзывов курса
reviews_df = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\customer_reviews.csv")

print("Примеры отзывов из базы:")
for idx, row in reviews_df.head(3).iterrows():
    print(f"[{row['platform']} | Рейтинг: {row['rating']}] {row['text']}")

# Агрегация по платформам и тональности
summary = reviews_df.groupby(['platform', 'sentiment_label']).size().unstack(fill_value=0)
print("\\nРаспределение тональности по каналам обратной связи:")
print(summary)
""")
])

create_notebook(os.path.join(m10, "lesson_03_structured_outputs_pydantic_json.ipynb"), [
    ("markdown", """# Модуль 10. Урок 3: Structured Outputs и Pydantic

Главное требование к LLM в аналитическом пайплайне — **строгий JSON без лишнего сопроводительного текста**.

Пример схемы Pydantic:
```python
from pydantic import BaseModel, Field
from typing import List, Literal

class CustomerFeedbackAnalysis(BaseModel):
    sentiment: Literal['Positive', 'Negative', 'Neutral']
    urgency_level: Literal['Low', 'Medium', 'Critical']
    identified_issues: List[str] = Field(description="Список конкретных проблем, например: доставка, оплата, интерфейс")
    estimated_satisfaction_score: int = Field(ge=1, le=5)
```
""")
])

create_notebook(os.path.join(m10, "lesson_04_batch_processing_and_costs.ipynb"), [
    ("markdown", """# Модуль 10. Урок 4: Экономика токенов (Token Economics)

Расчет стоимости обогащения датасета через LLM API:
- Модель: \$0.15 за 1M входных токенов, \$0.60 за 1M выходных токенов.
- 10 000 отзывов по 100 токенов = 1 000 000 входных токенов (\$0.15).
- Выходные JSON (50 токенов) = 500 000 выходных токенов (\$0.30).
- Итого: **\$0.45 за полную классификацию 10 000 отзывов!** (В 2021 году на это уходили недели разметчиков).
""")
])

with open(os.path.join(m10, "quiz.md"), "w", encoding="utf-8") as f:
    f.write("""# 🧠 Quiz: Самопроверка по Модулю 10 (LLM API)

### Вопрос 1
Зачем в аналитических пайплайнах использовать параметр Structured Outputs (JSON Schema / Pydantic)?
- [ ] Чтобы код работал только по выходным
- [x] Чтобы модель гарантированно вернула валидный JSON заданной структуры, который можно без ошибок распарсить в DataFrame
- [ ] Чтобы сэкономить оперативную память

### Вопрос 2
Какой параметр температуры (temperature) следует выставлять для задач извлечения данных и классификации?
- [ ] temperature = 1.8 (максимальная креативность)
- [x] temperature = 0.0 (детерминированный, максимально точный и воспроизводимый результат)
- [ ] temperature = -1.0
""")

print("Module 10 created successfully.")

# ==========================================
# MODULE 11: RAG & VECTOR DATABASES
# ==========================================
m11 = os.path.join(BASE, "module_11_rag_vector_db")
os.makedirs(m11, exist_ok=True)

with open(os.path.join(m11, "README.md"), "w", encoding="utf-8") as f:
    f.write("""# 🔍 Модуль 11: RAG и векторные базы данных — Умные BI-ассистенты

## 📌 О модуле
RAG (Retrieval-Augmented Generation) — архитектура, которая связывает генеративные возможности LLM с закрытыми корпоративными данными компании (вики, документация по метрикам, схемы БД, отчеты прошлых лет). Это основа интеллектуальных чатов в современном BI.

## 🎯 Learning Outcomes
- **Understand**: Векторные эмбеддинги (Embeddings), семантическое пространство, косинусная близость (Cosine Similarity).
- **Apply**: Развертывание локальной векторной БД ChromaDB, индексация корпоративных документов.
- **Create**: Рабочий RAG-пайплайн: вопрос аналитика -> поиск релевантных кусков документации -> формирование промпта -> ответ с источниками.
- **Analyze**: Text-to-SQL с RAG-обогащением (модель получает точную схему таблиц из базы знаний).

## 📚 Уроки
1. `lesson_01_embeddings_and_vector_space.ipynb` — Что такое эмбеддинги: перевод текста в векторы чисел, расчет сходства.
2. `lesson_02_vector_databases_chromadb.ipynb` — Практика с ChromaDB: коллекции, метаданные, семантический поиск.
3. `lesson_03_building_rag_pipeline_analyst.ipynb` — Сборка сквозного RAG-пайплайна по регламентам компании.
4. `lesson_04_text_to_sql_rag_assistant.ipynb` — Архитектура "Умного BI-ассистента": Text-to-SQL по метаданным.
5. `quiz.md` — Тест для самопроверки.
""")

create_notebook(os.path.join(m11, "lesson_01_embeddings_and_vector_space.ipynb"), [
    ("markdown", """# Модуль 11. Урок 1: Векторные эмбеддинги и семантическое сходство

Эмбеддинг — это список чисел (вектор), отражающий смысл фразы. Похожие по смыслу фразы находятся близко в многомерном пространстве:
"""),
    ("code", """import numpy as np

# Имитация векторов эмбеддингов для демонстрации косинусной близости
# Векторы размерности 3 для наглядности
vec_retention = np.array([0.9, 0.8, 0.1])
vec_churn = np.array([0.85, 0.75, 0.15])      # Очень близко по смыслу к retention
vec_pizza = np.array([0.05, 0.1, 0.95])        # Вообще про другое

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

sim_metrics = cosine_similarity(vec_retention, vec_churn)
sim_unrelated = cosine_similarity(vec_retention, vec_pizza)

print(f"Сходство (Retention vs Churn) : {sim_metrics:.4f} (Высокое семантическое сродство!)")
print(f"Сходство (Retention vs Pizza) : {sim_unrelated:.4f} (Не связаны)")
""")
])

create_notebook(os.path.join(m11, "lesson_02_vector_databases_chromadb.ipynb"), [
    ("markdown", """# Модуль 11. Урок 2: Векторная база ChromaDB для базы знаний аналитика

Индексируем словарь корпоративных метрик компании:
"""),
    ("code", """# Демонстрация логики индексации в базе знаний
metrics_knowledge_base = [
    {"id": "doc_1", "text": "LTV (Lifetime Value) — совокупная чистая прибыль от клиента за всё время работы. Формула: ARPU * Lifetime."},
    {"id": "doc_2", "text": "Churn Rate — процент клиентов, отказавшихся от подписки в отчетном периоде. Формула: Ушедшие / Активные на начало."},
    {"id": "doc_3", "text": "CAC (Customer Acquisition Cost) — стоимость привлечения платящего клиента: Маркетинг_расходы / Число_новых_клиентов."}
]

print("База знаний метрик готова к векторному поиску:")
for doc in metrics_knowledge_base:
    print(f"- [{doc['id']}]: {doc['text'][:60]}...")
""")
])

create_notebook(os.path.join(m11, "lesson_03_building_rag_pipeline_analyst.ipynb"), [
    ("markdown", """# Модуль 11. Урок 3: Сквозной пайплайн RAG
```
[Вопрос пользователя: "Как мы считаем отток?"]
                      │
           (Поиск в Векторной БД)
                      │
   [Найден контекст: doc_2 Churn Rate]
                      │
       (Промпт: "Ответь на основе контекста")
                      │
[Итоговый ответ: "Отток считается как отношение... Источник: doc_2"]
```
""")
])

create_notebook(os.path.join(m11, "lesson_04_text_to_sql_rag_assistant.ipynb"), [
    ("markdown", """# Модуль 11. Урок 4: Архитектура Text-to-SQL с RAG

Когда база данных содержит 500+ таблиц, передать всю схему в промпт невозможно (превысит лимит контекста).
Решение: **RAG по схеме БД**:
1. Индексируем описания таблиц в векторной базе.
2. По запросу пользователя («Сколько мы продали смартфонов в Москве?») находим 2-3 релевантные таблицы (`orders`, `products`, `customers`).
3. Передаем в LLM только схемы этих 3 таблиц.
4. Получаем точный и дешевый SQL-запрос!
""")
])

with open(os.path.join(m11, "quiz.md"), "w", encoding="utf-8") as f:
    f.write("""# 🧠 Quiz: Самопроверка по Модулю 11 (RAG и векторные БД)

### Вопрос 1
В чем главная роль Retrieval-Augmented Generation (RAG)?
- [ ] Обучение нейросети с нуля на суперкомпьютере
- [x] Обогащение запроса к LLM актуальными релевантными фрагментами из внешних документов или базы данных перед генерацией ответа
- [ ] Перевод текста на китайский язык

### Вопрос 2
Какая мера чаще всего используется для оценки близости двух векторов эмбеддингов?
- [ ] Евклидово расстояние
- [x] Косинусное сходство (Cosine Similarity)
- [ ] Дисперсия выборки
""")

print("Module 11 created successfully.")

# ==========================================
# MODULE 12: AI AGENTS & WORKFLOWS
# ==========================================
m12 = os.path.join(BASE, "module_12_ai_agents")
os.makedirs(m12, exist_ok=True)

with open(os.path.join(m12, "README.md"), "w", encoding="utf-8") as f:
    f.write("""# 🤖 Модуль 12: AI-агенты (Agentic Workflows) и мониторинг качества LLM

## 📌 О модуле
Высший пилотаж специалиста 2027 года: создание автономных аналитических цепочек (AI Agents), способных самостоятельно планировать шаги, запускать код, обращаться к базам данных и проверять результаты своего труда.

## 🎯 Learning Outcomes
- **Understand**: Фреймворк ReAct (Reasoning + Acting), концепцию инструментов (Tools) и памяти агента.
- **Apply**: Инструменты LangChain / LlamaIndex для автоматизации многоэтапного сбора и подготовки данных.
- **Evaluate**: LLM Evaluation — метрики оценки качества генерации (Faithfulness, Answer Relevance, Hallucination Rate).
- **Create**: Автономный аналитический агент, получающий сырую задачу и генерирующий проверенный отчет.

## 📚 Уроки
1. `lesson_01_agentic_workflows_concept.ipynb` — Концепция автономных агентов: ReAct, инструменты, циклы исполнения.
2. `lesson_02_langchain_llamaindex_for_analytics.ipynb` — LangChain и LlamaIndex: агент с доступом к SQLite и Python REPL.
3. `lesson_03_automated_data_collection_agent.ipynb` — Автономный пайплайн сбора, трансформации и валидации данных.
4. `lesson_04_llm_evaluation_and_monitoring.ipynb` — LLM Evaluation: фреймворки оценки надежности (Ragas, DeepEval).
5. `quiz.md` — Тест для самопроверки.
""")

create_notebook(os.path.join(m12, "lesson_01_agentic_workflows_concept.ipynb"), [
    ("markdown", """# Модуль 12. Урок 1: Архитектура аналитического агента (ReAct)

Цикл ReAct:
```
[Цель: "Выясни причину просадки выручки в октябре"]
                    │
            ┌───────┴───────┐
            │   Thought     │ (Мне нужно посмотреть заказы за октябрь)
            ├───────────────┤
            │   Action      │ (Вызов инструмента SQL_Query)
            ├───────────────┤
            │  Observation  │ (Выручка упала на 15%, заказы электроники упали на 40%)
            ├───────────────┤
            │   Thought     │ (Почему упала электроника? Проверю остатки на складе)
            ├───────────────┤
            │   Action      │ (Вызов инструмента Check_Inventory)
            ├───────────────┤
            │  Observation  │ (Топ-3 смартфона закончились на складе 5 октября)
            └───────┬───────┘
                    │
        [Final Answer бизнесу]
```
""")
])

create_notebook(os.path.join(m12, "lesson_02_langchain_llamaindex_for_analytics.ipynb"), [
    ("markdown", """# Модуль 12. Урок 2: Агент со встроенными инструментами на Python
"""),
    ("code", """# Демонстрация архитектуры агента с Tool Execution
class SimpleAnalyticsAgent:
    def __init__(self):
        self.tools = {
            'sql_query': self._mock_sql,
            'calc_ratio': lambda a, b: a / b if b != 0 else 0
        }
        
    def _mock_sql(self, query: str):
        return {"status": "success", "rows_returned": 150, "sample_metric": 420000}
        
    def execute_step(self, tool_name: str, **kwargs):
        if tool_name in self.tools:
            return self.tools[tool_name](**kwargs)
        raise ValueError(f"Unknown tool: {tool_name}")

agent = SimpleAnalyticsAgent()
step_res = agent.execute_step('sql_query', query="SELECT SUM(amount) FROM orders")
print("Результат шага агента:", step_res)
""")
])

create_notebook(os.path.join(m12, "lesson_03_automated_data_collection_agent.ipynb"), [
    ("markdown", """# Модуль 12. Урок 3: Автоматический пайплайн агента по сбору данных

Агент выполняет регулярный мониторинг:
1. Забирает свежие выгрузки из источников.
2. Прогоняет тесты качества данных.
3. Формирует саммари с главными отклонениями и отправляет алерт в Telegram/Slack.
""")
])

create_notebook(os.path.join(m12, "lesson_04_llm_evaluation_and_monitoring.ipynb"), [
    ("markdown", """# Модуль 12. Урок 4: LLM Evaluation (Оценка качества работы нейросетей)

В вакансиях Middle/Senior 2027 года стандартное требование — **LLM Evaluation**.

Ключевые метрики:
1. **Faithfulness (Верность фактам)**: Содержит ли ответ утверждения, которых не было в предоставленных данных? (Детектор галлюцинаций).
2. **Answer Relevance (Релевантность)**: Отвечает ли модель именно на заданный вопрос бизнеса?
3. **Context Recall (Полнота контекста)**: Нашел ли поисковый механизм все нужные таблицы?
""")
])

with open(os.path.join(m12, "quiz.md"), "w", encoding="utf-8") as f:
    f.write("""# 🧠 Quiz: Самопроверка по Модулю 12 (AI-агенты)

### Вопрос 1
Что отличает AI-агента от простого одиночного вызова LLM?
- [ ] Агент работает только на серверах Linux
- [x] Агент обладает циклом ReAct (рассуждение -> выбор инструмента -> получение результата -> корректировка плана) и может вызывать внешние функции (SQL, Python, API)
- [ ] Агент стоит дешевле

### Вопрос 2
Что оценивает метрика Faithfulness в фреймворках LLM Evaluation (Ragas, DeepEval)?
- [ ] Скорость печати ответа
- [x] Отсутствие галлюцинаций — проверяет, что каждый факт в сгенерированном ответе строго подтверждается переданным контекстом
- [ ] Количество грамматических ошибок
""")

print("Module 12 created successfully.")
