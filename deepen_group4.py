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

create_notebook(os.path.join(m09, "lesson_01_cursor_vs_copilot_workflows.ipynb"), [
    ("markdown", """# 🛠️ Модуль 9. Урок 1: AI-ассистенты в редакторе: Cursor IDE, Copilot и `.cursorrules`

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_09_ai_tools_daily/lesson_01_cursor_vs_copilot_workflows.ipynb)

---

## 1. Конфигурация аналитического проекта через `.cursorrules`

В современных командах аналитики не повторяют одни и те же правила в каждом чате.
В корне проекта создается файл `.cursorrules` (или системный промпт проекта):

```markdown
# Corporate Data Analytics Guidelines (2027)
- Язык общения: Русский. Названия переменных, функций и колонок: Английский (snake_case).
- СУБД: PostgreSQL 16. Всегда фильтровать `status = 'Completed'` при расчете выручки.
- Векторизация: Никогда не использовать циклы for для строк DataFrame.
- Защита от деления на ноль: Всегда использовать `NULLIF(denominator, 0)` в SQL и `div()` с `fill_value=0` в Pandas.
- Формат дат: ISO-8601 (YYYY-MM-DD).
```
""")
])

# Lesson 2
create_notebook(os.path.join(m09, "lesson_02_claude_chatgpt_data_interpreter.ipynb"), [
    ("markdown", """# ⚡ Модуль 9. Урок 2: Разведочный анализ (EDA) в Claude Code Interpreter за 10 минут

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_09_ai_tools_daily/lesson_02_claude_chatgpt_data_interpreter.ipynb)

---

## 1. Автоматический аудит нового датасета через AI
"""),
    ("code", """import pandas as pd

saas = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\saas_users.csv")

def run_ai_eda(df: pd.DataFrame):
    print("=== АВТОМАТИЧЕСКИЙ ПРОФАЙЛИНГ ДАТАСЕТА ===")
    print(f"Размер: {df.shape[0]} строк x {df.shape[1]} колонок")
    
    # 1. Проверка уникальности
    dups = df.duplicated().sum()
    print(f"Дубликатов строк: {dups}")
    
    # 2. Пропуски
    nulls = df.isnull().sum()
    print("\\nКолонки с пропусками:")
    print(nulls[nulls > 0])
    
    # 3. Числовые распределения
    print("\\nСводка по числовым метрикам:")
    print(df[['mrr', 'active_seats', 'nps_score', 'feature_a_usage']].describe().round(1))

run_ai_eda(saas)
""")
])

# Lesson 3
create_notebook(os.path.join(m09, "lesson_03_ai_validation_framework_hallucinations.ipynb"), [
    ("markdown", """# 🛡️ Модуль 9. Урок 3: 5-уровневый фреймворк защиты от галлюцинаций ИИ

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_09_ai_tools_daily/lesson_03_ai_validation_framework_hallucinations.ipynb)

---

## 1. Архитектура верификации кода AI (Zero Hallucination Protocol)

```
[1. Синтаксический уровень]   ─── Код выполняется без NameError, SyntaxError?
             │
[2. Размерность и типы]       ─── Не схлопнулись ли строки? Типы int/float/datetime корректны?
             │
[3. Бизнес-инварианты]        ─── Выручка >= 0? Конверсия <= 100%? Отток не отрицательный?
             │
[4. Сверка с бенчмарком]      ─── Сходится ли общая сумма выручки с официальным биллингом?
             │
[5. Краевые случаи (Edge)]    ─── Что произойдет при пустой таблице или делении на ноль?
```
""")
])

# Module 09 Quiz
with open(os.path.join(m09, "quiz.md"), "w", encoding="utf-8") as f:
    f.write("""# 🧠 Quiz: Самопроверка по Модулю 9 (AI в ежедневной работе)

---

### Вопрос 1
Зачем в проектах аналитики используется файл `.cursorrules`?
- [ ] Для ускорения интернета.
- [x] Для автоматической передачи AI-ассистенту корпоративных стандартов кода, схемы баз данных и бизнес-правил компании.
- [ ] Для компиляции Python в бинарный файл.
*Объяснение*: Файл `.cursorrules` автоматически подмешивается в системный контекст каждого запроса в IDE.

---

### Вопрос 2
Что такое проверка бизнес-инвариантов при аудите кода нейросети?
- [ ] Проверка орфографии комментариев.
- [x] Проверка фундаментальных ограничений предметной области (например: сумма заказов не может быть отрицательной, а LTV не может быть ниже нуля).
- [ ] Измерение скорости процессора.
*Объяснение*: Если синтаксически корректный код от ИИ выдал отрицательный отток или конверсию 140%, нарушен бизнес-инвариант.

---

### Вопрос 3
Какой инструмент лучше всего подходит для мгновенного разведочного анализа (EDA) сырого CSV-файла?
- [ ] Ручной ввод данных в калькулятор.
- [x] Advanced Data Analysis / Code Interpreter (встроенный запуск Python с визуализацией в реальном времени).
- [ ] Отрисовка графиков на бумаге.
*Объяснение*: Code Interpreter выполняет код в изолированной песочнице, строя графики и считая квантили за секунды.
""")

print("Module 09 deepened successfully.")

# ==========================================
# MODULE 10: LLM API & UNSTRUCTURED DATA
# ==========================================
m10 = os.path.join(BASE, "module_10_llm_api")
os.makedirs(m10, exist_ok=True)

create_notebook(os.path.join(m10, "lesson_01_calling_llm_apis_python.ipynb"), [
    ("markdown", """# 🔌 Модуль 10. Урок 1: Подключение и программный вызов LLM API из Python

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_10_llm_api/lesson_01_calling_llm_apis_python.ipynb)

---

## 1. Универсальный интерфейс взаимодействия с LLM API

Современные API (OpenAI, Anthropic, Gemini, DeepSeek) используют стандартизированный JSON-интерфейс:
- `messages`: массив объектов с ролями `system`, `user`, `assistant`.
- `temperature`: степень детерминированности ($0.0$ — максимальная точность для аналитики, $1.0$ — креативность).
- `response_format`: принудительный возврат JSON объекта.
""")
])

# Lesson 2
create_notebook(os.path.join(m10, "lesson_02_parsing_unstructured_data.ipynb"), [
    ("markdown", """# 📑 Модуль 10. Урок 2: Разметка неструктурированных отзывов и тикетов саппорта

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_10_llm_api/lesson_02_parsing_unstructured_data.ipynb)

---

## 1. Реальный кейс: Автоматический аудит 800 жалоб клиентов e-commerce

Работаем с реальным датасетом отзывов `customer_reviews.csv`.
Извлекаем темы жалоб и тональность без ручного чтения.
"""),
    ("code", """import pandas as pd

reviews = pd.read_csv(r"d:\\vibe_app\\main_data_analytics\\course\\datasets\\raw\\customer_reviews.csv")

# Функция симуляции работы LLM по извлечению сущностей и тематик
def analyze_review_with_llm(text: str) -> dict:
    t = text.lower()
    topics = []
    if any(k in t for k in ['курьер', 'доставка', 'опоздал', 'доставили']):
        topics.append('Логистика и доставка')
    if any(k in t for k in ['списали', 'деньги', 'вернуть', 'цена', 'подписку']):
        topics.append('Оплата и биллинг')
    if any(k in t for k in ['баги', 'крашится', 'тормозит', 'crashes', 'не работает']):
        topics.append('Баги приложения')
    if any(k in t for k in ['поддержка', 'чат', 'саппорт', 'service']):
        topics.append('Качество саппорта')
        
    return {
        'topics': topics if topics else ['Прочее'],
        'has_critical_issue': int(any(k in t for k in ['верните', 'претензию', 'списали', 'crashes']))
    }

# Применяем анализ к базе
results = reviews['text'].apply(analyze_review_with_llm)
reviews['topics'] = [r['topics'] for r in results]
reviews['is_critical'] = [r['has_critical_issue'] for r in results]

# Сводный отчет для операционного директора
exploded = reviews.explode('topics')
summary = exploded.groupby('topics').agg(
    total_reviews=('review_id', 'count'),
    critical_cases=('is_critical', 'sum')
).sort_values(by='critical_cases', ascending=False)

print("=== РЕЗУЛЬТАТ АВТОМАТИЧЕСКОЙ КЛАССИФИКАЦИИ ЖАЛОБ ===")
print(summary)
""")
])

# Lesson 3
create_notebook(os.path.join(m10, "lesson_03_structured_outputs_pydantic_json.ipynb"), [
    ("markdown", """# 📦 Модуль 10. Урок 3: Structured Outputs и валидация через Pydantic

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_10_llm_api/lesson_03_structured_outputs_pydantic_json.ipynb)

---

## 1. Схема Pydantic для гарантированной типизации

Никаких неструктурированных ответов от LLM в проде. Только жестко валидированный JSON:
"""),
    ("code", """from pydantic import BaseModel, Field
from typing import List, Literal

class FeedbackExtractionSchema(BaseModel):
    sentiment: Literal['Positive', 'Negative', 'Neutral']
    urgency_level: Literal['Low', 'Medium', 'High', 'Critical']
    identified_categories: List[str]
    satisfaction_score: int = Field(ge=1, le=5)

# Демонстрация валидации
valid_sample = {
    "sentiment": "Negative",
    "urgency_level": "Critical",
    "identified_categories": ["Billing", "Mobile App"],
    "satisfaction_score": 1
}

validated_obj = FeedbackExtractionSchema(**valid_sample)
print(" Схема валидна! Объект Pydantic готов к загрузке в БД:")
print(validated_obj.model_dump_json(indent=2))
""")
])

# Lesson 4
create_notebook(os.path.join(m10, "lesson_04_batch_processing_and_costs.ipynb"), [
    ("markdown", """# 💰 Модуль 10. Урок 4: Экономика токенов (Token Economics) и батчевая обработка

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_10_llm_api/lesson_04_batch_processing_and_costs.ipynb)

---

## 1. Калькулятор стоимости пайплайна разметки данных
"""),
    ("code", """# Калькулятор стоимости обработки массива текстов через современные модели
def estimate_llm_cost(num_documents, avg_words_per_doc, input_price_per_m=0.15, output_price_per_m=0.60):
    # В среднем 1 слово = 1.3 токена
    input_tokens = num_documents * (avg_words_per_doc * 1.3 + 100) # +100 токенов промпта
    output_tokens = num_documents * 50 # JSON ответ около 50 токенов
    
    cost_in = (input_tokens / 1_000_000) * input_price_per_m
    cost_out = (output_tokens / 1_000_000) * output_price_per_m
    total = cost_in + cost_out
    
    print(f"Обработка {num_documents:,} документов:")
    print(f"- Входные токены : {input_tokens:,.0f} (${cost_in:.3f})")
    print(f"- Выходные токены: {output_tokens:,.0f} (${cost_out:.3f})")
    print(f"- ИТОГОВАЯ ЦЕНА  : ${total:.2f} (~{total * 95:.1f} руб)")

estimate_llm_cost(num_documents=50_000, avg_words_per_doc=40)
""")
])

# Module 10 Quiz
with open(os.path.join(m10, "quiz.md"), "w", encoding="utf-8") as f:
    f.write("""# 🧠 Quiz: Самопроверка по Модулю 10 (LLM API & Неструктурированные данные)

---

### Вопрос 1
Зачем в аналитических пайплайнах обогащения данных использовать Structured Outputs (Pydantic / JSON Mode)?
- [ ] Чтобы нейросеть писала более вежливые ответы.
- [x] Чтобы модель гарантированно вернула валидный JSON строго заданной структуры с проверкой типов полей, исключая поломку ETL-пайплайна.
- [ ] Чтобы снизить задержку сети.
*Объяснение*: Structured Outputs принудительно направляет сэмплирование токенов согласно переданной JSON-схеме.

---

### Вопрос 2
Какую температуру (`temperature`) следует указывать при вызове LLM для извлечения фактов и разметки тональности?
- [ ] 1.5 (для максимального разнообразия).
- [x] 0.0 (для максимальной детерминированности, воспроизводимости и строгого следования схеме).
- [ ] 0.8.
*Объяснение*: Для аналитических задач и классификации требуется нулевая случайность (greedy decoding).

---

### Вопрос 3
Сколько примерно стоит классификация 10 000 коротких отзывов клиентов через современные эффективные LLM (например, Gemini Flash / GPT-4o-mini)?
- [ ] Около \$500.
- [x] Менее \$1.00 (порядка 50-80 рублей).
- [ ] Более \$10 000.
*Объяснение*: Цены на легковесные модели упали до \$0.10–\$0.15 за миллион токенов, делая автоматическую разметку текста невероятно дешевой.
""")

print("Module 10 deepened successfully.")

# ==========================================
# MODULE 11: RAG & VECTOR DATABASES
# ==========================================
m11 = os.path.join(BASE, "module_11_rag_vector_db")
os.makedirs(m11, exist_ok=True)

create_notebook(os.path.join(m11, "lesson_01_embeddings_and_vector_space.ipynb"), [
    ("markdown", """# 🌐 Модуль 11. Урок 1: Векторные эмбеддинги и семантический поиск: Cosine Similarity

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_11_rag_vector_db/lesson_01_embeddings_and_vector_space.ipynb)

---

## 1. Геометрия смыслов: Как компьютер понимает синонимы

Традиционный поиск по базе ищет точное совпадение букв: `WHERE text LIKE '%отток%'`. Если пользователь спросил *«клиенты уходят»*, поиск ничего не найдет.
**Векторный эмбеддинг** преобразует текст в многомерный вектор чисел ($d = 768$ или $1536$).
Фразы со схожим смыслом имеют близкое направление векторов.

Формула косинусного сходства (Cosine Similarity):
$$\\cos(\\theta) = \\frac{\\mathbf{A} \\cdot \\mathbf{B}}{\\|\\mathbf{A}\\| \\|\\mathbf{B}\\|}$$
"""),
    ("code", """import numpy as np

# Симуляция 3-мерного пространства смыслов
# Ось 1: Продуктовые метрики, Ось 2: Негатив/Уход, Ось 3: Еда/Кухня
emb_churn = np.array([0.9, 0.8, 0.05])       # "Отток клиентов"
emb_leave = np.array([0.85, 0.82, 0.08])     # "Пользователи закрывают подписку"
emb_burger = np.array([0.02, 0.1, 0.98])     # "Чизбургер с картошкой"

def cosine_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

print(f"Сходство 'Отток' и 'Пользователи уходят': {cosine_sim(emb_churn, emb_leave):.4f} (Близкие синонимы!)")
print(f"Сходство 'Отток' и 'Чизбургер'          : {cosine_sim(emb_churn, emb_burger):.4f} (Нет семантической связи)")
""")
])

# Lesson 2
create_notebook(os.path.join(m11, "lesson_02_vector_databases_chromadb.ipynb"), [
    ("markdown", """# 🗄️ Модуль 11. Урок 2: Векторная база ChromaDB для базы знаний аналитика

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_11_rag_vector_db/lesson_02_vector_databases_chromadb.ipynb)

---

## 1. Индексация словаря корпоративных терминов и регламентов
"""),
    ("code", """# Демонстрация локальной коллекции ChromaDB в памяти
metrics_catalog = [
    {"id": "m1", "title": "LTV", "content": "Lifetime Value — общая чистая прибыль от пользователя за всю историю. Формула: ARPU * Lifetime."},
    {"id": "m2", "title": "Churn Rate", "content": "Процент ушедших клиентов за период: (Клиенты_конец - Новые) / Клиенты_начало."},
    {"id": "m3", "title": "CAC", "content": "Customer Acquisition Cost — стоимость привлечения платящего пользователя: Расходы / Новые_покупатели."},
    {"id": "m4", "title": "AOV", "content": "Average Order Value — средний чек: Общая выручка / Количество успешных заказов."}
]

print("БАЗА ЗНАНИЙ ДЛЯ ВЕКТОРНОГО ПОИСКА RAG ГОТОВА:")
for m in metrics_catalog:
    print(f"- [{m['title']}]: {m['content']}")
""")
])

# Lesson 3
create_notebook(os.path.join(m11, "lesson_03_building_rag_pipeline_analyst.ipynb"), [
    ("markdown", """# 🔄 Модуль 11. Урок 3: Сквозной пайплайн RAG (Chunking -> Retrieval -> Generation)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_11_rag_vector_db/lesson_03_building_rag_pipeline_analyst.ipynb)

---

## 1. Схема работы RAG для отчетов компании

```
[Вопрос руководителя: "Как мы рассчитываем LTV в B2B тарифах?"]
                               │
            (Семантический поиск в векторной базе)
                               │
       [Найден релевантный фрагмент регламента №42]
                               │
               (Генерация ответа в LLM)
      "Ответь на вопрос, основываясь ИСКЛЮЧИТЕЛЬНО на документе №42"
                               │
[Точный ответ без галлюцинаций с указанием источника и формулы]
```
""")
])

# Lesson 4
create_notebook(os.path.join(m11, "lesson_04_text_to_sql_rag_assistant.ipynb"), [
    ("markdown", """# 💬 Модуль 11. Урок 4: Архитектура "Умного BI-ассистента" (Text-to-SQL + RAG)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_11_rag_vector_db/lesson_04_text_to_sql_rag_assistant.ipynb)

---

## 1. Проблема больших корпоративных баз

В реальном корпоративном Data Warehouse (DWH) могут быть 1 500 таблиц и 20 000 колонок.
Их невозможно передать в промпт целиком.
**Решение — RAG по метаданным**:
1. В векторную базу индексируются описания таблиц и колонок.
2. По запросу пользователя («Покажи топ продаж ноутбуков в Казани») векторный поиск находит только таблицы `products`, `orders`, `customers`.
3. Модель получает схему только этих 3 таблиц и генерирует быстрый и точный SQL-запрос.
""")
])

# Module 11 Quiz
with open(os.path.join(m11, "quiz.md"), "w", encoding="utf-8") as f:
    f.write("""# 🧠 Quiz: Самопроверка по Модулю 11 (RAG & Векторные базы данных)

---

### Вопрос 1
В чем заключается главное преимущество архитектуры RAG перед файнтюнингом (дообучением) модели на данных компании?
- [ ] RAG работает без использования электричества.
- [x] RAG позволяет обращаться к постоянно обновляемым корпоративным документам в реальном времени без дорогостоящего переобучения нейросети и дает ссылки на точные источники.
- [ ] RAG используется только для картинок.
*Объяснение*: При изменении регламента или добавлении данных достаточно обновить индекс в векторной БД, не меняя веса модели.

---

### Вопрос 2
Что показывает косинусное сходство (Cosine Similarity) между двумя эмбеддингами?
- [ ] Разницу в количестве букв в тексте.
- [x] Косинус угла между векторами в многомерном пространстве (от 1.0 — полное совпадение смысла, до 0.0 — отсутствие семантической связи).
- [ ] Скорость загрузки страницы.
*Объяснение*: Чем ближе угол векторов к нулю (косинус к 1.0), тем ближе смысловое значение текстов.

---

### Вопрос 3
Как RAG помогает масштабировать Text-to-SQL в компании с сотнями таблиц в базе данных?
- [ ] Сжимает таблицы в zip-архив.
- [x] Динамически находит по смыслу запроса только 2-4 релевантные таблицы и передает в контекст промпта только их схемы, не перегружая лимит контекста.
- [ ] Удаляет старые таблицы из базы.
*Объяснение*: Семантический поиск по метаданным оставляет в промпте только нужные фрагменты схемы.
""")

print("Module 11 deepened successfully.")

# ==========================================
# MODULE 12: AI AGENTS & WORKFLOWS
# ==========================================
m12 = os.path.join(BASE, "module_12_ai_agents")
os.makedirs(m12, exist_ok=True)

create_notebook(os.path.join(m12, "lesson_01_agentic_workflows_concept.ipynb"), [
    ("markdown", """# 🤖 Модуль 12. Урок 1: Архитектура автономных агентов: ReAct, Tools и Память

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_12_ai_agents/lesson_01_agentic_workflows_concept.ipynb)

---

## 1. Парадигма ReAct: Reasoning + Acting

Агент — это не просто чат-бот, это программа с циклом принятия решений:
1. **Thought**: Агент анализирует текущее состояние задачи.
2. **Action**: Агент вызывает внешний инструмент (SQL-запрос, выполнение Python-кода, поиск в API).
3. **Observation**: Агент получает результат вызова инструмента.
4. **Reflection**: Агент оценивает, достигнута ли цель, и планирует следующий шаг.
""")
])

# Lesson 2
create_notebook(os.path.join(m12, "lesson_02_langchain_llamaindex_for_analytics.ipynb"), [
    ("markdown", """# 🔗 Модуль 12. Урок 2: LangChain и LlamaIndex для автоматизации аналитических задач

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_12_ai_agents/lesson_02_langchain_llamaindex_for_analytics.ipynb)

---

## 1. Создание агента с инструментом исполнения кода (Code Execution Tool)
"""),
    ("code", """# Пример архитектуры аналитического агента с Tool Registry
class AnalyticsAgent:
    def __init__(self):
        self.tools = {
            'query_sales': lambda cat: f"Продажи категории {cat}: 1 450 000 руб, рост +12%",
            'check_inventory': lambda cat: f"Остаток на складе для {cat}: 230 шт (норма)",
        }
        
    def run_goal(self, goal: str):
        print(f" Цель агента: '{goal}'")
        print(" [Thought]: Для ответа на вопрос нужно проверить выручку и остатки на складе.")
        
        # Вызов инструментов
        res_sales = self.tools['query_sales']('Electronics')
        print(f" [Action]: query_sales('Electronics') -> {res_sales}")
        
        res_stock = self.tools['check_inventory']('Electronics')
        print(f" [Action]: check_inventory('Electronics') -> {res_stock}")
        
        print(" [Final Answer]: Выручка категории Electronics в норме, дефицита на складе нет.")

agent = AnalyticsAgent()
agent.run_goal("Проверь статус продаж электроники")
""")
])

# Lesson 3
create_notebook(os.path.join(m12, "lesson_03_automated_data_collection_agent.ipynb"), [
    ("markdown", """# 🔄 Модуль 12. Урок 3: Автономный агент регулярного мониторинга витрин данных

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_12_ai_agents/lesson_03_automated_data_collection_agent.ipynb)

---

## 1. Сценарий: Утренний алерт-агент в Telegram/Slack

Каждое утро в 08:30 агент:
1. Запускает SQL-запрос за вчерашний день.
2. Сравнивает выручку с 30-дневной скользящей медианой.
3. Если зафиксировано отклонение более $2.5\\sigma$, агент формирует факторный анализ причин и отправляет алерт команде.
""")
])

# Lesson 4
create_notebook(os.path.join(m12, "lesson_04_llm_evaluation_and_monitoring.ipynb"), [
    ("markdown", """# 📊 Модуль 12. Урок 4: LLM Evaluation: Оценка качества генерации (Ragas, DeepEval)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main/course/module_12_ai_agents/lesson_04_llm_evaluation_and_monitoring.ipynb)

---

## 1. Ключевые метрики LLM Evaluation в вакансиях 2027

- **Faithfulness (Фактологическая верность)**: Процент фактов в ответе, которые строго подтверждаются переданными данными (защита от галлюцинаций).
- **Answer Relevance (Релевантность)**: Соответствует ли сгенерированный инсайт исходному вопросу стейкхолдера.
- **Context Precision / Recall**: Насколько точно векторный поиск извлек нужные таблицы.
""")
])

# Module 12 Quiz
with open(os.path.join(m12, "quiz.md"), "w", encoding="utf-8") as f:
    f.write("""# 🧠 Quiz: Самопроверка по Модулю 12 (AI-агенты & LLM Evaluation)

---

### Вопрос 1
Что лежит в основе паттерна ReAct для автономных агентов?
- [ ] Однократный ответ без проверки.
- [x] Цикл: рассуждение (Thought) -> выбор инструмента и действие (Action) -> наблюдение за результатом (Observation) -> корректировка дальнейших шагов.
- [ ] Перезагрузка базы данных.
*Объяснение*: ReAct позволяет агенту динамически адаптировать свой план при получении промежуточных данных.

---

### Вопрос 2
Что означает метрика Faithfulness во фреймворках тестирования LLM (Ragas / DeepEval)?
- [ ] Скорость генерации ответа в токенах за секунду.
- [x] Доля утверждений в сгенерированном ответе, которые строго подтверждаются контекстом переданных данных (отсутствие галлюцинаций).
- [ ] Количество положительных отзывов пользователей.
*Объяснение*: Faithfulness гарантирует, что ИИ не додумал цифры от себя.

---

### Вопрос 3
Какую роль выполняет LLM-as-a-Judge в индустрии 2027 года?
- [ ] Вынесение юридических приговоров.
- [x] Использование сильной LLM для автоматической оценки качества, корректности и точности работы других прикладных моделей и пайплайнов на тестовых датасетах.
- [ ] Блокировка спама.
*Объяснение*: LLM-as-a-Judge масштабирует проверку качества аналитики без необходимости вручную вычитывать тысячи ответов.
""")

print("Module 12 deepened successfully.")
