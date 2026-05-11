---
demo:
    title: 'Marketing Demo'
layout: none
---

<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Marketing Demo | Learning</title>
<link rel="stylesheet" href="../../Allfiles/demo-style.css">
<style>:root { --hero-from: #880E4F; --hero-via: #AD1457; --hero-to: #FF6F61; }</style>
</head>
<body>

<div class="back-bar">
  <a href="https://emontes07.github.io/Learning/">← Back to Index</a>
</div>

<div class="hero">
  <div class="hero-inner">
    <h1>Microsoft 365 Copilot for Marketing</h1>
    <p class="subtitle">Analyze, ideate, and create — campaigns that resonate</p>
    <div class="scenario">
      <strong>Scenario:</strong> You're in Marketing for a beverage company. Your goal is to analyze market trends, create a marketing analysis, and develop a new social media campaign for Mystic Spice Premium Chai Tea in Latin America.
    </div>
    <div class="hero-meta">
      <span>🎨 Marketing</span>
      <span>📝 Word</span>
      <span>💬 Copilot Chat</span>
      <span>📈 Excel</span>
      <span>🌎 LATAM</span>
    </div>
  </div>
</div>

<div class="sidebar-overlay" id="sidebarOverlay" onclick="closeSidebar()"></div>

<div class="layout">

<nav class="sidebar" id="sidebar">
  <a class="sb-home" href="https://emontes07.github.io/Learning/">← Back to Index</a>
  <div class="sb-title">Marketing Demo</div>

  <a href="#sec-objectives" class="section-link">Learning Objectives</a>
  <a href="#sec-prereqs" class="section-link">Demo Setup</a>

    <a href="#part1" class="part-link">Part 1: Copilot in Word</a>
  <a href="#part2" class="part-link">Part 2: Copilot Chat</a>
  <a href="#part3" class="part-link">Part 3: Copilot in Excel</a>

  <a href="#sec-takeaways" class="section-link" style="margin-top:0.5rem;">Key Takeaways</a>
</nav>

<div class="main-content">

<div class="section" id="sec-objectives">
  <h2>🎯 Learning Objectives</h2>
  <ul class="objectives-list">
    <li>Draft a market analysis grounded on multiple source documents</li>
    <li>Evaluate and refine social media campaign concepts</li>
    <li>Quantify campaign performance with Copilot in Excel</li>
  </ul>
</div>

<div class="section" id="sec-prereqs">
  <h2>📋 Demo Setup</h2>
  <p>Required files from the MS-4021 GitHub <a href='https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/tree/master/ResourceFiles' target='_blank'>repository</a>:</p>    <ul class="tips-list">
      <li><a href='https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/raw/master/ResourceFiles/Promotion_Plan_for_Chai_Tea_in_Latin_America.docx'>Promotion_Plan_for_Chai_Tea_in_Latin_America.docx</a></li>
      <li><a href='https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/raw/master/ResourceFiles/Mystic_Spice_Premium_Chai_Tea_product_description.docx'>Mystic_Spice_Premium_Chai_Tea_product_description.docx</a></li>
      <li><a href='https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/raw/master/ResourceFiles/Contoso_Chai_Tea_market_trends.docx'>Contoso_Chai_Tea_market_trends.docx</a></li>
      <li><a href='https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/raw/master/ResourceFiles/Contoso_Chai_Tea_social_marketing_trends.xlsx'>Contoso_Chai_Tea_social_marketing_trends.xlsx</a></li>
    </ul><div class="callout warn"><strong>📝 NOTE:</strong> Allow up to 10 minutes for OneDrive sync.</div>
</div>

<div class="part-card" id="part1">
  <div class="part-header-bar navy"></div>
  <div class="part-header" onclick="togglePart('body1', this)">
    <h2>Part 1: Copilot in Word — Draft a Market Analysis</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body1">
<div class="callout"><strong>💡 Why This Matters:</strong> Strong campaigns start with a clear point of view. Copilot synthesizes multiple research documents into one cohesive analysis.</div>
    <ol class="steps" start="1">
      <li>Open <strong>Word</strong>.</li>
      <li>In <strong>Describe what you'd like to write</strong>, enter the prompt below.</li>
    </ol>
<div class="prompt-box">Create a Market Analysis report for Mystic Spice Premium Chai Tea using the attached files. Include the product description, market trend analysis, and a promotion plan for Latin America.

[Promotion_Plan_for_Chai_Tea_in_Latin_America.docx], [Mystic_Spice_Premium_Chai_Tea_product_description.docx], [Contoso_Chai_Tea_market_trends.docx]<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="callout"><strong>📝 NOTE:</strong> Brackets indicate referenced documents — paste shared links or filenames in OneDrive.</div>
<div class="prompt-box">Draft a new section for social media campaigns to promote Mystic Spice Premium Chai Tea. Include a brief description of 2-3 campaign ideas, each with a unique focus. For each campaign, provide a tagline that reflects its theme and resonates with our target audience of young professionals and tea enthusiasts.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <ol class="steps" start="3">
      <li>Save the new document as <strong>LATAM_Market_Analysis.docx</strong>.</li>
    </ol>
    <div class="self-check">
      <h4>✅ Self-Check: Part 1</h4>
      <label><input type="checkbox"> I built a market analysis from multiple sources</label>
      <label><input type="checkbox"> I added campaign concepts</label>
    </div>
  </div>
</div>

<div class="part-card" id="part2">
  <div class="part-header-bar blue"></div>
  <div class="part-header" onclick="togglePart('body2', this)">
    <h2>Part 2: Copilot Chat — Evaluate Campaign Concepts</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body2">
<div class="callout"><strong>💡 Why This Matters:</strong> Get a second opinion on which campaign concept best fits the LATAM market — and a slogan to test.</div>
    <ol class="steps" start="1">
      <li>Open <a href='https://m365copilot.com' target='_blank'>M365copilot.com</a> in Web mode.</li>
      <li>Upload <strong>LATAM_Market_Analysis.docx</strong> via <strong>Add Content</strong>.</li>
    </ol>
<div class="prompt-box">Review the social media campaigns outlined in the Market Analysis Report for Mystic Spice Premium Chai Tea.docx. Evaluate which campaign might resonate best with the LATAM market based on cultural relevance, target audience preferences, and alignment with regional trends. Provide reasons for your choice and suggest any adjustments to improve its impact.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="prompt-box">Generate a catchy marketing slogan for the [Campaign name - e.g., 'Morning Motivation'] campaign that highlights its unique value proposition and resonates with the LATAM market. Ensure the slogan reflects a vibrant and culturally relevant tone that appeals to young professionals.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <p>Optionally, switch to the <strong>Visual Creator Agent</strong> on the right rail and request a short campaign video:</p>
<div class="prompt-box">Create a captivating social media video for Mystic Spice Chai Tea that highlights its unique flavor and vibrant appeal. The video should feature eye-catching visuals, with colors, and themes that resonate with young professionals and tea enthusiasts.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <div class="self-check">
      <h4>✅ Self-Check: Part 2</h4>
      <label><input type="checkbox"> I selected the best-fit campaign</label>
      <label><input type="checkbox"> I generated a slogan</label>
      <label><input type="checkbox"> I tried the Visual Creator Agent (optional)</label>
    </div>
  </div>
</div>

<div class="part-card" id="part3">
  <div class="part-header-bar green"></div>
  <div class="part-header" onclick="togglePart('body3', this)">
    <h2>Part 3: Copilot in Excel — Quantify the Campaigns</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body3">
<div class="callout"><strong>💡 Why This Matters:</strong> Creative is half the story — the numbers tell the rest. Copilot helps you correlate engagement to sales.</div>
    <ol class="steps" start="1">
      <li>Download <a href='https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/raw/master/ResourceFiles/Contoso_Chai_Tea_social_marketing_trends.xlsx'>Contoso_Chai_Tea_social_marketing_trends.xlsx</a> and open in Excel.</li>
      <li>Click <strong>Copilot</strong> in the ribbon.</li>
    </ol>
<div class="prompt-box">On average, how many sales do we get per social media campaign view?<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="prompt-box">Can you show a correlation between social media engagement and sales?<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="prompt-box">How many social media campaign views did we have from September to December?<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <div class="self-check">
      <h4>✅ Self-Check: Part 3</h4>
      <label><input type="checkbox"> I quantified the campaign performance</label>
    </div>
  </div>
</div>

<div class="section" id="sec-takeaways">
  <h2>🔑 Key Takeaways</h2>
  <div class="takeaways-grid">
    <div class="takeaway-card"><div class="icon">🧵</div><h4>Thread Insights Together</h4><p>Combine multiple docs into one cohesive POV.</p></div>
    <div class="takeaway-card"><div class="icon">🌎</div><h4>Localize with Confidence</h4><p>Pressure-test ideas against cultural fit.</p></div>
    <div class="takeaway-card"><div class="icon">📈</div><h4>Show the Numbers</h4><p>Tie creative concepts back to engagement data.</p></div>
    <div class="takeaway-card"><div class="icon">🎥</div><h4>Create What You Need</h4><p>Agents can extend beyond text — video, visuals, more.</p></div>
  </div>
</div>

</div>
</div>

<footer>
  <p><strong>Microsoft 365 Copilot — Marketing Demo</strong></p>
  <p>For questions or feedback, reach out to your training facilitator.</p>
</footer>

<button class="sidebar-toggle" id="sidebarToggle" onclick="openSidebar()" aria-label="Open navigation">☰</button>

<script src="../../Allfiles/demo-script.js"></script>
</body>
</html>
