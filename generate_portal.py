import os
import json
import glob

BASE_DIR = r"d:\vibe_app\main_data_analytics\course"
OUTPUT_HTML = r"d:\vibe_app\main_data_analytics\index.html"
PORTAL_HTML = os.path.join(BASE_DIR, "index.html")

modules = [
    {"id": "module_00_onboarding", "title": "Модуль 0. Онбординг и мышление аналитика", "category": "Фундамент", "badge": "Старт"},
    {"id": "module_01_excel", "title": "Модуль 1. Excel и Google Sheets", "category": "Хард база", "badge": "Таблицы"},
    {"id": "module_02_sql", "title": "Модуль 2. SQL Master от SELECT до оконных функций", "category": "Хард база", "badge": "SQL"},
    {"id": "module_03_python", "title": "Модуль 3. Python и Pandas с AI напарником", "category": "Хард база", "badge": "Python"},
    {"id": "module_04_data_cleaning", "title": "Модуль 4. Очистка данных и Data Quality", "category": "Хард база", "badge": "Качество"},
    {"id": "module_05_statistics", "title": "Модуль 5. Статистика и гипотезы", "category": "Математика", "badge": "Статистика"},
    {"id": "module_06_bi_looker_studio", "title": "Модуль 6. BI аналитика в Looker Studio", "category": "Визуализация", "badge": "BI"},
    {"id": "module_07_ab_testing", "title": "Модуль 7. A/B тестирование и эксперименты", "category": "Эксперименты", "badge": "A/B тесты"},
    {"id": "module_08_prompt_engineering", "title": "Модуль 8. Prompt Engineering для аналитики", "category": "AI стек", "badge": "Промпты"},
    {"id": "module_09_ai_tools_daily", "title": "Модуль 9. AI в ежедневной работе аналитика", "category": "AI стек", "badge": "Инструменты"},
    {"id": "module_10_llm_api", "title": "Модуль 10. LLM API и неструктурированные данные", "category": "AI стек", "badge": "API"},
    {"id": "module_11_rag_vector_db", "title": "Модуль 11. RAG и векторные базы данных", "category": "AI стек", "badge": "RAG"},
    {"id": "module_12_ai_agents", "title": "Модуль 12. AI агенты и мониторинг качества", "category": "AI стек", "badge": "Агенты"},
    {"id": "module_13_soft_skills_storytelling", "title": "Модуль 13. Soft Skills и Data Storytelling", "category": "Бизнес", "badge": "Soft Skills"},
    {"id": "module_14_portfolio_project_1", "title": "Проект 1. E Commerce 360 аудит", "category": "Портфолио", "badge": "Проект"},
    {"id": "module_15_portfolio_project_2", "title": "Проект 2. SaaS продуктовая аналитика и A/B", "category": "Портфолио", "badge": "Проект"},
    {"id": "module_16_portfolio_project_3", "title": "Проект 3. AI Driven аналитический пайплайн", "category": "Портфолио", "badge": "Проект"},
    {"id": "module_17_career", "title": "Модуль 17. Карьерный трек и портфолио", "category": "Карьера", "badge": "Карьера"}
]

course_data = []

for mod in modules:
    mod_dir = os.path.join(BASE_DIR, mod["id"])
    if not os.path.exists(mod_dir):
        continue
    
    readme_path = os.path.join(mod_dir, "README.md")
    readme_text = ""
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            readme_text = f.read()

    quiz_path = os.path.join(mod_dir, "quiz.md")
    quiz_text = ""
    if os.path.exists(quiz_path):
        with open(quiz_path, "r", encoding="utf-8") as f:
            quiz_text = f.read()

    cs_path = os.path.join(mod_dir, "cheatsheet.md")
    cs_text = ""
    if os.path.exists(cs_path):
        with open(cs_path, "r", encoding="utf-8") as f:
            cs_text = f.read()
            
    nb_files = sorted(glob.glob(os.path.join(mod_dir, "*.ipynb")))
    notebooks = []
    for nb_path in nb_files:
        nb_name = os.path.basename(nb_path)
        try:
            with open(nb_path, "r", encoding="utf-8") as nf:
                nb_raw_text = nf.read()
                nb_json = json.loads(nb_raw_text)
                
                cells = []
                for cell in nb_json.get("cells", []):
                    c_type = cell.get("cell_type", "markdown")
                    source = "".join(cell.get("source", []))
                    cells.append({"type": c_type, "content": source})
                    
                notebooks.append({
                    "filename": nb_name,
                    "rel_path": f"course/{mod['id']}/{nb_name}",
                    "filepath": os.path.abspath(nb_path).replace("\\", "/"),
                    "raw_json": nb_raw_text,
                    "cells": cells
                })
        except Exception as e:
            notebooks.append({
                "filename": nb_name,
                "rel_path": f"course/{mod['id']}/{nb_name}",
                "filepath": os.path.abspath(nb_path).replace("\\", "/"),
                "raw_json": "{}",
                "cells": [{"type": "markdown", "content": f"Ошибка: {e}"}]
            })
            
    course_data.append({
        "id": mod["id"],
        "title": mod["title"],
        "category": mod["category"],
        "badge": mod["badge"],
        "readme": readme_text,
        "quiz": quiz_text,
        "cheatsheet": cs_text,
        "notebooks": notebooks
    })

# High-polish design compliant with elayadesign/ai-design-skills & redesign-existing-projects
html_content = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Data Analyst 2027: Практический курс</title>
  
  <!-- Approved Typography: Geist & Geist Mono (Never Inter/Roboto/Arial, no italics) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  
  <!-- Favicon: Solar Lens Style -->
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Ccircle cx='28' cy='28' r='20' fill='%23181818' stroke='%23FFFFFF' stroke-width='3.5'/%3E%3Crect x='19' y='27' width='3.5' height='12' rx='1' fill='%239B9B9B'/%3E%3Crect x='26' y='21' width='3.5' height='18' rx='1' fill='%23FFFFFF'/%3E%3Crect x='33' y='16' width='3.5' height='23' rx='1' fill='%23F97316'/%3E%3Crect x='41' y='41' width='6' height='18' rx='3' transform='rotate(-45 41 41)' fill='%23FFFFFF'/%3E%3C/svg%3E">
  <link rel="alternate icon" href="favicon.svg">

  <!-- Code Highlighting & Markdown Parser -->
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-sql.min.js"></script>

  <style>
    /* DESIGN VALUES: Approved Dark Palette & Strict Spacing/Radius Scale */
    :root {{
      --bg-base: #181818;
      --bg-surface: #1F1F1F;
      --bg-card: #272727;
      --bg-card-hover: #313131;
      --border: #313131;
      --border-focus: #9B9B9B;
      --text-main: #FFFFFF;
      --text-muted: #9B9B9B;
      --accent-cta: #F97316;
      --code-bg: #121212;
      --ease-base: cubic-bezier(0.22, 1, 0.36, 1);
    }}

    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-style: normal !important; /* No italics */
    }}

    body {{
      font-family: 'Geist', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg-base);
      color: var(--text-main);
      display: flex;
      min-height: 100dvh;
      height: 100vh;
      overflow: hidden;
      -webkit-font-smoothing: antialiased;
    }}

    /* SIDEBAR */
    #sidebar {{
      width: 360px;
      background-color: var(--bg-surface);
      border-right: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      flex-shrink: 0;
      height: 100vh;
    }}

    .sidebar-header {{
      padding: 24px 20px 16px 20px;
      border-bottom: 1px solid var(--border);
    }}

    .brand {{
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 18px; /* text-lg */
      font-weight: 600;
      letter-spacing: -0.02em;
      color: var(--text-main);
    }}

    .brand-logo {{
      width: 24px;
      height: 24px;
      flex-shrink: 0;
    }}

    .progress-bar-container {{
      margin-top: 16px;
      background-color: #000000;
      border-radius: 9999px;
      height: 6px;
      overflow: hidden;
    }}

    .progress-bar-fill {{
      background-color: var(--text-main);
      height: 100%;
      width: 0%;
      transition: width 500ms var(--ease-base);
    }}

    .progress-text {{
      display: flex;
      justify-content: space-between;
      font-size: 12px; /* text-xs */
      line-height: 16px;
      color: var(--text-muted);
      margin-top: 8px;
      font-variant-numeric: tabular-nums;
    }}

    .search-box {{
      padding: 12px 16px;
      border-bottom: 1px solid var(--border);
    }}

    .search-input {{
      width: 100%;
      background-color: var(--bg-card);
      border: 1px solid var(--border);
      color: var(--text-main);
      padding: 8px 12px;
      border-radius: 8px; /* rounded-lg */
      font-size: 14px; /* text-sm */
      font-family: inherit;
      transition: border-color 300ms var(--ease-base);
    }}

    .search-input:focus {{
      outline: none;
      border-color: var(--border-focus);
    }}

    .module-list {{
      flex: 1;
      overflow-y: auto;
      padding: 12px;
    }}

    .module-card {{
      background-color: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 12px; /* rounded-xl */
      padding: 12px 16px;
      margin-bottom: 8px;
      cursor: pointer;
      transition: background-color 300ms var(--ease-base), transform 300ms var(--ease-base), border-color 300ms var(--ease-base);
    }}

    .module-card:hover {{
      background-color: var(--bg-card-hover);
      border-color: #404040;
    }}

    .module-card:active {{
      transform: scale(0.98);
    }}

    .module-card.active {{
      background-color: #313131;
      border-color: var(--text-main);
    }}

    .module-card-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 6px;
    }}

    .badge {{
      font-size: 12px; /* text-xs */
      line-height: 16px;
      font-weight: 500;
      padding: 2px 8px;
      border-radius: 4px;
      background-color: #181818;
      color: var(--text-muted);
      border: 1px solid var(--border);
    }}

    .module-card-title {{
      font-size: 14px; /* text-sm */
      line-height: 20px;
      font-weight: 600;
      color: var(--text-main);
      text-wrap: balance;
    }}

    .module-card-footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 8px;
      font-size: 12px; /* text-xs */
      color: var(--text-muted);
      font-variant-numeric: tabular-nums;
    }}

    /* MAIN CONTENT VIEWPORT */
    #main-content {{
      flex: 1;
      display: flex;
      flex-direction: column;
      height: 100vh;
      overflow: hidden;
      background-color: var(--bg-base);
    }}

    .topbar {{
      padding: 12px 32px;
      border-bottom: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
      background-color: var(--bg-surface);
      gap: 16px;
    }}

    .tabs {{
      display: flex;
      gap: 8px;
    }}

    .tab-btn {{
      background-color: transparent;
      border: 1px solid var(--border);
      color: var(--text-muted);
      padding: 8px 14px;
      border-radius: 8px;
      font-size: 14px; /* text-sm */
      font-weight: 500;
      cursor: pointer;
      font-family: inherit;
      transition: background-color 300ms var(--ease-base), color 300ms var(--ease-base), border-color 300ms var(--ease-base);
    }}

    .tab-btn:hover {{
      background-color: var(--bg-card);
      color: var(--text-main);
    }}

    .tab-btn:active {{
      transform: scale(0.98);
    }}

    .tab-btn.active {{
      background-color: var(--text-main);
      color: #000000;
      border-color: var(--text-main);
      font-weight: 600;
    }}

    .top-actions {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .github-repo-input {{
      background-color: var(--bg-card);
      border: 1px solid var(--border);
      color: var(--text-muted);
      padding: 8px 12px;
      border-radius: 8px;
      font-size: 12px;
      font-family: 'Geist Mono', monospace;
      width: 240px;
      transition: border-color 300ms var(--ease-base);
    }}

    .github-repo-input:focus {{
      outline: none;
      border-color: var(--border-focus);
      color: var(--text-main);
    }}

    .content-body {{
      flex: 1;
      overflow-y: auto;
      padding: 40px 48px;
      line-height: 24px;
      max-width: 1100px;
    }}

    /* TYPOGRAPHY RULES (B1 & Redesign Audit) */
    .markdown-view h1 {{
      font-size: 36px; /* text-4xl */
      line-height: 40px;
      font-weight: 600;
      margin-bottom: 24px;
      letter-spacing: -0.03em;
      text-wrap: balance;
      /* Permitted Hero Text Gradient: White -> #9B9B9B */
      background: linear-gradient(to right, #FFFFFF, #9B9B9B);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .markdown-view h2 {{
      font-size: 24px; /* text-2xl */
      line-height: 32px;
      font-weight: 600;
      margin-top: 32px;
      margin-bottom: 16px;
      color: var(--text-main);
      letter-spacing: -0.02em;
      border-bottom: 1px solid var(--border);
      padding-bottom: 8px;
      text-wrap: balance;
    }}

    .markdown-view h3 {{
      font-size: 18px; /* text-lg */
      line-height: 28px;
      font-weight: 600;
      margin-top: 24px;
      margin-bottom: 12px;
      color: var(--text-main);
      text-wrap: balance;
    }}

    .markdown-view p {{
      font-size: 16px; /* text-base */
      line-height: 24px;
      margin-bottom: 16px;
      color: #E2E8F0;
      text-wrap: pretty;
      max-width: 72ch;
    }}

    .markdown-view ul, .markdown-view ol {{
      margin-left: 24px;
      margin-bottom: 20px;
      color: #E2E8F0;
    }}

    .markdown-view li {{
      margin-bottom: 8px;
      line-height: 24px;
    }}

    .markdown-view code {{
      font-family: 'Geist Mono', monospace;
      font-size: 14px;
      background-color: var(--bg-card);
      padding: 2px 6px;
      border-radius: 4px;
      color: #F8FAFC;
      border: 1px solid var(--border);
    }}

    .markdown-view table {{
      width: 100%;
      border-collapse: collapse;
      margin: 24px 0;
      font-size: 14px;
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid var(--border);
    }}

    .markdown-view th, .markdown-view td {{
      padding: 12px 16px;
      text-align: left;
      border-bottom: 1px solid var(--border);
    }}

    .markdown-view th {{
      background-color: var(--bg-surface);
      color: var(--text-main);
      font-weight: 600;
    }}

    .markdown-view td {{
      background-color: var(--bg-base);
      color: #E2E8F0;
      font-variant-numeric: tabular-nums;
    }}

    /* INTERACTIVE NOTEBOOK CELLS */
    .cell {{
      margin-bottom: 24px;
      border-radius: 12px; /* rounded-xl */
      overflow: hidden;
      border: 1px solid var(--border);
      background-color: var(--bg-surface);
    }}

    .cell-header {{
      background-color: var(--bg-card);
      padding: 8px 16px;
      font-size: 12px;
      color: var(--text-muted);
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border);
      font-family: 'Geist Mono', monospace;
    }}

    .cell-markdown {{
      padding: 24px;
      background-color: var(--bg-surface);
    }}

    .cell-code {{
      background-color: var(--code-bg);
      padding: 0;
      overflow-x: auto;
    }}

    .cell-code pre {{
      margin: 0 !important;
      padding: 20px !important;
      background: transparent !important;
      font-family: 'Geist Mono', monospace !important;
      font-size: 13px !important;
      line-height: 20px !important;
    }}

    /* PRO-LEVEL ACTION BUTTONS */
    .action-btn {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 14px;
      font-weight: 600;
      padding: 8px 16px;
      border-radius: 8px;
      cursor: pointer;
      text-decoration: none;
      border: none;
      font-family: inherit;
      transition: transform 200ms var(--ease-base), opacity 200ms var(--ease-base), background-color 200ms var(--ease-base);
    }}

    .action-btn:active {{
      transform: scale(0.98);
    }}

    .colab-cta-btn {{
      background-color: var(--accent-cta);
      color: #FFFFFF;
    }}

    .colab-cta-btn:hover {{
      background-color: #EA580C;
    }}

    /* NOTICE BANNER IN LESSON */
    .colab-banner {{
      background-color: var(--bg-surface);
      border: 1px solid var(--border);
      border-left: 4px solid var(--accent-cta);
      padding: 16px 20px;
      border-radius: 12px;
      margin-bottom: 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 20px;
    }}

    .colab-banner-title {{
      font-size: 14px;
      font-weight: 600;
      color: var(--text-main);
      margin-bottom: 4px;
    }}

    .colab-banner-desc {{
      font-size: 13px;
      color: var(--text-muted);
      line-height: 18px;
    }}

    /* REDUCED MOTION PREFERENCE */
    @media (prefers-reduced-motion: reduce) {{
      *, *::before, *::after {{
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
      }}
    }}
  </style>
</head>
<body>

  <!-- SIDEBAR -->
  <aside id="sidebar">
    <div class="sidebar-header">
      <div class="brand">
        <!-- Minimal Solar Lens SVG Icon -->
        <svg class="brand-logo" viewBox="0 0 64 64" fill="none">
          <circle cx="28" cy="28" r="20" fill="#181818" stroke="#FFFFFF" stroke-width="4"/>
          <rect x="19" y="27" width="3.5" height="12" rx="1" fill="#9B9B9B"/>
          <rect x="26" y="21" width="3.5" height="18" rx="1" fill="#FFFFFF"/>
          <rect x="33" y="16" width="3.5" height="23" rx="1" fill="#F97316"/>
          <rect x="41" y="41" width="6" height="18" rx="3" transform="rotate(-45 41 41)" fill="#FFFFFF"/>
        </svg>
        <span>Data Analyst 2027</span>
      </div>

      <div class="progress-bar-container">
        <div id="progress-bar" class="progress-bar-fill"></div>
      </div>
      <div class="progress-text">
        <span>Прогресс курса</span>
        <span id="progress-val">0%</span>
      </div>
    </div>

    <div class="search-box">
      <input type="text" id="search-input" class="search-input" placeholder="Поиск по темам, SQL, Python, AI...">
    </div>

    <div id="module-list" class="module-list"></div>
  </aside>

  <!-- MAIN VIEWPORT -->
  <main id="main-content">
    <header class="topbar">
      <nav class="tabs" id="view-tabs">
        <button class="tab-btn active" onclick="switchTab('notebooks')">Уроки и код (.ipynb)</button>
        <button class="tab-btn" onclick="switchTab('overview')">Обзор модуля</button>
        <button class="tab-btn" onclick="switchTab('quiz')">Quiz проверка</button>
        <button class="tab-btn" id="cheatsheet-tab-btn" onclick="switchTab('cheatsheet')">Шпаргалка</button>
      </nav>

      <div class="top-actions">
        <input type="text" id="github-repo" class="github-repo-input" title="GitHub username/repo" value="Enlyl/data-analyst-2027" placeholder="Enlyl/data-analyst-2027" onchange="saveGithubRepo(this.value)">
      </div>
    </header>

    <div id="content-body" class="content-body"></div>
  </main>

  <script>
    const courseData = {json.dumps(course_data, ensure_ascii=False)};
    let currentModuleIndex = 0;
    let currentTab = 'notebooks';
    let currentNotebookIndex = 0;

    function getProgress() {{
      try {{
        return JSON.parse(localStorage.getItem('da_2027_progress')) || {{}};
      }} catch (e) {{
        return {{}};
      }}
    }}

    function saveProgress(id, completed) {{
      const p = getProgress();
      p[id] = completed;
      localStorage.setItem('da_2027_progress', JSON.stringify(p));
      updateProgressBar();
    }}

    function getGithubRepo() {{
      return localStorage.getItem('da_2027_gh_repo') || 'Enlyl/data-analyst-2027';
    }}

    function saveGithubRepo(val) {{
      localStorage.setItem('da_2027_gh_repo', val.trim());
      renderContent();
    }}

    function updateProgressBar() {{
      const p = getProgress();
      const total = courseData.length;
      let count = 0;
      courseData.forEach(m => {{
        if (p[m.id]) count++;
      }});
      const pct = Math.round((count / total) * 100);
      document.getElementById('progress-bar').style.width = pct + '%';
      document.getElementById('progress-val').innerText = pct + '% (' + count + '/' + total + ')';
    }}

    function renderSidebar(filtered = courseData) {{
      const list = document.getElementById('module-list');
      list.innerHTML = '';
      const p = getProgress();

      filtered.forEach((m, idx) => {{
        const isDone = !!p[m.id];
        const card = document.createElement('div');
        card.className = `module-card ${{idx === currentModuleIndex ? 'active' : ''}}`;
        card.onclick = () => selectModule(idx);

        card.innerHTML = `
          <div class="module-card-header">
            <span class="badge">${{m.badge}}</span>
            <input type="checkbox" ${{isDone ? 'checked' : ''}} onclick="event.stopPropagation(); toggleModuleDone('${{m.id}}', this.checked)">
          </div>
          <div class="module-card-title">${{m.title}}</div>
          <div class="module-card-footer">
            <span>${{m.category}}</span>
            <span>${{m.notebooks.length}} уроков</span>
          </div>
        `;
        list.appendChild(card);
      }});
    }}

    function toggleModuleDone(id, isChecked) {{
      saveProgress(id, isChecked);
    }}

    function selectModule(index) {{
      currentModuleIndex = index;
      currentNotebookIndex = 0;
      renderSidebar();
      renderContent();
    }}

    function switchTab(tab) {{
      currentTab = tab;
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      event.target.classList.add('active');
      renderContent();
    }}

    function renderContent() {{
      const body = document.getElementById('content-body');
      const mod = courseData[currentModuleIndex];
      if (!mod) return;

      const csBtn = document.getElementById('cheatsheet-tab-btn');
      csBtn.style.display = mod.cheatsheet ? 'inline-block' : 'none';

      if (currentTab === 'overview') {{
        body.innerHTML = `
          <div class="markdown-view">
            ${{marked.parse(mod.readme || 'Обзор отсутствует')}}
          </div>
        `;
      }} else if (currentTab === 'quiz') {{
        body.innerHTML = `
          <div class="markdown-view">
            ${{marked.parse(mod.quiz || 'Тест отсутствует')}}
          </div>
        `;
      }} else if (currentTab === 'cheatsheet') {{
        body.innerHTML = `
          <div class="markdown-view">
            ${{marked.parse(mod.cheatsheet || 'Шпаргалка отсутствует')}}
          </div>
        `;
      }} else if (currentTab === 'notebooks') {{
        renderNotebooksView(mod);
      }}

      Prism.highlightAll();
    }}

    function renderNotebooksView(mod) {{
      const body = document.getElementById('content-body');
      if (!mod.notebooks || mod.notebooks.length === 0) {{
        body.innerHTML = '<p style="color:var(--text-muted)">В этом модуле нет уроков в формате .ipynb</p>';
        return;
      }}

      let navHtml = '<div style="display:flex; gap:8px; margin-bottom:24px; flex-wrap:wrap;">';
      mod.notebooks.forEach((nb, i) => {{
        navHtml += `
          <button class="tab-btn ${{i === currentNotebookIndex ? 'active' : ''}}" onclick="currentNotebookIndex=${{i}}; renderNotebooksView(courseData[currentModuleIndex]);">
            ${{nb.filename.replace('.ipynb', '')}}
          </button>
        `;
      }});
      navHtml += '</div>';

      const activeNb = mod.notebooks[currentNotebookIndex];
      const ghRepo = getGithubRepo();
      const colabDirectUrl = `https://colab.research.google.com/github/${{ghRepo}}/blob/main/${{activeNb.rel_path}}`;

      let bannerHtml = `
        <div class="colab-banner">
          <div>
            <div class="colab-banner-title">Интерактивный запуск в Google Colab</div>
            <div class="colab-banner-desc">Откройте урок в облаке для выполнения кода и выполнения практических заданий</div>
          </div>
          <a class="action-btn colab-cta-btn" target="_blank" href="${{colabDirectUrl}}">
            Запустить в Colab
          </a>
        </div>
      `;

      let cellsHtml = '';
      activeNb.cells.forEach((c, idx) => {{
        if (c.type === 'markdown') {{
          cellsHtml += `
            <div class="cell">
              <div class="cell-header">
                <span>Теория и кейс · Блок #${{idx+1}}</span>
              </div>
              <div class="cell-markdown markdown-view">
                ${{marked.parse(c.content)}}
              </div>
            </div>
          `;
        }} else if (c.type === 'code') {{
          cellsHtml += `
            <div class="cell">
              <div class="cell-header">
                <span>Python Executable · Блок #${{idx+1}}</span>
                <button style="background:transparent; border:none; color:var(--text-muted); cursor:pointer; font-size:12px; font-family:inherit;" onclick="navigator.clipboard.writeText(this.parentElement.nextElementSibling.innerText); this.innerText='Скопировано'; setTimeout(()=>this.innerText='Копировать код', 1500)">Копировать код</button>
              </div>
              <div class="cell-code">
                <pre><code class="language-python">${{escapeHtml(c.content)}}</code></pre>
              </div>
            </div>
          `;
        }}
      }});

      body.innerHTML = `
        <div class="markdown-view">
          <h1>${{activeNb.filename.replace('.ipynb', '')}}</h1>
          <p style="color:var(--text-muted); font-family:'Geist Mono',monospace; font-size:13px; margin-bottom:20px;">
            ${{activeNb.rel_path}}
          </p>
        </div>
        ${{bannerHtml}}
        ${{navHtml}}
        <div>${{cellsHtml}}</div>
      `;
    }}

    function escapeHtml(str) {{
      return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    }}

    document.getElementById('search-input').addEventListener('input', (e) => {{
      const q = e.target.value.toLowerCase();
      const filtered = courseData.filter(m => 
        m.title.toLowerCase().includes(q) || 
        m.category.toLowerCase().includes(q) ||
        m.badge.toLowerCase().includes(q)
      );
      renderSidebar(filtered);
    }});

    const savedRepo = getGithubRepo();
    if (savedRepo) {{
      document.getElementById('github-repo').value = savedRepo;
    }}
    renderSidebar();
    renderContent();
    updateProgressBar();
  </script>
</body>
</html>
"""

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(html_content)
with open(PORTAL_HTML, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Design-polished portal successfully created at {OUTPUT_HTML} and {PORTAL_HTML}")
