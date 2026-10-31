# 🧪 Модуль 7: A/B-тестирование — Научный подход к изменениям в продукте

## 📌 О модуле
Бизнес не может полагаться на интуицию («мне кажется, эта синяя кнопка красивее»). A/B-тестирование — золотой стандарт проверки гипотез в продуктовых и маркетинговых компаниях (Яндекс, Авито, Ozon, Netflix, Uber).

## 🎯 Learning Outcomes
- **Understand**: Ошибки I рода ($\alpha$, ложная тревога) и II рода ($\beta$, упущенная выгода), статистическая мощность ($1 - \beta$).
- **Apply**: Расчет размера выборки (Sample Size) и MDE (Minimum Detectable Effect) до старта теста.
- **Analyze**: Проверка корректности сплитования: A/A-тесты и Sample Ratio Mismatch (SRM).
- **Evaluate**: Проблема ранней остановки (Peeking Problem), множественное тестирование (поправка Бонферрони).
- **Create**: Полный Python-ноутбук анализа A/B-теста от валидации до решения о раскатке.

## 📚 Уроки
1. `lesson_01_ab_testing_framework_and_mde.ipynb` — Дизайн эксперимента: формулировка гипотезы, метрики OEC, расчет Sample Size & MDE.
2. `lesson_02_splitting_aa_tests_srm.ipynb` — Рандомизация, A/A-тестирование и проверка Sample Ratio Mismatch (Chi-Square).
3. `lesson_03_evaluating_metrics_proportions_means.ipynb` — Оценка результатов: тест пропорций для конверсий, t-тест / бутстрап для выручки.
4. `lesson_04_p_hacking_peeking_problem.ipynb` — Ловушки: p-hacking, peeking problem (почему нельзя подглядывать каждый день).
5. `lesson_05_business_decision_rollout.ipynb` — Принятие бизнес-решения: статистическая значимость vs экономическая целесообразность.
6. `quiz.md` — Тест для закрепления.
7. `cheatsheet.md` — Памятка формул A/B теста.
