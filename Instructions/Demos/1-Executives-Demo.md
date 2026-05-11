---
demo:
    title: 'Executives Demo'
layout: none
---

<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executives Demo | Learning</title>
<link rel="stylesheet" href="../../Allfiles/demo-style.css">
<style>:root { --hero-from: #0B3D91; --hero-via: #1565C0; --hero-to: #0078D4; }</style>
</head>
<body>

<div class="back-bar">
  <a href="https://emontes07.github.io/Learning/">← Back to Index</a>
</div>

<div class="hero">
  <div class="hero-inner">
    <h1>Microsoft 365 Copilot for Executives</h1>
    <p class="subtitle">Strategic insights, faster decisions — Copilot for executive leadership</p>
    <div class="scenario">
      <strong>Scenario:</strong> As an executive, you need to digest large volumes of information, communicate vision clearly, and make data-informed decisions quickly. This demo highlights how Copilot accelerates each of those activities across Chat, Word, and PowerPoint.
    </div>
    <div class="hero-meta">
      <span>💼 Executive Leadership</span>
      <span>💬 Copilot Chat</span>
      <span>📝 Word</span>
      <span>🎯 PowerPoint</span>
      <span>⏱️ Quick Overview</span>
    </div>
  </div>
</div>

<div class="sidebar-overlay" id="sidebarOverlay" onclick="closeSidebar()"></div>

<div class="layout">

<nav class="sidebar" id="sidebar">
  <a class="sb-home" href="https://emontes07.github.io/Learning/">← Back to Index</a>
  <div class="sb-title">Executives Demo</div>

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
    <li>Use Copilot Chat to summarize complex topics quickly</li>
    <li>Draft executive communications and memos in Word</li>
    <li>Build leadership presentations in PowerPoint</li>
    <li>Adopt a repeatable executive workflow with Copilot</li>
  </ul>
</div>

<div class="section" id="sec-prereqs">
  <h2>📋 Demo Setup</h2>
  <p>There are no sample documents required for this demo.</p><div class="callout"><strong>📝 NOTE:</strong> The default demonstrations for this experience are <strong>Microsoft 365 Copilot Chat (Work tab)</strong>, <strong>Copilot in Word</strong>, and <strong>Copilot in PowerPoint</strong>. If you have previously delivered demos for <strong>MS-4008</strong> or <strong>MS-4012</strong>, use the same structure and format for your demonstrations in this course.</div>
</div>

<div class="part-card" id="part1">
  <div class="part-header-bar blue"></div>
  <div class="part-header" onclick="togglePart('body1', this)">
    <h2>Part 1: Copilot Chat — Brief Yourself in Minutes</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body1">
<div class="callout"><strong>💡 Why This Matters:</strong> Executives can't read everything. Copilot Chat distills internal knowledge and external signals into briefings that fit between meetings.</div>
    <p>Use the Work tab to ground answers on company content (emails, files, Teams), or switch to Web mode for market and competitor context.</p>
    <ol class="steps" start="1">
      <li>Open <a href='https://m365copilot.com' target='_blank'>M365copilot.com</a> and ensure <strong>Work</strong> is selected.</li>
      <li>Ask for a briefing on a current strategic topic.</li>
      <li>Follow up with sharper, more specific prompts to refine.</li>
    </ol>
<div class="prompt-box">Give me a one-page executive briefing on our top 3 strategic priorities this quarter. Reference recent emails, Teams messages, and shared files I'm involved in. Surface key risks, decisions needed from me, and recommended talking points.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <div class="self-check">
      <h4>✅ Self-Check: Part 1</h4>
      <label><input type="checkbox"> I generated an executive briefing in Copilot Chat</label>
      <label><input type="checkbox"> I refined results with follow-up prompts</label>
    </div>
  </div>
</div>

<div class="part-card" id="part2">
  <div class="part-header-bar navy"></div>
  <div class="part-header" onclick="togglePart('body2', this)">
    <h2>Part 2: Copilot in Word — Draft a Leadership Memo</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body2">
<div class="callout"><strong>💡 Why This Matters:</strong> Strong written communication scales executive influence. Copilot gives you a polished first draft so you focus on the message — not the mechanics.</div>
    <ol class="steps" start="1">
      <li>Open <strong>Word</strong> (web or desktop).</li>
      <li>In <strong>Describe what you'd like to write</strong>, enter the prompt below.</li>
      <li>Use Copilot to refine tone, length, and structure.</li>
    </ol>
<div class="prompt-box">Draft a 1-page memo to the leadership team on our Q3 priorities. Include: a 3-sentence executive summary, top 3 priorities with owners, key risks, and a clear call-to-action for the next leadership meeting. Tone: confident, direct, and concise.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <div class="self-check">
      <h4>✅ Self-Check: Part 2</h4>
      <label><input type="checkbox"> I drafted a leadership memo using Copilot in Word</label>
      <label><input type="checkbox"> I refined tone and length with follow-up prompts</label>
    </div>
  </div>
</div>

<div class="part-card" id="part3">
  <div class="part-header-bar magenta"></div>
  <div class="part-header" onclick="togglePart('body3', this)">
    <h2>Part 3: Copilot in PowerPoint — Build a Leadership Deck</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body3">
<div class="callout"><strong>💡 Why This Matters:</strong> Turn a Word memo into a presentation in under a minute. Copilot respects your template and brand.</div>
    <ol class="steps" start="1">
      <li>Open a new presentation at <a href='https://powerpoint.new' target='_blank'>PowerPoint.new</a>.</li>
      <li>Click <strong>Copilot</strong> → <strong>Create presentation from file</strong>.</li>
      <li>Paste the link to the Word memo from Part 2.</li>
    </ol>
<div class="prompt-box">Create a presentation from [Link to leadership memo]. Keep slides minimal — 4 bullets max per slide. Include a title slide, executive summary, priorities, risks, and an 'asks of leadership' closing slide.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <div class="self-check">
      <h4>✅ Self-Check: Part 3</h4>
      <label><input type="checkbox"> I generated an executive deck from a Word memo</label>
      <label><input type="checkbox"> I tailored the deck for a leadership audience</label>
    </div>
  </div>
</div>

<div class="section" id="sec-takeaways">
  <h2>🔑 Key Takeaways</h2>
  <div class="takeaways-grid">
    <div class="takeaway-card"><div class="icon">⚡</div><h4>Move Faster</h4><p>Get from question to insight in minutes, not hours.</p></div>
    <div class="takeaway-card"><div class="icon">🎯</div><h4>Stay Strategic</h4><p>Spend time on judgment, not on first drafts.</p></div>
    <div class="takeaway-card"><div class="icon">🔗</div><h4>Chain Your Tools</h4><p>Chat → Word → PowerPoint — one fluid workflow.</p></div>
    <div class="takeaway-card"><div class="icon">🧠</div><h4>AI Assists, You Decide</h4><p>Copilot accelerates the work — executive judgment remains with you.</p></div>
  </div>
</div>

</div>
</div>

<footer>
  <p><strong>Microsoft 365 Copilot — Executives Demo</strong></p>
  <p>For questions or feedback, reach out to your training facilitator.</p>
</footer>

<button class="sidebar-toggle" id="sidebarToggle" onclick="openSidebar()" aria-label="Open navigation">☰</button>

<script src="../../Allfiles/demo-script.js"></script>
</body>
</html>
