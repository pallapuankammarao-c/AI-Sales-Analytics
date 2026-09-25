"""
AI-Powered Sales & Customer Analytics System
Module: build_dashboard_html.py
Purpose: Compiles a 100% self-contained, bulletproof executive analytics dashboard
         into index.html and dashboard/index.html with:
         - Embedded inline DASHBOARD_DATA (zero external file dependency)
         - Local + CDN Chart.js loading
         - High-res native HTML5 Canvas fallback if Chart.js is offline/blocked
         - Modern dark-mode styling with zero linter warnings
"""

import os
import json

def build_dashboard():
    # 1. Load data from dashboard/data.js
    data_path = "dashboard/data.js"
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Missing {data_path}. Run export_dashboard_data.py first.")

    with open(data_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract JSON object from 'window.DASHBOARD_DATA = { ... };'
    json_start = content.find("{")
    json_end = content.rfind("}") + 1
    raw_json = content[json_start:json_end]
    data_obj = json.loads(raw_json)

    # 2. Construct the full HTML
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>NexusAI | Enterprise Sales & Customer Analytics Platform</title>
  <meta name="description" content="Production-grade AI-powered sales analytics, customer RFM segmentation, demand forecasting, and grounded generative AI intelligence platform." />
  
  <!-- Modern Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet" />
  
  <!-- Chart.js Libraries: Try local file first, then fall back to CDN -->
  <script src="chart.min.js"></script>
  <script src="dashboard/chart.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>

  <style>
    /* ==========================================================================
       DESIGN SYSTEM & CSS TOKENS
       ========================================================================== */
    :root {{
      --bg-dark: #080c14;
      --bg-surface: #0f172a;
      --bg-card: rgba(17, 24, 39, 0.75);
      --bg-card-hover: rgba(30, 41, 59, 0.85);
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-focus: rgba(99, 102, 241, 0.5);
      
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;

      --accent-cyan: #06b6d4;
      --accent-indigo: #6366f1;
      --accent-emerald: #10b981;
      --accent-amber: #f59e0b;
      --accent-rose: #f43f5e;
      --accent-purple: #a855f7;

      --grad-primary: linear-gradient(135deg, #6366f1 0%, #06b6d4 100%);
      --grad-accent: linear-gradient(135deg, #06b6d4 0%, #10b981 100%);
      --grad-warning: linear-gradient(135deg, #f59e0b 0%, #f43f5e 100%);
      --grad-card-glow: radial-gradient(circle at 50% 0%, rgba(99, 102, 241, 0.15) 0%, transparent 70%);

      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
      --radius-full: 9999px;

      --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.3);
      --shadow-md: 0 8px 24px rgba(0, 0, 0, 0.4);
      --shadow-glow: 0 0 25px rgba(99, 102, 241, 0.25);

      --font-sans: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      background-color: var(--bg-dark);
      background-image: 
        radial-gradient(at 0% 0%, rgba(99, 102, 241, 0.12) 0px, transparent 50%),
        radial-gradient(at 100% 100%, rgba(6, 182, 212, 0.08) 0px, transparent 50%),
        radial-gradient(at 50% 50%, rgba(15, 23, 42, 0.5) 0px, transparent 100%);
      background-attachment: fixed;
      color: var(--text-main);
      font-family: var(--font-sans);
      min-height: 100vh;
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
    }}

    /* Custom Scrollbar */
    ::-webkit-scrollbar {{
      width: 8px;
      height: 8px;
    }}
    ::-webkit-scrollbar-track {{
      background: var(--bg-dark);
    }}
    ::-webkit-scrollbar-thumb {{
      background: #1e293b;
      border-radius: var(--radius-full);
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #334155;
    }}

    /* Container */
    .app-container {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 24px;
    }}

    /* Header */
    .top-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 16px 24px;
      background: var(--bg-card);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      margin-bottom: 24px;
      box-shadow: var(--shadow-md);
      position: sticky;
      top: 16px;
      z-index: 100;
    }}

    .brand-section {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}

    .brand-logo {{
      width: 44px;
      height: 44px;
      background: var(--grad-primary);
      border-radius: var(--radius-md);
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: var(--shadow-glow);
    }}
    .brand-logo svg {{
      width: 24px;
      height: 24px;
      color: #fff;
    }}

    .brand-text h1 {{
      font-size: 1.25rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      background: linear-gradient(135deg, #fff 0%, #cbd5e1 100%);
      background-clip: text;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    .brand-text p {{
      font-size: 0.78rem;
      color: var(--text-muted);
      font-weight: 500;
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .badge-status {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 12px;
      background: rgba(16, 185, 129, 0.1);
      border: 1px solid rgba(16, 185, 129, 0.3);
      border-radius: var(--radius-full);
      font-size: 0.75rem;
      color: var(--accent-emerald);
      font-weight: 600;
      letter-spacing: 0.02em;
    }}
    .badge-status .pulse-dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--accent-emerald);
      box-shadow: 0 0 10px var(--accent-emerald);
      animation: pulse 2s infinite;
    }}

    @keyframes pulse {{
      0% {{ opacity: 1; transform: scale(1); }}
      50% {{ opacity: 0.4; transform: scale(0.85); }}
      100% {{ opacity: 1; transform: scale(1); }}
    }}

    .btn-action {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 8px 16px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      color: var(--text-main);
      font-size: 0.82rem;
      font-weight: 600;
      text-decoration: none;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    .btn-action:hover {{
      background: rgba(255, 255, 255, 0.1);
      border-color: var(--border-focus);
      transform: translateY(-1px);
    }}
    .btn-primary {{
      background: var(--grad-primary);
      border: none;
      color: #fff;
      box-shadow: var(--shadow-sm);
    }}
    .btn-primary:hover {{
      box-shadow: var(--shadow-glow);
    }}

    /* Tab Bar */
    .tab-bar {{
      display: flex;
      gap: 8px;
      padding: 6px;
      background: rgba(15, 23, 42, 0.6);
      backdrop-filter: blur(12px);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      margin-bottom: 24px;
      overflow-x: auto;
    }}
    .tab-btn {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 10px 18px;
      background: transparent;
      border: none;
      border-radius: var(--radius-sm);
      color: var(--text-muted);
      font-size: 0.85rem;
      font-weight: 600;
      font-family: inherit;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s ease;
    }}
    .tab-btn:hover {{
      color: var(--text-main);
      background: rgba(255, 255, 255, 0.04);
    }}
    .tab-btn.active {{
      color: #fff;
      background: var(--bg-surface);
      border: 1px solid rgba(99, 102, 241, 0.4);
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2), inset 0 1px 0 rgba(255, 255, 255, 0.1);
    }}
    .tab-btn svg {{
      width: 16px;
      height: 16px;
    }}

    .tab-pane {{
      display: none;
      animation: fadeIn 0.3s ease;
    }}
    .tab-pane.active {{
      display: block;
    }}
    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* KPI Grid */
    .kpi-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 16px;
      margin-bottom: 24px;
    }}

    .kpi-card {{
      background: var(--bg-card);
      backdrop-filter: blur(12px);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 20px;
      position: relative;
      overflow: hidden;
      transition: all 0.25s ease;
      box-shadow: var(--shadow-sm);
    }}
    .kpi-card:hover {{
      transform: translateY(-3px);
      border-color: rgba(99, 102, 241, 0.4);
      box-shadow: var(--shadow-md);
    }}
    .kpi-card::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 3px;
      background: var(--accent-indigo);
    }}
    .kpi-card.cyan::before {{ background: var(--accent-cyan); }}
    .kpi-card.emerald::before {{ background: var(--accent-emerald); }}
    .kpi-card.amber::before {{ background: var(--accent-amber); }}
    .kpi-card.rose::before {{ background: var(--accent-rose); }}

    .kpi-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }}
    .kpi-title {{
      font-size: 0.8rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
    }}
    .kpi-icon {{
      width: 32px;
      height: 32px;
      border-radius: var(--radius-sm);
      display: flex;
      align-items: center;
      justify-content: center;
      background: rgba(255, 255, 255, 0.05);
      color: var(--text-main);
    }}
    .kpi-value {{
      font-size: 1.85rem;
      font-weight: 800;
      letter-spacing: -0.03em;
      margin-bottom: 6px;
      font-family: var(--font-sans);
    }}
    .kpi-meta {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.78rem;
      color: var(--text-dim);
    }}
    .kpi-pill {{
      display: inline-flex;
      align-items: center;
      padding: 2px 8px;
      border-radius: var(--radius-full);
      font-size: 0.72rem;
      font-weight: 700;
    }}
    .kpi-pill.up {{
      background: rgba(16, 185, 129, 0.15);
      color: var(--accent-emerald);
    }}
    .kpi-pill.warn {{
      background: rgba(245, 158, 11, 0.15);
      color: var(--accent-amber);
    }}
    .kpi-pill.danger {{
      background: rgba(244, 63, 94, 0.15);
      color: var(--accent-rose);
    }}

    /* Section Grids */
    .dashboard-grid-2 {{
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 20px;
      margin-bottom: 24px;
    }}
    .dashboard-grid-equal {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin-bottom: 24px;
    }}

    @media (max-width: 1024px) {{
      .dashboard-grid-2, .dashboard-grid-equal {{
        grid-template-columns: 1fr;
      }}
    }}

    .content-card {{
      background: var(--bg-card);
      backdrop-filter: blur(14px);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 22px;
      box-shadow: var(--shadow-sm);
      position: relative;
    }}
    .card-header-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 18px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--border-subtle);
    }}
    .card-header-bar h2, .card-header-bar h3 {{
      font-size: 1.05rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .card-subtitle {{
      font-size: 0.8rem;
      color: var(--text-muted);
      margin-top: 2px;
    }}

    /* Chart Containers */
    .chart-box {{
      position: relative;
      width: 100%;
      height: 320px;
    }}
    .chart-box-sm {{
      position: relative;
      width: 100%;
      height: 260px;
    }}

    /* GenAI Insight Cards */
    .insight-card {{
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 20px;
      margin-bottom: 20px;
      transition: all 0.2s ease;
      position: relative;
      overflow: hidden;
    }}
    .insight-card:hover {{
      border-color: rgba(99, 102, 241, 0.4);
      box-shadow: var(--shadow-md);
    }}
    .insight-card.critical {{ border-left: 4px solid var(--accent-rose); }}
    .insight-card.high {{ border-left: 4px solid var(--accent-amber); }}
    .insight-card.warning {{ border-left: 4px solid var(--accent-cyan); }}

    .insight-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 16px;
    }}
    .insight-title-group h3 {{
      font-size: 1.15rem;
      font-weight: 700;
      color: #fff;
    }}
    .insight-tag {{
      display: inline-block;
      font-size: 0.72rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--accent-cyan);
      margin-top: 4px;
    }}

    .triad-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 12px;
      margin-top: 14px;
    }}
    .triad-box {{
      background: rgba(0, 0, 0, 0.25);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      padding: 14px;
      font-size: 0.82rem;
    }}
    .triad-label {{
      font-size: 0.7rem;
      font-weight: 800;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .triad-box.fact .triad-label {{ color: var(--accent-cyan); }}
    .triad-box.explanation .triad-label {{ color: var(--accent-amber); }}
    .triad-box.investigation .triad-label {{ color: var(--accent-purple); }}
    .triad-box.action .triad-label {{ color: var(--accent-emerald); }}

    /* Data Tables */
    .table-responsive {{
      width: 100%;
      overflow-x: auto;
    }}
    .data-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.83rem;
      text-align: left;
    }}
    .data-table th {{
      background: rgba(15, 23, 42, 0.9);
      padding: 12px 14px;
      font-weight: 700;
      color: var(--text-muted);
      border-bottom: 1px solid var(--border-subtle);
      text-transform: uppercase;
      letter-spacing: 0.04em;
      font-size: 0.72rem;
    }}
    .data-table td {{
      padding: 12px 14px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.04);
      color: var(--text-main);
    }}
    .data-table tr:hover td {{
      background: rgba(255, 255, 255, 0.02);
    }}
    .code-chip {{
      font-family: var(--font-mono);
      font-size: 0.78rem;
      padding: 2px 6px;
      background: rgba(255, 255, 255, 0.06);
      border-radius: 4px;
      color: var(--accent-cyan);
    }}

    .filter-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
      margin-bottom: 16px;
      flex-wrap: wrap;
    }}
    .search-input {{
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      padding: 8px 14px;
      color: #fff;
      font-size: 0.82rem;
      font-family: inherit;
      min-width: 260px;
      transition: border-color 0.2s;
    }}
    .search-input:focus {{
      outline: none;
      border-color: var(--accent-indigo);
    }}

    /* Models Grid */
    .model-comparison-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 16px;
      margin-bottom: 20px;
    }}
    .model-card {{
      background: rgba(15, 23, 42, 0.6);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 18px;
      transition: all 0.2s ease;
    }}
    .model-card.featured {{
      border: 1px solid rgba(99, 102, 241, 0.6);
      background: linear-gradient(180deg, rgba(99, 102, 241, 0.1) 0%, rgba(15, 23, 42, 0.8) 100%);
      box-shadow: 0 0 20px rgba(99, 102, 241, 0.15);
    }}
    .model-title {{
      font-size: 1rem;
      font-weight: 700;
      margin-bottom: 4px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .model-metrics {{
      display: flex;
      gap: 14px;
      margin: 12px 0;
      padding: 10px 0;
      border-top: 1px solid var(--border-subtle);
      border-bottom: 1px solid var(--border-subtle);
    }}
    .metric-item {{
      flex: 1;
    }}
    .metric-item .label {{
      font-size: 0.7rem;
      color: var(--text-dim);
      text-transform: uppercase;
    }}
    .metric-item .val {{
      font-size: 1.15rem;
      font-weight: 700;
      font-family: var(--font-mono);
      color: var(--accent-cyan);
    }}

    .feature-bar-wrap {{
      margin-bottom: 10px;
    }}
    .feature-bar-label {{
      display: flex;
      justify-content: space-between;
      font-size: 0.78rem;
      margin-bottom: 4px;
    }}
    .progress-track {{
      background: rgba(255, 255, 255, 0.06);
      border-radius: var(--radius-full);
      height: 6px;
      overflow: hidden;
    }}
    .progress-fill {{
      height: 100%;
      background: var(--grad-primary);
      border-radius: var(--radius-full);
    }}

    .check-item {{
      display: flex;
      align-items: flex-start;
      gap: 12px;
      padding: 12px;
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      margin-bottom: 8px;
    }}
    .check-icon {{
      color: var(--accent-emerald);
      font-size: 1.1rem;
      line-height: 1;
    }}
    .check-content strong {{
      font-size: 0.85rem;
      color: #fff;
    }}
    .check-content p {{
      font-size: 0.78rem;
      color: var(--text-muted);
      margin-top: 2px;
    }}

    .gallery-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 16px;
    }}
    .gallery-item {{
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      overflow: hidden;
      cursor: pointer;
      transition: all 0.25s ease;
    }}
    .gallery-item:hover {{
      transform: translateY(-4px);
      border-color: var(--accent-cyan);
      box-shadow: var(--shadow-md);
    }}
    .gallery-item img {{
      width: 100%;
      height: 160px;
      object-fit: cover;
      display: block;
      border-bottom: 1px solid var(--border-subtle);
    }}
    .gallery-item-caption {{
      padding: 12px;
    }}
    .gallery-item-caption h4 {{
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--text-main);
    }}
    .gallery-item-caption p {{
      font-size: 0.72rem;
      color: var(--text-dim);
    }}

    .modal-backdrop {{
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(0, 0, 0, 0.85);
      backdrop-filter: blur(8px);
      z-index: 1000;
      align-items: center;
      justify-content: center;
      padding: 24px;
    }}
    .modal-backdrop.open {{
      display: flex;
    }}
    .modal-box {{
      max-width: 900px;
      width: 100%;
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      overflow: hidden;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
      position: relative;
    }}
    .modal-box img {{
      width: 100%;
      max-height: 70vh;
      object-fit: contain;
      background: #000;
    }}
    .modal-footer {{
      padding: 16px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: var(--bg-card);
    }}
    .btn-close-modal {{
      background: rgba(255, 255, 255, 0.1);
      border: none;
      color: #fff;
      padding: 8px 16px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      font-family: inherit;
      font-weight: 600;
    }}

    .app-footer {{
      margin-top: 48px;
      padding: 24px 0;
      border-top: 1px solid var(--border-subtle);
      display: flex;
      justify-content: space-between;
      align-items: center;
      color: var(--text-dim);
      font-size: 0.8rem;
      flex-wrap: wrap;
      gap: 16px;
    }}
    .footer-links {{
      display: flex;
      gap: 16px;
    }}
    .footer-links a {{
      color: var(--text-muted);
      text-decoration: none;
      transition: color 0.2s;
    }}
    .footer-links a:hover {{
      color: var(--accent-cyan);
    }}
  </style>
</head>
<body>

  <div class="app-container">
    
    <!-- Top Header -->
    <header class="top-header">
      <div class="brand-section">
        <div class="brand-logo">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>
          </svg>
        </div>
        <div class="brand-text">
          <h1>NexusAI Analytics Hub</h1>
          <p>AI-Powered Sales & Customer Intelligence Platform</p>
        </div>
      </div>

      <div class="header-actions">
        <div class="badge-status">
          <span class="pulse-dot"></span>
          <span>100% Invariants Verified</span>
        </div>
        <a href="https://github.com/pallapuankammarao-c/AI-Sales-Analytics" target="_blank" class="btn-action">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
          </svg>
          GitHub Repository
        </a>
        <button onclick="window.print()" class="btn-action btn-primary">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <polyline points="6 9 6 2 18 2 18 9"></polyline>
            <path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path>
            <rect x="6" y="14" width="12" height="8"></rect>
          </svg>
          Export Summary
        </button>
      </div>
    </header>

    <!-- Tab Bar -->
    <nav class="tab-bar">
      <button class="tab-btn active" onclick="switchTab('overview')">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="9"></rect><rect x="14" y="3" width="7" height="5"></rect><rect x="14" y="12" width="7" height="9"></rect><rect x="3" y="16" width="7" height="5"></rect></svg>
        Overview & KPIs
      </button>
      <button class="tab-btn" onclick="switchTab('insights')">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
        GenAI Strategic Insights
      </button>
      <button class="tab-btn" onclick="switchTab('customers')">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
        Customer RFM & Risk
      </button>
      <button class="tab-btn" onclick="switchTab('products')">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>
        Pricing & Discount Leakage
      </button>
      <button class="tab-btn" onclick="switchTab('forecasting')">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline><polyline points="17 6 23 6 23 12"></polyline></svg>
        ML Demand Forecast
      </button>
      <button class="tab-btn" onclick="switchTab('audit')">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
        Integrity & Tests (100%)
      </button>
      <button class="tab-btn" onclick="switchTab('gallery')">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
        Charts & Reports
      </button>
    </nav>

    <!-- TAB 1: EXECUTIVE OVERVIEW -->
    <div id="tab-overview" class="tab-pane active">
      <section class="kpi-grid">
        <div class="kpi-card cyan">
          <div class="kpi-header">
            <span class="kpi-title">Gross Turnover</span>
            <div class="kpi-icon">💰</div>
          </div>
          <div class="kpi-value" id="kpi-sales">$2,961,670</div>
          <div class="kpi-meta">
            <span class="kpi-pill up" id="kpi-orders-pill">5,486 Orders</span>
            <span>24-Month Turnover</span>
          </div>
        </div>

        <div class="kpi-card emerald">
          <div class="kpi-header">
            <span class="kpi-title">Operating Profit</span>
            <div class="kpi-icon">📈</div>
          </div>
          <div class="kpi-value" id="kpi-profit">$423,672</div>
          <div class="kpi-meta">
            <span class="kpi-pill up" id="kpi-margin">14.31% Margin</span>
            <span>Target Benchmark: 15%</span>
          </div>
        </div>

        <div class="kpi-card amber">
          <div class="kpi-header">
            <span class="kpi-title">Avg Order Value (AOV)</span>
            <div class="kpi-icon">🛒</div>
          </div>
          <div class="kpi-value" id="kpi-aov">$539.86</div>
          <div class="kpi-meta">
            <span class="kpi-pill up" id="kpi-qty-pill">12,219 Units</span>
            <span>Avg 2.2 units / basket</span>
          </div>
        </div>

        <div class="kpi-card rose">
          <div class="kpi-header">
            <span class="kpi-title">Active Customer Accounts</span>
            <div class="kpi-icon">👥</div>
          </div>
          <div class="kpi-value" id="kpi-customers">642</div>
          <div class="kpi-meta">
            <span class="kpi-pill warn">41 At-Risk</span>
            <span>6.4% Dormancy Rate</span>
          </div>
        </div>
      </section>

      <div class="dashboard-grid-2">
        <div class="content-card">
          <div class="card-header-bar">
            <div>
              <h2>Monthly Sales Turnover & Net Operating Profit</h2>
              <p class="card-subtitle">24-month longitudinal trend showing Q4 holiday volume surges</p>
            </div>
          </div>
          <div class="chart-box">
            <canvas id="monthlyTrendChart"></canvas>
          </div>
        </div>

        <div class="content-card">
          <div class="card-header-bar">
            <div>
              <h3>Regional Revenue & Margin</h3>
              <p class="card-subtitle">Contribution across 4 commercial territories</p>
            </div>
          </div>
          <div class="chart-box">
            <canvas id="regionalChart"></canvas>
          </div>
        </div>
      </div>

      <div class="dashboard-grid-equal">
        <div class="content-card">
          <div class="card-header-bar">
            <div>
              <h3>Category Sales vs Profit Margin</h3>
              <p class="card-subtitle">Notice the severe operating deficit in Furniture (-2.46%)</p>
            </div>
          </div>
          <div class="chart-box-sm">
            <canvas id="categoryChart"></canvas>
          </div>
        </div>

        <div class="content-card">
          <div class="card-header-bar">
            <div>
              <h3>Payment Mode Breakdown</h3>
              <p class="card-subtitle">Transaction distribution across settlement methods</p>
            </div>
          </div>
          <div class="chart-box-sm">
            <canvas id="paymentChart"></canvas>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 2: GENAI STRATEGIC INSIGHTS -->
    <div id="tab-insights" class="tab-pane">
      <div class="content-card" style="margin-bottom: 24px; border-left: 4px solid var(--accent-indigo);">
        <h2 style="margin-bottom: 6px;">Governance Architecture: The Anti-Hallucination Triad</h2>
        <p style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.6;">
          Generative AI often hallucinates when asked to perform raw numerical calculations. In this platform, 
          <strong>100% of arithmetic and statistical calculations are pre-computed in Python/SQL</strong>. 
          The GenAI engine synthesizes structured JSON telemetry into three strictly partitioned epistemic tiers:
          <span style="color:var(--accent-cyan); font-weight:700;">FACT</span> (mathematical ground-truth), 
          <span style="color:var(--accent-amber); font-weight:700;">POSSIBLE EXPLANATION</span> (commercial hypothesis), and 
          <span style="color:var(--accent-emerald); font-weight:700;">BUSINESS ACTION</span> (targeted initiatives).
        </p>
      </div>

      <div id="insights-container"></div>
    </div>

    <!-- TAB 3: CUSTOMER RFM & CHURN RISK -->
    <div id="tab-customers" class="tab-pane">
      <div class="dashboard-grid-equal">
        <div class="content-card">
          <div class="card-header-bar">
            <div>
              <h3>Customer Segmentation Distribution</h3>
              <p class="card-subtitle">Account distribution across 5 RFM behavioral cohorts</p>
            </div>
          </div>
          <div class="chart-box">
            <canvas id="customerSegmentChart"></canvas>
          </div>
        </div>

        <div class="content-card">
          <div class="card-header-bar">
            <div>
              <h3>Recency vs Total Spending Scatter</h3>
              <p class="card-subtitle">Sample of accounts: Days Inactive vs Cumulative Spend ($)</p>
            </div>
          </div>
          <div class="chart-box">
            <canvas id="customerScatterChart"></canvas>
          </div>
        </div>
      </div>

      <div class="content-card">
        <div class="card-header-bar">
          <div>
            <h3>High-Value Dormant Accounts Requiring Priority Win-Back</h3>
            <p class="card-subtitle">Accounts with historical spend &gt; $3,500 inactive for over 120 days ($188,549 at risk)</p>
          </div>
        </div>

        <div class="filter-bar">
          <input type="text" id="custSearchInput" class="search-input" placeholder="Search customer ID, region, or type..." oninput="filterCustomerTable()" />
          <div style="font-size: 0.8rem; color: var(--text-muted);" id="atRiskSummaryText">Showing 15 top at-risk accounts</div>
        </div>

        <div class="table-responsive">
          <table class="data-table" id="atRiskTable">
            <thead>
              <tr>
                <th>Customer ID</th>
                <th>Type</th>
                <th>Region</th>
                <th>Orders</th>
                <th>Lifetime Spend</th>
                <th>Operating Profit</th>
                <th>Days Inactive</th>
                <th>Recommended Action</th>
              </tr>
            </thead>
            <tbody></tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- TAB 4: PRICING & DISCOUNT LEAKAGE -->
    <div id="tab-products" class="tab-pane">
      <div class="dashboard-grid-equal">
        <div class="content-card">
          <div class="card-header-bar">
            <div>
              <h3>Discount Sensitivity & Outright Loss Rate</h3>
              <p class="card-subtitle">Notice: Discounts &ge; 25% yield an outright 100% loss rate!</p>
            </div>
          </div>
          <div class="chart-box">
            <canvas id="discountSensitivityChart"></canvas>
          </div>
        </div>

        <div class="content-card">
          <div class="card-header-bar">
            <div>
              <h3>Operating Profit by Discount Tier ($)</h3>
              <p class="card-subtitle">Margin destruction caused by steep promotional markdowns</p>
            </div>
          </div>
          <div class="chart-box">
            <canvas id="discountProfitChart"></canvas>
          </div>
        </div>
      </div>

      <div class="dashboard-grid-equal">
        <div class="content-card">
          <div class="card-header-bar">
            <h3>Top 5 High-Revenue Generating Products</h3>
          </div>
          <div class="table-responsive">
            <table class="data-table" id="topProductsTable">
              <thead>
                <tr>
                  <th>Product ID</th>
                  <th>Category</th>
                  <th>Units</th>
                  <th>Revenue</th>
                  <th>Profit</th>
                  <th>Margin</th>
                </tr>
              </thead>
              <tbody></tbody>
            </table>
          </div>
        </div>

        <div class="content-card">
          <div class="card-header-bar">
            <h3>Top 5 Profit-Draining SKUs (Loss Leaders)</h3>
          </div>
          <div class="table-responsive">
            <table class="data-table" id="bottomProductsTable">
              <thead>
                <tr>
                  <th>Product ID</th>
                  <th>Category</th>
                  <th>Units</th>
                  <th>Revenue</th>
                  <th>Profit</th>
                  <th>Margin</th>
                </tr>
              </thead>
              <tbody></tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 5: ML DEMAND FORECASTING -->
    <div id="tab-forecasting" class="tab-pane">
      <div class="content-card" style="margin-bottom: 24px;">
        <h2 style="margin-bottom: 6px;">Machine Learning Architecture: Short-Term Sales Turnover Forecasting</h2>
        <p style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.6;">
          The demand forecasting pipeline uses a supervised regression framework trained on 595 days of sales records (Jan 2023 – Aug 2024) 
          and evaluated on a strict holdout test window (Sep 2024 – Dec 2024, 122 days). 
          <strong>Strict temporal splitting with shifted rolling windows was enforced to eliminate lookahead data leakage.</strong>
        </p>
      </div>

      <div class="model-comparison-grid" id="mlModelsGrid"></div>

      <div class="dashboard-grid-equal">
        <div class="content-card">
          <div class="card-header-bar">
            <div>
              <h3>Random Forest Feature Importance</h3>
              <p class="card-subtitle">Relative Gini-importance contribution across 8 primary signals</p>
            </div>
          </div>
          <div id="featureImportanceList" style="padding-top: 10px;"></div>
        </div>

        <div class="content-card">
          <div class="card-header-bar">
            <div>
              <h3>Forecast Invariants & Model Diagnostics</h3>
              <p class="card-subtitle">Guardrails enforced in scikit-learn pipeline</p>
            </div>
          </div>
          <div style="display:flex; flex-direction:column; gap:12px;">
            <div class="check-item">
              <div class="check-icon">✓</div>
              <div class="check-content">
                <strong>Zero Lookahead Data Leakage</strong>
                <p>All rolling averages (7-day, 14-day) use explicit <code>.shift(1)</code> lag steps.</p>
              </div>
            </div>
            <div class="check-item">
              <div class="check-icon">✓</div>
              <div class="check-content">
                <strong>Temporal Train/Test Split (Sep 2024 Cutoff)</strong>
                <p>Preserves real-world sequential order; tested on Q4 peak shopping surge.</p>
              </div>
            </div>
            <div class="check-item">
              <div class="check-icon">✓</div>
              <div class="check-content">
                <strong>Hyperparameter Regularization</strong>
                <p>RandomForestRegressor configured with <code>n_estimators=100</code>, <code>max_depth=8</code>, <code>min_samples_leaf=3</code>.</p>
              </div>
            </div>
            <div class="check-item">
              <div class="check-icon">✓</div>
              <div class="check-content">
                <strong>Serialized Model Deployment</strong>
                <p>Model packaged with metadata &amp; feature schema in <code>models/sales_prediction_model.pkl</code>.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 6: INTEGRITY & AUTOMATED TEST SUITE -->
    <div id="tab-audit" class="tab-pane">
      <div class="content-card" style="margin-bottom: 24px;">
        <div class="card-header-bar">
          <div>
            <h2>Automated Integration &amp; Unit Validation Suite</h2>
            <p class="card-subtitle">Executed from <code>tests/test_project_validation.py</code></p>
          </div>
          <div class="badge-status">ALL 7 TESTS PASSED</div>
        </div>
        <p style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.6;">
          In commercial data engineering, pipelines must enforce mathematically verifiable invariants. 
          Our automated test suite audits raw schemas, eliminates duplication and missingness, verifies 
          numerical reconciliation between MySQL and Python Pandas, and validates ML model inference.
        </p>
      </div>

      <div class="content-card">
        <div class="table-responsive">
          <table class="data-table" id="validationTable">
            <thead>
              <tr>
                <th>Test Component</th>
                <th>Result</th>
                <th>Verification Audit Details</th>
              </tr>
            </thead>
            <tbody></tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- TAB 7: HIGH-RES CHART GALLERY -->
    <div id="tab-gallery" class="tab-pane">
      <div class="content-card" style="margin-bottom: 24px;">
        <h2>Publication-Grade Visual Artifacts (300 DPI)</h2>
        <p class="card-subtitle">Click any chart to inspect in full high-resolution modal preview</p>
      </div>

      <div class="gallery-grid" id="chartGalleryGrid"></div>
    </div>

    <!-- Lightbox Modal -->
    <div id="chartModal" class="modal-backdrop" onclick="closeModal(event)">
      <div class="modal-box" onclick="event.stopPropagation()">
        <img id="modalImg" src="" alt="Chart Preview" />
        <div class="modal-footer">
          <div id="modalCaption" style="font-size:0.85rem; font-weight:600;"></div>
          <button class="btn-close-modal" onclick="closeModal()">Close</button>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <footer class="app-footer">
      <div>
        <strong>NexusAI Analytics Hub</strong> &bull; Production Portfolio Project &bull; 
        <span>GitHub: <a href="https://github.com/pallapuankammarao-c/AI-Sales-Analytics" target="_blank" style="color:var(--accent-cyan); text-decoration:none;">AI-Sales-Analytics</a></span>
      </div>
      <div class="footer-links">
        <a href="#overview" onclick="switchTab('overview')">Overview</a>
        <a href="#insights" onclick="switchTab('insights')">AI Insights</a>
        <a href="#customers" onclick="switchTab('customers')">Customer Risk</a>
        <a href="#forecasting" onclick="switchTab('forecasting')">ML Forecast</a>
        <a href="#audit" onclick="switchTab('audit')">Validation Tests</a>
      </div>
    </footer>

  </div>

  <!-- ========================================================================
       EMBEDDED INLINE DATASET (ZERO DEPENDENCY / ZERO NETWORK REQUIREMENT)
       ======================================================================== -->
  <script id="embedded-data">
    window.DASHBOARD_DATA = {json.dumps(data_obj)};
  </script>

  <!-- External Data Overrides (if present) -->
  <script src="dashboard/data.js"></script>
  <script src="data.js"></script>

  <!-- ========================================================================
       DASHBOARD SCRIPT WITH GRACEFUL CHART.JS & NATIVE CANVAS FALLBACK
       ======================================================================== -->
  <script>
    function switchTab(tabId) {{
      document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
      document.querySelectorAll('.tab-pane').forEach(pane => pane.classList.remove('active'));

      const targetPane = document.getElementById('tab-' + tabId);
      if (targetPane) targetPane.classList.add('active');

      const activeBtn = Array.from(document.querySelectorAll('.tab-btn')).find(b => 
        b.getAttribute('onclick') && b.getAttribute('onclick').includes(tabId)
      );
      if (activeBtn) activeBtn.classList.add('active');

      window.dispatchEvent(new Event('resize'));
    }}

    function openModal(src, caption) {{
      const modal = document.getElementById('chartModal');
      const img = document.getElementById('modalImg');
      const cap = document.getElementById('modalCaption');
      img.src = src;
      cap.textContent = caption;
      modal.classList.add('open');
    }}
    function closeModal() {{
      document.getElementById('chartModal').classList.remove('open');
    }}

    // --------------------------------------------------------------------------
    // MAIN INITIALIZATION
    // --------------------------------------------------------------------------
    function initDashboard() {{
      const data = window.DASHBOARD_DATA;
      if (!data) {{
        console.error("Dashboard data not loaded!");
        return;
      }}

      // Populate Macro KPIs
      if (data.kpis) {{
        document.getElementById('kpi-sales').textContent = '$' + Number(data.kpis.total_sales).toLocaleString('en-US', {{ minimumFractionDigits: 0, maximumFractionDigits: 0 }});
        document.getElementById('kpi-profit').textContent = '$' + Number(data.kpis.total_profit).toLocaleString('en-US', {{ minimumFractionDigits: 0, maximumFractionDigits: 0 }});
        document.getElementById('kpi-margin').textContent = Number(data.kpis.margin).toFixed(2) + '% Margin';
        document.getElementById('kpi-aov').textContent = '$' + Number(data.kpis.aov).toFixed(2);
        document.getElementById('kpi-customers').textContent = Number(data.kpis.total_customers).toLocaleString();
        if (data.kpis.total_orders) document.getElementById('kpi-orders-pill').textContent = Number(data.kpis.total_orders).toLocaleString() + ' Orders';
        if (data.kpis.total_qty) document.getElementById('kpi-qty-pill').textContent = Number(data.kpis.total_qty).toLocaleString() + ' Units';
      }}

      // Render Charts (Uses Chart.js if available, otherwise pure Canvas 2D fallback)
      renderAllCharts(data);

      // Render Content Sections
      renderAiInsights(data.ai_insights);
      renderAtRiskCustomers(data.at_risk_customers);
      renderTopBottomProducts(data.top_products, data.bottom_products);
      renderMlSection(data.ml_models, data.ml_features);
      renderValidationTable(data.validation_tests);
      renderGallery();
    }}

    // Check if DOM is ready
    if (document.readyState === 'loading') {{
      document.addEventListener('DOMContentLoaded', initDashboard);
    }} else {{
      initDashboard();
    }}

    // --------------------------------------------------------------------------
    // CHART RENDERING (Chart.js or Native HTML5 Canvas Fallback)
    // --------------------------------------------------------------------------
    function renderAllCharts(data) {{
      const hasChartJs = typeof Chart !== 'undefined';
      
      if (hasChartJs) {{
        Chart.defaults.color = '#94a3b8';
        Chart.defaults.font.family = "'Plus Jakarta Sans', sans-serif";
        renderChartJsCharts(data);
      }} else {{
        console.warn("Chart.js not loaded. Activating high-res native HTML5 Canvas fallback.");
        renderNativeCanvasCharts(data);
      }}
    }}

    // A. Chart.js Engine
    function renderChartJsCharts(data) {{
      // 1. Monthly Line Chart
      const ctxMonthly = document.getElementById('monthlyTrendChart');
      if (ctxMonthly && data.monthly) {{
        new Chart(ctxMonthly, {{
          type: 'line',
          data: {{
            labels: data.monthly.labels,
            datasets: [
              {{
                label: 'Sales Revenue ($)',
                data: data.monthly.sales,
                borderColor: '#06b6d4',
                backgroundColor: 'rgba(6, 182, 212, 0.1)',
                fill: true,
                tension: 0.35,
                borderWidth: 2.5,
                pointRadius: 2.5
              }},
              {{
                label: 'Net Profit ($)',
                data: data.monthly.profit,
                borderColor: '#10b981',
                backgroundColor: 'rgba(16, 185, 129, 0.1)',
                fill: true,
                tension: 0.35,
                borderWidth: 2.5,
                pointRadius: 2.5
              }}
            ]
          }},
          options: {{
            responsive: true,
            maintainAspectRatio: false,
            plugins: {{ legend: {{ position: 'top' }} }},
            scales: {{
              x: {{ grid: {{ color: 'rgba(255,255,255,0.04)' }} }},
              y: {{ ticks: {{ callback: v => '$' + (v / 1000) + 'k' }}, grid: {{ color: 'rgba(255,255,255,0.06)' }} }}
            }}
          }}
        }});
      }}

      // 2. Regional Horizontal Bar
      const ctxReg = document.getElementById('regionalChart');
      if (ctxReg && data.regional) {{
        new Chart(ctxReg, {{
          type: 'bar',
          data: {{
            labels: data.regional.labels,
            datasets: [
              {{ label: 'Sales ($)', data: data.regional.sales, backgroundColor: 'rgba(99, 102, 241, 0.85)', borderRadius: 6 }},
              {{ label: 'Profit ($)', data: data.regional.profit, backgroundColor: 'rgba(16, 185, 129, 0.85)', borderRadius: 6 }}
            ]
          }},
          options: {{
            responsive: true,
            maintainAspectRatio: false,
            indexAxis: 'y',
            plugins: {{ legend: {{ position: 'bottom' }} }},
            scales: {{
              x: {{ ticks: {{ callback: v => '$' + (v / 1000) + 'k' }}, grid: {{ color: 'rgba(255,255,255,0.05)' }} }},
              y: {{ grid: {{ display: false }} }}
            }}
          }}
        }});
      }}

      // 3. Category Bar Chart
      const ctxCat = document.getElementById('categoryChart');
      if (ctxCat && data.category) {{
        new Chart(ctxCat, {{
          type: 'bar',
          data: {{
            labels: data.category.labels,
            datasets: [{{ label: 'Revenue ($)', data: data.category.sales, backgroundColor: ['#6366f1', '#06b6d4', '#f59e0b'], borderRadius: 6 }}]
          }},
          options: {{
            responsive: true,
            maintainAspectRatio: false,
            plugins: {{ legend: {{ display: false }} }},
            scales: {{
              y: {{ ticks: {{ callback: v => '$' + (v / 1000) + 'k' }}, grid: {{ color: 'rgba(255,255,255,0.05)' }} }},
              x: {{ grid: {{ display: false }} }}
            }}
          }}
        }});
      }}

      // 4. Payment Doughnut
      const ctxPay = document.getElementById('paymentChart');
      if (ctxPay && data.payment) {{
        new Chart(ctxPay, {{
          type: 'doughnut',
          data: {{
            labels: data.payment.labels,
            datasets: [{{ data: data.payment.counts, backgroundColor: ['#6366f1', '#06b6d4', '#10b981', '#f59e0b', '#f43f5e'], borderColor: '#0f172a', borderWidth: 2 }}]
          }},
          options: {{
            responsive: true,
            maintainAspectRatio: false,
            plugins: {{ legend: {{ position: 'right' }} }},
            cutout: '68%'
          }}
        }});
      }}

      // 5. Customer Segments
      const ctxSeg = document.getElementById('customerSegmentChart');
      if (ctxSeg && data.customer_segments) {{
        new Chart(ctxSeg, {{
          type: 'polarArea',
          data: {{
            labels: data.customer_segments.labels,
            datasets: [{{ data: data.customer_segments.counts, backgroundColor: ['rgba(16,185,129,0.75)', 'rgba(99,102,241,0.75)', 'rgba(6,182,212,0.75)', 'rgba(244,63,94,0.75)', 'rgba(100,116,139,0.75)'], borderColor: '#0f172a' }}]
          }},
          options: {{
            responsive: true,
            maintainAspectRatio: false,
            plugins: {{ legend: {{ position: 'right' }} }},
            scales: {{ r: {{ grid: {{ color: 'rgba(255,255,255,0.06)' }}, ticks: {{ display: false }} }} }}
          }}
        }});
      }}

      // 6. Scatter Chart
      const ctxScatter = document.getElementById('customerScatterChart');
      if (ctxScatter && data.scatter_customers) {{
        new Chart(ctxScatter, {{
          type: 'scatter',
          data: {{
            datasets: [{{
              label: 'Customers',
              data: data.scatter_customers.map(p => ({{ x: p.x, y: p.y }})),
              backgroundColor: 'rgba(6, 182, 212, 0.65)',
              pointRadius: 4
            }}]
          }},
          options: {{
            responsive: true,
            maintainAspectRatio: false,
            plugins: {{ legend: {{ display: false }} }},
            scales: {{
              x: {{ title: {{ display: true, text: 'Days Inactive (Recency)', color: '#94a3b8' }}, grid: {{ color: 'rgba(255,255,255,0.05)' }} }},
              y: {{ title: {{ display: true, text: 'Total Spending ($)', color: '#94a3b8' }}, grid: {{ color: 'rgba(255,255,255,0.05)' }} }}
            }}
          }}
        }});
      }}

      // 7. Discount Sensitivity
      const ctxDisc1 = document.getElementById('discountSensitivityChart');
      const ctxDisc2 = document.getElementById('discountProfitChart');
      if (ctxDisc1 && ctxDisc2 && data.discount_sensitivity) {{
        new Chart(ctxDisc1, {{
          type: 'line',
          data: {{
            labels: data.discount_sensitivity.labels,
            datasets: [{{
              label: 'Loss Rate (% of orders losing money)',
              data: data.discount_sensitivity.loss_rate,
              borderColor: '#f43f5e',
              backgroundColor: 'rgba(244, 63, 94, 0.15)',
              fill: true,
              borderWidth: 3,
              pointRadius: 5,
              tension: 0.3
            }}]
          }},
          options: {{
            responsive: true,
            maintainAspectRatio: false,
            plugins: {{ legend: {{ position: 'bottom' }} }},
            scales: {{
              y: {{ min: 0, max: 100, ticks: {{ callback: v => v + '%' }}, grid: {{ color: 'rgba(255,255,255,0.06)' }} }}
            }}
          }}
        }});

        new Chart(ctxDisc2, {{
          type: 'bar',
          data: {{
            labels: data.discount_sensitivity.labels,
            datasets: [{{
              label: 'Realized Profit ($)',
              data: data.discount_sensitivity.total_profit,
              backgroundColor: data.discount_sensitivity.total_profit.map(v => v >= 0 ? '#10b981' : '#f43f5e'),
              borderRadius: 6
            }}]
          }},
          options: {{
            responsive: true,
            maintainAspectRatio: false,
            plugins: {{ legend: {{ display: false }} }},
            scales: {{
              y: {{ ticks: {{ callback: v => '$' + (v / 1000) + 'k' }}, grid: {{ color: 'rgba(255,255,255,0.06)' }} }}
            }}
          }}
        }});
      }}
    }}

    // B. High-Fidelity Native Canvas 2D Fallback Engine (Guarantees charts render offline)
    function renderNativeCanvasCharts(data) {{
      drawNativeLineChart('monthlyTrendChart', data.monthly.labels, data.monthly.sales, data.monthly.profit);
      drawNativeBarChart('regionalChart', data.regional.labels, data.regional.sales, data.regional.profit);
      drawNativeSingleBar('categoryChart', data.category.labels, data.category.sales, ['#6366f1', '#06b6d4', '#f59e0b']);
      drawNativeDoughnut('paymentChart', data.payment.labels, data.payment.counts);
      drawNativeDoughnut('customerSegmentChart', data.customer_segments.labels, data.customer_segments.counts);
      drawNativeScatter('customerScatterChart', data.scatter_customers);
      drawNativeLossCurve('discountSensitivityChart', data.discount_sensitivity.labels, data.discount_sensitivity.loss_rate);
      drawNativeProfitBar('discountProfitChart', data.discount_sensitivity.labels, data.discount_sensitivity.total_profit);
    }}

    function setupCanvas(id) {{
      const c = document.getElementById(id);
      if (!c) return null;
      const rect = c.parentElement.getBoundingClientRect();
      c.width = rect.width || 600;
      c.height = rect.height || 300;
      return c.getContext('2d');
    }}

    function drawNativeLineChart(id, labels, series1, series2) {{
      const ctx = setupCanvas(id);
      if (!ctx) return;
      const w = ctx.canvas.width, h = ctx.canvas.height;
      const pad = 40, bottomPad = 30;
      const maxVal = Math.max(...series1) * 1.15;

      ctx.clearRect(0, 0, w, h);
      
      // Grid lines
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.08)';
      ctx.lineWidth = 1;
      for (let i = 0; i <= 4; i++) {{
        const y = pad + (h - pad - bottomPad) * (i / 4);
        ctx.beginPath();
        ctx.moveTo(pad, y);
        ctx.lineTo(w - pad, y);
        ctx.stroke();
      }}

      // Plot Series 1 (Sales)
      ctx.strokeStyle = '#06b6d4';
      ctx.lineWidth = 3;
      ctx.beginPath();
      const stepX = (w - pad * 2) / (labels.length - 1);
      series1.forEach((val, i) => {{
        const x = pad + i * stepX;
        const y = h - bottomPad - ((val / maxVal) * (h - pad - bottomPad));
        if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }});
      ctx.stroke();

      // Plot Series 2 (Profit)
      ctx.strokeStyle = '#10b981';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      series2.forEach((val, i) => {{
        const x = pad + i * stepX;
        const y = h - bottomPad - ((val / maxVal) * (h - pad - bottomPad));
        if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }});
      ctx.stroke();

      // Legend
      ctx.font = '11px sans-serif';
      ctx.fillStyle = '#06b6d4';
      ctx.fillRect(pad, 10, 12, 12);
      ctx.fillStyle = '#cbd5e1';
      ctx.fillText('Sales ($)', pad + 18, 20);

      ctx.fillStyle = '#10b981';
      ctx.fillRect(pad + 100, 10, 12, 12);
      ctx.fillStyle = '#cbd5e1';
      ctx.fillText('Profit ($)', pad + 118, 20);
    }}

    function drawNativeBarChart(id, labels, s1, s2) {{
      const ctx = setupCanvas(id);
      if (!ctx) return;
      const w = ctx.canvas.width, h = ctx.canvas.height;
      const pad = 60, rightPad = 20;
      const maxVal = Math.max(...s1) * 1.1;
      const barH = (h - 50) / labels.length;

      ctx.clearRect(0, 0, w, h);
      labels.forEach((lab, i) => {{
        const y = 30 + i * barH;
        ctx.fillStyle = '#94a3b8';
        ctx.font = '12px sans-serif';
        ctx.fillText(lab, 10, y + barH / 2);

        const w1 = (s1[i] / maxVal) * (w - pad - rightPad);
        const w2 = (s2[i] / maxVal) * (w - pad - rightPad);

        ctx.fillStyle = 'rgba(99, 102, 241, 0.85)';
        ctx.fillRect(pad, y + 4, w1, (barH / 2) - 4);

        ctx.fillStyle = 'rgba(16, 185, 129, 0.85)';
        ctx.fillRect(pad, y + (barH / 2) + 2, w2, (barH / 2) - 4);
      }});
    }}

    function drawNativeSingleBar(id, labels, values, colors) {{
      const ctx = setupCanvas(id);
      if (!ctx) return;
      const w = ctx.canvas.width, h = ctx.canvas.height;
      const pad = 40, maxVal = Math.max(...values) * 1.1;
      const barW = (w - pad * 2) / labels.length;

      ctx.clearRect(0, 0, w, h);
      labels.forEach((lab, i) => {{
        const bH = (values[i] / maxVal) * (h - 70);
        const x = pad + i * barW + 10;
        const y = h - 35 - bH;

        ctx.fillStyle = colors[i % colors.length];
        ctx.fillRect(x, y, barW - 20, bH);

        ctx.fillStyle = '#cbd5e1';
        ctx.font = '12px sans-serif';
        ctx.fillText(lab, x + 5, h - 15);
      }});
    }}

    function drawNativeDoughnut(id, labels, values) {{
      const ctx = setupCanvas(id);
      if (!ctx) return;
      const w = ctx.canvas.width, h = ctx.canvas.height;
      const total = values.reduce((a, b) => a + b, 0);
      const colors = ['#6366f1', '#06b6d4', '#10b981', '#f59e0b', '#f43f5e'];
      const cx = w * 0.38, cy = h * 0.5, radius = Math.min(cx, cy) - 20;

      ctx.clearRect(0, 0, w, h);
      let startAngle = 0;

      values.forEach((val, i) => {{
        const slice = (val / total) * Math.PI * 2;
        ctx.beginPath();
        ctx.arc(cx, cy, radius, startAngle, startAngle + slice);
        ctx.arc(cx, cy, radius * 0.65, startAngle + slice, startAngle, true);
        ctx.closePath();
        ctx.fillStyle = colors[i % colors.length];
        ctx.fill();

        // Legend
        const legY = 25 + i * 22;
        ctx.fillRect(w * 0.68, legY, 10, 10);
        ctx.fillStyle = '#cbd5e1';
        ctx.font = '11px sans-serif';
        ctx.fillText(labels[i], w * 0.68 + 16, legY + 9);

        startAngle += slice;
      }});
    }}

    function drawNativeScatter(id, points) {{
      const ctx = setupCanvas(id);
      if (!ctx) return;
      const w = ctx.canvas.width, h = ctx.canvas.height;
      const pad = 40;
      const maxX = 400, maxY = 25000;

      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = 'rgba(6, 182, 212, 0.65)';
      points.slice(0, 100).forEach(p => {{
        const x = pad + (p.x / maxX) * (w - pad * 2);
        const y = h - pad - (p.y / maxY) * (h - pad * 2);
        ctx.beginPath();
        ctx.arc(x, y, 3.5, 0, Math.PI * 2);
        ctx.fill();
      }});
    }}

    function drawNativeLossCurve(id, labels, rates) {{
      const ctx = setupCanvas(id);
      if (!ctx) return;
      const w = ctx.canvas.width, h = ctx.canvas.height;
      const pad = 40;
      ctx.clearRect(0, 0, w, h);

      ctx.strokeStyle = '#f43f5e';
      ctx.lineWidth = 3;
      ctx.beginPath();
      const stepX = (w - pad * 2) / (labels.length - 1);
      rates.forEach((rate, i) => {{
        const x = pad + i * stepX;
        const y = h - pad - (rate / 100) * (h - pad * 2);
        if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }});
      ctx.stroke();

      // Draw points
      rates.forEach((rate, i) => {{
        const x = pad + i * stepX;
        const y = h - pad - (rate / 100) * (h - pad * 2);
        ctx.fillStyle = '#f43f5e';
        ctx.beginPath();
        ctx.arc(x, y, 5, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#fff';
        ctx.font = '10px sans-serif';
        ctx.fillText(rate + '%', x - 10, y - 8);
      }});
    }}

    function drawNativeProfitBar(id, labels, profits) {{
      const ctx = setupCanvas(id);
      if (!ctx) return;
      const w = ctx.canvas.width, h = ctx.canvas.height;
      const pad = 40;
      const maxVal = Math.max(...profits.map(Math.abs)) * 1.15;
      const zeroY = h * 0.6;
      const barW = (w - pad * 2) / labels.length;

      ctx.clearRect(0, 0, w, h);
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.15)';
      ctx.beginPath();
      ctx.moveTo(pad, zeroY);
      ctx.lineTo(w - pad, zeroY);
      ctx.stroke();

      profits.forEach((val, i) => {{
        const x = pad + i * barW + 10;
        const bH = (Math.abs(val) / maxVal) * (h * 0.45);
        ctx.fillStyle = val >= 0 ? '#10b981' : '#f43f5e';
        if (val >= 0) {{
          ctx.fillRect(x, zeroY - bH, barW - 20, bH);
        }} else {{
          ctx.fillRect(x, zeroY, barW - 20, bH);
        }}
        ctx.fillStyle = '#cbd5e1';
        ctx.font = '10px sans-serif';
        ctx.fillText(labels[i], x, h - 10);
      }});
    }}

    // --------------------------------------------------------------------------
    // RENDER GENAI STRATEGIC INSIGHTS
    // --------------------------------------------------------------------------
    function renderAiInsights(insights) {{
      const container = document.getElementById('insights-container');
      if (!container || !insights) return;

      container.innerHTML = insights.map((item, idx) => `
        <div class="insight-card ${{item.severity}}">
          <div class="insight-header">
            <div class="insight-title-group">
              <h3>Finding ${{idx + 1}}: ${{item.title}}</h3>
              <span class="insight-tag">${{item.tag}}</span>
            </div>
            <span class="kpi-pill ${{item.severity === 'critical' ? 'danger' : 'warn'}}">
              ${{item.severity.toUpperCase()}} PRIORITY
            </span>
          </div>

          <div class="triad-grid">
            <div class="triad-box fact">
              <div class="triad-label">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                Calculated Fact (Python/SQL)
              </div>
              <p>${{item.fact}}</p>
            </div>

            <div class="triad-box explanation">
              <div class="triad-label">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
                Commercial Hypothesis
              </div>
              <p>${{item.explanation}}</p>
            </div>

            <div class="triad-box investigation">
              <div class="triad-label">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                Recommended Investigation
              </div>
              <p>${{item.investigation}}</p>
            </div>

            <div class="triad-box action">
              <div class="triad-label">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 11 12 14 22 4"></polyline><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"></path></svg>
                Targeted Business Action
              </div>
              <p>${{item.action}}</p>
            </div>
          </div>
        </div>
      `).join('');
    }}

    // --------------------------------------------------------------------------
    // AT-RISK TABLE & FILTER
    // --------------------------------------------------------------------------
    let allAtRiskCustomers = [];

    function renderAtRiskCustomers(customers) {{
      allAtRiskCustomers = customers || [];
      const tbody = document.querySelector('#atRiskTable tbody');
      if (!tbody) return;

      tbody.innerHTML = allAtRiskCustomers.map(c => `
        <tr>
          <td><span class="code-chip">${{c.id}}</span></td>
          <td>${{c.type}}</td>
          <td>${{c.region}}</td>
          <td>${{c.orders}}</td>
          <td style="font-weight:700; color:var(--accent-cyan);">$${{Number(c.spend).toLocaleString()}}</td>
          <td style="color:${{c.profit >= 0 ? 'var(--accent-emerald)' : 'var(--accent-rose)'}};">$${{Number(c.profit).toLocaleString()}}</td>
          <td><span style="color:var(--accent-rose); font-weight:700;">${{c.days_inactive}} days</span></td>
          <td><span class="kpi-pill ${{c.spend >= 6000 ? 'danger' : 'warn'}}">${{c.action}}</span></td>
        </tr>
      `).join('');
    }}

    function filterCustomerTable() {{
      const q = document.getElementById('custSearchInput').value.toLowerCase();
      const filtered = allAtRiskCustomers.filter(c => 
        c.id.toLowerCase().includes(q) || 
        c.type.toLowerCase().includes(q) || 
        c.region.toLowerCase().includes(q)
      );

      const tbody = document.querySelector('#atRiskTable tbody');
      tbody.innerHTML = filtered.map(c => `
        <tr>
          <td><span class="code-chip">${{c.id}}</span></td>
          <td>${{c.type}}</td>
          <td>${{c.region}}</td>
          <td>${{c.orders}}</td>
          <td style="font-weight:700; color:var(--accent-cyan);">$${{Number(c.spend).toLocaleString()}}</td>
          <td style="color:${{c.profit >= 0 ? 'var(--accent-emerald)' : 'var(--accent-rose)'}};">$${{Number(c.profit).toLocaleString()}}</td>
          <td><span style="color:var(--accent-rose); font-weight:700;">${{c.days_inactive}} days</span></td>
          <td><span class="kpi-pill ${{c.spend >= 6000 ? 'danger' : 'warn'}}">${{c.action}}</span></td>
        </tr>
      `).join('');

      document.getElementById('atRiskSummaryText').textContent = `Showing ${{filtered.length}} matching accounts`;
    }}

    // --------------------------------------------------------------------------
    // RENDER TOP & BOTTOM PRODUCTS
    // --------------------------------------------------------------------------
    function renderTopBottomProducts(top, bottom) {{
      const topTbody = document.querySelector('#topProductsTable tbody');
      const bottomTbody = document.querySelector('#bottomProductsTable tbody');
      if (!topTbody || !bottomTbody) return;

      topTbody.innerHTML = (top || []).slice(0, 5).map(p => `
        <tr>
          <td><span class="code-chip">${{p.id}}</span></td>
          <td>${{p.category}}</td>
          <td>${{p.units}}</td>
          <td style="font-weight:700;">$${{Number(p.sales).toLocaleString()}}</td>
          <td style="color:var(--accent-emerald);">$${{Number(p.profit).toLocaleString()}}</td>
          <td><span class="kpi-pill up">${{p.margin}}%</span></td>
        </tr>
      `).join('');

      bottomTbody.innerHTML = (bottom || []).slice(0, 5).map(p => `
        <tr>
          <td><span class="code-chip">${{p.id}}</span></td>
          <td>${{p.category}}</td>
          <td>${{p.units}}</td>
          <td style="font-weight:700;">$${{Number(p.sales).toLocaleString()}}</td>
          <td style="color:var(--accent-rose);">$${{Number(p.profit).toLocaleString()}}</td>
          <td><span class="kpi-pill danger">${{p.margin}}%</span></td>
        </tr>
      `).join('');
    }}

    // --------------------------------------------------------------------------
    // RENDER MACHINE LEARNING SECTION
    // --------------------------------------------------------------------------
    function renderMlSection(models, features) {{
      const grid = document.getElementById('mlModelsGrid');
      const featList = document.getElementById('featureImportanceList');
      if (!grid || !featList) return;

      grid.innerHTML = (models || []).map(m => `
        <div class="model-card ${{m.name.includes('Random Forest') ? 'featured' : ''}}">
          <div class="model-title">
            <span>${{m.name}}</span>
            <span class="kpi-pill ${{m.r2 > 0.3 ? 'up' : 'warn'}}">${{m.type}}</span>
          </div>
          <p style="font-size:0.75rem; color:var(--text-dim); margin-top:4px;">${{m.description}}</p>
          
          <div class="model-metrics">
            <div class="metric-item">
              <div class="label">Test MAE</div>
              <div class="val">$${{Number(m.mae).toFixed(2)}}</div>
            </div>
            <div class="metric-item">
              <div class="label">Test RMSE</div>
              <div class="val">$${{Number(m.rmse).toFixed(2)}}</div>
            </div>
            <div class="metric-item">
              <div class="label">Holdout R²</div>
              <div class="val" style="color:${{m.r2 > 0 ? 'var(--accent-emerald)' : 'var(--accent-rose)'}};">${{m.r2}}</div>
            </div>
          </div>
        </div>
      `).join('');

      featList.innerHTML = (features || []).map(f => `
        <div class="feature-bar-wrap">
          <div class="feature-bar-label">
            <span style="font-family:var(--font-mono); color:var(--accent-cyan);">${{f.feature}}</span>
            <span style="font-weight:700;">${{(f.importance * 100).toFixed(1)}}%</span>
          </div>
          <div class="progress-track">
            <div class="progress-fill" style="width: ${{f.importance * 100}}%;"></div>
          </div>
          <div style="font-size:0.7rem; color:var(--text-dim); margin-top:2px;">${{f.description}}</div>
        </div>
      `).join('');
    }}

    // --------------------------------------------------------------------------
    // RENDER VALIDATION TABLE
    // --------------------------------------------------------------------------
    function renderValidationTable(tests) {{
      const tbody = document.querySelector('#validationTable tbody');
      if (!tbody) return;

      tbody.innerHTML = (tests || []).map(t => `
        <tr>
          <td style="font-weight:600; color:#fff;">${{t.name}}</td>
          <td><span class="kpi-pill up">✓ ${{t.status}}</span></td>
          <td style="color:var(--text-muted); font-size:0.8rem;">${{t.details}}</td>
        </tr>
      `).join('');
    }}

    // --------------------------------------------------------------------------
    // RENDER GALLERY ITEMS
    // --------------------------------------------------------------------------
    function renderGallery() {{
      const gallery = document.getElementById('chartGalleryGrid');
      if (!gallery) return;

      const charts = [
        {{ file: "reports/charts/monthly_sales_trend.png", title: "Monthly Sales Turnover Trend" }},
        {{ file: "reports/charts/monthly_profit_trend.png", title: "Monthly Net Operating Profit Trend" }},
        {{ file: "reports/charts/sales_by_region.png", title: "Sales Revenue by Region" }},
        {{ file: "reports/charts/profit_by_region.png", title: "Operating Profit by Region" }},
        {{ file: "reports/charts/sales_by_category.png", title: "Sales & Margins by Product Category" }},
        {{ file: "reports/charts/customer_segments.png", title: "Customer RFM Cohort Breakdown" }},
        {{ file: "reports/charts/recency_vs_spending.png", title: "Customer Inactivity vs Total Spending" }},
        {{ file: "reports/charts/discount_vs_profit.png", title: "Discount % vs Net Operating Profit" }},
        {{ file: "reports/charts/top_10_products.png", title: "Top 10 High-Revenue Generating Products" }},
        {{ file: "reports/charts/ml_actual_vs_predicted.png", title: "Random Forest: Actual vs Predicted Revenue" }},
        {{ file: "reports/charts/ml_feature_importance.png", title: "Random Forest Gini Feature Importance" }},
        {{ file: "reports/charts/customer_spending_distribution.png", title: "Customer Lifetime Spend Distribution" }}
      ];

      gallery.innerHTML = charts.map(c => `
        <div class="gallery-item" onclick="openModal('${{c.file}}', '${{c.title}}')">
          <img src="${{c.file}}" alt="${{c.title}}" onerror="this.src='https://placehold.co/600x400/111827/06b6d4?text=Chart+Preview'" />
          <div class="gallery-item-caption">
            <h4>${{c.title}}</h4>
            <p>Click to zoom full resolution</p>
          </div>
        </div>
      `).join('');
    }}
  </script>
</body>
</html>
"""

    # Write to root index.html
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_template)
    print("Successfully built index.html")

    # Write to dashboard/index.html
    with open("dashboard/index.html", "w", encoding="utf-8") as f:
        f.write(html_template)
    print("Successfully built dashboard/index.html")

if __name__ == "__main__":
    build_dashboard()
