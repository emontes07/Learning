---
demo:
    title: 'Sales Demo'
layout: none
---

<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Sales Demo | Learning</title>
<link rel="stylesheet" href="../../Allfiles/demo-style.css">
<style>:root { --hero-from: #C73E1D; --hero-via: #E64A19; --hero-to: #FF8A00; }</style>
</head>
<body>

<div class="back-bar">
  <a href="https://emontes07.github.io/Learning/">← Back to Index</a>
</div>

<div class="hero">
  <div class="hero-inner">
    <h1>Microsoft 365 Copilot for Sales</h1>
    <p class="subtitle">From market research to revenue strategy to executive deck</p>
    <div class="scenario">
      <strong>Scenario:</strong> You're in sales for an EV charging company and are developing a strategic plan for the upcoming year. Use Copilot to research market trends, analyze your company's performance, draft proposals, and build leadership-ready presentations.
    </div>
    <div class="hero-meta">
      <span>💼 Sales</span>
      <span>💬 Copilot Chat</span>
      <span>📝 Word</span>
      <span>🎯 PowerPoint</span>
      <span>📊 Strategy</span>
    </div>
  </div>
</div>

<div class="sidebar-overlay" id="sidebarOverlay" onclick="closeSidebar()"></div>

<div class="layout">

<nav class="sidebar" id="sidebar">
  <a class="sb-home" href="https://emontes07.github.io/Learning/">← Back to Index</a>
  <div class="sb-title">Sales Demo</div>

  <a href="#sec-objectives" class="section-link">Learning Objectives</a>
  <a href="#sec-prereqs" class="section-link">Demo Setup</a>

    <a href="#part1" class="part-link">Part 1: Copilot Chat</a>
  <a href="#part2" class="part-link">Part 2: Copilot in Word</a>
  <a href="#part3" class="part-link">Part 3: Copilot in PowerPoint</a>

  <a href="#sec-takeaways" class="section-link" style="margin-top:0.5rem;">Key Takeaways</a>
</nav>

<div class="main-content">

<div class="section" id="sec-objectives">
  <h2>🎯 Learning Objectives</h2>
  <ul class="objectives-list">
    <li>Research EV market trends and benchmark performance</li>
    <li>Visualize quarterly sales trends from your own data</li>
    <li>Draft an actionable sales proposal and translate it into a leadership deck</li>
  </ul>
</div>

<div class="section" id="sec-prereqs">
  <h2>📋 Demo Setup</h2>
  <p>Required file from the MS-4021 GitHub <a href='https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/tree/master/ResourceFiles' target='_blank'>repository</a>:</p>    <ul class="tips-list">
      <li><a href='https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/raw/master/ResourceFiles/Charger_sales_report_2022-2024.xlsx'>Charger_sales_report_2022-2024.xlsx</a></li>
    </ul><div class="callout warn"><strong>📝 NOTE:</strong> Allow up to 10 minutes for OneDrive sync after download.</div>
</div>

<div class="part-card" id="part1">
  <div class="part-header-bar blue"></div>
  <div class="part-header" onclick="togglePart('body1', this)">
    <h2>Part 1: Copilot Chat — Market Research & Sales Analysis</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body1">
<div class="callout"><strong>💡 Why This Matters:</strong> Strategy starts with context. Copilot blends industry data with your own numbers so you can see where you stand.</div>
    <ol class="steps" start="1">
      <li>Open <a href='https://m365copilot.com' target='_blank'>M365copilot.com</a> and ensure <strong>Web mode</strong> is selected.</li>
      <li>Start with a market-level research prompt.</li>
    </ol>
<div class="prompt-box">What is the ratio of EV cars to EV chargers by region in the US for the past 3 years? Please show it in a table organized by region.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <ol class="steps" start="3">
      <li>Upload <strong>Charger_sales_report_2022-2024.xlsx</strong> via <strong>Add Content</strong>, then run the next prompt.</li>
    </ol>
<div class="prompt-box">I need to know the quarterly trends for each of our sales regions. Create a quarterly revenue line graph for the past 2 years based on the attached data.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <ol class="steps" start="4">
      <li>Ask Copilot for actionable recommendations and export to Word.</li>
    </ol>
<div class="prompt-box">Based on the trend, suggest two ways I can increase EV charger sales in the Mountain and Midwest regions. Export the recommendations to a Word Document.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <div class="self-check">
      <h4>✅ Self-Check: Part 1</h4>
      <label><input type="checkbox"> I researched market trends</label>
      <label><input type="checkbox"> I visualized my own sales data</label>
      <label><input type="checkbox"> I exported recommendations to Word</label>
    </div>
  </div>
</div>

<div class="part-card" id="part2">
  <div class="part-header-bar navy"></div>
  <div class="part-header" onclick="togglePart('body2', this)">
    <h2>Part 2: Copilot in Word — Draft a Sales Proposal</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body2">
<div class="callout"><strong>💡 Why This Matters:</strong> Recommendations are just ideas until you make them actionable. Copilot turns strategy bullets into a full proposal with owners and timelines.</div>
    <ol class="steps" start="1">
      <li>Open the Word document generated by Copilot in Part 1.</li>
      <li>Click anywhere in the body → click the <strong>Copilot</strong> icon.</li>
    </ol>
<div class="prompt-box">Draft a detailed proposal on how we could implement each of the strategies outlined in this document. Ensure the plan is actionable and includes resource requirements, timelines, and key stakeholders.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <ol class="steps" start="3">
      <li>Save as <strong>EV Sales Proposal.docx</strong> and copy the shared URL.</li>
    </ol>
<div class="callout green"><strong>💡 Trainer Tip:</strong> Use this step to show how Copilot builds on prior outputs — refining ideas into a cohesive proposal.</div>
    <div class="self-check">
      <h4>✅ Self-Check: Part 2</h4>
      <label><input type="checkbox"> I drafted a proposal grounded on Part 1's recommendations</label>
      <label><input type="checkbox"> I saved and shared the document</label>
    </div>
  </div>
</div>

<div class="part-card" id="part3">
  <div class="part-header-bar magenta"></div>
  <div class="part-header" onclick="togglePart('body3', this)">
    <h2>Part 3: Copilot in PowerPoint — Leadership Deck</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body3">
<div class="callout"><strong>💡 Why This Matters:</strong> Get to a leadership-ready deck without rebuilding from scratch — Copilot creates slides from your proposal.</div>
    <ol class="steps" start="1">
      <li>Open a new presentation at <a href='https://powerpoint.new' target='_blank'>PowerPoint.new</a>.</li>
      <li>In the Copilot pane, select <strong>Create presentation from file</strong>.</li>
      <li>Paste the <strong>EV Sales Proposal.docx</strong> link.</li>
    </ol>
<div class="prompt-box">Create a presentation from [Link to EV Sales Proposal.docx].<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="callout"><strong>📝 NOTE:</strong> Slide generation can take up to two minutes depending on document complexity.</div>
    <div class="self-check">
      <h4>✅ Self-Check: Part 3</h4>
      <label><input type="checkbox"> I generated a sales deck from the proposal</label>
      <label><input type="checkbox"> I reviewed slides and notes</label>
    </div>
  </div>
</div>

<div class="section" id="sec-takeaways">
  <h2>🔑 Key Takeaways</h2>
  <div class="takeaways-grid">
    <div class="takeaway-card"><div class="icon">📈</div><h4>Data-Backed Strategy</h4><p>Combine market context with your own numbers.</p></div>
    <div class="takeaway-card"><div class="icon">🎯</div><h4>Make It Actionable</h4><p>Turn ideas into proposals with owners and timelines.</p></div>
    <div class="takeaway-card"><div class="icon">🎨</div><h4>Ready for Leadership</h4><p>Build decks at the speed of thought.</p></div>
    <div class="takeaway-card"><div class="icon">🔗</div><h4>End-to-End Flow</h4><p>Research → Proposal → Deck in one session.</p></div>
  </div>
</div>

</div>
</div>

<footer>
  <p><strong>Microsoft 365 Copilot — Sales Demo</strong></p>
  <p>For questions or feedback, reach out to your training facilitator.</p>
</footer>

<button class="sidebar-toggle" id="sidebarToggle" onclick="openSidebar()" aria-label="Open navigation">☰</button>

<script src="../../Allfiles/demo-script.js"></script>
</body>
</html>
