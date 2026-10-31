# -*- coding: utf-8 -*-
"""
Premium HTML Portal Generator for Data Analyst 2027 Course.
Design system: Geist font, dark palette (#181818/#1F1F1F/#272727/#313131),
cubic-bezier(0.22,1,0.36,1) motion, no gradients except hero heading text.
"""
import os
import json
import glob
import shutil

BASE_DIR = r"d:\vibe_app\main_data_analytics\course"
OUTPUT_HTML = r"d:\vibe_app\main_data_analytics\index.html"
PORTAL_HTML = os.path.join(BASE_DIR, "index.html")
GITHUB_BASE = "https://colab.research.google.com/github/Enlyl/data-analyst-2027/blob/main"

modules_meta = [
    {"id": "module_00_onboarding", "title": "Модуль 0. Онбординг и мышление аналитика", "cat": "Фундамент", "badge": "Старт", "icon": "🚀", "desc": "Инструменты, майндсет AI-эры, постановка ТЗ и первая тетрадь в Colab."},
    {"id": "module_01_excel", "title": "Модуль 1. Excel и Google Sheets", "cat": "Хард база", "badge": "Таблицы", "icon": "📊", "desc": "ВПР, XLOOKUP, сводные таблицы, формулы массивов и аудит вычислений."},
    {"id": "module_02_sql", "title": "Модуль 2. SQL Master: от SELECT до оконных функций", "cat": "Хард база", "badge": "SQL", "icon": "🗄️", "desc": "CTE, оконные агрегаты, партиционирование, когорты и оптимизация запросов."},
    {"id": "module_03_python", "title": "Модуль 3. Python и Pandas для AI аналитика", "cat": "Хард база", "badge": "Python", "icon": "🐍", "desc": "Векторная обработка, фильтрация, агрегация, группировка без зубрежки синтаксиса."},
    {"id": "module_04_data_cleaning", "title": "Модуль 4. Очистка данных и Data Quality", "cat": "Хард база", "badge": "Качество", "icon": "🧹", "desc": "Пропуски, аномалии, дедупликация, приведение типов и автоматические валидаторы."},
    {"id": "module_05_statistics", "title": "Модуль 5. Статистика и проверка гипотез", "cat": "Аналитика", "badge": "Статы", "icon": "📈", "desc": "ЦПТ, p-value, t-тест Стьюдента, Манн-Уитни, бутстреп и доверительные интервалы."},
    {"id": "module_06_bi_looker_studio", "title": "Модуль 6. BI дашборды в Looker Studio", "cat": "BI", "badge": "BI", "icon": "📉", "desc": "Моделирование данных, интерактивные фильтры, executive-дашборды для бизнеса."},
    {"id": "module_07_ab_testing", "title": "Модуль 7. A/B тестирование и эксперименты", "cat": "Аналитика", "badge": "A/B", "icon": "🧪", "desc": "Расчет размера выборки, MDE, ловушка подглядывания (Peeking), SRM и множественные тесты."},
    {"id": "module_08_prompt_engineering", "title": "Модуль 8. Prompt Engineering для аналитиков", "cat": "AI стек", "badge": "Промпты", "icon": "💬", "desc": "Few-shot, Chain-of-Thought, Structured Outputs, генерация чистого SQL и Python кода."},
    {"id": "module_09_ai_tools_daily", "title": "Модуль 9. AI инструменты в ежедневной работе", "cat": "AI стек", "badge": "Workflow", "icon": "🤖", "desc": "Cursor, Copilot, валидация AI-галлюцинаций и автоматизация рутинных пайплайнов."},
    {"id": "module_10_llm_api", "title": "Модуль 10. LLM API и неструктурированные данные", "cat": "AI стек", "badge": "API", "icon": "🔌", "desc": "Парсинг отзывов, классификация клиентских обращений, NER и извлечение JSON из текста."},
    {"id": "module_11_rag_vector_db", "title": "Модуль 11. RAG и векторные базы данных", "cat": "AI стек", "badge": "RAG", "icon": "🔍", "desc": "ChromaDB, семантический поиск, эмбеддинги и вопросно-ответные системы по документам."},
    {"id": "module_12_ai_agents", "title": "Модуль 12. AI агенты и автоматический анализ", "cat": "AI стек", "badge": "Агенты", "icon": "🕹️", "desc": "Паттерн ReAct, LangChain, автономные аналитические агенты, вызывающие SQL и код."},
    {"id": "module_13_soft_skills_storytelling", "title": "Модуль 13. Soft Skills и Data Storytelling", "cat": "Soft Skills", "badge": "Коммуникация", "icon": "🎤", "desc": "Пирамида Минто, юнит-экономика (LTV, CAC, Retention) и презентация выводов стейкхолдерам."},
    {"id": "module_14_portfolio_project_1", "title": "Проект 1. E-Commerce 360 аудит", "cat": "Портфолио", "badge": "Проект", "icon": "🛒", "desc": "Сквозной аудит 15 000+ заказов: когортный анализ, LTV, выручка, воронка конверсий."},
    {"id": "module_15_portfolio_project_2", "title": "Проект 2. SaaS аналитика и A/B тест", "cat": "Портфолио", "badge": "Проект", "icon": "📱", "desc": "Анализ 2 000 пользователей, оценка воронки активации и расчет результатов A/B теста фичи."},
    {"id": "module_16_portfolio_project_3", "title": "Проект 3. AI-Driven аналитический пайплайн", "cat": "Портфолио", "badge": "Проект", "icon": "⚡", "desc": "Обработка 800+ отзывов через LLM API, категоризация болей и интерактивный дашборд."},
    {"id": "module_17_career", "title": "Модуль 17. Карьерный трек и резюме 2027", "cat": "Карьера", "badge": "Карьера", "icon": "🎯", "desc": "Оформление GitHub, портфолио в Notion, прохождение технических и поведенческих интервью."},
]

# ------- Collect all course data -------
course_data = []
for mod in modules_meta:
    mod_dir = os.path.join(BASE_DIR, mod["id"])
    if not os.path.exists(mod_dir):
        continue

    def read_md(name):
        p = os.path.join(mod_dir, name)
        if os.path.exists(p):
            with open(p, "r", encoding="utf-8") as f:
                return f.read()
        return ""

    readme_text = read_md("README.md")
    quiz_text = read_md("quiz.md")
    cs_text = read_md("cheatsheet.md")

    nb_files = sorted(glob.glob(os.path.join(mod_dir, "*.ipynb")))
    notebooks = []
    for nb_path in nb_files:
        nb_name = os.path.basename(nb_path)
        try:
            with open(nb_path, "r", encoding="utf-8") as nf:
                nb_json = json.loads(nf.read())
            cells = []
            for cell in nb_json.get("cells", []):
                c_type = cell.get("cell_type", "markdown")
                source = "".join(cell.get("source", []))
                cells.append({"type": c_type, "content": source})
            notebooks.append({"filename": nb_name, "rel_path": f"course/{mod['id']}/{nb_name}", "cells": cells})
        except Exception as e:
            notebooks.append({"filename": nb_name, "rel_path": f"course/{mod['id']}/{nb_name}", "cells": [{"type": "markdown", "content": f"Error: {e}"}]})

    course_data.append({**mod, "readme": readme_text, "quiz": quiz_text, "cheatsheet": cs_text, "notebooks": notebooks})

# ------- Escape for JS embedding -------
def js_str(s):
    return json.dumps(s, ensure_ascii=False)

# Build JSON data blob (no raw_json to save space)
course_json_data = []
for m in course_data:
    course_json_data.append({
        "id": m["id"],
        "title": m["title"],
        "cat": m["cat"],
        "badge": m["badge"],
        "icon": m["icon"],
        "desc": m["desc"],
        "readme": m["readme"],
        "quiz": m["quiz"],
        "cheatsheet": m["cheatsheet"],
        "notebooks": [{"filename": n["filename"], "rel_path": n["rel_path"], "cells": n["cells"]} for n in m["notebooks"]]
    })

course_json_str = json.dumps(course_json_data, ensure_ascii=False, indent=None)

html = f'''<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Data Analyst 2027</title>

  <!-- Fonts: Geist only (never Inter/Roboto/Arial) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500;600&display=swap" rel="stylesheet">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Ccircle cx='28' cy='28' r='20' fill='%23181818' stroke='%23FFFFFF' stroke-width='3.5'/%3E%3Crect x='19' y='27' width='3.5' height='12' rx='1' fill='%239B9B9B'/%3E%3Crect x='26' y='21' width='3.5' height='18' rx='1' fill='%23FFFFFF'/%3E%3Crect x='33' y='16' width='3.5' height='23' rx='1' fill='%23F97316'/%3E%3Crect x='41' y='41' width='6' height='18' rx='3' transform='rotate(-45 41 41)' fill='%23FFFFFF'/%3E%3C/svg%3E">

  <!-- Marked + Prism -->
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-sql.min.js"></script>

  <style>
    /* ===== DESIGN TOKENS (landing-page-design B4 dark palette) ===== */
    :root {{
      --bg-base: #181818;
      --bg-surface: #1F1F1F;
      --bg-card: #272727;
      --bg-card-hover: #313131;
      --bg-deep: #000000;
      --border: #313131;
      --border-focus: #9B9B9B;
      --text-main: #FFFFFF;
      --text-secondary: #C0C0C0;
      --text-muted: #9B9B9B;
      --text-dim: #666666;
      --accent: #F97316;
      --accent-hover: #FB923C;
      --success: #22C55E;
      --error: #EF4444;
      --code-bg: #0D0D0D;
      --ease: cubic-bezier(0.22, 1, 0.36, 1);
      --font-sans: 'Geist', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-mono: 'Geist Mono', 'Fira Code', monospace;
    }}

    /* ===== RESET ===== */
    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-style: normal !important;
    }}

    html {{ height: 100%; }}

    body {{
      font-family: var(--font-sans);
      background: var(--bg-base);
      color: var(--text-main);
      display: flex;
      height: 100vh;
      overflow: hidden;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }}

    /* ===== SIDEBAR ===== */
    #sidebar {{
      width: 340px;
      min-width: 340px;
      background: var(--bg-surface);
      border-right: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      height: 100vh;
      overflow: hidden;
    }}

    .sidebar-header {{
      padding: 24px 20px 16px;
      border-bottom: 1px solid var(--border);
    }}

    .brand {{
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 18px;
      font-weight: 600;
      letter-spacing: -0.02em;
    }}

    .brand svg {{ width: 24px; height: 24px; flex-shrink: 0; }}

    /* Progress */
    .progress-wrap {{ margin-top: 16px; }}
    .progress-bar {{
      background: var(--bg-deep);
      border-radius: 9999px;
      height: 4px;
      overflow: hidden;
    }}
    .progress-fill {{
      background: var(--text-main);
      height: 100%;
      width: 0%;
      transition: width 500ms var(--ease);
      border-radius: 9999px;
    }}
    .progress-label {{
      display: flex;
      justify-content: space-between;
      font-size: 12px;
      line-height: 16px;
      color: var(--text-muted);
      margin-top: 8px;
      font-variant-numeric: tabular-nums;
    }}

    /* Search */
    .search-box {{
      padding: 12px 16px;
      border-bottom: 1px solid var(--border);
    }}
    .search-input {{
      width: 100%;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 8px 12px 8px 36px;
      font-size: 14px;
      color: var(--text-main);
      font-family: var(--font-sans);
      outline: none;
      transition: border-color 300ms var(--ease);
    }}
    .search-input:focus {{ border-color: var(--border-focus); }}
    .search-input::placeholder {{ color: var(--text-dim); }}
    .search-wrap {{
      position: relative;
    }}
    .search-icon {{
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-dim);
      width: 16px;
      height: 16px;
    }}

    /* Module list */
    .module-list {{
      flex: 1;
      overflow-y: auto;
      padding: 8px 0;
      scrollbar-width: thin;
      scrollbar-color: var(--border) transparent;
    }}
    .module-list::-webkit-scrollbar {{ width: 4px; }}
    .module-list::-webkit-scrollbar-thumb {{ background: var(--border); border-radius: 4px; }}

    .cat-group {{ margin-bottom: 4px; }}
    .cat-label {{
      padding: 12px 20px 4px;
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--text-dim);
    }}

    .mod-item {{
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 10px 20px;
      cursor: pointer;
      transition: background 300ms var(--ease);
      border-left: 3px solid transparent;
      font-size: 14px;
      line-height: 20px;
      color: var(--text-secondary);
    }}
    .mod-item:hover {{ background: var(--bg-card); }}
    .mod-item.active {{
      background: var(--bg-card);
      border-left-color: var(--accent);
      color: var(--text-main);
      font-weight: 500;
    }}
    .mod-item .mod-icon {{ font-size: 16px; flex-shrink: 0; width: 20px; text-align: center; }}
    .mod-item .mod-badge {{
      margin-left: auto;
      font-size: 11px;
      padding: 2px 8px;
      border-radius: 9999px;
      background: var(--bg-card-hover);
      color: var(--text-muted);
      font-weight: 500;
      flex-shrink: 0;
    }}
    .mod-item .check-done {{
      color: var(--success);
      font-size: 14px;
      margin-left: 4px;
    }}

    /* ===== MAIN CONTENT ===== */
    #main {{
      flex: 1;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }}

    /* Top bar */
    .topbar {{
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 12px 32px;
      border-bottom: 1px solid var(--border);
      background: var(--bg-surface);
      min-height: 56px;
    }}
    .topbar-title {{
      font-size: 16px;
      font-weight: 600;
      color: var(--text-main);
      flex: 1;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    /* Tabs */
    .tabs {{
      display: flex;
      gap: 0;
      border-bottom: 1px solid var(--border);
      background: var(--bg-surface);
      padding: 0 32px;
    }}
    .tab {{
      padding: 12px 16px;
      font-size: 14px;
      font-weight: 500;
      color: var(--text-muted);
      cursor: pointer;
      border-bottom: 2px solid transparent;
      transition: color 300ms var(--ease), border-color 300ms var(--ease);
      white-space: nowrap;
    }}
    .tab:hover {{ color: var(--text-secondary); }}
    .tab.active {{
      color: var(--text-main);
      border-bottom-color: var(--accent);
    }}

    /* Content area */
    #content-area {{
      flex: 1;
      overflow-y: auto;
      padding: 32px;
      scrollbar-width: thin;
      scrollbar-color: var(--border) transparent;
    }}
    #content-area::-webkit-scrollbar {{ width: 6px; }}
    #content-area::-webkit-scrollbar-thumb {{ background: var(--border); border-radius: 4px; }}

    /* ===== HERO (landing page) ===== */
    .hero {{
      text-align: center;
      padding: 80px 32px 64px;
      max-width: 800px;
      margin: 0 auto;
    }}
    .hero-badge {{
      display: inline-block;
      padding: 4px 12px;
      border-radius: 9999px;
      border: 1px solid var(--border);
      font-size: 12px;
      font-weight: 500;
      color: var(--text-muted);
      margin-bottom: 24px;
      letter-spacing: 0.04em;
    }}
    .hero h1 {{
      font-size: 48px;
      line-height: 48px;
      font-weight: 600;
      max-width: 680px;
      margin: 0 auto 24px;
      background: linear-gradient(to right, #FFFFFF, #9B9B9B);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      text-wrap: balance;
    }}
    .hero p {{
      font-size: 18px;
      line-height: 28px;
      color: var(--text-muted);
      max-width: 680px;
      margin: 0 auto 40px;
      text-wrap: pretty;
    }}
    .hero-stats {{
      display: flex;
      justify-content: center;
      gap: 48px;
      margin-top: 40px;
    }}
    .hero-stat {{
      text-align: center;
    }}
    .hero-stat-num {{
      font-size: 36px;
      line-height: 40px;
      font-weight: 600;
      color: var(--text-main);
      font-family: var(--font-mono);
    }}
    .hero-stat-label {{
      font-size: 14px;
      line-height: 20px;
      color: var(--text-muted);
      margin-top: 4px;
    }}

    /* ===== NOTEBOOK LESSON VIEW ===== */
    .lesson-header {{
      margin-bottom: 32px;
    }}
    .lesson-header h2 {{
      font-size: 30px;
      line-height: 36px;
      font-weight: 600;
      margin-bottom: 8px;
    }}
    .lesson-header .lesson-desc {{
      font-size: 16px;
      line-height: 24px;
      color: var(--text-muted);
    }}

    /* Colab button */
    .colab-btn {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 8px 16px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 8px;
      color: var(--text-main);
      font-size: 14px;
      font-weight: 500;
      font-family: var(--font-sans);
      cursor: pointer;
      text-decoration: none;
      transition: background 300ms var(--ease), border-color 300ms var(--ease);
      margin-bottom: 24px;
    }}
    .colab-btn:hover {{ background: var(--bg-card-hover); border-color: var(--border-focus); }}
    .colab-btn svg {{ width: 18px; height: 18px; }}

    /* Notebook sub-tabs */
    .nb-tabs {{
      display: flex;
      gap: 0;
      border-bottom: 1px solid var(--border);
      margin-bottom: 24px;
      flex-wrap: wrap;
    }}
    .nb-tab {{
      padding: 8px 14px;
      font-size: 13px;
      font-weight: 500;
      color: var(--text-muted);
      cursor: pointer;
      border-bottom: 2px solid transparent;
      transition: color 300ms var(--ease), border-color 300ms var(--ease);
      font-family: var(--font-mono);
      white-space: nowrap;
    }}
    .nb-tab:hover {{ color: var(--text-secondary); }}
    .nb-tab.active {{
      color: var(--accent);
      border-bottom-color: var(--accent);
    }}

    /* Cell rendering */
    .cell {{
      margin-bottom: 16px;
      border-radius: 8px;
      overflow: hidden;
    }}
    .cell-md {{
      padding: 16px 20px;
      background: transparent;
      font-size: 16px;
      line-height: 24px;
      color: var(--text-secondary);
    }}
    .cell-md h1, .cell-md h2, .cell-md h3, .cell-md h4 {{
      color: var(--text-main);
      margin-top: 24px;
      margin-bottom: 8px;
    }}
    .cell-md h1 {{ font-size: 30px; line-height: 36px; font-weight: 600; }}
    .cell-md h2 {{ font-size: 24px; line-height: 32px; font-weight: 600; }}
    .cell-md h3 {{ font-size: 20px; line-height: 28px; font-weight: 600; }}
    .cell-md h4 {{ font-size: 18px; line-height: 28px; font-weight: 500; }}
    .cell-md p {{ margin-bottom: 12px; }}
    .cell-md ul, .cell-md ol {{ padding-left: 24px; margin-bottom: 12px; }}
    .cell-md li {{ margin-bottom: 4px; }}
    .cell-md code {{
      background: var(--code-bg);
      padding: 2px 6px;
      border-radius: 4px;
      font-family: var(--font-mono);
      font-size: 14px;
    }}
    .cell-md pre {{
      background: var(--code-bg);
      border-radius: 8px;
      padding: 16px;
      overflow-x: auto;
      margin-bottom: 12px;
    }}
    .cell-md pre code {{ background: none; padding: 0; }}
    .cell-md blockquote {{
      border-left: 3px solid var(--accent);
      padding-left: 16px;
      color: var(--text-muted);
      margin: 12px 0;
    }}
    .cell-md table {{
      width: 100%;
      border-collapse: collapse;
      margin: 12px 0;
    }}
    .cell-md th, .cell-md td {{
      padding: 8px 12px;
      border: 1px solid var(--border);
      text-align: left;
      font-size: 14px;
    }}
    .cell-md th {{ background: var(--bg-card); font-weight: 600; }}
    .cell-md strong {{ color: var(--text-main); font-weight: 600; }}
    .cell-md a {{ color: var(--accent); text-decoration: none; }}
    .cell-md a:hover {{ text-decoration: underline; }}

    .cell-code {{
      position: relative;
      background: var(--code-bg);
      border: 1px solid var(--border);
      border-radius: 8px;
    }}
    .cell-code-label {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 8px 16px;
      font-size: 12px;
      font-weight: 500;
      color: var(--text-dim);
      border-bottom: 1px solid var(--border);
      font-family: var(--font-mono);
    }}
    .copy-btn {{
      background: none;
      border: 1px solid var(--border);
      border-radius: 6px;
      color: var(--text-muted);
      font-size: 11px;
      padding: 4px 8px;
      cursor: pointer;
      font-family: var(--font-sans);
      transition: color 300ms var(--ease), border-color 300ms var(--ease);
    }}
    .copy-btn:hover {{ color: var(--text-main); border-color: var(--border-focus); }}
    .cell-code pre {{
      padding: 16px;
      overflow-x: auto;
      margin: 0;
      font-size: 14px;
      line-height: 22px;
    }}
    .cell-code code {{
      font-family: var(--font-mono);
    }}

    /* ===== README / QUIZ / CHEATSHEET views ===== */
    .md-view {{
      max-width: 800px;
    }}
    .md-view h1, .md-view h2, .md-view h3 {{ color: var(--text-main); margin-top: 24px; margin-bottom: 12px; }}
    .md-view h1 {{ font-size: 30px; line-height: 36px; font-weight: 600; }}
    .md-view h2 {{ font-size: 24px; line-height: 32px; font-weight: 600; }}
    .md-view h3 {{ font-size: 20px; line-height: 28px; font-weight: 600; }}
    .md-view p {{ margin-bottom: 12px; color: var(--text-secondary); font-size: 16px; line-height: 24px; }}
    .md-view ul, .md-view ol {{ padding-left: 24px; margin-bottom: 12px; color: var(--text-secondary); }}
    .md-view li {{ margin-bottom: 6px; font-size: 16px; line-height: 24px; }}
    .md-view code {{ background: var(--code-bg); padding: 2px 6px; border-radius: 4px; font-family: var(--font-mono); font-size: 14px; }}
    .md-view pre {{ background: var(--code-bg); border-radius: 8px; padding: 16px; overflow-x: auto; margin-bottom: 16px; }}
    .md-view pre code {{ background: none; padding: 0; }}
    .md-view blockquote {{ border-left: 3px solid var(--accent); padding-left: 16px; color: var(--text-muted); margin: 12px 0; }}
    .md-view strong {{ color: var(--text-main); }}
    .md-view a {{ color: var(--accent); text-decoration: none; }}
    .md-view a:hover {{ text-decoration: underline; }}
    .md-view table {{ width: 100%; border-collapse: collapse; margin: 12px 0; }}
    .md-view th, .md-view td {{ padding: 8px 12px; border: 1px solid var(--border); text-align: left; font-size: 14px; }}
    .md-view th {{ background: var(--bg-card); font-weight: 600; }}
    .md-view hr {{ border: none; border-top: 1px solid var(--border); margin: 24px 0; }}

    /* ===== QUIZ INTERACTIVE ===== */
    .quiz-question {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 24px;
      margin-bottom: 16px;
    }}
    .quiz-question h3 {{
      font-size: 16px;
      font-weight: 600;
      margin-bottom: 16px;
      color: var(--text-main);
    }}
    .quiz-option {{
      display: flex;
      align-items: flex-start;
      gap: 12px;
      padding: 12px 16px;
      border-radius: 8px;
      cursor: pointer;
      margin-bottom: 8px;
      border: 1px solid var(--border);
      transition: background 300ms var(--ease), border-color 300ms var(--ease);
      font-size: 14px;
      line-height: 20px;
      color: var(--text-secondary);
    }}
    .quiz-option:hover {{ background: var(--bg-card-hover); }}
    .quiz-option.correct {{
      border-color: var(--success);
      background: rgba(34, 197, 94, 0.1);
    }}
    .quiz-option.wrong {{
      border-color: var(--error);
      background: rgba(239, 68, 68, 0.1);
    }}
    .quiz-option .radio {{
      width: 18px;
      height: 18px;
      border: 2px solid var(--border);
      border-radius: 50%;
      flex-shrink: 0;
      margin-top: 1px;
      transition: border-color 300ms var(--ease);
    }}
    .quiz-option.correct .radio {{ border-color: var(--success); background: var(--success); }}
    .quiz-option.wrong .radio {{ border-color: var(--error); }}
    .quiz-explanation {{
      margin-top: 12px;
      padding: 12px 16px;
      background: var(--bg-surface);
      border-radius: 8px;
      font-size: 14px;
      line-height: 20px;
      color: var(--text-muted);
      display: none;
    }}
    .quiz-explanation.show {{ display: block; }}

    .quiz-score {{
      text-align: center;
      padding: 24px;
      background: var(--bg-card);
      border-radius: 12px;
      border: 1px solid var(--border);
      margin-bottom: 24px;
    }}
    .quiz-score-num {{
      font-size: 48px;
      font-weight: 600;
      font-family: var(--font-mono);
      color: var(--accent);
    }}
    .quiz-score-label {{ font-size: 14px; color: var(--text-muted); margin-top: 4px; }}

    /* Mark complete button */
    .complete-btn {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 8px 16px;
      background: var(--accent);
      border: none;
      border-radius: 8px;
      color: #000000;
      font-size: 14px;
      font-weight: 600;
      cursor: pointer;
      font-family: var(--font-sans);
      transition: opacity 300ms var(--ease);
      margin-top: 24px;
    }}
    .complete-btn:hover {{ opacity: 0.85; }}
    .complete-btn.done {{
      background: var(--success);
      cursor: default;
    }}

    /* Responsive: hide sidebar on small screens */
    @media (max-width: 768px) {{
      #sidebar {{ display: none; }}
    }}

    /* Reduced motion */
    @media (prefers-reduced-motion: reduce) {{
      *, *::before, *::after {{
        transition-duration: 0.01ms !important;
        animation-duration: 0.01ms !important;
      }}
    }}
  </style>
</head>
<body>

<!-- ===== SIDEBAR ===== -->
<nav id="sidebar">
  <div class="sidebar-header">
    <div class="brand">
      <svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="28" cy="28" r="20" fill="#181818" stroke="#FFFFFF" stroke-width="3.5"/>
        <rect x="19" y="27" width="3.5" height="12" rx="1" fill="#9B9B9B"/>
        <rect x="26" y="21" width="3.5" height="18" rx="1" fill="#FFFFFF"/>
        <rect x="33" y="16" width="3.5" height="23" rx="1" fill="#F97316"/>
        <rect x="41" y="41" width="6" height="18" rx="3" transform="rotate(-45 41 41)" fill="#FFFFFF"/>
      </svg>
      Data Analyst 2027
    </div>
    <div class="progress-wrap">
      <div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div>
      <div class="progress-label">
        <span id="progressText">0 / 0 уроков</span>
        <span id="progressPct">0%</span>
      </div>
    </div>
  </div>

  <div class="search-box">
    <div class="search-wrap">
      <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
      <input type="text" class="search-input" id="searchInput" placeholder="Поиск по модулям...">
    </div>
  </div>

  <div class="module-list" id="moduleList"></div>
</nav>

<!-- ===== MAIN ===== -->
<main id="main">
  <div class="topbar">
    <div class="topbar-title" id="topbarTitle">Data Analyst 2027</div>
  </div>
  <div class="tabs" id="tabsBar"></div>
  <div id="content-area"></div>
</main>

<script>
// ===== DATA =====
const GITHUB_BASE = "{GITHUB_BASE}";
const COURSE = {course_json_str};

// ===== STATE =====
let currentModIdx = -1;  // -1 = hero
let currentTab = "readme";
let currentNbIdx = 0;
let completedLessons = JSON.parse(localStorage.getItem("da2027_completed") || "{{}}");

// ===== INIT =====
document.addEventListener("DOMContentLoaded", () => {{
  buildSidebar();
  showHero();
  updateProgress();
  document.getElementById("searchInput").addEventListener("input", filterModules);
}});

// ===== SIDEBAR =====
function buildSidebar() {{
  const list = document.getElementById("moduleList");
  let html = "";
  let lastCat = "";
  COURSE.forEach((mod, idx) => {{
    if (mod.cat !== lastCat) {{
      lastCat = mod.cat;
      html += `<div class="cat-group"><div class="cat-label">${{mod.cat}}</div></div>`;
    }}
    const done = completedLessons[mod.id] ? '<span class="check-done">&#10003;</span>' : "";
    const active = idx === currentModIdx ? " active" : "";
    const title = mod.title.replace(/^(Модуль \\d+\\.|Проект \\d+\\.)\\s*/, "");
    html += `<div class="mod-item${{active}}" data-idx="${{idx}}" onclick="selectModule(${{idx}})">
      <span class="mod-icon">${{mod.icon}}</span>
      <span style="flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">${{title}}</span>
      <span class="mod-badge">${{mod.badge}}</span>
      ${{done}}
    </div>`;
  }});
  list.innerHTML = html;
}}

function filterModules() {{
  const q = document.getElementById("searchInput").value.toLowerCase();
  document.querySelectorAll(".mod-item").forEach(el => {{
    const idx = parseInt(el.dataset.idx);
    const mod = COURSE[idx];
    const match = !q || mod.title.toLowerCase().includes(q) || mod.desc.toLowerCase().includes(q) || mod.cat.toLowerCase().includes(q);
    el.style.display = match ? "" : "none";
  }});
  // Show/hide category labels
  document.querySelectorAll(".cat-group").forEach(g => {{
    const items = g.querySelectorAll ? [] : [];
    // just show all cat labels; simple approach
  }});
}}

function updateProgress() {{
  const total = COURSE.reduce((s, m) => s + Math.max(m.notebooks.length, 1), 0);
  const done = Object.keys(completedLessons).length;
  const pct = total > 0 ? Math.round((done / COURSE.length) * 100) : 0;
  document.getElementById("progressFill").style.width = pct + "%";
  document.getElementById("progressText").textContent = done + " / " + COURSE.length + " модулей";
  document.getElementById("progressPct").textContent = pct + "%";
}}

// ===== HERO =====
function showHero() {{
  currentModIdx = -1;
  currentTab = "readme";
  document.getElementById("topbarTitle").textContent = "Data Analyst 2027";
  document.getElementById("tabsBar").innerHTML = "";

  // deactivate sidebar
  document.querySelectorAll(".mod-item").forEach(el => el.classList.remove("active"));

  const totalNb = COURSE.reduce((s, m) => s + m.notebooks.length, 0);

  document.getElementById("content-area").innerHTML = `
    <div class="hero">
      <div class="hero-badge">Интерактивный курс 2027</div>
      <h1>Стань Data Analyst<br>в эпоху AI</h1>
      <p>18 модулей, от Excel до AI-агентов. Каждый урок запускается в Google Colab одним кликом. Реальные датасеты, 3 портфолио-проекта, квизы для самопроверки.</p>
      <div class="hero-stats">
        <div class="hero-stat">
          <div class="hero-stat-num">${{COURSE.length}}</div>
          <div class="hero-stat-label">модулей</div>
        </div>
        <div class="hero-stat">
          <div class="hero-stat-num">${{totalNb}}</div>
          <div class="hero-stat-label">Colab ноутбуков</div>
        </div>
        <div class="hero-stat">
          <div class="hero-stat-num">3</div>
          <div class="hero-stat-label">проекта портфолио</div>
        </div>
      </div>
    </div>
  `;
}}

// ===== MODULE SELECT =====
function selectModule(idx) {{
  currentModIdx = idx;
  currentTab = "readme";
  currentNbIdx = 0;
  const mod = COURSE[idx];

  document.getElementById("topbarTitle").textContent = mod.title;

  // Highlight sidebar
  document.querySelectorAll(".mod-item").forEach(el => {{
    el.classList.toggle("active", parseInt(el.dataset.idx) === idx);
  }});

  // Build tabs
  const tabs = ["readme"];
  const tabLabels = {{"readme": "Обзор"}};
  if (mod.notebooks.length > 0) {{
    tabs.push("lessons");
    tabLabels["lessons"] = "Уроки (" + mod.notebooks.length + ")";
  }}
  if (mod.quiz) {{
    tabs.push("quiz");
    tabLabels["quiz"] = "Квиз";
  }}
  if (mod.cheatsheet) {{
    tabs.push("cheatsheet");
    tabLabels["cheatsheet"] = "Шпаргалка";
  }}

  let tabsHtml = "";
  tabs.forEach(t => {{
    tabsHtml += `<div class="tab${{t === currentTab ? ' active' : ''}}" onclick="switchTab('${{t}}')">${{tabLabels[t]}}</div>`;
  }});
  document.getElementById("tabsBar").innerHTML = tabsHtml;

  renderTab();
}}

function switchTab(tab) {{
  currentTab = tab;
  document.querySelectorAll(".tab").forEach(el => {{
    el.classList.toggle("active", el.textContent.startsWith(
      tab === "readme" ? "Обзор" :
      tab === "lessons" ? "Уроки" :
      tab === "quiz" ? "Квиз" :
      "Шпаргалка"
    ));
  }});
  renderTab();
}}

function renderTab() {{
  const mod = COURSE[currentModIdx];
  const area = document.getElementById("content-area");

  if (currentTab === "readme") {{
    area.innerHTML = '<div class="md-view">' + renderMd(mod.readme) + markCompleteBtn(mod.id) + '</div>';
  }} else if (currentTab === "lessons") {{
    renderLessons(mod);
  }} else if (currentTab === "quiz") {{
    renderQuiz(mod);
  }} else if (currentTab === "cheatsheet") {{
    area.innerHTML = '<div class="md-view">' + renderMd(mod.cheatsheet) + '</div>';
  }}
  highlightAll();
}}

// ===== LESSONS (Notebooks) =====
function renderLessons(mod) {{
  const area = document.getElementById("content-area");
  if (mod.notebooks.length === 0) {{
    area.innerHTML = '<p style="color:var(--text-muted)">Нет ноутбуков в этом модуле.</p>';
    return;
  }}
  const nb = mod.notebooks[currentNbIdx];
  const colabUrl = GITHUB_BASE + "/" + nb.rel_path;

  let nbTabsHtml = '<div class="nb-tabs">';
  mod.notebooks.forEach((n, i) => {{
    const label = n.filename.replace(".ipynb", "").replace(/_/g, " ");
    nbTabsHtml += `<div class="nb-tab${{i === currentNbIdx ? ' active' : ''}}" onclick="switchNb(${{i}})">${{label}}</div>`;
  }});
  nbTabsHtml += '</div>';

  let cellsHtml = "";
  nb.cells.forEach(cell => {{
    if (cell.type === "markdown") {{
      cellsHtml += '<div class="cell cell-md">' + renderMd(cell.content) + '</div>';
    }} else {{
      const lang = cell.content.includes("SELECT") || cell.content.includes("CREATE") ? "sql" : "python";
      const escaped = escapeHtml(cell.content);
      cellsHtml += `<div class="cell cell-code">
        <div class="cell-code-label"><span>Python</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
        <pre><code class="language-${{lang}}">${{escaped}}</code></pre>
      </div>`;
    }}
  }});

  area.innerHTML = `
    <div class="lesson-header">
      <a href="${{colabUrl}}" target="_blank" rel="noopener" class="colab-btn">
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>
        Запустить в Colab
      </a>
      ${{nbTabsHtml}}
    </div>
    ${{cellsHtml}}
    ${{markCompleteBtn(mod.id)}}
  `;
}}

function switchNb(i) {{
  currentNbIdx = i;
  renderLessons(COURSE[currentModIdx]);
  highlightAll();
}}

// ===== QUIZ =====
function renderQuiz(mod) {{
  const area = document.getElementById("content-area");
  const questions = parseQuiz(mod.quiz);

  if (questions.length === 0) {{
    area.innerHTML = '<div class="md-view">' + renderMd(mod.quiz) + '</div>';
    return;
  }}

  let html = '<div class="quiz-score"><div class="quiz-score-num" id="quizScore">0/' + questions.length + '</div><div class="quiz-score-label">Правильных ответов</div></div>';

  questions.forEach((q, qi) => {{
    html += `<div class="quiz-question" id="q${{qi}}">
      <h3>Вопрос ${{qi + 1}}: ${{escapeHtml(q.question)}}</h3>`;
    q.options.forEach((opt, oi) => {{
      html += `<div class="quiz-option" data-q="${{qi}}" data-o="${{oi}}" data-correct="${{opt.correct}}" onclick="answerQuiz(this)">
        <div class="radio"></div>
        <span>${{escapeHtml(opt.text)}}</span>
      </div>`;
    }});
    if (q.explanation) {{
      html += `<div class="quiz-explanation" id="expl${{qi}}">${{escapeHtml(q.explanation)}}</div>`;
    }}
    html += '</div>';
  }});

  area.innerHTML = html;
}}

let quizAnswered = {{}};
function answerQuiz(el) {{
  const qi = el.dataset.q;
  if (quizAnswered[qi]) return;
  quizAnswered[qi] = true;
  const isCorrect = el.dataset.correct === "true";

  // Mark all options in this question
  document.querySelectorAll(`.quiz-option[data-q="${{qi}}"]`).forEach(opt => {{
    if (opt.dataset.correct === "true") opt.classList.add("correct");
    else if (opt === el) opt.classList.add("wrong");
    opt.style.pointerEvents = "none";
  }});

  // Show explanation
  const expl = document.getElementById("expl" + qi);
  if (expl) expl.classList.add("show");

  // Update score
  const total = document.querySelectorAll(".quiz-question").length;
  const correct = document.querySelectorAll(".quiz-option.correct").length;
  // Count unique correct answers
  const answered = Object.keys(quizAnswered).length;
  let score = 0;
  Object.keys(quizAnswered).forEach(k => {{
    const chosen = document.querySelector(`.quiz-option[data-q="${{k}}"].correct`);
    // Check if user clicked the correct one
    const userClicked = document.querySelector(`.quiz-option[data-q="${{k}}"].wrong`);
    if (chosen && !userClicked) score++;
    else if (chosen) {{
      // correct was highlighted but user may have clicked wrong
      const userEl = document.querySelector(`.quiz-option[data-q="${{k}}"].wrong`);
      if (!userEl) score++;
    }}
  }});
  document.getElementById("quizScore").textContent = score + "/" + total;
}}

function parseQuiz(text) {{
  const questions = [];
  const blocks = text.split(/###\\s*Вопрос\\s*\\d+/i);
  blocks.shift(); // remove header
  blocks.forEach(block => {{
    const lines = block.trim().split("\\n");
    let question = "";
    let options = [];
    let explanation = "";

    // First non-empty line is the question
    let i = 0;
    while (i < lines.length && !lines[i].trim()) i++;
    if (i < lines.length) {{ question = lines[i].trim(); i++; }}

    for (; i < lines.length; i++) {{
      const line = lines[i].trim();
      const optMatch = line.match(/^-\\s*\\[(x| )\\]\\s*(.+)/i);
      if (optMatch) {{
        options.push({{ text: optMatch[2].trim(), correct: optMatch[1].toLowerCase() === "x" }});
      }}
      if (line.startsWith("*Объяснение*") || line.startsWith("**Объяснение**")) {{
        explanation = line.replace(/^\\*+Объяснение\\*+:?\\s*/, "").trim();
      }}
    }}

    if (question && options.length > 0) {{
      questions.push({{ question, options, explanation }});
    }}
  }});
  return questions;
}}

// ===== HELPERS =====
function renderMd(text) {{
  if (!text) return '<p style="color:var(--text-muted)">Нет содержимого.</p>';
  if (typeof marked !== "undefined") {{
    return marked.parse(text);
  }}
  return '<pre>' + escapeHtml(text) + '</pre>';
}}

function escapeHtml(s) {{
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
}}

function highlightAll() {{
  if (typeof Prism !== "undefined") {{
    setTimeout(() => Prism.highlightAll(), 50);
  }}
}}

function copyCode(btn) {{
  const code = btn.closest(".cell-code").querySelector("code");
  navigator.clipboard.writeText(code.textContent).then(() => {{
    btn.textContent = "Copied!";
    setTimeout(() => btn.textContent = "Copy", 2000);
  }});
}}

function markCompleteBtn(modId) {{
  const isDone = completedLessons[modId];
  return `<button class="complete-btn${{isDone ? ' done' : ''}}" onclick="toggleComplete('${{modId}}', this)">
    ${{isDone ? '&#10003; Пройдено' : 'Отметить как пройденное'}}
  </button>`;
}}

function toggleComplete(modId, btn) {{
  if (completedLessons[modId]) {{
    delete completedLessons[modId];
    btn.classList.remove("done");
    btn.innerHTML = "Отметить как пройденное";
  }} else {{
    completedLessons[modId] = true;
    btn.classList.add("done");
    btn.innerHTML = "&#10003; Пройдено";
  }}
  localStorage.setItem("da2027_completed", JSON.stringify(completedLessons));
  updateProgress();
  buildSidebar();
}}
</script>
</body>
</html>'''

# Write both copies
with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(html)
with open(PORTAL_HTML, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Portal written: {OUTPUT_HTML} ({len(html)} bytes)")
print(f"Portal copied:  {PORTAL_HTML}")
total_nb = sum(len(m["notebooks"]) for m in course_data)
print(f"Modules: {len(course_data)}, Notebooks: {total_nb}")
