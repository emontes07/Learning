---
demo:
    title: 'Finance Demo'
layout: none
---

<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Finance Demo | Learning</title>
<link rel="stylesheet" href="../../Allfiles/demo-style.css">
<style>:root { --hero-from: #1B5E20; --hero-via: #2E7D32; --hero-to: #43A047; }</style>
</head>
<body>

<div class="back-bar">
  <a href="https://emontes07.github.io/Learning/">← Back to Index</a>
</div>

<div class="hero">
  <div class="hero-inner">
    <h1>Microsoft 365 Copilot for Finance</h1>
    <p class="subtitle">Analyze, benchmark, and communicate — financial insights at speed</p>
    <div class="scenario">
      <strong>Scenario:</strong> You're a financial analyst at Contoso, responsible for evaluating sales performance and market positioning in the EV charging industry. Your goal is to analyze sales data, generate insights, and prepare a summary for your team.
    </div>
    <div class="hero-meta">
      <span>💰 Finance</span>
      <span>📈 Excel</span>
      <span>💬 Copilot Chat</span>
      <span>📝 Word</span>
    </div>
  </div>
</div>

<div class="sidebar-overlay" id="sidebarOverlay" onclick="closeSidebar()"></div>

<div class="layout">

<nav class="sidebar" id="sidebar">
  <a class="sb-home" href="https://emontes07.github.io/Learning/">← Back to Index</a>
  <div class="sb-title">Finance Demo</div>

  <a href="#sec-objectives" class="section-link">Learning Objectives</a>
  <a href="#sec-prereqs" class="section-link">Demo Setup</a>

    <a href="#part1" class="part-link">Part 1: Copilot in Excel</a>
  <a href="#part2" class="part-link">Part 2: Copilot Chat</a>
  <a href="#part3" class="part-link">Part 3: Copilot in Word</a>

  <a href="#sec-takeaways" class="section-link" style="margin-top:0.5rem;">Key Takeaways</a>
</nav>

<div class="main-content">

<div class="section" id="sec-objectives">
  <h2>🎯 Learning Objectives</h2>
  <ul class="objectives-list">
    <li>Crunch sales data in Excel with conversational prompts</li>
    <li>Benchmark performance against industry and competitors</li>
    <li>Communicate key financial insights to your team</li>
  </ul>
</div>

<div class="section" id="sec-prereqs">
  <h2>📋 Demo Setup</h2>
  <p>Required file from the MS-4021 GitHub <a href='https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/tree/master/ResourceFiles' target='_blank'>repository</a>:</p>    <ul class="tips-list">
      <li><a href='https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/raw/master/ResourceFiles/EV_Charger_Sales_Analysis_v1.xlsx'>EV_Charger_Sales_Analysis_v1.xlsx</a></li>
    </ul>
</div>

<div class="part-card" id="part1">
  <div class="part-header-bar green"></div>
  <div class="part-header" onclick="togglePart('body1', this)">
    <h2>Part 1: Copilot in Excel — Analyze the Numbers</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body1">
<div class="callout"><strong>💡 Why This Matters:</strong> No more wrestling with formulas. Copilot drives Excel from natural-language prompts.</div>
    <ol class="steps" start="1">
      <li>Open <strong>EV_Charger_Sales_Analysis_v1.xlsx</strong> in Excel.</li>
      <li>Navigate to <strong>Sales by Product</strong>.</li>
    </ol>
<div class="prompt-box">Sort the table by date in descending order, from the most recent to the oldest entry.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="prompt-box">Add a new column named 'Total Revenue'. Populate it by multiplying 'Units Sold' by 'Product Price' for each row.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="prompt-box">Create a summary table for total sales in 2024. The table should include Product ID, total units sold, and total revenue.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="prompt-box">Identify the product ID with the highest total revenue in 2024. Provide both total revenue and total units sold for better comparison.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <ol class="steps" start="3">
      <li>Navigate to the <strong>Customers</strong> sheet.</li>
    </ol>
<div class="prompt-box">Sort the 'Customers' tab by annual revenue in descending order.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="prompt-box">Calculate the average revenue per customer.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="prompt-box">Analyze the data to determine which industry has the highest total power consumption. Provide the industry name and total power usage.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <p>Save the workbook and copy the shared URL (enable AutoSave).</p>
    <div class="self-check">
      <h4>✅ Self-Check: Part 1</h4>
      <label><input type="checkbox"> I sorted, totaled, and summarized the data</label>
      <label><input type="checkbox"> I identified top-revenue products and customers</label>
    </div>
  </div>
</div>

<div class="part-card" id="part2">
  <div class="part-header-bar blue"></div>
  <div class="part-header" onclick="togglePart('body2', this)">
    <h2>Part 2: Copilot Chat — Benchmark Against the Industry</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body2">
<div class="callout"><strong>💡 Why This Matters:</strong> Numbers without context don't tell a story. Copilot pulls competitive intel and industry benchmarks.</div>
    <ol class="steps" start="1">
      <li>Open <a href='https://m365copilot.com' target='_blank'>M365copilot.com</a> in Web mode.</li>
    </ol>
<div class="prompt-box">Our total revenue for [EV chargers] exceeded $50,000,000 for first half of 2024. Compare this to the industry average and provide insights on whether we are above or below industry standards. If possible, include market share estimates and trends.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="prompt-box">Summarize the key financial statements of two major competitors in the [EV charging] industry. Include revenue, net profit, and any other relevant financial insights. If available, provide comparisons to our financial performance.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="prompt-box">Export this conversation, including financial insights, to a Word document for further review.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <p>Open the resulting document (e.g., <strong>Charging_industry_Financial_Summary.docx</strong>), enable editing, and copy the shared URL.</p>
    <div class="self-check">
      <h4>✅ Self-Check: Part 2</h4>
      <label><input type="checkbox"> I benchmarked our performance vs. industry and competitors</label>
      <label><input type="checkbox"> I exported insights to Word</label>
    </div>
  </div>
</div>

<div class="part-card" id="part3">
  <div class="part-header-bar navy"></div>
  <div class="part-header" onclick="togglePart('body3', this)">
    <h2>Part 3: Copilot in Word — Brief Your Team</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body3">
<div class="callout"><strong>💡 Why This Matters:</strong> Insight isn't valuable until it's shared. Copilot turns your findings into a team-ready email.</div>
    <ol class="steps" start="1">
      <li>Open a new Word document.</li>
      <li>In <strong>Describe what you'd like to write</strong>, enter the prompt below.</li>
    </ol>
<div class="prompt-box">Draft an email to my team summarizing the key insights from [Charging_industry_Financial_Summary.docx].<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="callout"><strong>📝 NOTE:</strong> Attach the file or paste the share link so Copilot can read it.</div>
<div class="prompt-box">Shorten this email draft<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <ul class="tips-list">
      <li>Ask Copilot to reword for a more professional tone.</li>
      <li>Expand with additional sections.</li>
      <li>Try a less formal version for a peer-to-peer audience.</li>
    </ul>
    <div class="self-check">
      <h4>✅ Self-Check: Part 3</h4>
      <label><input type="checkbox"> I drafted a team email summarizing the financial insights</label>
    </div>
  </div>
</div>

<div class="section" id="sec-takeaways">
  <h2>🔑 Key Takeaways</h2>
  <div class="takeaways-grid">
    <div class="takeaway-card"><div class="icon">📊</div><h4>Analyze in Plain English</h4><p>Replace formulas with conversation.</p></div>
    <div class="takeaway-card"><div class="icon">🌐</div><h4>Always Bring Context</h4><p>Pair your numbers with industry benchmarks.</p></div>
    <div class="takeaway-card"><div class="icon">✉️</div><h4>Communicate the Story</h4><p>Turn analysis into a clear team brief.</p></div>
    <div class="takeaway-card"><div class="icon">✅</div><h4>Verify Critical Numbers</h4><p>Spot-check key figures before sharing.</p></div>
  </div>
</div>

</div>
</div>

<footer>
  <p><strong>Microsoft 365 Copilot — Finance Demo</strong></p>
  <p>For questions or feedback, reach out to your training facilitator.</p>
</footer>

<button class="sidebar-toggle" id="sidebarToggle" onclick="openSidebar()" aria-label="Open navigation">☰</button>

<script src="../../Allfiles/demo-script.js"></script>
</body>
</html>
