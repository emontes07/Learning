---
demo:
    title: 'Researcher and Analyst Demo'
layout: none
---

<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Researcher and Analyst Demo | Learning</title>
<link rel="stylesheet" href="../../Allfiles/demo-style.css">
<style>:root { --hero-from: #1A237E; --hero-via: #283593; --hero-to: #0078D4; }</style>
</head>
<body>

<div class="back-bar">
  <a href="https://emontes07.github.io/Learning/">← Back to Index</a>
</div>

<div class="hero">
  <div class="hero-inner">
    <h1>Microsoft 365 Copilot — Researcher & Analyst Agents</h1>
    <p class="subtitle">Expert agents for deep research and data analysis</p>
    <div class="scenario">
      <strong>Scenario:</strong> Demonstrate how Researcher and Analyst — two expert agents built into the Copilot app — tackle multi-step research and advanced data analysis. Researcher combines web data with your company's files; Analyst thinks like a data scientist and can run Python on your behalf.
    </div>
    <div class="hero-meta">
      <span>🔬 Researcher</span>
      <span>📊 Analyst</span>
      <span>🤖 Agents</span>
      <span>🎯 Strategy</span>
    </div>
  </div>
</div>

<div class="sidebar-overlay" id="sidebarOverlay" onclick="closeSidebar()"></div>

<div class="layout">

<nav class="sidebar" id="sidebar">
  <a class="sb-home" href="https://emontes07.github.io/Learning/">← Back to Index</a>
  <div class="sb-title">Researcher & Analyst Demo</div>

  <a href="#sec-objectives" class="section-link">Learning Objectives</a>
  <a href="#sec-prereqs" class="section-link">Demo Setup</a>

    <a href="#part1" class="part-link">Part 1: Researcher</a>
  <a href="#part2" class="part-link">Part 2: Analyst</a>

  <a href="#sec-takeaways" class="section-link" style="margin-top:0.5rem;">Key Takeaways</a>
</nav>

<div class="main-content">

<div class="section" id="sec-objectives">
  <h2>🎯 Learning Objectives</h2>
  <ul class="objectives-list">
    <li>Use Researcher to build a citation-backed marketing plan</li>
    <li>Use Analyst to identify customer segments and model financials</li>
    <li>Understand when to reach for each agent</li>
  </ul>
</div>

<div class="section" id="sec-prereqs">
  <h2>📋 Demo Setup</h2>
  <p>Download the <a href='https://microsoft.sharepoint.com/:u:/r/teams/MTTCentral/Immersion%20Experience%20Source%20Control/MS-4021%20Copilot%20Immersion%20Experience/Demos/Agent%20Demo%20Sample%20Docs/Researcher%20and%20Analyst%20Demo%20-%20Content%20Pack.zip?csf=1&web=1&e=384sFW' target='_blank'>Researcher and Analyst Demo - Content Pack</a> for all required files.</p><div class="callout green"><strong>💡 TIP:</strong> Create a demo SharePoint site to host the files, or reference them locally with <strong>/</strong>.</div>
    <p>To access the agents:</p>
    <ul class="tips-list">
      <li>Open the <strong>Copilot app</strong> at <a href='https://m365.cloud.microsoft' target='_blank'>m365.cloud.microsoft</a>.</li>
      <li>Use the left navigation to select <strong>Researcher</strong> or <strong>Analyst</strong>.</li>
    </ul><div class="callout"><strong>📝 Note:</strong> Point Researcher and Analyst at internal files (SharePoint/OneDrive) for grounded insights.</div>
</div>

<div class="part-card" id="part1">
  <div class="part-header-bar purple"></div>
  <div class="part-header" onclick="togglePart('body1', this)">
    <h2>Part 1: Researcher — Build a Marketing Plan</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body1">
<div class="callout"><strong>💡 Why This Matters:</strong> Researcher acts like a senior consultant — blending internal files, competitor intelligence, and web sources into structured deliverables with citations.</div>
<div class="callout warn"><strong>⚠️ IMPORTANT:</strong> Run this prompt at the start of training (slide 5) — Researcher needs a few minutes to complete it.</div>
    <ol class="steps" start="1">
      <li>Open <strong>Researcher</strong> from the left navigation of the Copilot app.</li>
    </ol>
    <p><img src='../Prompts/Media/researcher.png' alt='Researcher in M365 Copilot menu' style='max-width:100%;border-radius:6px;' /></p>
    <ol class="steps" start="2">
      <li>Enter the prompt below.</li>
    </ol>
<div class="prompt-box">Create a marketing plan for our newest SprintCycle EV charger launch. Emphasize its AI-powered adaptive charging, modular design, and biometric access control. Make sure to include recommendations on the right digital channels and content strategy. Include insights from competitors and our past GTM campaigns.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <ol class="steps" start="3">
      <li>Attach reference files using <strong>/</strong>:</li>
    </ol>
    <ul class="tips-list">
      <li><strong>/SprintCycle Charger Product Launch.docx</strong></li>
      <li><em>(Optional)</em> <strong>/Contoso - PedalPerks GTM Plan.docx</strong></li>
    </ul>
    <ol class="steps" start="4">
      <li>Click <strong>Submit</strong> and watch Researcher work.</li>
    </ol>
    <p>Researcher will combine internal and web sources, structure a marketing plan with channel recommendations, and cite its sources so you can validate.</p>
<div class="callout"><strong>📝 Note:</strong> Researcher shows its chain of thought and can call other agents when needed.</div>
    <div class="self-check">
      <h4>✅ Self-Check: Part 1</h4>
      <label><input type="checkbox"> I ran Researcher with grounding files</label>
      <label><input type="checkbox"> I reviewed the citations and reasoning</label>
    </div>
  </div>
</div>

<div class="part-card" id="part2">
  <div class="part-header-bar green"></div>
  <div class="part-header" onclick="togglePart('body2', this)">
    <h2>Part 2: Analyst — Segment Customers & Model Financials</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body2">
<div class="callout"><strong>💡 Why This Matters:</strong> Analyst behaves like a data scientist on your team — performing advanced analysis and Python execution, with visualizations to back its recommendations.</div>
    <ol class="steps" start="1">
      <li>Open <strong>Analyst</strong> from the left navigation.</li>
    </ol>
    <p><img src='../Prompts/Media/Analyst.png' alt='Analyst in M365 Copilot menu' style='max-width:100%;border-radius:6px;' /></p>
    <ol class="steps" start="2">
      <li>Enter the prompt below.</li>
    </ol>
<div class="prompt-box">Find the right customer segment and demographic to sell our new EV charger, include a graph to show how this will maximize our market opportunity.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <ol class="steps" start="3">
      <li>Attach <strong>BoulderEV ebike Internal Market Forecast.xlsx</strong> using <strong>+</strong>.</li>
    </ol>
    <p><img src='../Prompts/Media/Analyst-attach-files.png' alt='Attach files in Analyst' style='max-width:100%;border-radius:6px;' /></p>
    <ol class="steps" start="4">
      <li>Click <strong>Submit</strong>.</li>
    </ol>
    <h3>Additional Analyst scenarios</h3>
    <p>Each follows the same pattern: prompt → attach file → submit → review.</p>
    <h4>Financial Projection</h4>
<div class="prompt-box">Build a 5-year financial projection from this data along with a graph to view revenue growth over time.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <p>File: <strong>BoulderEV ebike Internal Market Forecast.xlsx</strong></p>
    <h4>Sales Performance</h4>
<div class="prompt-box">Analyze sales volume across locations to identify our highest and lowest performing stores, along with a visualization of the best-selling products.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <p>File: <strong>BoulderEV ebike Internal Market Forecast.xlsx</strong></p>
    <h4>Campaign Performance</h4>
<div class="prompt-box">Analyze and visualize how the marketing campaign performed across each target segment and help me decide where to re-target our next campaign.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <p>File: <strong>BoulderEV ebike Internal Market Forecast.xlsx</strong></p>
    <div class="self-check">
      <h4>✅ Self-Check: Part 2</h4>
      <label><input type="checkbox"> I ran customer segmentation with Analyst</label>
      <label><input type="checkbox"> I tried at least one additional scenario</label>
    </div>
  </div>
</div>

<div class="section" id="sec-takeaways">
  <h2>🔑 Key Takeaways</h2>
  <div class="takeaways-grid">
    <div class="takeaway-card"><div class="icon">🧠</div><h4>Researcher = Strategy</h4><p>Citation-backed deliverables in minutes.</p></div>
    <div class="takeaway-card"><div class="icon">🧮</div><h4>Analyst = Data Science</h4><p>Advanced analysis without needing to code.</p></div>
    <div class="takeaway-card"><div class="icon">🔗</div><h4>Better Together</h4><p>Pair them for the full strategy-to-execution flow.</p></div>
    <div class="takeaway-card"><div class="icon">⏱️</div><h4>Weeks → Minutes</h4><p>Shorten the path from question to insight.</p></div>
  </div>
</div>

</div>
</div>

<footer>
  <p><strong>Microsoft 365 Copilot — Researcher & Analyst Demo</strong></p>
  <p>For questions or feedback, reach out to your training facilitator.</p>
</footer>

<button class="sidebar-toggle" id="sidebarToggle" onclick="openSidebar()" aria-label="Open navigation">☰</button>

<script src="../../Allfiles/demo-script.js"></script>
</body>
</html>
