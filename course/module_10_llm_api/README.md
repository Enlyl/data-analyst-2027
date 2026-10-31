# 🧠 Модуль 10: Работа с LLM API и анализ неструктурированных данных

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
