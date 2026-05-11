---
demo:
    title: 'Business Manager Demo'
layout: none
---

<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Business Manager Demo | Learning</title>
<link rel="stylesheet" href="../../Allfiles/demo-style.css">
<style>:root { --hero-from: #1A237E; --hero-via: #283593; --hero-to: #0078D4; }</style>
</head>
<body>

<div class="back-bar">
  <a href="https://emontes07.github.io/Learning/">← Back to Index</a>
</div>

<div class="hero">
  <div class="hero-inner">
    <h1>Microsoft 365 Copilot for Business Managers</h1>
    <p class="subtitle">Spot issues, research solutions, and align your team</p>
    <div class="scenario">
      <strong>Scenario:</strong> Analyze sales performance and customer feedback to address a product issue, then collaborate with your team to plan improvements.
    </div>
    <div class="hero-meta">
      <span>📊 Business Management</span>
      <span>📈 Excel</span>
      <span>💬 Copilot Chat</span>
      <span>📧 Outlook</span>
    </div>
  </div>
</div>

<div class="sidebar-overlay" id="sidebarOverlay" onclick="closeSidebar()"></div>

<div class="layout">

<nav class="sidebar" id="sidebar">
  <a class="sb-home" href="https://emontes07.github.io/Learning/">← Back to Index</a>
  <div class="sb-title">Business Manager Demo</div>

  <a href="#sec-objectives" class="section-link">Learning Objectives</a>
  <a href="#sec-prereqs" class="section-link">Demo Setup</a>

    <a href="#part1" class="part-link">Part 1: Copilot in Excel</a>
  <a href="#part2" class="part-link">Part 2: Copilot Chat</a>
  <a href="#part3" class="part-link">Part 3: Copilot in Outlook</a>

  <a href="#sec-takeaways" class="section-link" style="margin-top:0.5rem;">Key Takeaways</a>
</nav>

<div class="main-content">

<div class="section" id="sec-objectives">
  <h2>🎯 Learning Objectives</h2>
  <ul class="objectives-list">
    <li>Analyze sales data and customer reviews in Excel</li>
    <li>Research industry context with Copilot Chat</li>
    <li>Schedule a working session with the product team</li>
  </ul>
</div>

<div class="section" id="sec-prereqs">
  <h2>📋 Demo Setup</h2>
  <p>Required file from the MS-4021 GitHub <a href='https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/tree/master/ResourceFiles' target='_blank'>repository</a>:</p>    <ul class="tips-list">
      <li><a href='https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/raw/master/ResourceFiles/EV_Charger_Sales_Analysis_v1.xlsx'>EV_Charger_Sales_Analysis_v1.xlsx</a></li>
    </ul><div class="callout warn"><strong>📝 NOTE:</strong> Allow up to 10 minutes for OneDrive sync.</div>
</div>

<div class="part-card" id="part1">
  <div class="part-header-bar green"></div>
  <div class="part-header" onclick="togglePart('body1', this)">
    <h2>Part 1: Copilot in Excel — Spot the Issue in Your Data</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body1">
<div class="callout"><strong>💡 Why This Matters:</strong> Copilot turns Excel into a conversational analyst — calculate, highlight, and surface insights in plain English.</div>
    <ol class="steps" start="1">
      <li>Open <strong>EV_Charger_Sales_Analysis_v1.xlsx</strong> in Excel.</li>
      <li>Navigate to the <strong>Sales by Product</strong> tab.</li>
    </ol>
<div class="prompt-box">Calculate monthly revenue by product and add a column with total revenue - refer to the Prices worksheet.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="prompt-box">What is the total revenue for each category so far in 2024?<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="prompt-box">Highlight rows where the value in column H is less than $100K.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <ol class="steps" start="3">
      <li>Navigate to the <strong>Reviews</strong> tab to analyze customer feedback.</li>
    </ol>
<div class="prompt-box">Summarize the top 3 customer concerns we should focus on.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="prompt-box">Highlight reviews that mention issues related to charging speeds.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <div class="self-check">
      <h4>✅ Self-Check: Part 1</h4>
      <label><input type="checkbox"> I calculated and highlighted in Excel</label>
      <label><input type="checkbox"> I identified a customer pain point in reviews</label>
    </div>
  </div>
</div>

<div class="part-card" id="part2">
  <div class="part-header-bar blue"></div>
  <div class="part-header" onclick="togglePart('body2', this)">
    <h2>Part 2: Copilot Chat — Research the Charging Speed Issue</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body2">
<div class="callout"><strong>💡 Why This Matters:</strong> Once you've identified a problem, Copilot helps you research industry-wide causes and competitive responses.</div>
    <ol class="steps" start="1">
      <li>Open <a href='https://m365copilot.com' target='_blank'>M365copilot.com</a> in Web mode.</li>
    </ol>
<div class="prompt-box">Research common issues with EV charger speeds and identify potential causes or solutions. Summarize findings in a format suitable for a business presentation. Highlight any relevant industry benchmarks or competitor data.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="prompt-box">What are the latest innovations or technologies addressing slow EV charger speeds in 2024?<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="prompt-box">Assuming competitors in the EV charging market are improving speed by 20% annually, suggest how we could position our CC-2001 and CC-2000 models to stay competitive.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="prompt-box">Based on this information, suggest 5 strategic questions to ask the product team during our meeting tomorrow. Focus on identifying root causes, assessing risks, and brainstorming potential improvements.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <div class="self-check">
      <h4>✅ Self-Check: Part 2</h4>
      <label><input type="checkbox"> I researched industry context</label>
      <label><input type="checkbox"> I prepared strategic questions for the product team</label>
    </div>
  </div>
</div>

<div class="part-card" id="part3">
  <div class="part-header-bar purple"></div>
  <div class="part-header" onclick="togglePart('body3', this)">
    <h2>Part 3: Copilot in Outlook — Convene the Team</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body3">
<div class="callout"><strong>💡 Why This Matters:</strong> Lock in the meeting with the right people and a productive agenda.</div>
    <ol class="steps" start="1">
      <li>Open <a href='https://outlook.office.com' target='_blank'>outlook.office.com</a>.</li>
      <li>Click the <strong>Copilot</strong> icon.</li>
    </ol>
<div class="prompt-box">I need to schedule a meeting with [/Pick a colleague] tomorrow afternoon to discuss the EV charger issue reports. Can you suggest a time that works? If they are unavailable, please suggest an alternative time.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <ol class="steps" start="3">
      <li>Edit the proposed event, confirm availability via Scheduling Assistant.</li>
      <li>Click <strong>Draft with Copilot</strong> in the event body.</li>
    </ol>
<div class="prompt-box">Create an agenda for a meeting to discuss slow charging speeds with our CC-2001 and CC-2000 models. Include time for an introduction to the issue, a review of any available data or customer feedback, and a brainstorming session for potential solutions.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <div class="self-check">
      <h4>✅ Self-Check: Part 3</h4>
      <label><input type="checkbox"> I scheduled the working session</label>
      <label><input type="checkbox"> I drafted a focused agenda</label>
    </div>
  </div>
</div>

<div class="section" id="sec-takeaways">
  <h2>🔑 Key Takeaways</h2>
  <div class="takeaways-grid">
    <div class="takeaway-card"><div class="icon">🔎</div><h4>Find the Signal</h4><p>Let Copilot find patterns in volume — sales and feedback alike.</p></div>
    <div class="takeaway-card"><div class="icon">🌐</div><h4>Context from the Web</h4><p>Pair internal data with industry context.</p></div>
    <div class="takeaway-card"><div class="icon">🤝</div><h4>Drive Alignment</h4><p>Get the right team in the room with a clear agenda.</p></div>
    <div class="takeaway-card"><div class="icon">✅</div><h4>Ask Better Questions</h4><p>Use AI-prepared questions to lead better conversations.</p></div>
  </div>
</div>

</div>
</div>

<footer>
  <p><strong>Microsoft 365 Copilot — Business Manager Demo</strong></p>
  <p>For questions or feedback, reach out to your training facilitator.</p>
</footer>

<button class="sidebar-toggle" id="sidebarToggle" onclick="openSidebar()" aria-label="Open navigation">☰</button>

<script src="../../Allfiles/demo-script.js"></script>
</body>
</html>
