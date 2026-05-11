---
demo:
    title: 'Executive Assistant Demo'
layout: none
---

<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Executive Assistant Demo | Learning</title>
<link rel="stylesheet" href="../../Allfiles/demo-style.css">
<style>:root { --hero-from: #4A148C; --hero-via: #6A1B9A; --hero-to: #0078D4; }</style>
</head>
<body>

<div class="back-bar">
  <a href="https://emontes07.github.io/Learning/">← Back to Index</a>
</div>

<div class="hero">
  <div class="hero-inner">
    <h1>Microsoft 365 Copilot for Executive Assistants</h1>
    <p class="subtitle">Summarize, brief, and schedule — keep your executive ahead</p>
    <div class="scenario">
      <strong>Scenario:</strong> You've been tasked with summarizing the latest earnings conference call transcript for your executive. This task includes extracting key insights, creating an executive summary, and preparing for a follow-up meeting.
    </div>
    <div class="hero-meta">
      <span>🗓️ Executive Assistant</span>
      <span>📝 Word</span>
      <span>💬 Copilot Chat</span>
      <span>📧 Outlook</span>
    </div>
  </div>
</div>

<div class="sidebar-overlay" id="sidebarOverlay" onclick="closeSidebar()"></div>

<div class="layout">

<nav class="sidebar" id="sidebar">
  <a class="sb-home" href="https://emontes07.github.io/Learning/">← Back to Index</a>
  <div class="sb-title">Executive Assistant Demo</div>

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
    <li>Summarize a long transcript with grounded references</li>
    <li>Produce an executive summary and leadership talking points</li>
    <li>Schedule and prepare a follow-up meeting with Outlook + Copilot</li>
  </ul>
</div>

<div class="section" id="sec-prereqs">
  <h2>📋 Demo Setup</h2>
  <p>Required file from the MS-4021 GitHub <a href='https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/tree/master/ResourceFiles' target='_blank'>repository</a>:</p>    <ul class="tips-list">
      <li><a href='https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/raw/master/ResourceFiles/Microsoft_FY24_Second_Quarter_Earnings_Conference_Call_Transcript.docx'>Microsoft_FY24_Second_Quarter_Earnings_Conference_Call_Transcript.docx</a></li>
    </ul><div class="callout warn"><strong>📝 NOTE:</strong> Allow up to 10 minutes for OneDrive sync.</div>
</div>

<div class="part-card" id="part1">
  <div class="part-header-bar navy"></div>
  <div class="part-header" onclick="togglePart('body1', this)">
    <h2>Part 1: Copilot in Word — Summarize a Long Transcript</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body1">
<div class="callout"><strong>💡 Why This Matters:</strong> Earnings calls are long. Copilot pulls the signal out — with clickable references back to the source.</div>
    <ol class="steps" start="1">
      <li>Open <strong>Microsoft_FY24_Second_Quarter_Earnings_Conference_Call_Transcript.docx</strong> in Word.</li>
      <li>Click the <strong>Copilot</strong> icon in the ribbon.</li>
    </ol>
<div class="prompt-box">Summarize the key points from the Microsoft FY24 Second Quarter Earnings Conference Call.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="prompt-box">Provide a brief summary of Satya Nadella's remarks during the earnings call.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <p>Click any reference Copilot provides to jump straight to that section of the document.</p>
<div class="prompt-box">Analyze the Microsoft FY24 Second Quarter Earnings Conference Call document to provide a comprehensive report that includes:
- A summary of the key points from each speaker
- Identification of the top three growth areas and their contributing factors.
- A detailed breakdown of the financial performance, including revenue, operating income, and earnings per share.
- Trends in AI adoption and its influence on Microsoft's business strategy.
- A comparison of this quarter's performance with the same quarter last year, highlighting significant changes.
- Key strategic initiatives and future outlook as discussed in the call.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="callout green"><strong>💡 Tip:</strong> This is a complex prompt — Copilot may take a few seconds to produce the full analysis.</div>
    <p>Click the <strong>Copy</strong> icon next to Copilot's response to save the output for the next part.</p>
    <div class="self-check">
      <h4>✅ Self-Check: Part 1</h4>
      <label><input type="checkbox"> I summarized the transcript</label>
      <label><input type="checkbox"> I produced a comprehensive analysis</label>
      <label><input type="checkbox"> I copied the output</label>
    </div>
  </div>
</div>

<div class="part-card" id="part2">
  <div class="part-header-bar blue"></div>
  <div class="part-header" onclick="togglePart('body2', this)">
    <h2>Part 2: Copilot Chat — Executive Summary & Talking Points</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body2">
<div class="callout"><strong>💡 Why This Matters:</strong> Your executive needs the headlines and the soundbites — not the full report.</div>
    <ol class="steps" start="1">
      <li>Open <a href='https://m365copilot.com' target='_blank'>M365copilot.com</a> in Web mode.</li>
      <li>Paste the Word output into the prompt below.</li>
    </ol>
<div class="prompt-box">Based on the following information, provide an executive summary on the following information:

[paste the Word output here]<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="callout"><strong>📝 Note:</strong> Clean up any extraneous text from the copied content for best results.</div>
<div class="prompt-box">Summarize this executive summary into a more concise format by focusing on the most critical insights and metrics for each speaker. Use a structured format with headings and bullet points to improve readability. Export to a Word document.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="prompt-box">Based on the summarized executive summary, generate 5-7 concise and impactful talking points my manager can use in their next leadership call. Focus on key achievements, growth areas, and strategic priorities.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <div class="self-check">
      <h4>✅ Self-Check: Part 2</h4>
      <label><input type="checkbox"> I produced an executive summary</label>
      <label><input type="checkbox"> I generated talking points for leadership</label>
    </div>
  </div>
</div>

<div class="part-card" id="part3">
  <div class="part-header-bar purple"></div>
  <div class="part-header" onclick="togglePart('body3', this)">
    <h2>Part 3: Copilot in Outlook — Schedule the Follow-Up</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body3">
<div class="callout"><strong>💡 Why This Matters:</strong> Don't just summarize — set up the conversation. Copilot finds time and drafts an agenda.</div>
    <ol class="steps" start="1">
      <li>Open <a href='https://outlook.office.com' target='_blank'>outlook.office.com</a>.</li>
      <li>Click the <strong>Copilot</strong> icon in the ribbon.</li>
    </ol>
<div class="prompt-box">I need to schedule a 30-minute meeting with [/Pick a colleague] tomorrow afternoon to discuss the Second Quarter Earnings Conference Call. Can you suggest a time that works? If they are unavailable, provide an alternative.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <ol class="steps" start="3">
      <li>Copilot proposes a calendar item — click <strong>Edit</strong>.</li>
      <li>Use Scheduling Assistant to confirm everyone is free.</li>
      <li>Back on the event tab, click <strong>Draft with Copilot</strong> in the event body.</li>
    </ol>
<div class="prompt-box">I'm meeting with my boss to discuss key updates and strategic initiatives they missed from the Second Quarter Earnings Conference Call. Create an agenda to discuss financial performance, AI and technology integration, strategic acquisitions, productivity updates, and future outlook.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <div class="self-check">
      <h4>✅ Self-Check: Part 3</h4>
      <label><input type="checkbox"> I scheduled a follow-up</label>
      <label><input type="checkbox"> I drafted an agenda using Copilot</label>
    </div>
  </div>
</div>

<div class="section" id="sec-takeaways">
  <h2>🔑 Key Takeaways</h2>
  <div class="takeaways-grid">
    <div class="takeaway-card"><div class="icon">📚</div><h4>Read Less, Know More</h4><p>Summarize long documents in seconds with references.</p></div>
    <div class="takeaway-card"><div class="icon">✨</div><h4>Polish for Leadership</h4><p>Turn raw analysis into clear, executive-ready briefs.</p></div>
    <div class="takeaway-card"><div class="icon">🗓️</div><h4>Schedule + Prepare</h4><p>Move from insight to scheduled follow-up in one flow.</p></div>
    <div class="takeaway-card"><div class="icon">🧠</div><h4>Always Verify</h4><p>Spot-check key numbers and quotes before sharing.</p></div>
  </div>
</div>

</div>
</div>

<footer>
  <p><strong>Microsoft 365 Copilot — Executive Assistant Demo</strong></p>
  <p>For questions or feedback, reach out to your training facilitator.</p>
</footer>

<button class="sidebar-toggle" id="sidebarToggle" onclick="openSidebar()" aria-label="Open navigation">☰</button>

<script src="../../Allfiles/demo-script.js"></script>
</body>
</html>
