---
demo:
    title: 'Operations Demo'
layout: none
---

<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Operations Demo | Learning</title>
<link rel="stylesheet" href="../../Allfiles/demo-style.css">
<style>:root { --hero-from: #004D40; --hero-via: #00695C; --hero-to: #0078D4; }</style>
</head>
<body>

<div class="back-bar">
  <a href="https://emontes07.github.io/Learning/">← Back to Index</a>
</div>

<div class="hero">
  <div class="hero-inner">
    <h1>Microsoft 365 Copilot for Operations</h1>
    <p class="subtitle">From RFP research to vendor outreach in one flow</p>
    <div class="scenario">
      <strong>Scenario:</strong> You're an Operations Manager at Contoso, responsible for vendor procurement and project execution. Your goal is to review past RFPs, extract key selection criteria, and draft a new RFP for an upcoming initiative.
    </div>
    <div class="hero-meta">
      <span>⚙️ Operations</span>
      <span>📝 Word</span>
      <span>💬 Copilot Chat</span>
      <span>📧 Outlook</span>
      <span>🤝 Procurement</span>
    </div>
  </div>
</div>

<div class="sidebar-overlay" id="sidebarOverlay" onclick="closeSidebar()"></div>

<div class="layout">

<nav class="sidebar" id="sidebar">
  <a class="sb-home" href="https://emontes07.github.io/Learning/">← Back to Index</a>
  <div class="sb-title">Operations Demo</div>

  <a href="#sec-objectives" class="section-link">Learning Objectives</a>
  <a href="#sec-prereqs" class="section-link">Demo Setup</a>

    <a href="#part1" class="part-link">Part 1: Copilot in Word</a>
  <a href="#part2" class="part-link">Part 2: Copilot Chat</a>
  <a href="#part3" class="part-link">Part 3: Copilot in Outlook</a>

  <a href="#sec-takeaways" class="section-link" style="margin-top:0.5rem;">Key Takeaways</a>
</nav>

<div class="main-content">

<div class="section" id="sec-objectives">
  <h2>🎯 Learning Objectives</h2>
  <ul class="objectives-list">
    <li>Extract structure and criteria from an existing RFP</li>
    <li>Draft a new RFP grounded on project guidelines and a template</li>
    <li>Communicate the RFP to suppliers via Outlook</li>
  </ul>
</div>

<div class="section" id="sec-prereqs">
  <h2>📋 Demo Setup</h2>
  <p>Required files from the MS-4021 GitHub <a href='https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/tree/master/ResourceFiles' target='_blank'>repository</a>:</p>    <ul class="tips-list">
      <li><a href='https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/raw/master/ResourceFiles/Contoso_Completed_RFP.docx'>Contoso_Completed_RFP.docx</a></li>
      <li><a href='https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/raw/master/ResourceFiles/Project_Guidelines_Contoso.docx'>Project_Guidelines_Contoso.docx</a></li>
      <li><a href='https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/raw/master/ResourceFiles/Contoso_RFP_Template.docx'>Contoso_RFP_Template.docx</a></li>
    </ul><div class="callout warn"><strong>📝 NOTE:</strong> Allow up to 10 minutes for OneDrive sync.</div>
</div>

<div class="part-card" id="part1">
  <div class="part-header-bar navy"></div>
  <div class="part-header" onclick="togglePart('body1', this)">
    <h2>Part 1: Copilot in Word — Decompose an RFP</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body1">
<div class="callout"><strong>💡 Why This Matters:</strong> Don't start from scratch. Copilot extracts structure and requirements from an existing RFP so you can reuse what worked.</div>
    <ol class="steps" start="1">
      <li>Open <strong>Contoso_Completed_RFP.docx</strong> in Word.</li>
      <li>Click the <strong>Copilot</strong> icon in the ribbon.</li>
    </ol>
<div class="prompt-box">Summarize this document<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="prompt-box">Analyze this document and generate a categorized list of required items needed to create an RFP.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="prompt-box">Analyze this document and create an RFP template based on the content.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="callout"><strong>📝 NOTE:</strong> No need to copy the output — we'll use a provided template in the next part. Optionally show how to insert Copilot's response into the document.</div>
    <div class="self-check">
      <h4>✅ Self-Check: Part 1</h4>
      <label><input type="checkbox"> I summarized and decomposed the existing RFP</label>
    </div>
  </div>
</div>

<div class="part-card" id="part2">
  <div class="part-header-bar blue"></div>
  <div class="part-header" onclick="togglePart('body2', this)">
    <h2>Part 2: Copilot Chat — Draft a New RFP</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body2">
<div class="callout"><strong>💡 Why This Matters:</strong> Combine your project guidelines with a proven template — Copilot generates the new RFP draft.</div>
    <ol class="steps" start="1">
      <li>Open <a href='https://m365copilot.com' target='_blank'>M365copilot.com</a> in Web mode.</li>
    </ol>
<div class="prompt-box">Summarize [Project_Guidelines_Contoso.docx] highlighting the key objectives, scope, implementation timeline, budget, compliance needs, and vendor selection criteria in a bulleted list.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="prompt-box">Extract and summarize the key vendor selection criteria from this document, including weight percentages and evaluation factors.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="prompt-box">Using the project requirements outlined above, draft an RFP using the following template: [Contoso_RFP_Template.docx].<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <p>Copy the generated RFP to your clipboard. Optionally ask Copilot to export it to a Word document.</p>
    <div class="self-check">
      <h4>✅ Self-Check: Part 2</h4>
      <label><input type="checkbox"> I drafted a new RFP grounded on guidelines and template</label>
    </div>
  </div>
</div>

<div class="part-card" id="part3">
  <div class="part-header-bar purple"></div>
  <div class="part-header" onclick="togglePart('body3', this)">
    <h2>Part 3: Copilot in Outlook — Reach Out to Suppliers</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body3">
<div class="callout"><strong>💡 Why This Matters:</strong> Once the RFP is ready, getting it in front of suppliers fast is half the win.</div>
    <ol class="steps" start="1">
      <li>Open <strong>Outlook</strong> → <strong>New Email</strong>.</li>
      <li>Click <strong>Copilot</strong> → <strong>Draft with Copilot</strong>.</li>
    </ol>
<div class="prompt-box">Draft an email to potential suppliers summarizing the RFP below:

[paste contents of RFP]<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="callout"><strong>📝 NOTE:</strong> Paste the RFP contents you copied from Part 2.</div>
    <div class="self-check">
      <h4>✅ Self-Check: Part 3</h4>
      <label><input type="checkbox"> I sent supplier outreach grounded on the new RFP</label>
    </div>
  </div>
</div>

<div class="section" id="sec-takeaways">
  <h2>🔑 Key Takeaways</h2>
  <div class="takeaways-grid">
    <div class="takeaway-card"><div class="icon">📂</div><h4>Mine What Worked</h4><p>Reuse structure from past RFPs.</p></div>
    <div class="takeaway-card"><div class="icon">🧱</div><h4>Ground on Templates</h4><p>Combine guidelines + template + Copilot.</p></div>
    <div class="takeaway-card"><div class="icon">📤</div><h4>Move to Outreach Fast</h4><p>Close the loop with suppliers in the same flow.</p></div>
    <div class="takeaway-card"><div class="icon">🔁</div><h4>Iterate</h4><p>Refine the RFP and outreach until they're ready.</p></div>
  </div>
</div>

</div>
</div>

<footer>
  <p><strong>Microsoft 365 Copilot — Operations Demo</strong></p>
  <p>For questions or feedback, reach out to your training facilitator.</p>
</footer>

<button class="sidebar-toggle" id="sidebarToggle" onclick="openSidebar()" aria-label="Open navigation">☰</button>

<script src="../../Allfiles/demo-script.js"></script>
</body>
</html>
