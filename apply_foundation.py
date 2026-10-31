# -*- coding: utf-8 -*-
"""
Apply Foundation (ZURB) design system to Data Analyst 2027 HTML Portal.
Tokens:
  --foundation-primary: #1779ba
  --foundation-secondary: #767676
  --foundation-success: #3adb76
  --foundation-warning: #ffae00
  --foundation-alert: #cc4b37
  --foundation-black: #0a0a0a
  --foundation-white: #fefefe
  --foundation-medium-gray: #cacaca
  Radius: 3px
  Font: 'Helvetica Neue', Helvetica, Roboto, Arial, sans-serif
  Scale: h1 48/62, h2 40/52, h3 31/40, body 16/24
"""
import re

INDEX_PATH = r"d:\vibe_app\main_data_analytics\index.html"
COURSE_INDEX_PATH = r"d:\vibe_app\main_data_analytics\course\index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# Replace fonts in head: Foundation uses Helvetica Neue
old_fonts = '''  <!-- Fonts: Geist only (never Inter/Roboto/Arial) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500;600&display=swap" rel="stylesheet">'''

new_fonts = '''  <!-- Foundation (ZURB) Design System Typography: Helvetica Neue -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">'''

if old_fonts in html:
    html = html.replace(old_fonts, new_fonts, 1)

# Build Foundation CSS
foundation_css = '''<style>
    /* ===== FOUNDATION (ZURB) DESIGN SYSTEM TOKENS ===== */
    :root {
      /* Foundation Palette */
      --foundation-primary: #1779ba;
      --foundation-primary-hover: #126195;
      --foundation-secondary: #767676;
      --foundation-success: #3adb76;
      --foundation-warning: #ffae00;
      --foundation-alert: #cc4b37;
      --foundation-black: #0a0a0a;
      --foundation-white: #fefefe;
      --foundation-medium-gray: #cacaca;
      --foundation-light-gray: #f4f4f4;
      --foundation-subtle-blue: #eef6fb;

      /* Semantic Mappings */
      --bg-base: #f4f4f4;
      --bg-surface: #fefefe;
      --bg-card: #fefefe;
      --bg-card-hover: #f0f7fb;
      --bg-deep: #e6e6e6;
      --border: #cacaca;
      --border-focus: #1779ba;
      --text-main: #0a0a0a;
      --text-secondary: #333333;
      --text-muted: #767676;
      --text-dim: #8a8a8a;
      --accent: #1779ba;
      --accent-hover: #126195;
      --success: #3adb76;
      --error: #cc4b37;
      --warning: #ffae00;
      --code-bg: #1e1e1e;
      --code-text: #fefefe;

      /* Typography */
      --font-body: 'Helvetica Neue', Helvetica, Roboto, Arial, sans-serif;
      --font-mono: 'JetBrains Mono', 'SFMono-Regular', Consolas, Menlo, monospace;

      /* Type Scale (Foundation Spec) */
      --text-h1: 48px;
      --line-h1: 62px;
      --text-h2: 40px;
      --line-h2: 52px;
      --text-h3: 31px;
      --line-h3: 40px;
      --text-body: 16px;
      --line-body: 24px;

      /* Spacing rhythm */
      --space-1: 8px;
      --space-2: 16px;
      --space-3: 24px;
      --space-4: 32px;

      /* Radius: Foundation default is strictly 3px */
      --radius-default: 3px;
      --radius-pill: 3px;

      --ease: cubic-bezier(0.22, 1, 0.36, 1);
    }

    /* ===== RESET ===== */
    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html { height: 100%; }

    body {
      font-family: var(--font-body);
      background: var(--bg-base);
      color: var(--text-main);
      display: flex;
      height: 100vh;
      overflow: hidden;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    /* ===== SIDEBAR ===== */
    #sidebar {
      width: 340px;
      min-width: 340px;
      background: var(--bg-surface);
      border-right: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      height: 100vh;
      overflow: hidden;
    }

    .sidebar-header {
      padding: 20px 20px 16px;
      border-bottom: 1px solid var(--border);
      background: var(--foundation-white);
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 18px;
      font-weight: 700;
      letter-spacing: -0.01em;
      color: var(--foundation-primary);
    }

    .brand svg { width: 26px; height: 26px; flex-shrink: 0; }

    /* Progress */
    .progress-wrap { margin-top: 16px; }
    .progress-bar {
      background: var(--bg-deep);
      border-radius: var(--radius-default);
      height: 6px;
      overflow: hidden;
    }
    .progress-fill {
      background: var(--foundation-primary);
      height: 100%;
      width: 0%;
      transition: width 400ms var(--ease);
      border-radius: var(--radius-default);
    }
    .progress-label {
      display: flex;
      justify-content: space-between;
      font-size: 12px;
      line-height: 16px;
      color: var(--text-muted);
      margin-top: 8px;
      font-weight: 500;
    }

    /* Search */
    .search-box {
      padding: 12px 16px;
      border-bottom: 1px solid var(--border);
      background: var(--bg-surface);
    }
    .search-input {
      width: 100%;
      background: var(--foundation-white);
      border: 1px solid var(--border);
      border-radius: var(--radius-default);
      padding: 8px 12px 8px 36px;
      font-size: 14px;
      color: var(--text-main);
      font-family: var(--font-body);
      outline: none;
      transition: border-color 200ms var(--ease), box-shadow 200ms var(--ease);
    }
    .search-input:focus {
      border-color: var(--foundation-primary);
      box-shadow: 0 0 4px rgba(23, 121, 186, 0.35);
    }
    .search-input::placeholder { color: var(--text-dim); }
    .search-wrap {
      position: relative;
    }
    .search-icon {
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
      width: 16px;
      height: 16px;
    }

    /* Module list */
    .module-list {
      flex: 1;
      overflow-y: auto;
      padding: 8px 0;
      scrollbar-width: thin;
      scrollbar-color: var(--border) transparent;
      background: var(--bg-surface);
    }
    .module-list::-webkit-scrollbar { width: 5px; }
    .module-list::-webkit-scrollbar-thumb { background: var(--border); border-radius: 2px; }

    .cat-group { margin-bottom: 4px; }
    .cat-label {
      padding: 12px 20px 4px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: var(--foundation-secondary);
    }

    .mod-item {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 10px 20px;
      cursor: pointer;
      transition: background 150ms var(--ease);
      border-left: 3px solid transparent;
      font-size: 14px;
      line-height: 20px;
      color: var(--text-main);
    }
    .mod-item:hover {
      background: var(--bg-card-hover);
    }
    .mod-item.active {
      background: var(--foundation-subtle-blue);
      border-left-color: var(--foundation-primary);
      color: var(--foundation-primary);
      font-weight: 600;
    }
    .mod-item .mod-icon { font-size: 16px; flex-shrink: 0; width: 20px; text-align: center; }
    .mod-item .mod-badge {
      margin-left: auto;
      font-size: 11px;
      padding: 2px 8px;
      border-radius: var(--radius-default);
      background: var(--bg-deep);
      color: var(--text-secondary);
      font-weight: 600;
      flex-shrink: 0;
      border: 1px solid #d4d4d4;
    }
    .mod-item.active .mod-badge {
      background: #dbebf6;
      color: var(--foundation-primary);
      border-color: #bcd9ee;
    }
    .mod-item .check-done {
      color: var(--foundation-success);
      font-size: 14px;
      margin-left: 4px;
      font-weight: bold;
    }

    /* ===== MAIN CONTENT ===== */
    #main {
      flex: 1;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      background: var(--bg-base);
    }

    /* Top bar (Foundation Top-Bar Style) */
    .topbar {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 12px 32px;
      border-bottom: 1px solid var(--border);
      background: var(--foundation-white);
      min-height: 56px;
      box-shadow: 0 1px 2px rgba(10, 10, 10, 0.04);
    }
    .topbar-title {
      font-size: 16px;
      font-weight: 700;
      color: var(--foundation-black);
      flex: 1;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    /* Tabs */
    .tabs {
      display: flex;
      gap: 0;
      border-bottom: 1px solid var(--border);
      background: var(--foundation-white);
      padding: 0 32px;
    }
    .tab {
      padding: 12px 18px;
      font-size: 14px;
      font-weight: 600;
      color: var(--foundation-secondary);
      cursor: pointer;
      border-bottom: 3px solid transparent;
      transition: color 150ms var(--ease), border-color 150ms var(--ease);
      white-space: nowrap;
    }
    .tab:hover { color: var(--foundation-primary); }
    .tab.active {
      color: var(--foundation-primary);
      border-bottom-color: var(--foundation-primary);
    }

    /* Content area */
    #content-area {
      flex: 1;
      overflow-y: auto;
      padding: 32px;
      scrollbar-width: thin;
      scrollbar-color: var(--border) transparent;
      background: var(--bg-base);
    }
    #content-area::-webkit-scrollbar { width: 6px; }
    #content-area::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }

    /* ===== HERO (Foundation Style) ===== */
    .hero {
      text-align: center;
      padding: 64px 32px 48px;
      max-width: 900px;
      margin: 0 auto;
    }
    .hero-badge {
      display: inline-block;
      padding: 5px 14px;
      border-radius: var(--radius-default);
      border: 1px solid var(--border);
      background: var(--foundation-subtle-blue);
      font-size: 12px;
      font-weight: 700;
      color: var(--foundation-primary);
      margin-bottom: 24px;
      letter-spacing: 0.04em;
      text-transform: uppercase;
    }
    .hero h1 {
      font-size: var(--text-h1);
      line-height: var(--line-h1);
      font-weight: 700;
      max-width: 720px;
      margin: 0 auto 20px;
      color: var(--foundation-black);
      letter-spacing: -0.02em;
    }
    .hero p {
      font-size: 18px;
      line-height: 28px;
      color: var(--foundation-secondary);
      max-width: 680px;
      margin: 0 auto 36px;
    }
    .hero-stats {
      display: flex;
      justify-content: center;
      gap: 32px;
      margin-top: 36px;
      flex-wrap: wrap;
    }
    .hero-stat {
      text-align: center;
      background: var(--foundation-white);
      border: 1px solid var(--border);
      border-radius: var(--radius-default);
      padding: 16px 28px;
      min-width: 160px;
      box-shadow: 0 1px 3px rgba(10, 10, 10, 0.05);
    }
    .hero-stat-num {
      font-size: var(--text-h2);
      line-height: var(--line-h2);
      font-weight: 700;
      color: var(--foundation-primary);
      font-family: var(--font-body);
    }
    .hero-stat-label {
      font-size: 13px;
      line-height: 18px;
      color: var(--foundation-secondary);
      margin-top: 4px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    /* ===== NOTEBOOK LESSON VIEW ===== */
    .lesson-header {
      margin-bottom: 24px;
      background: var(--foundation-white);
      border: 1px solid var(--border);
      border-radius: var(--radius-default);
      padding: 24px;
      box-shadow: 0 1px 3px rgba(10, 10, 10, 0.04);
    }
    .lesson-header h2 {
      font-size: var(--text-h3);
      line-height: var(--line-h3);
      font-weight: 700;
      margin-bottom: 8px;
      color: var(--foundation-black);
    }
    .lesson-header .lesson-desc {
      font-size: 16px;
      line-height: 24px;
      color: var(--foundation-secondary);
    }

    /* Foundation Button */
    .colab-btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 10px 18px;
      background: var(--foundation-primary);
      border: 1px solid var(--foundation-primary-hover);
      border-radius: var(--radius-default);
      color: #ffffff;
      font-size: 14px;
      font-weight: 700;
      font-family: var(--font-body);
      cursor: pointer;
      text-decoration: none;
      transition: background 150ms var(--ease), border-color 150ms var(--ease);
      margin-bottom: 20px;
      box-shadow: 0 1px 2px rgba(10, 10, 10, 0.1);
    }
    .colab-btn:hover {
      background: var(--foundation-primary-hover);
      border-color: #0e4c75;
      color: #ffffff;
    }
    .colab-btn svg { width: 18px; height: 18px; fill: currentColor; }

    /* Notebook sub-tabs */
    .nb-tabs {
      display: flex;
      gap: 4px;
      border-bottom: 1px solid var(--border);
      margin-bottom: 20px;
      flex-wrap: wrap;
    }
    .nb-tab {
      padding: 8px 14px;
      font-size: 13px;
      font-weight: 600;
      color: var(--foundation-secondary);
      cursor: pointer;
      border-bottom: 2px solid transparent;
      border-radius: var(--radius-default) var(--radius-default) 0 0;
      transition: color 150ms var(--ease), background 150ms var(--ease);
      font-family: var(--font-body);
      white-space: nowrap;
    }
    .nb-tab:hover {
      color: var(--foundation-primary);
      background: var(--foundation-subtle-blue);
    }
    .nb-tab.active {
      color: var(--foundation-primary);
      border-bottom-color: var(--foundation-primary);
      background: var(--foundation-subtle-blue);
    }

    /* Cell rendering */
    .cell {
      margin-bottom: 16px;
      border-radius: var(--radius-default);
      overflow: hidden;
    }
    .cell-md {
      padding: 20px 24px;
      background: var(--foundation-white);
      border: 1px solid var(--border);
      border-radius: var(--radius-default);
      font-size: 16px;
      line-height: 24px;
      color: var(--text-secondary);
      box-shadow: 0 1px 2px rgba(10, 10, 10, 0.03);
    }
    .cell-md h1, .cell-md h2, .cell-md h3, .cell-md h4 {
      color: var(--foundation-black);
      margin-top: 24px;
      margin-bottom: 10px;
      font-weight: 700;
    }
    .cell-md h1 { font-size: 30px; line-height: 38px; }
    .cell-md h2 { font-size: 24px; line-height: 32px; border-bottom: 1px solid var(--border); padding-bottom: 6px; }
    .cell-md h3 { font-size: 20px; line-height: 28px; }
    .cell-md h4 { font-size: 17px; line-height: 24px; }
    .cell-md p { margin-bottom: 12px; }
    .cell-md ul, .cell-md ol { padding-left: 24px; margin-bottom: 12px; }
    .cell-md li { margin-bottom: 4px; }
    .cell-md code {
      background: var(--bg-deep);
      color: var(--foundation-black);
      padding: 2px 6px;
      border-radius: var(--radius-default);
      font-family: var(--font-mono);
      font-size: 14px;
      border: 1px solid #d4d4d4;
    }
    .cell-md pre {
      background: var(--code-bg);
      color: var(--code-text);
      border-radius: var(--radius-default);
      padding: 16px;
      overflow-x: auto;
      margin-bottom: 12px;
      border: 1px solid #333333;
    }
    .cell-md pre code { background: none; padding: 0; color: #fefefe; border: none; }
    .cell-md blockquote {
      border-left: 4px solid var(--foundation-primary);
      background: var(--foundation-subtle-blue);
      padding: 12px 16px;
      color: var(--text-secondary);
      margin: 12px 0;
      border-radius: 0 var(--radius-default) var(--radius-default) 0;
    }
    .cell-md table {
      width: 100%;
      border-collapse: collapse;
      margin: 14px 0;
      background: var(--foundation-white);
    }
    .cell-md th, .cell-md td {
      padding: 10px 14px;
      border: 1px solid var(--border);
      text-align: left;
      font-size: 14px;
    }
    .cell-md th {
      background: var(--bg-deep);
      font-weight: 700;
      color: var(--foundation-black);
    }
    .cell-md strong { color: var(--foundation-black); font-weight: 700; }
    .cell-md a { color: var(--foundation-primary); text-decoration: none; font-weight: 600; }
    .cell-md a:hover { text-decoration: underline; color: var(--foundation-primary-hover); }

    .cell-code {
      position: relative;
      background: var(--code-bg);
      border: 1px solid #333333;
      border-radius: var(--radius-default);
      box-shadow: 0 1px 3px rgba(10, 10, 10, 0.12);
    }
    .cell-code-label {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 8px 16px;
      font-size: 12px;
      font-weight: 600;
      color: #999999;
      border-bottom: 1px solid #333333;
      background: #181818;
      font-family: var(--font-mono);
      border-radius: var(--radius-default) var(--radius-default) 0 0;
    }
    .copy-btn {
      background: #2a2a2a;
      border: 1px solid #444444;
      border-radius: var(--radius-default);
      color: #cccccc;
      font-size: 11px;
      font-weight: 600;
      padding: 4px 10px;
      cursor: pointer;
      font-family: var(--font-body);
      transition: background 150ms var(--ease), color 150ms var(--ease);
    }
    .copy-btn:hover { color: #ffffff; background: #3a3a3a; border-color: #666666; }
    .cell-code pre {
      padding: 16px;
      overflow-x: auto;
      margin: 0;
      font-size: 14px;
      line-height: 22px;
      color: #fefefe;
    }
    .cell-code code {
      font-family: var(--font-mono);
    }

    /* ===== README / QUIZ / CHEATSHEET views ===== */
    .md-view {
      max-width: 860px;
      background: var(--foundation-white);
      border: 1px solid var(--border);
      border-radius: var(--radius-default);
      padding: 28px 32px;
      box-shadow: 0 1px 3px rgba(10, 10, 10, 0.04);
    }
    .md-view h1, .md-view h2, .md-view h3 {
      color: var(--foundation-black);
      margin-top: 24px;
      margin-bottom: 12px;
      font-weight: 700;
    }
    .md-view h1 { font-size: 30px; line-height: 38px; }
    .md-view h2 { font-size: 24px; line-height: 32px; border-bottom: 1px solid var(--border); padding-bottom: 6px; }
    .md-view h3 { font-size: 20px; line-height: 28px; }
    .md-view p { margin-bottom: 12px; color: var(--text-secondary); font-size: 16px; line-height: 24px; }
    .md-view ul, .md-view ol { padding-left: 24px; margin-bottom: 12px; color: var(--text-secondary); }
    .md-view li { margin-bottom: 6px; font-size: 16px; line-height: 24px; }
    .md-view code {
      background: var(--bg-deep);
      padding: 2px 6px;
      border-radius: var(--radius-default);
      font-family: var(--font-mono);
      font-size: 14px;
      border: 1px solid #d4d4d4;
    }
    .md-view pre {
      background: var(--code-bg);
      color: var(--code-text);
      border-radius: var(--radius-default);
      padding: 16px;
      overflow-x: auto;
      margin-bottom: 16px;
      border: 1px solid #333333;
    }
    .md-view pre code { background: none; padding: 0; color: #fefefe; border: none; }
    .md-view blockquote {
      border-left: 4px solid var(--foundation-primary);
      background: var(--foundation-subtle-blue);
      padding: 12px 16px;
      color: var(--text-secondary);
      margin: 12px 0;
      border-radius: 0 var(--radius-default) var(--radius-default) 0;
    }
    .md-view strong { color: var(--foundation-black); font-weight: 700; }
    .md-view a { color: var(--foundation-primary); text-decoration: none; font-weight: 600; }
    .md-view a:hover { text-decoration: underline; color: var(--foundation-primary-hover); }
    .md-view table { width: 100%; border-collapse: collapse; margin: 14px 0; }
    .md-view th, .md-view td { padding: 10px 14px; border: 1px solid var(--border); text-align: left; font-size: 14px; }
    .md-view th { background: var(--bg-deep); font-weight: 700; color: var(--foundation-black); }
    .md-view hr { border: none; border-top: 1px solid var(--border); margin: 24px 0; }

    /* ===== QUIZ INTERACTIVE ===== */
    .quiz-question {
      background: var(--foundation-white);
      border: 1px solid var(--border);
      border-radius: var(--radius-default);
      padding: 24px;
      margin-bottom: 16px;
      box-shadow: 0 1px 3px rgba(10, 10, 10, 0.04);
    }
    .quiz-question h3 {
      font-size: 16px;
      font-weight: 700;
      margin-bottom: 16px;
      color: var(--foundation-black);
    }
    .quiz-option {
      display: flex;
      align-items: flex-start;
      gap: 12px;
      padding: 12px 16px;
      border-radius: var(--radius-default);
      cursor: pointer;
      margin-bottom: 8px;
      border: 1px solid var(--border);
      background: var(--foundation-white);
      transition: background 150ms var(--ease), border-color 150ms var(--ease);
      font-size: 14px;
      line-height: 20px;
      color: var(--text-main);
    }
    .quiz-option:hover {
      background: var(--bg-card-hover);
      border-color: var(--foundation-primary);
    }
    .quiz-option.correct {
      border-color: var(--foundation-success);
      background: rgba(58, 219, 118, 0.16);
      color: #0b612c;
      font-weight: 600;
    }
    .quiz-option.wrong {
      border-color: var(--foundation-alert);
      background: rgba(204, 75, 55, 0.14);
      color: #8c2515;
    }
    .quiz-option .radio {
      width: 18px;
      height: 18px;
      border: 2px solid var(--border);
      border-radius: 50%;
      flex-shrink: 0;
      margin-top: 1px;
      transition: border-color 150ms var(--ease);
      background: #ffffff;
    }
    .quiz-option.correct .radio { border-color: var(--foundation-success); background: var(--foundation-success); }
    .quiz-option.wrong .radio { border-color: var(--foundation-alert); background: var(--foundation-alert); }
    .quiz-explanation {
      margin-top: 12px;
      padding: 14px 18px;
      background: var(--foundation-subtle-blue);
      border-left: 4px solid var(--foundation-primary);
      border-radius: 0 var(--radius-default) var(--radius-default) 0;
      font-size: 14px;
      line-height: 20px;
      color: var(--text-secondary);
      display: none;
    }
    .quiz-explanation.show { display: block; }

    .quiz-score {
      text-align: center;
      padding: 24px;
      background: var(--foundation-white);
      border-radius: var(--radius-default);
      border: 1px solid var(--border);
      margin-bottom: 24px;
      box-shadow: 0 1px 3px rgba(10, 10, 10, 0.04);
    }
    .quiz-score-num {
      font-size: 48px;
      font-weight: 700;
      font-family: var(--font-body);
      color: var(--foundation-primary);
    }
    .quiz-score-label {
      font-size: 13px;
      color: var(--foundation-secondary);
      margin-top: 4px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    /* Mark complete button */
    .complete-btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 10px 18px;
      background: var(--foundation-primary);
      border: 1px solid var(--foundation-primary-hover);
      border-radius: var(--radius-default);
      color: #ffffff;
      font-size: 14px;
      font-weight: 700;
      cursor: pointer;
      font-family: var(--font-body);
      transition: background 150ms var(--ease);
      margin-top: 24px;
      box-shadow: 0 1px 2px rgba(10, 10, 10, 0.1);
    }
    .complete-btn:hover { background: var(--foundation-primary-hover); }
    .complete-btn.done {
      background: var(--foundation-success);
      border-color: #2bb35f;
      color: #ffffff;
      cursor: default;
    }

    /* ===== LIEFLAT CHARTS (Foundation steel-blue & light card theme) ===== */
    .lf-charts-row {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 16px;
      max-width: 900px;
      margin: 40px auto 0;
    }
    .lf-card {
      background: var(--foundation-white);
      border-radius: var(--radius-default);
      padding: 20px 20px 14px;
      cursor: pointer;
      border: 1px solid var(--border);
      box-shadow: 0 1px 3px rgba(10, 10, 10, 0.05);
      transition: border-color 150ms var(--ease), box-shadow 150ms var(--ease);
    }
    .lf-card:hover {
      border-color: var(--foundation-primary);
      box-shadow: 0 2px 6px rgba(23, 121, 186, 0.15);
    }
    .lf-card h3 {
      font-size: 14px;
      font-weight: 700;
      letter-spacing: -0.01em;
      margin-bottom: 2px;
      color: var(--foundation-black);
    }
    .lf-card .lf-sub {
      font-size: 11px;
      color: var(--foundation-secondary);
      margin-bottom: 12px;
    }
    .lf-card svg { width: 100%; display: block; }
    .lf-card .lf-src {
      font-size: 9px;
      color: var(--foundation-secondary);
      margin-top: 8px;
      letter-spacing: 0.06em;
      font-weight: 600;
      text-transform: uppercase;
      font-family: var(--font-body);
    }
    .lf-pop { transform-box: fill-box; transform-origin: center bottom; animation: lfPop 0.5s cubic-bezier(0.2,0.7,0.3,1.3) both; }
    @keyframes lfPop { from { transform: scaleY(0); } to { transform: none; } }
    .lf-fade { animation: lfFade 0.9s ease both; }
    @keyframes lfFade { from { opacity: 0; } }
    .lf-draw { stroke-dasharray: 1; stroke-dashoffset: 1; animation: lfDraw 1.2s cubic-bezier(0.4,0,0.2,1) both; }
    @keyframes lfDraw { to { stroke-dashoffset: 0; } }
    .lf-dot-pop { transform-box: fill-box; transform-origin: center; animation: lfDotPop 0.4s cubic-bezier(0.2,0.7,0.3,1.3) both; }
    @keyframes lfDotPop { from { transform: scale(0); } to { transform: none; } }
    @media (max-width: 768px) {
      .lf-charts-row { grid-template-columns: 1fr; max-width: 320px; }
      #sidebar { display: none; }
    }

    /* Reduced motion */
    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after {
        transition-duration: 0.01ms !important;
        animation-duration: 0.01ms !important;
      }
      .lf-pop, .lf-fade, .lf-dot-pop { animation: none; }
      .lf-draw { animation: none; stroke-dasharray: none; stroke-dashoffset: 0; }
    }
  </style>'''

# Replace <style>...</style> block
style_pattern = re.compile(r'<style>.*?</style>', re.DOTALL)
html = style_pattern.sub(foundation_css, html, count=1)

# Now update the LF object and chart colors in JavaScript to Foundation theme
old_lf_engine = '''// ===== LIEFLAT CHARTS ENGINE (dark-adapted mono tokens) =====
const LF = {
  INK: '#FFFFFF', PAPER: '#272727', MUTED: '#9B9B9B', FAINT: '#666666',
  GRID: '#313131', ACCENT: '#F97316',
  L: ['#FFFFFF','#E0E0E0','#C0C0C0','#9B9B9B','#777777','#666666','#555555'],
  rnd: (i,k) => Math.abs(((i*73856093)^(k*19349663))%1000)/1000,
  el: (p,t,a) => { const n=document.createElementNS('http://www.w3.org/2000/svg',t); for(const k in a) n.setAttribute(k,a[k]); p.appendChild(n); return n; },
  txt: (p,a,s) => { const n=LF.el(p,'text',a); n.textContent=s; return n; },
};'''

new_lf_engine = '''// ===== LIEFLAT CHARTS ENGINE (Foundation ZURB Design Tokens) =====
const LF = {
  PRIMARY: '#1779ba',
  SECONDARY: '#767676',
  SUCCESS: '#3adb76',
  WARNING: '#ffae00',
  ALERT: '#cc4b37',
  INK: '#0a0a0a',
  PAPER: '#fefefe',
  MUTED: '#767676',
  FAINT: '#cacaca',
  GRID: '#e6e6e6',
  ACCENT: '#1779ba',
  // Foundation steel-blue shade ladder
  L: ['#1779ba', '#2486c7', '#3d9ad9', '#63b1e5', '#8fc6ee', '#bcdcf5', '#dceefb'],
  rnd: (i,k) => Math.abs(((i*73856093)^(k*19349663))%1000)/1000,
  el: (p,t,a) => { const n=document.createElementNS('http://www.w3.org/2000/svg',t); for(const k in a) n.setAttribute(k,a[k]); p.appendChild(n); return n; },
  txt: (p,a,s) => { const n=LF.el(p,'text',a); n.textContent=s; return n; },
};'''

if old_lf_engine in html:
    html = html.replace(old_lf_engine, new_lf_engine, 1)

# Update drawRungs function with Foundation colors
old_draw_rungs = '''function drawRungs() {
  const svg = document.getElementById('lfRungs');
  if (!svg) return;
  svg.innerHTML = '';

  const data = [
    {label: '\u0425\u0430\u0440\u0434', v: 5, shade: LF.L[0]},
    {label: 'AI',   v: 5, shade: LF.L[1]},
    {label: '\u041f\u043e\u0440\u0442\u0444.', v: 3, shade: LF.L[2]},
    {label: '\u0421\u0442\u0430\u0442\u044b', v: 2, shade: LF.L[3]},
    {label: '\u0421\u043e\u0444\u0442', v: 2, shade: LF.L[4]},
    {label: '\u041a\u0430\u0440\u044c\u0435\u0440\u0430', v: 1, shade: LF.L[5]},
  ];
  const maxV = Math.max(...data.map(d=>d.v));
  const barW = 28, gap = 12, startX = 50, startY = 175;
  const rungH = 6, rungGap = 3;

  data.forEach((d, i) => {
    const x = startX + i * (barW + gap);
    // Draw rungs (each rung = 1 module)
    for (let r = 0; r < d.v; r++) {
      const ry = startY - (r+1) * (rungH + rungGap);
      const rect = LF.el(svg, 'rect', {
        x: x, y: ry, width: barW, height: rungH,
        rx: 3, fill: d.shade,
        class: 'lf-pop',
        style: `animation-delay: ${(i * 100 + r * 30)}ms`
      });
    }
    // Value on top
    const topY = startY - d.v * (rungH + rungGap) - 6;
    LF.txt(svg, {x: x + barW/2, y: topY, 'text-anchor': 'middle', fill: LF.INK,
      'font-size': '11', 'font-weight': '700', 'font-family': "'Geist','Inter',sans-serif",
      class: 'lf-fade', style: `animation-delay: ${i * 100 + 200}ms`
    }, d.v);
    // Label below
    LF.txt(svg, {x: x + barW/2, y: startY + 14, 'text-anchor': 'middle', fill: LF.MUTED,
      'font-size': '9', 'font-weight': '600', 'font-family': "'Geist','Inter',sans-serif",
      class: 'lf-fade', style: `animation-delay: ${i * 100 + 100}ms`
    }, d.label);
  });

  // Baseline
  LF.el(svg, 'line', {x1: startX-8, y1: startY+1, x2: startX + data.length*(barW+gap)-gap+8, y2: startY+1,
    stroke: LF.GRID, 'stroke-width': '0.7'});
}'''

new_draw_rungs = '''function drawRungs() {
  const svg = document.getElementById('lfRungs');
  if (!svg) return;
  svg.innerHTML = '';

  const data = [
    {label: '\u0425\u0430\u0440\u0434', v: 5, shade: '#1779ba'},
    {label: 'AI',   v: 5, shade: '#2486c7'},
    {label: '\u041f\u043e\u0440\u0442\u0444.', v: 3, shade: '#3d9ad9'},
    {label: '\u0421\u0442\u0430\u0442\u044b', v: 2, shade: '#63b1e5'},
    {label: '\u0421\u043e\u0444\u0442', v: 2, shade: '#8fc6ee'},
    {label: '\u041a\u0430\u0440\u044c\u0435\u0440\u0430', v: 1, shade: '#bcdcf5'},
  ];
  const maxV = Math.max(...data.map(d=>d.v));
  const barW = 28, gap = 12, startX = 50, startY = 175;
  const rungH = 6, rungGap = 3;

  data.forEach((d, i) => {
    const x = startX + i * (barW + gap);
    // Draw rungs (Foundation 3px corner radius)
    for (let r = 0; r < d.v; r++) {
      const ry = startY - (r+1) * (rungH + rungGap);
      const rect = LF.el(svg, 'rect', {
        x: x, y: ry, width: barW, height: rungH,
        rx: 3, fill: d.shade,
        class: 'lf-pop',
        style: `animation-delay: ${(i * 100 + r * 30)}ms`
      });
    }
    // Value on top
    const topY = startY - d.v * (rungH + rungGap) - 6;
    LF.txt(svg, {x: x + barW/2, y: topY, 'text-anchor': 'middle', fill: '#0a0a0a',
      'font-size': '12', 'font-weight': '700', 'font-family': "'Helvetica Neue',Helvetica,Roboto,Arial,sans-serif",
      class: 'lf-fade', style: `animation-delay: ${i * 100 + 200}ms`
    }, d.v);
    // Label below
    LF.txt(svg, {x: x + barW/2, y: startY + 14, 'text-anchor': 'middle', fill: '#767676',
      'font-size': '10', 'font-weight': '600', 'font-family': "'Helvetica Neue',Helvetica,Roboto,Arial,sans-serif",
      class: 'lf-fade', style: `animation-delay: ${i * 100 + 100}ms`
    }, d.label);
  });

  // Baseline
  LF.el(svg, 'line', {x1: startX-8, y1: startY+1, x2: startX + data.length*(barW+gap)-gap+8, y2: startY+1,
    stroke: '#cacaca', 'stroke-width': '1'});
}'''

if old_draw_rungs in html:
    html = html.replace(old_draw_rungs, new_draw_rungs, 1)

# Update drawWaffle function with Foundation colors
old_draw_waffle = '''function drawWaffle() {
  const svg = document.getElementById('lfWaffle');
  if (!svg) return;
  svg.innerHTML = '';

  // Category dot counts (total ~67 notebooks)
  const cats = [
    {n: 24, color: '#FFFFFF', label: '\u0425\u0430\u0440\u0434 \u0431\u0430\u0437\u0430'},
    {n: 19, color: '#C0C0C0', label: 'AI \u0441\u0442\u0435\u043a'},
    {n:  8, color: '#F97316', label: '\u041f\u043e\u0440\u0442\u0444\u043e\u043b\u0438\u043e'},
    {n: 10, color: '#9B9B9B', label: '\u0421\u0442\u0430\u0442\u044b & A/B'},
    {n:  6, color: '#666666', label: '\u041e\u0441\u0442\u0430\u043b\u044c\u043d\u043e\u0435'},
  ];'''

new_draw_waffle = '''function drawWaffle() {
  const svg = document.getElementById('lfWaffle');
  if (!svg) return;
  svg.innerHTML = '';

  // Foundation Color Role dots (total ~67 notebooks)
  const cats = [
    {n: 24, color: '#1779ba', label: '\u0425\u0430\u0440\u0434 \u0431\u0430\u0437\u0430'},
    {n: 19, color: '#3adb76', label: 'AI \u0441\u0442\u0435\u043a'},
    {n:  8, color: '#ffae00', label: '\u041f\u043e\u0440\u0442\u0444\u043e\u043b\u0438\u043e'},
    {n: 10, color: '#cc4b37', label: '\u0421\u0442\u0430\u0442\u044b & A/B'},
    {n:  6, color: '#767676', label: '\u041e\u0441\u0442\u0430\u043b\u044c\u043d\u043e\u0435'},
  ];'''

if old_draw_waffle in html:
    html = html.replace(old_draw_waffle, new_draw_waffle, 1)

# Update drawLine with Foundation steel-blue
old_draw_line = '''  // Grid lines
  for (let g = 0; g <= 4; g++) {
    const gy = oy + (py - oy) * (1 - g/4);
    LF.el(svg, 'line', {x1: ox, y1: gy, x2: px, y2: gy, stroke: LF.GRID, 'stroke-width': '0.5'});
    LF.txt(svg, {x: ox - 4, y: gy + 3, 'text-anchor': 'end', fill: LF.FAINT,
      'font-size': '8', 'font-family': "'Geist Mono',monospace"
    }, Math.round(g * 25) + '%');
  }

  // Area fill
  let areaD = `M${ox} ${py}`;
  vals.forEach((v, i) => {
    const x = ox + i * sx;
    const y = oy + (py - oy) * (1 - v / maxV);
    areaD += ` L${x} ${y}`;
  });
  areaD += ` L${ox + (weeks-1)*sx} ${py} Z`;
  LF.el(svg, 'path', {d: areaD, fill: LF.INK, opacity: '0.06', class: 'lf-fade'});

  // Line with draw animation
  let lineD = '';
  vals.forEach((v, i) => {
    const x = ox + i * sx;
    const y = oy + (py - oy) * (1 - v / maxV);
    lineD += (i === 0 ? 'M' : ' L') + x.toFixed(1) + ' ' + y.toFixed(1);
  });
  const line = LF.el(svg, 'polyline', {
    points: lineD.replace(/[ML]/g,'').trim().replace(/ L/g, ' '),
    fill: 'none', stroke: LF.INK, 'stroke-width': '2',
    'stroke-linecap': 'round', 'stroke-linejoin': 'round',
    'pathLength': '1', class: 'lf-draw'
  });
  // Fix: polyline needs points not d. Redo with path:
  svg.removeChild(line);
  LF.el(svg, 'path', {
    d: lineD, fill: 'none', stroke: LF.INK, 'stroke-width': '2',
    'stroke-linecap': 'round', 'stroke-linejoin': 'round',
    'pathLength': '1', class: 'lf-draw'
  });

  // Dots at each week
  vals.forEach((v, i) => {
    const x = ox + i * sx;
    const y = oy + (py - oy) * (1 - v / maxV);
    LF.el(svg, 'circle', {
      cx: x, cy: y, r: 2.5,
      fill: (i === weeks - 1) ? LF.ACCENT : LF.INK,
      class: 'lf-dot-pop',
      style: `animation-delay: ${600 + i * 40}ms`
    });
  });

  // End value label
  const lastX = ox + (weeks-1) * sx;
  const lastY = oy + (py - oy) * (1 - vals[weeks-1] / maxV);
  LF.txt(svg, {x: lastX + 1, y: lastY - 8, 'text-anchor': 'middle', fill: LF.ACCENT,
    'font-size': '12', 'font-weight': '700', 'font-family': "'Geist Mono',monospace",
    class: 'lf-fade', style: 'animation-delay: 1200ms'
  }, vals[weeks-1] + '%');'''

new_draw_line = '''  // Grid lines
  for (let g = 0; g <= 4; g++) {
    const gy = oy + (py - oy) * (1 - g/4);
    LF.el(svg, 'line', {x1: ox, y1: gy, x2: px, y2: gy, stroke: '#e6e6e6', 'stroke-width': '1'});
    LF.txt(svg, {x: ox - 4, y: gy + 3, 'text-anchor': 'end', fill: '#767676',
      'font-size': '9', 'font-family': "'Helvetica Neue',Helvetica,Roboto,Arial,sans-serif"
    }, Math.round(g * 25) + '%');
  }

  // Area fill with subtle steel blue
  let areaD = `M${ox} ${py}`;
  vals.forEach((v, i) => {
    const x = ox + i * sx;
    const y = oy + (py - oy) * (1 - v / maxV);
    areaD += ` L${x} ${y}`;
  });
  areaD += ` L${ox + (weeks-1)*sx} ${py} Z`;
  LF.el(svg, 'path', {d: areaD, fill: '#1779ba', opacity: '0.12', class: 'lf-fade'});

  // Line with draw animation (Foundation primary steel blue)
  let lineD = '';
  vals.forEach((v, i) => {
    const x = ox + i * sx;
    const y = oy + (py - oy) * (1 - v / maxV);
    lineD += (i === 0 ? 'M' : ' L') + x.toFixed(1) + ' ' + y.toFixed(1);
  });
  LF.el(svg, 'path', {
    d: lineD, fill: 'none', stroke: '#1779ba', 'stroke-width': '2.5',
    'stroke-linecap': 'round', 'stroke-linejoin': 'round',
    'pathLength': '1', class: 'lf-draw'
  });

  // Dots at each week
  vals.forEach((v, i) => {
    const x = ox + i * sx;
    const y = oy + (py - oy) * (1 - v / maxV);
    LF.el(svg, 'circle', {
      cx: x, cy: y, r: 2.8,
      fill: (i === weeks - 1) ? '#ffae00' : '#1779ba',
      stroke: '#fefefe', 'stroke-width': '1',
      class: 'lf-dot-pop',
      style: `animation-delay: ${600 + i * 40}ms`
    });
  });

  // End value label
  const lastX = ox + (weeks-1) * sx;
  const lastY = oy + (py - oy) * (1 - vals[weeks-1] / maxV);
  LF.txt(svg, {x: lastX + 1, y: lastY - 8, 'text-anchor': 'middle', fill: '#1779ba',
    'font-size': '13', 'font-weight': '700', 'font-family': "'Helvetica Neue',Helvetica,Roboto,Arial,sans-serif",
    class: 'lf-fade', style: 'animation-delay: 1200ms'
  }, vals[weeks-1] + '%');'''

if old_draw_line in html:
    html = html.replace(old_draw_line, new_draw_line, 1)

# Update Brand SVG in Sidebar
old_brand_svg = '''      <svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="28" cy="28" r="20" fill="#181818" stroke="#FFFFFF" stroke-width="3.5"/>
        <rect x="19" y="27" width="3.5" height="12" rx="1" fill="#9B9B9B"/>
        <rect x="26" y="21" width="3.5" height="18" rx="1" fill="#FFFFFF"/>
        <rect x="33" y="16" width="3.5" height="23" rx="1" fill="#F97316"/>
        <rect x="41" y="41" width="6" height="18" rx="3" transform="rotate(-45 41 41)" fill="#FFFFFF"/>
      </svg>'''

new_brand_svg = '''      <svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect x="6" y="6" width="52" height="52" rx="3" fill="#1779ba"/>
        <path d="M20 22H44V28H28V33H40V39H28V46H20V22Z" fill="#fefefe"/>
      </svg>'''

if old_brand_svg in html:
    html = html.replace(old_brand_svg, new_brand_svg, 1)

# Write to files
with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)
with open(COURSE_INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("Foundation design system applied successfully to index.html and course/index.html")
print("Total length:", len(html))
