import os
import json
import glob

BASE_DIR = r"d:\vibe_app\main_data_analytics\course"
OUTPUT_HTML = r"d:\vibe_app\main_data_analytics\index.html"
PORTAL_HTML = os.path.join(BASE_DIR, "index.html")

modules = [
    {"id": "module_00_onboarding", "title": "Модуль 0: Онбординг & Мышление 2027", "category": "Фундамент", "badge": "Старт"},
    {"id": "module_01_excel", "title": "Модуль 1: Excel & Google Sheets", "category": "Хард-база", "badge": "Таблицы"},
    {"id": "module_02_sql", "title": "Модуль 2: SQL Master: От SELECT до Оконных функций", "category": "Хард-база", "badge": "SQL"},
    {"id": "module_03_python", "title": "Модуль 3: Python & Pandas (AI-Assisted)", "category": "Хард-база", "badge": "Python"},
    {"id": "module_04_data_cleaning", "title": "Модуль 4: Очистка данных & Data Quality", "category": "Хард-база", "badge": "Data Quality"},
    {"id": "module_05_statistics", "title": "Модуль 5: Статистика & Регрессия", "category": "Математика", "badge": "Статистика"},
    {"id": "module_06_bi_looker_studio", "title": "Модуль 6: BI-аналитика в Looker Studio", "category": "Визуализация", "badge": "BI"},
    {"id": "module_07_ab_testing", "title": "Модуль 7: A/B-тестирование & Эксперименты", "category": "Эксперименты", "badge": "A/B"},
    {"id": "module_08_prompt_engineering", "title": "Модуль 8: Prompt Engineering для аналитика", "category": "AI Стек", "badge": "AI"},
    {"id": "module_09_ai_tools_daily", "title": "Модуль 9: AI в ежедневной работе (Cursor, Copilot)", "category": "AI Стек", "badge": "AI"},
    {"id": "module_10_llm_api", "title": "Модуль 10: LLM API & Неструктурированные данные", "category": "AI Стек", "badge": "AI"},
    {"id": "module_11_rag_vector_db", "title": "Модуль 11: RAG & Векторные базы данных", "category": "AI Стек", "badge": "AI"},
    {"id": "module_12_ai_agents", "title": "Модуль 12: AI-агенты (Agentic Workflows)", "category": "AI Стек", "badge": "AI"},
    {"id": "module_13_soft_skills_storytelling", "title": "Модуль 13: Soft Skills, Юнит-экономика & Storytelling", "category": "Бизнес", "badge": "Soft Skills"},
    {"id": "module_14_portfolio_project_1", "title": "Проект 1: E-Commerce 360° Audit", "category": "Портфолио", "badge": "Проект"},
    {"id": "module_15_portfolio_project_2", "title": "Проект 2: SaaS Product Analytics & A/B", "category": "Портфолио", "badge": "Проект"},
    {"id": "module_16_portfolio_project_3", "title": "Проект 3: AI-Driven BI Pipeline & Assistant", "category": "Портфолио", "badge": "Проект"},
    {"id": "module_17_career", "title": "Модуль 17: Карьера 2027: Резюме & Собеседования", "category": "Карьера", "badge": "Карьера"}
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

html_content = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Data Analyst 2027: Интерактивный портал курса</title>
  <!-- Favicon: Magnifier & Data Analytics -->
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Cdefs%3E%3ClinearGradient id='lg' x1='0%25' y1='0%25' x2='100%25' y2='100%25'%3E%3Cstop offset='0%25' stop-color='%2338bdf8'/%3E%3Cstop offset='100%25' stop-color='%23818cf8'/%3E%3C/linearGradient%3E%3C/defs%3E%3Ccircle cx='28' cy='28' r='24' fill='%230f172a'/%3E%3Ccircle cx='28' cy='28' r='19' fill='%231e293b' stroke='url(%23lg)' stroke-width='4'/%3E%3Crect x='18' y='27' width='4' height='13' rx='1.5' fill='%2338bdf8'/%3E%3Crect x='25' y='20' width='4' height='20' rx='1.5' fill='%23818cf8'/%3E%3Crect x='32' y='14' width='4' height='26' rx='1.5' fill='%2334d399'/%3E%3Cpath d='M16 29 L 26 19 L 35 13' stroke='%23f8fafc' stroke-width='2.5' stroke-linecap='round' fill='none'/%3E%3Crect x='42' y='42' width='7' height='20' rx='3.5' transform='rotate(-45 42 42)' fill='%23818cf8'/%3E%3C/svg%3E">
  <link rel="alternate icon" href="favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap">
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-sql.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-bash.min.js"></script>

  <style>
    :root {{
      --bg-dark: #0f172a;
      --bg-card: #1e293b;
      --bg-hover: #334155;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --accent: #38bdf8;
      --accent-gradient: linear-gradient(135deg, #38bdf8 0%, #818cf8 100%);
      --accent-green: #34d399;
      --border: #334155;
      --code-bg: #090d16;
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      font-family: 'Inter', -apple-system, sans-serif;
      background: var(--bg-dark);
      color: var(--text-main);
      display: flex;
      height: 100vh;
      overflow: hidden;
    }}
    /* SIDEBAR */
    #sidebar {{
      width: 380px;
      background: #111827;
      border-right: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      flex-shrink: 0;
      height: 100vh;
    }}
    .sidebar-header {{
      padding: 16px 20px;
      border-bottom: 1px solid var(--border);
      background: rgba(17, 24, 39, 0.95);
    }}
    .brand {{
      display: flex;
      align-items: center;
      gap: 10px;
      font-weight: 800;
      font-size: 1.15rem;
      background: var(--accent-gradient);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    .progress-bar-container {{
      margin-top: 12px;
      background: #1f2937;
      border-radius: 999px;
      height: 7px;
      overflow: hidden;
    }}
    .progress-bar-fill {{
      background: var(--accent-gradient);
      height: 100%;
      width: 0%;
      transition: width 0.3s ease;
    }}
    .progress-text {{
      display: flex;
      justify-content: space-between;
      font-size: 0.75rem;
      color: var(--text-muted);
      margin-top: 5px;
    }}
    .search-box {{
      padding: 10px 16px;
      border-bottom: 1px solid var(--border);
    }}
    .search-input {{
      width: 100%;
      background: #1f2937;
      border: 1px solid var(--border);
      color: #fff;
      padding: 8px 12px;
      border-radius: 6px;
      font-size: 0.85rem;
    }}
    .search-input:focus {{
      outline: 1px solid var(--accent);
    }}
    .module-list {{
      flex: 1;
      overflow-y: auto;
      padding: 10px;
    }}
    .module-card {{
      background: var(--bg-card);
      border: 1px solid transparent;
      border-radius: 8px;
      padding: 12px;
      margin-bottom: 8px;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .module-card:hover {{
      background: var(--bg-hover);
      border-color: var(--accent);
      transform: translateY(-1px);
    }}
    .module-card.active {{
      background: #1e3a8a;
      border-color: var(--accent);
    }}
    .module-card-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 4px;
    }}
    .badge {{
      font-size: 0.65rem;
      font-weight: 600;
      padding: 2px 6px;
      border-radius: 4px;
      background: #374151;
      color: var(--accent);
    }}
    .module-card-title {{
      font-size: 0.85rem;
      font-weight: 600;
      line-height: 1.3;
    }}
    .module-card-footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 6px;
      font-size: 0.72rem;
      color: var(--text-muted);
    }}

    /* MAIN CONTENT VIEW */
    #main-content {{
      flex: 1;
      display: flex;
      flex-direction: column;
      height: 100vh;
      overflow: hidden;
      background: var(--bg-dark);
    }}
    .topbar {{
      padding: 12px 28px;
      border-bottom: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #111827;
      gap: 16px;
    }}
    .tabs {{
      display: flex;
      gap: 8px;
    }}
    .tab-btn {{
      background: transparent;
      border: 1px solid var(--border);
      color: var(--text-muted);
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 0.85rem;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .tab-btn:hover {{
      background: var(--bg-hover);
      color: #fff;
    }}
    .tab-btn.active {{
      background: var(--accent);
      color: #0f172a;
      border-color: var(--accent);
      font-weight: 600;
    }}
    .top-actions {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .github-repo-input {{
      background: #1f2937;
      border: 1px solid var(--border);
      color: #94a3b8;
      padding: 6px 10px;
      border-radius: 6px;
      font-size: 0.75rem;
      width: 220px;
    }}
    .github-repo-input:focus {{
      outline: 1px solid var(--accent);
      color: #fff;
    }}
    .action-btn {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 0.8rem;
      font-weight: 600;
      padding: 6px 12px;
      border-radius: 6px;
      cursor: pointer;
      text-decoration: none;
      border: none;
      transition: opacity 0.2s ease;
    }}
    .action-btn:hover {{
      opacity: 0.88;
    }}
    .colab-btn {{
      background: #f97316;
      color: #fff;
    }}
    .download-btn {{
      background: #2563eb;
      color: #fff;
    }}
    .content-body {{
      flex: 1;
      overflow-y: auto;
      padding: 28px 40px;
      line-height: 1.6;
    }}

    /* MARKDOWN STYLES */
    .markdown-view h1 {{
      font-size: 1.8rem;
      margin-bottom: 16px;
      background: var(--accent-gradient);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    .markdown-view h2 {{
      font-size: 1.4rem;
      margin-top: 24px;
      margin-bottom: 12px;
      color: #e2e8f0;
      border-bottom: 1px solid var(--border);
      padding-bottom: 6px;
    }}
    .markdown-view h3 {{
      font-size: 1.15rem;
      margin-top: 18px;
      margin-bottom: 8px;
      color: var(--accent);
    }}
    .markdown-view p {{
      margin-bottom: 12px;
      color: #cbd5e1;
    }}
    .markdown-view ul, .markdown-view ol {{
      margin-left: 24px;
      margin-bottom: 14px;
      color: #cbd5e1;
    }}
    .markdown-view li {{
      margin-bottom: 6px;
    }}
    .markdown-view table {{
      width: 100%;
      border-collapse: collapse;
      margin: 16px 0;
      font-size: 0.9rem;
    }}
    .markdown-view th, .markdown-view td {{
      border: 1px solid var(--border);
      padding: 8px 12px;
      text-align: left;
    }}
    .markdown-view th {{
      background: #1e293b;
      color: var(--accent);
    }}

    /* NOTEBOOK CELLS */
    .cell {{
      margin-bottom: 20px;
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid var(--border);
    }}
    .cell-header {{
      background: #1e293b;
      padding: 6px 12px;
      font-size: 0.75rem;
      color: var(--text-muted);
      display: flex;
      justify-content: space-between;
      border-bottom: 1px solid var(--border);
    }}
    .cell-markdown {{
      background: var(--bg-card);
      padding: 16px;
    }}
    .cell-code {{
      background: var(--code-bg);
      padding: 0;
      overflow-x: auto;
    }}
    .cell-code pre {{
      margin: 0 !important;
      padding: 16px !important;
      background: transparent !important;
    }}

    /* NOTICE BANNER */
    .colab-notice {{
      background: #1e293b;
      border-left: 4px solid #f97316;
      padding: 12px 16px;
      border-radius: 6px;
      margin-bottom: 20px;
      font-size: 0.85rem;
      color: #e2e8f0;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
    }}
  </style>
</head>
<body>

  <!-- SIDEBAR -->
  <div id="sidebar">
    <div class="sidebar-header">
      <div class="brand">
        <svg width="22" height="22" viewBox="0 0 64 64" fill="none" style="flex-shrink:0;">
          <circle cx="28" cy="28" r="19" fill="#1e293b" stroke="#38bdf8" stroke-width="4.5"/>
          <rect x="18" y="27" width="4" height="13" rx="1.5" fill="#38bdf8"/>
          <rect x="25" y="20" width="4" height="20" rx="1.5" fill="#818cf8"/>
          <rect x="32" y="14" width="4" height="26" rx="1.5" fill="#34d399"/>
          <path d="M16 29 L 26 19 L 35 13" stroke="#f8fafc" stroke-width="2.5" stroke-linecap="round" fill="none"/>
          <rect x="42" y="42" width="7" height="20" rx="3.5" transform="rotate(-45 42 42)" fill="#818cf8"/>
        </svg>
        <span>DATA ANALYST 2027</span>
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
      <input type="text" id="search-input" class="search-input" placeholder="🔍 Поиск по темам, SQL, Python, AI...">
    </div>

    <div id="module-list" class="module-list"></div>
  </div>

  <!-- MAIN CONTENT -->
  <div id="main-content">
    <div class="topbar">
      <div class="tabs" id="view-tabs">
        <button class="tab-btn active" onclick="switchTab('overview')">📖 Обзор модуля</button>
        <button class="tab-btn" onclick="switchTab('notebooks')">💻 Уроки & Код (.ipynb)</button>
        <button class="tab-btn" onclick="switchTab('quiz')">🧠 Quiz (Проверка)</button>
        <button class="tab-btn" id="cheatsheet-tab-btn" onclick="switchTab('cheatsheet')">📋 Шпаргалка</button>
      </div>

      <div class="top-actions">
        <input type="text" id="github-repo" class="github-repo-input" title="Ваш GitHub username/repo" value="Enlyl/data-analyst-2027" placeholder="Enlyl/data-analyst-2027" onchange="saveGithubRepo(this.value)">
      </div>
    </div>

    <div id="content-body" class="content-body"></div>
  </div>

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
      updateColabLink();
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
      updateColabLink();
    }}

    function switchTab(tab) {{
      currentTab = tab;
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      event.target.classList.add('active');
      renderContent();
    }}

    function updateColabLink() {{
      // Colab button is rendered inside the active lesson
    }}

    function downloadActiveNotebook() {{
      const mod = courseData[currentModuleIndex];
      if (!mod.notebooks || !mod.notebooks[currentNotebookIndex]) return;
      const nb = mod.notebooks[currentNotebookIndex];
      
      const blob = new Blob([nb.raw_json], {{ type: 'application/x-ipynb+json' }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = nb.filename;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
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

      updateColabLink();
      Prism.highlightAll();
    }}

    function renderNotebooksView(mod) {{
      const body = document.getElementById('content-body');
      if (!mod.notebooks || mod.notebooks.length === 0) {{
        body.innerHTML = '<p style="color:var(--text-muted)">В этом модуле нет ноутбуков .ipynb</p>';
        return;
      }}

      let navHtml = '<div style="display:flex; gap:8px; margin-bottom:20px; flex-wrap:wrap;">';
      mod.notebooks.forEach((nb, i) => {{
        navHtml += `
          <button class="tab-btn ${{i === currentNotebookIndex ? 'active' : ''}}" onclick="currentNotebookIndex=${{i}}; renderNotebooksView(courseData[currentModuleIndex]); updateColabLink();">
            📓 ${{nb.filename.replace('.ipynb', '')}}
          </button>
        `;
      }});
      navHtml += '</div>';

      const activeNb = mod.notebooks[currentNotebookIndex];
      const ghRepo = getGithubRepo();

      let noticeHtml = `
        <div class="colab-notice">
          <div>
            <strong>🚀 Интерактивный запуск:</strong><br>
            Урок готов к исполнению в облаке через Google Colab. Нажмите кнопку справа для запуска в 1 клик.
          </div>
          <a class="action-btn colab-btn" target="_blank" href="https://colab.research.google.com/github/${{ghRepo}}/blob/main/${{activeNb.rel_path}}">
            🚀 Запустить в Colab
          </a>
        </div>
      `;

      let cellsHtml = '';
      activeNb.cells.forEach((c, idx) => {{
        if (c.type === 'markdown') {{
          cellsHtml += `
            <div class="cell">
              <div class="cell-header">
                <span>Markdown Block #${{idx+1}}</span>
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
                <span>Python Cell #${{idx+1}}</span>
                <button style="background:transparent; border:none; color:var(--accent); cursor:pointer; font-size:0.75rem;" onclick="navigator.clipboard.writeText(this.parentElement.nextElementSibling.innerText); this.innerText='Скопировано!'; setTimeout(()=>this.innerText='Копировать код', 1500)">Копировать код</button>
              </div>
              <div class="cell-code">
                <pre><code class="language-python">${{escapeHtml(c.content)}}</code></pre>
              </div>
            </div>
          `;
        }}
      }});

      body.innerHTML = `
        <h2>${{activeNb.filename}}</h2>
        <p style="color:var(--text-muted); margin-bottom:12px;">Путь к файлу: <code>${{activeNb.filepath}}</code></p>
        ${{noticeHtml}}
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

print(f"Interactive portal updated at {OUTPUT_HTML} and {PORTAL_HTML}")
