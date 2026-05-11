---
demo:
    title: 'Legal Demo'
layout: none
---

<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Copilot Training for Legal | Learning</title>
<style>
  :root {
    --primary: #0078D4;
    --primary-dark: #005A9E;
    --primary-light: #DEECF9;
    --accent: #107C10;
    --accent-light: #DFF6DD;
    --warn: #D83B01;
    --warn-light: #FED9CC;
    --purple: #5C2D91;
    --purple-light: #E8DAEF;
    --neutral-900: #201F1E;
    --neutral-700: #323130;
    --neutral-500: #605E5C;
    --neutral-300: #A19F9D;
    --neutral-100: #F3F2F1;
    --white: #FFFFFF;
    --shadow: 0 2px 8px rgba(0,0,0,0.08);
    --radius: 8px;
    --sidebar-width: 260px;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
    color: var(--neutral-700);
    line-height: 1.6;
    background: var(--neutral-100);
  }

  .back-bar {
    background: var(--white);
    border-bottom: 1px solid #E0E0E0;
    padding: 0.5rem 1.5rem;
    font-size: 0.88rem;
  }
  .back-bar a {
    color: var(--primary);
    text-decoration: none;
    font-weight: 600;
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
  }
  .back-bar a:hover { text-decoration: underline; }

  .hero {
    background: linear-gradient(135deg, #4A148C 0%, #5C2D91 40%, #0078D4 100%);
    color: var(--white);
    padding: 3rem 2rem 2.5rem;
    position: relative; overflow: hidden;
  }
  .hero::after {
    content: '';
    position: absolute; top: -40%; right: -10%;
    width: 500px; height: 500px;
    background: rgba(255,255,255,0.04);
    border-radius: 50%;
  }
  .hero-inner { max-width: 960px; margin: 0 auto; position: relative; z-index: 1; }
  .hero h1 { font-size: 2rem; font-weight: 700; margin-bottom: 0.4rem; }
  .hero .subtitle { font-size: 1.1rem; opacity: 0.9; margin-bottom: 0.5rem; }
  .hero .scenario {
    background: rgba(255,255,255,0.12);
    border-radius: 6px;
    padding: 0.75rem 1rem;
    margin: 1rem 0 1.25rem;
    font-size: 0.95rem;
    line-height: 1.5;
  }
  .hero-meta {
    display: flex; gap: 1.5rem; flex-wrap: wrap;
    font-size: 0.9rem; opacity: 0.85;
  }
  .hero-meta span { display: flex; align-items: center; gap: 0.4rem; }

  .layout {
    display: flex;
    max-width: 1260px;
    margin: 0 auto;
  }

  .sidebar {
    width: var(--sidebar-width);
    flex-shrink: 0;
    position: sticky;
    top: 0;
    height: 100vh;
    overflow-y: auto;
    background: var(--white);
    border-right: 1px solid #E0E0E0;
    padding: 1rem 0;
    font-size: 0.84rem;
    z-index: 100;
  }
  .sidebar::-webkit-scrollbar { width: 4px; }
  .sidebar::-webkit-scrollbar-thumb { background: var(--neutral-300); border-radius: 4px; }

  .sidebar .sb-home {
    display: block;
    padding: 0.5rem 1.25rem 0.75rem;
    color: var(--primary);
    text-decoration: none;
    font-weight: 600;
    font-size: 0.85rem;
    border-bottom: 1px solid var(--neutral-100);
    margin-bottom: 0.5rem;
  }
  .sidebar .sb-home:hover { text-decoration: underline; }

  .sidebar .sb-title {
    padding: 0.4rem 1.25rem;
    font-weight: 700;
    font-size: 0.9rem;
    color: var(--neutral-900);
  }

  .sidebar a {
    display: block;
    padding: 0.35rem 1.25rem;
    color: var(--neutral-500);
    text-decoration: none;
    border-left: 3px solid transparent;
    transition: all 0.2s;
  }
  .sidebar a:hover {
    color: var(--neutral-900);
    background: var(--neutral-100);
  }
  .sidebar a.active {
    color: var(--primary);
    font-weight: 600;
    border-left-color: var(--primary);
    background: var(--primary-light);
  }
  .sidebar a.part-link {
    font-weight: 600;
    color: var(--neutral-700);
    margin-top: 0.5rem;
    padding-top: 0.5rem;
    border-top: 1px solid var(--neutral-100);
  }
  .sidebar a.section-link {
    color: var(--neutral-700);
    font-weight: 500;
    margin-top: 0.35rem;
  }

  .main-content {
    flex: 1;
    min-width: 0;
    padding: 2rem 2rem 4rem;
  }

  .sidebar-toggle {
    display: none;
    position: fixed;
    bottom: 1.25rem;
    left: 1.25rem;
    z-index: 200;
    background: var(--primary);
    color: var(--white);
    border: none;
    width: 48px; height: 48px;
    border-radius: 50%;
    font-size: 1.3rem;
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(0,0,0,0.25);
    transition: background 0.2s;
  }
  .sidebar-toggle:hover { background: var(--primary-dark); }

  .section {
    background: var(--white); border-radius: var(--radius);
    box-shadow: var(--shadow); padding: 2rem; margin-bottom: 1.5rem;
  }
  .section h2 {
    font-size: 1.35rem; font-weight: 700;
    color: var(--neutral-900); margin-bottom: 1rem;
  }
  .section h3 {
    font-size: 1.1rem; font-weight: 600;
    color: var(--neutral-700); margin: 1.5rem 0 0.75rem;
  }
  .section p { margin-bottom: 0.75rem; }

  .objectives-list { list-style: none; padding: 0; }
  .objectives-list li {
    padding: 0.6rem 0 0.6rem 2rem; position: relative;
    border-bottom: 1px solid var(--neutral-100);
  }
  .objectives-list li:last-child { border-bottom: none; }
  .objectives-list li::before {
    content: '✓'; position: absolute; left: 0; top: 0.6rem;
    width: 22px; height: 22px; background: var(--accent-light);
    color: var(--accent); border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.8rem; font-weight: 700;
  }

  .prereq-grid {
    display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 0.75rem;
  }
  .prereq-item {
    display: flex; align-items: center; gap: 0.5rem;
    padding: 0.6rem 0.75rem; background: var(--neutral-100);
    border-radius: 6px; font-size: 0.9rem;
  }
  .prereq-icon {
    width: 28px; height: 28px; border-radius: 6px;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.85rem; font-weight: 700; flex-shrink: 0;
  }
  .prereq-icon.blue { background: var(--primary-light); color: var(--primary); }
  .prereq-icon.green { background: var(--accent-light); color: var(--accent); }
  .prereq-icon.purple { background: var(--purple-light); color: var(--purple); }

  .part-card {
    background: var(--white); border-radius: var(--radius);
    box-shadow: var(--shadow); margin-bottom: 1.5rem;
    overflow: hidden;
  }
  .part-header-bar { height: 5px; width: 100%; }
  .part-header-bar.basics    { background: var(--primary); }
  .part-header-bar.chat      { background: #0078D4; }
  .part-header-bar.word      { background: #2B579A; }
  .part-header-bar.outlook   { background: var(--purple); }
  .part-header-bar.prompts   { background: var(--accent); }

  .part-header {
    display: flex; align-items: center; justify-content: space-between;
    padding: 1.25rem 2rem; cursor: pointer; user-select: none;
  }
  .part-header:hover { background: var(--neutral-100); }
  .part-header h2 { margin: 0; font-size: 1.25rem; }
  .part-header .toggle-icon {
    font-size: 1.4rem; color: var(--neutral-500);
    transition: transform 0.3s;
  }
  .part-header .toggle-icon.open { transform: rotate(180deg); }
  .part-body { padding: 0 2rem 2rem; }
  .part-body.collapsed { display: none; }

  .part-body h3 {
    font-size: 1.1rem; font-weight: 600;
    color: var(--neutral-700); margin: 1.5rem 0 0.75rem;
    scroll-margin-top: 1rem;
  }
  .part-body p { margin-bottom: 0.75rem; }

  .prompt-box {
    position: relative; background: #1E1E1E; color: #D4D4D4;
    border-radius: 6px; padding: 1rem 1.25rem;
    font-family: 'Cascadia Code', 'Consolas', monospace;
    font-size: 0.88rem; line-height: 1.7;
    margin: 0.75rem 0 1rem; white-space: pre-wrap; word-wrap: break-word;
  }
  .copy-btn {
    position: absolute; top: 8px; right: 8px;
    background: rgba(255,255,255,0.1); border: none;
    color: #D4D4D4; padding: 4px 10px; border-radius: 4px;
    font-size: 0.75rem; cursor: pointer; transition: background 0.2s;
  }
  .copy-btn:hover { background: rgba(255,255,255,0.25); }
  .copy-btn.copied { background: var(--accent); color: var(--white); }

  .callout {
    border-left: 4px solid var(--primary);
    background: var(--primary-light);
    padding: 0.85rem 1rem; border-radius: 0 6px 6px 0;
    margin: 1rem 0; font-size: 0.92rem;
  }
  .callout.green { border-left-color: var(--accent); background: var(--accent-light); }
  .callout.warn { border-left-color: var(--warn); background: var(--warn-light); }
  .callout.purple { border-left-color: var(--purple); background: var(--purple-light); }
  .callout strong { font-weight: 600; }

  .steps { counter-reset: step; padding-left: 0; list-style: none; margin: 1rem 0; }
  .steps li {
    counter-increment: step; position: relative;
    padding: 0.5rem 0 0.5rem 2.5rem; margin-bottom: 0.5rem;
  }
  .steps li::before {
    content: counter(step);
    position: absolute; left: 0; top: 0.45rem;
    width: 26px; height: 26px; border-radius: 50%;
    background: var(--primary-light); color: var(--primary);
    display: flex; align-items: center; justify-content: center;
    font-size: 0.8rem; font-weight: 700;
  }

  .self-check {
    background: var(--accent-light); border-radius: 6px;
    padding: 1rem 1.25rem; margin: 1.5rem 0 0.5rem;
  }
  .self-check h4 { color: var(--accent); margin-bottom: 0.5rem; font-size: 0.95rem; }
  .self-check label {
    display: flex; align-items: center; gap: 0.5rem;
    font-size: 0.9rem; margin-bottom: 0.3rem; cursor: pointer;
  }
  .self-check input[type="checkbox"] { accent-color: var(--accent); width: 16px; height: 16px; }

  .tips-list { list-style: none; padding: 0; margin: 0.5rem 0; }
  .tips-list li {
    padding: 0.3rem 0 0.3rem 1.5rem; position: relative; font-size: 0.92rem;
  }
  .tips-list li::before {
    content: '💡'; position: absolute; left: 0; top: 0.3rem;
  }

  .takeaways-grid {
    display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 1rem; margin: 1rem 0;
  }
  .takeaway-card {
    background: var(--neutral-100); border-radius: var(--radius);
    padding: 1.25rem; text-align: center;
  }
  .takeaway-card .icon { font-size: 2rem; margin-bottom: 0.5rem; }
  .takeaway-card h4 { font-size: 0.95rem; margin-bottom: 0.4rem; color: var(--neutral-900); }
  .takeaway-card p { font-size: 0.85rem; color: var(--neutral-500); }

  footer {
    text-align: center; padding: 2rem; font-size: 0.85rem;
    color: var(--neutral-500); border-top: 1px solid var(--neutral-300);
    margin-top: 2rem;
  }

  @media (max-width: 900px) {
    .sidebar {
      position: fixed;
      left: -280px;
      top: 0;
      height: 100vh;
      width: 270px;
      transition: left 0.3s ease;
      box-shadow: 4px 0 20px rgba(0,0,0,0.15);
      z-index: 300;
    }
    .sidebar.open { left: 0; }
    .sidebar-overlay {
      display: none;
      position: fixed; inset: 0;
      background: rgba(0,0,0,0.4);
      z-index: 250;
    }
    .sidebar-overlay.open { display: block; }
    .sidebar-toggle { display: flex; align-items: center; justify-content: center; }
    .main-content { padding: 1.5rem 1.25rem 3rem; }
    .hero h1 { font-size: 1.5rem; }
    .hero-meta { flex-direction: column; gap: 0.5rem; }
    .part-header { padding: 1rem 1.25rem; }
    .part-body { padding: 0 1.25rem 1.5rem; }
    .takeaways-grid { grid-template-columns: 1fr; }
  }

  @media print {
    .sidebar, .sidebar-toggle, .sidebar-overlay, .back-bar { display: none !important; }
    .main-content { padding: 0; }
    .part-body.collapsed { display: block !important; }
  }

  [id] { scroll-margin-top: 1rem; }
</style>
</head>
<body>

<div class="back-bar">
  <a href="../../">← Back to Index</a>
</div>

<div class="hero">
  <div class="hero-inner">
    <h1>Microsoft 365 Copilot Training for Legal</h1>
    <p class="subtitle">Copilot for Legal Professionals — Research, Drafting &amp; Compliance</p>
    <div class="scenario">
      <strong>Scenario:</strong> You're a legal advisor at Contoso, responsible for assessing whether the company's AI Resume Screening Software complies with the EU AI Act. Your goal is to research legal risks, draft an executive summary, and communicate recommendations to leadership.<br><br>
      <em>Sample prompts are provided to help you get started. Feel free to personalize them — if Copilot doesn't deliver the result you want, refine your prompt and try again.</em>
    </div>
    <div class="hero-meta">
      <span>⚖️ Legal Research</span>
      <span>💬 Copilot Chat</span>
      <span>📝 Word</span>
      <span>📧 Outlook</span>
      <span>🎓 Instructor-Led</span>
    </div>
  </div>
</div>

<div class="sidebar-overlay" id="sidebarOverlay" onclick="closeSidebar()"></div>

<div class="layout">

<nav class="sidebar" id="sidebar">
  <a class="sb-home" href="../../">← Back to Index</a>
  <div class="sb-title">Copilot Training for Legal</div>

  <a href="#sec-objectives" class="section-link">Learning Objectives</a>
  <a href="#sec-prereqs" class="section-link">Demo Setup</a>

  <a href="#part1" class="part-link">Part 1: Copilot Basics</a>
  <a href="#part2" class="part-link">Part 2: Copilot Chat — Research</a>
  <a href="#part3" class="part-link">Part 3: Copilot in Word</a>
  <a href="#part4" class="part-link">Part 4: Copilot in Outlook</a>
  <a href="#part5" class="part-link">Part 5: Additional Prompts</a>

  <a href="#sec-takeaways" class="section-link" style="margin-top:0.5rem;">Key Takeaways</a>
</nav>

<div class="main-content">

<div class="section" id="sec-objectives">
  <h2>🎯 Learning Objectives</h2>
  <ul class="objectives-list">
    <li>Save and reuse legal-specific prompts for daily productivity</li>
    <li>Use Copilot Memory and Custom Instructions to personalize Copilot for legal work</li>
    <li>Research regulations like the EU AI Act using Copilot Chat in Web mode</li>
    <li>Draft an executive summary in Word grounded on Copilot Chat research</li>
    <li>Communicate findings and recommendations to leadership via Copilot in Outlook</li>
    <li>Apply advanced prompting techniques to interpret legal language and run scenario analyses</li>
  </ul>
</div>

<div class="section" id="sec-prereqs">
  <h2>📋 Demo Setup</h2>
  <p>There are no sample documents required for this demo.</p>
  <div class="prereq-grid">
    <div class="prereq-item"><div class="prereq-icon blue">M</div>Microsoft 365 Copilot License</div>
    <div class="prereq-item"><div class="prereq-icon blue">🌐</div>Access to <strong>m365copilot.com</strong></div>
    <div class="prereq-item"><div class="prereq-icon blue">📝</div>Word (Web or Desktop)</div>
    <div class="prereq-item"><div class="prereq-icon purple">📧</div>Outlook (Web or Desktop)</div>
    <div class="prereq-item"><div class="prereq-icon green">☁</div>OneDrive / SharePoint access</div>
  </div>
  <div class="callout">
    <strong>📝 NOTE:</strong> Sample prompts are provided to help you get started. Feel free to personalize them to suit your needs — be creative and explore! Learn more about new features <a href="https://www.microsoft.com/en-us/microsoft-365/roadmap/copilotchat" target="_blank">here</a>.
  </div>
</div>

<div class="part-card" id="part1">
  <div class="part-header-bar basics"></div>
  <div class="part-header" onclick="togglePart('body1', this)">
    <h2>Part 1: Copilot Basics — Save Prompts &amp; Customize Copilot</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body1">

    <div class="callout">
      <strong>💡 Why This Matters:</strong> Legal professionals run similar prompts repeatedly — clause comparisons, regulatory summaries, plain-English translations. Saving prompts and configuring Copilot Memory lets you reuse your best instructions without retyping them and ensures Copilot understands your legal context.
    </div>

    <h3>Practice 1: How to Save Prompts in Copilot</h3>
    <p>Saving prompts helps you quickly reuse instructions or queries without having to rewrite them each time.</p>

    <p><strong>Step 1: Save a Prompt</strong></p>
    <ol class="steps">
      <li>Open a new browser tab and navigate to <strong><a href="https://m365copilot.com" target="_blank">M365copilot.com</a></strong>.</li>
      <li>Start by running a prompt, for example:</li>
    </ol>
    <div class="prompt-box">Copilot, summarize my emails, Teams messages, and channel messages from the last 1 workday. Categorize them as internal activities, external activities, or messages from my team or manager, and prioritize them for my attention. List action items in a dedicated column and suggest follow-ups if possible, in a dedicated column.

The table should look like this:
Type (Mail/Teams/Channel) | Topic | Summarization | Category | Priority | Action Item | Follow-up.

If I have been directly mentioned, make the font of the topic bold.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <ol class="steps" start="3">
      <li>Hover over the prompt.</li>
      <li>Click <strong>Save Prompt</strong>.</li>
      <li>Give it a name for easy reference.</li>
    </ol>
    <p><img src="../Prompts/Media/ADimage6.png" alt="Save prompt screenshot" style="max-width:100%;border-radius:6px;" /></p>
    <ul class="tips-list">
      <li>Use clear names for prompts (e.g., "Weekly Legal Catch-Up", "Contract Clause Review").</li>
      <li>Share the most frequently used prompts with your team to maintain consistency.</li>
      <li>Regularly review and update saved prompts to keep them relevant.</li>
    </ul>

    <p><strong>Step 2: Access your saved Prompts</strong></p>
    <ol class="steps">
      <li>Open Copilot.</li>
      <li>Click <strong>See more</strong>.</li>
      <li>Select <strong>Prompt Gallery</strong>.</li>
      <li>Go to <strong>Your prompts</strong> — from here, you can delete prompts, share them via link, or share them with a team.</li>
    </ol>
    <p><img src="../Prompts/Media/ADimage3.png" alt="Prompt gallery 1" style="max-width:100%;border-radius:6px;" /></p>
    <p><img src="../Prompts/Media/ADimage4.png" alt="Prompt gallery 2" style="max-width:100%;border-radius:6px;" /></p>
    <p><img src="../Prompts/Media/ADimage5.png" alt="Prompt gallery 3" style="max-width:100%;border-radius:6px;" /></p>

    <h3>Practice 2: Memory and Customization of Copilot</h3>
    <p>Copilot Memory offers a more personalized experience based on your previous chats, work profile, custom instructions, and other metadata. Copilot Customization uses this information to create tailored interactions — for example, you can tell Copilot your writing style so AI-generated drafts sound more like you.</p>

    <p><strong>Step 1: Access Copilot</strong></p>
    <p>Open a new browser tab and navigate to <a href="https://m365.cloud.microsoft/chat" target="_blank">Copilot</a> (or use your usual method to access Copilot).</p>

    <p><strong>Step 2: Add instructions</strong></p>
    <ul class="tips-list">
      <li>Click on the settings by selecting <strong>"…"</strong></li>
      <li>Open <strong>Settings</strong> and select <strong>Personalization</strong>.</li>
      <li>Then select <strong>Custom Instructions</strong>.</li>
    </ul>
    <p><img src="../Prompts/Media/ADimage1.png" alt="Personalization settings" style="max-width:100%;border-radius:6px;" /></p>
    <p><img src="../Prompts/Media/ADimage2.png" alt="Custom instructions" style="max-width:100%;border-radius:6px;" /></p>

    <p>You can add your custom instructions in this section. For reference, here's a guide with sample instructions you can add to Copilot:</p>
    <ul class="tips-list">
      <li><a href="https://livesend.microsoft.com/i/rNoOVLzAAYKpEIxHcPLUSSIGNURf0AnaauPLUSSIGNpTT12ioHC1iT2S9v5zfm___ebPPLUSSIGNq8yBBDVxGsPLUSSIGNGevpl4gM20eehkcX55fDwwHvmMnfisgImZ___gDPLUSSIGN7MtPeWjGSVb8I5OJM40FI6OPIj" target="_blank">Copilot Custom Instructions</a></li>
    </ul>

    <div class="self-check">
      <h4>✅ Self-Check: Part 1</h4>
      <label><input type="checkbox"> I saved a prompt to my Prompt Gallery</label>
      <label><input type="checkbox"> I located my saved prompts in the Prompt Gallery</label>
      <label><input type="checkbox"> I configured Custom Instructions for my legal role</label>
    </div>
  </div>
</div>

<div class="part-card" id="part2">
  <div class="part-header-bar chat"></div>
  <div class="part-header" onclick="togglePart('body2', this)">
    <h2>Part 2: Copilot Chat — Research the EU AI Act</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body2">

    <div class="callout">
      <strong>💡 Why This Matters:</strong> Regulations evolve quickly and legal teams must assess compliance impact under tight timelines. Copilot Chat in Web mode can summarize complex regulations, identify compliance obligations, and surface legal risks — accelerating the research phase of any legal assessment.
    </div>

    <p>Let's start by researching the AI Act and its potential impact on Contoso's AI hiring tool.</p>

    <ol class="steps">
      <li>Open a browser and navigate to <strong><a href="https://m365copilot.com" target="_blank">M365copilot.com</a></strong>.</li>
      <li>Ensure <strong>Web Mode</strong> is selected.</li>
    </ol>
    <p><img src="../Prompts/Media/web-mode.png" alt="Web mode tab" style="max-width:100%;border-radius:6px;" /></p>

    <ol class="steps" start="3">
      <li>In the prompt window, type the following:</li>
    </ol>
    <div class="prompt-box">Contoso is launching an AI Resume Screening Software to evaluate job applicants. As a legal advisor, I need to assess whether it complies with the EU Artificial Intelligence Act. Summarize key provisions related to AI in hiring, compliance requirements for high-risk systems, and potential legal risks.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

    <ol class="steps" start="4">
      <li>Review Copilot's response and take notes on relevant legal risks and compliance requirements.</li>
      <li>Now ask Copilot a series of follow-up questions to gather more information:</li>
    </ol>
    <div class="prompt-box">Does the AI Act classify resume screening software as a high-risk AI system?<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <div class="prompt-box">What are the key obligations for high-risk AI systems under the AI Act?<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <div class="prompt-box">Are there any exemptions in the AI Act that could apply to Contoso's system?<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

    <ol class="steps" start="6">
      <li>Now ask Copilot to summarize all the information so far:</li>
    </ol>
    <div class="prompt-box">Summarize all the information we've discussed into a structured list, ensuring no key details are missed. Then, export the summary to a Word document.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

    <ol class="steps" start="7">
      <li>Select the hyperlink Copilot provides for the new Word document to open it.</li>
      <li>Once opened, select <strong>Enable Editing</strong> and then turn on <strong>AutoSave</strong>. Select your OneDrive account when prompted.</li>
      <li>Copy the shared URL for use in the next step.</li>
    </ol>
    <p><img src="../Demos/Media/share-menu-with-copy-link-9fd1c60a.png" alt="Share link menu" style="max-width:100%;border-radius:6px;" /></p>

    <div class="self-check">
      <h4>✅ Self-Check: Part 2</h4>
      <label><input type="checkbox"> I researched the EU AI Act using Copilot Chat in Web mode</label>
      <label><input type="checkbox"> I asked follow-up questions to refine the legal analysis</label>
      <label><input type="checkbox"> I exported a structured summary to a Word document</label>
    </div>
  </div>
</div>

<div class="part-card" id="part3">
  <div class="part-header-bar word"></div>
  <div class="part-header" onclick="togglePart('body3', this)">
    <h2>Part 3: Copilot in Word — Executive Summary</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body3">

    <div class="callout purple">
      <strong>💡 Why This Matters:</strong> Executive leadership needs concise, well-structured summaries — not raw research. Copilot in Word can transform your research notes into polished executive-ready documents in seconds, letting you focus on the legal judgment and recommendations.
    </div>

    <p>Now, we'll draft an executive summary outlining legal risks and recommendations for Contoso's leadership.</p>

    <ol class="steps">
      <li>Open a new instance of Word, either in your browser or desktop application.</li>
      <li>In the <strong>"Describe what you'd like to write"</strong> prompt box, type the following:</li>
    </ol>
    <div class="prompt-box">Reference the following document [Link to exported Copilot Chat summary from the first task] and draft an executive summary outlining key legal risks, compliance requirements, and recommendations for Contoso's AI Resume Screening Software.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

    <div class="callout">
      <strong>📝 NOTE:</strong> Attach the document or paste the shared link directly into the prompt to ensure Copilot can access the relevant content.
    </div>

    <ol class="steps" start="3">
      <li>Review Copilot's output. Before selecting <strong>Keep it</strong>, refine the response by asking Copilot:</li>
    </ol>
    <div class="prompt-box">Add a section on the potential business impact of these compliance requirements.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

    <p>Other optional refinements:</p>
    <ul class="tips-list">
      <li>Ask Copilot to reword sections for a more professional tone.</li>
      <li>Request a shorter, more concise version if the summary is too long.</li>
      <li>Expand with additional sections.</li>
    </ul>

    <ol class="steps" start="4">
      <li>After reviewing and finalizing the document, <strong>copy the generated Executive Summary</strong> to your clipboard for use in the next demo.</li>
    </ol>

    <div class="self-check">
      <h4>✅ Self-Check: Part 3</h4>
      <label><input type="checkbox"> I drafted an executive summary in Word using Copilot</label>
      <label><input type="checkbox"> I refined the draft with follow-up prompts</label>
      <label><input type="checkbox"> I copied the finalized summary for the next step</label>
    </div>
  </div>
</div>

<div class="part-card" id="part4">
  <div class="part-header-bar outlook"></div>
  <div class="part-header" onclick="togglePart('body4', this)">
    <h2>Part 4: Copilot in Outlook — Communicate with Leadership</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body4">

    <div class="callout">
      <strong>💡 Why This Matters:</strong> A legal assessment is only useful if the right stakeholders understand it. Copilot in Outlook can package your findings into a clear, professional email — making it easier to align leadership on next steps.
    </div>

    <p>Lastly, we'll draft an email to Contoso's leadership summarizing our findings and next steps.</p>

    <ol class="steps">
      <li>Open <strong>Outlook</strong> (either in your browser or desktop application).</li>
      <li>Select <strong>New Email</strong>.</li>
      <li>Select <strong>Copilot</strong> in the ribbon. From the drop-down menu, choose <strong>Draft with Copilot</strong>.</li>
      <li>In the <strong>"What do you want this email to say?"</strong> prompt window, type:</li>
    </ol>
    <div class="prompt-box">Draft an email to Contoso's executive leadership summarizing our legal assessment of the AI Resume Screening Software under the EU AI Act. Use the following executive summary as a reference.

[paste Executive Summary from the previous task]

Conclude the email with a request for leadership's input on the next steps, including a proposed compliance review meeting.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

    <div class="callout">
      <strong>📝 NOTE:</strong> Paste the Executive Summary contents that you copied from the previous demo.
    </div>

    <ol class="steps" start="5">
      <li>Once the draft is generated, you can use the <strong>Adjust</strong> feature to modify the tone, length, or level of formality.</li>
    </ol>

    <div class="self-check">
      <h4>✅ Self-Check: Part 4</h4>
      <label><input type="checkbox"> I drafted a leadership email using Copilot in Outlook</label>
      <label><input type="checkbox"> I used the Adjust feature to refine tone or length</label>
    </div>
  </div>
</div>

<div class="part-card" id="part5">
  <div class="part-header-bar prompts"></div>
  <div class="part-header" onclick="togglePart('body5', this)">
    <h2>Part 5: Additional Sample Prompts</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body5">

    <div class="callout green">
      <strong>💡 Why This Matters:</strong> Beyond the core demo flow, these prompts show how Copilot can support common legal tasks — translating legalese for non-lawyers and running "what-if" scenario analyses against contract language.
    </div>

    <h3>Lawyer's Second Copilot Prompt: Plain-English Summary</h3>
    <div class="prompt-box">Convert the technical language of Article I, paragraphs 1 (Normal Exercise) and 2 (Acceleration) into a plain-English summary suitable for non-lawyers, while preserving all legal obligations.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

    <h3>Lawyer's Third Copilot Prompt: Scenario Analysis</h3>
    <div class="prompt-box">Scenario: What happens if the optionee voluntarily leaves the company before the second anniversary (i.e., before any shares vest on October 12, 2012)? Explain which shares, if any, remain exercisable and for how long.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

    <div class="callout warn">
      <strong>⚠️ Reminder:</strong> Always validate Copilot's interpretations against the source legal text. AI outputs are a starting point for analysis — final legal judgment remains with the attorney.
    </div>
  </div>
</div>

<div class="section" id="sec-takeaways">
  <h2>🔑 Key Takeaways</h2>
  <div class="takeaways-grid">
    <div class="takeaway-card">
      <div class="icon">⚖️</div>
      <h4>Research Faster</h4>
      <p>Use Copilot Chat in Web mode to summarize regulations and identify compliance obligations in minutes.</p>
    </div>
    <div class="takeaway-card">
      <div class="icon">🔗</div>
      <h4>Chain Your Tools</h4>
      <p>Chat to research → Word to draft → Outlook to communicate. End-to-end legal workflow without context switching.</p>
    </div>
    <div class="takeaway-card">
      <div class="icon">🔄</div>
      <h4>Iterate, Don't Accept First Draft</h4>
      <p>Refine and follow up. Copilot gets better with each iteration — treat it as a conversation, not a one-shot answer.</p>
    </div>
    <div class="takeaway-card">
      <div class="icon">🧠</div>
      <h4>AI Assists, You Decide</h4>
      <p>Copilot accelerates research and drafting, but legal judgment and final review remain with you.</p>
    </div>
  </div>
</div>

</div>
</div>

<footer>
  <p><strong>Microsoft 365 Copilot Training for Legal</strong> — Research, Drafting &amp; Compliance</p>
  <p>For questions or feedback, reach out to your training facilitator.</p>
</footer>

<button class="sidebar-toggle" id="sidebarToggle" onclick="openSidebar()" aria-label="Open navigation">☰</button>

<script>
  function togglePart(bodyId, headerEl) {
    const body = document.getElementById(bodyId);
    const icon = headerEl.querySelector('.toggle-icon');
    body.classList.toggle('collapsed');
    icon.classList.toggle('open');
  }

  function copyPrompt(btn) {
    const box = btn.parentElement;
    const text = box.textContent.replace('Copy', '').replace('Copied!', '').trim();
    navigator.clipboard.writeText(text).then(() => {
      btn.textContent = 'Copied!';
      btn.classList.add('copied');
      setTimeout(() => {
        btn.textContent = 'Copy';
        btn.classList.remove('copied');
      }, 2000);
    });
  }

  function openSidebar() {
    document.getElementById('sidebar').classList.add('open');
    document.getElementById('sidebarOverlay').classList.add('open');
  }
  function closeSidebar() {
    document.getElementById('sidebar').classList.remove('open');
    document.getElementById('sidebarOverlay').classList.remove('open');
  }

  document.querySelectorAll('.sidebar a').forEach(link => {
    link.addEventListener('click', () => {
      if (window.innerWidth <= 900) closeSidebar();
    });
  });

  document.addEventListener('DOMContentLoaded', () => {
    const sidebarLinks = document.querySelectorAll('.sidebar a[href^="#"]');
    const targets = [];

    sidebarLinks.forEach(link => {
      const id = link.getAttribute('href').substring(1);
      const el = document.getElementById(id);
      if (el) targets.push({ link, el });
    });

    sidebarLinks.forEach(link => {
      link.addEventListener('click', (e) => {
        const id = link.getAttribute('href').substring(1);
        const target = document.getElementById(id);
        if (!target) return;

        const partCard = target.closest('.part-card');
        if (partCard) {
          const bodyEl = partCard.querySelector('.part-body');
          if (bodyEl && bodyEl.classList.contains('collapsed')) {
            const header = partCard.querySelector('.part-header');
            const bodyId = bodyEl.id;
            togglePart(bodyId, header);
          }
        }
      });
    });

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const id = entry.target.id;
          sidebarLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === '#' + id) {
              link.classList.add('active');
            }
          });
        }
      });
    }, { threshold: 0.2, rootMargin: '-10% 0px -70% 0px' });

    targets.forEach(t => observer.observe(t.el));
  });
</script>
</body>
</html>
