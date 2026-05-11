---
demo:
    title: 'Communications Demo'
layout: none
---

<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Communications Demo | Learning</title>
<link rel="stylesheet" href="../../Allfiles/demo-style.css">
<style>:root { --hero-from: #006064; --hero-via: #00838F; --hero-to: #0078D4; }</style>
</head>
<body>

<div class="back-bar">
  <a href="https://emontes07.github.io/Learning/">← Back to Index</a>
</div>

<div class="hero">
  <div class="hero-inner">
    <h1>Microsoft 365 Copilot for Communications</h1>
    <p class="subtitle">Prepare for interviews, tailor your messaging, and publish with confidence</p>
    <div class="scenario">
      <strong>Scenario:</strong> You're preparing for an interview with a reporter from a prominent news outlet. Your goal is to gather insights about the reporter, tailor your messaging to their audience, and develop well-crafted answers to potential interview questions. Copilot assists you throughout this process.
    </div>
    <div class="hero-meta">
      <span>📰 Communications</span>
      <span>💬 Copilot Chat</span>
      <span>📝 Word</span>
      <span>🎙️ Interview Prep</span>
    </div>
  </div>
</div>

<div class="sidebar-overlay" id="sidebarOverlay" onclick="closeSidebar()"></div>

<div class="layout">

<nav class="sidebar" id="sidebar">
  <a class="sb-home" href="https://emontes07.github.io/Learning/">← Back to Index</a>
  <div class="sb-title">Communications Demo</div>

  <a href="#sec-objectives" class="section-link">Learning Objectives</a>
  <a href="#sec-prereqs" class="section-link">Demo Setup</a>

    <a href="#part1" class="part-link">Part 1: Copilot Chat</a>
  <a href="#part2" class="part-link">Part 2: Copilot in Word</a>

  <a href="#sec-takeaways" class="section-link" style="margin-top:0.5rem;">Key Takeaways</a>
</nav>

<div class="main-content">

<div class="section" id="sec-objectives">
  <h2>🎯 Learning Objectives</h2>
  <ul class="objectives-list">
    <li>Research a reporter and outlet using Copilot Chat</li>
    <li>Anticipate interview questions and draft answers</li>
    <li>Transform Q&A into a polished FAQ in Word</li>
  </ul>
</div>

<div class="section" id="sec-prereqs">
  <h2>📋 Demo Setup</h2>
  <p>There are no sample documents required for this demo.</p>
</div>

<div class="part-card" id="part1">
  <div class="part-header-bar blue"></div>
  <div class="part-header" onclick="togglePart('body1', this)">
    <h2>Part 1: Copilot Chat — Reporter Research & Interview Prep</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body1">
<div class="callout"><strong>💡 Why This Matters:</strong> Knowing your audience is half the battle. Copilot researches the reporter, outlet, and audience so you walk in prepared.</div>
    <ol class="steps" start="1">
      <li>Open <a href='https://m365copilot.com' target='_blank'>M365copilot.com</a>.</li>
      <li>Ensure <strong>Web mode</strong> is selected.</li>
      <li>Use the prompts below in sequence.</li>
    </ol>
    <p><img src='../Prompts/Media/web-mode.png' alt='Web mode tab' style='max-width:100%;border-radius:6px;' /></p>
<div class="prompt-box">I am going to be interviewed by {Reporter Name} from {News Outlet Name} about {Specific Topic, e.g., 'sustainability in tech'}. What are some key things I should know about their previous work and approach to this topic?<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="prompt-box">Tell me about {News Outlet Name}'s demographic and their audience's interests and knowledge level on {Specific Topic}.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="prompt-box">Generate the top 10 questions that {Reporter Name} might ask in my interview. They should be informed by the research conducted above and crafted to be conversational yet concise.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="prompt-box">Draft answers to the questions in a table format. Save the table with questions and answers into a Word document.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="callout"><strong>📝 NOTE:</strong> The Word document created here will be referenced in the next part.</div>
    <div class="self-check">
      <h4>✅ Self-Check: Part 1</h4>
      <label><input type="checkbox"> I researched the reporter and outlet</label>
      <label><input type="checkbox"> I generated anticipated questions</label>
      <label><input type="checkbox"> I drafted Q&A and exported to Word</label>
    </div>
  </div>
</div>

<div class="part-card" id="part2">
  <div class="part-header-bar navy"></div>
  <div class="part-header" onclick="togglePart('body2', this)">
    <h2>Part 2: Copilot in Word — Turn Q&A into a Public FAQ</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body2">
<div class="callout"><strong>💡 Why This Matters:</strong> Once you've prepared your answers, repurpose them. Copilot in Word reshapes your Q&A into an FAQ ready for publishing on a blog or press kit.</div>
    <ol class="steps" start="1">
      <li>Open the Word document containing the Q&A table from Part 1.</li>
      <li>Select anywhere in the body and click the <strong>Copilot</strong> icon.</li>
      <li>Use the prompt below.</li>
    </ol>
<div class="prompt-box">Create an FAQ for a technical audience who are new to {Specific Topic}. Include the top 15 questions for publishing on a blog. Leverage the questions and answers from this document.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <ul class="tips-list">
      <li>Confirm answers are accurate, relevant, and concise.</li>
      <li>Structure logically — group related questions.</li>
      <li>Identify gaps and add new questions where useful.</li>
    </ul>
    <div class="self-check">
      <h4>✅ Self-Check: Part 2</h4>
      <label><input type="checkbox"> I generated an FAQ from the Q&A table</label>
      <label><input type="checkbox"> I reviewed it for clarity and completeness</label>
    </div>
  </div>
</div>

<div class="section" id="sec-takeaways">
  <h2>🔑 Key Takeaways</h2>
  <div class="takeaways-grid">
    <div class="takeaway-card"><div class="icon">🔍</div><h4>Audience First</h4><p>Research the outlet and reporter before crafting your message.</p></div>
    <div class="takeaway-card"><div class="icon">💬</div><h4>Anticipate the Ask</h4><p>Predict tough questions — prepare crisp answers.</p></div>
    <div class="takeaway-card"><div class="icon">♻️</div><h4>Reuse Your Work</h4><p>Turn interview prep into a public-facing FAQ in one click.</p></div>
    <div class="takeaway-card"><div class="icon">🧠</div><h4>Iterate, Don't Stop at First Draft</h4><p>Refine Copilot's outputs until they sound like you.</p></div>
  </div>
</div>

</div>
</div>

<footer>
  <p><strong>Microsoft 365 Copilot — Communications Demo</strong></p>
  <p>For questions or feedback, reach out to your training facilitator.</p>
</footer>

<button class="sidebar-toggle" id="sidebarToggle" onclick="openSidebar()" aria-label="Open navigation">☰</button>

<script src="../../Allfiles/demo-script.js"></script>
</body>
</html>
