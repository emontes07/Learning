---
demo:
    title: 'IT Demo'
layout: none
---

<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>IT Demo | Learning</title>
<link rel="stylesheet" href="../../Allfiles/demo-style.css">
<style>:root { --hero-from: #01579B; --hero-via: #0277BD; --hero-to: #00ACC1; }</style>
</head>
<body>

<div class="back-bar">
  <a href="https://emontes07.github.io/Learning/">← Back to Index</a>
</div>

<div class="hero">
  <div class="hero-inner">
    <h1>Microsoft 365 Copilot for IT</h1>
    <p class="subtitle">Plan, document, and present complex IT projects faster</p>
    <div class="scenario">
      <strong>Scenario:</strong> As an IT Infrastructure Manager, you're planning to install a new network security product into your corporate network. Use Copilot to build a project plan, ground it on product specifications, and create a deck to brief leadership.
    </div>
    <div class="hero-meta">
      <span>🔒 IT Infrastructure</span>
      <span>💬 Copilot Chat</span>
      <span>📝 Word</span>
      <span>🎯 PowerPoint</span>
    </div>
  </div>
</div>

<div class="sidebar-overlay" id="sidebarOverlay" onclick="closeSidebar()"></div>

<div class="layout">

<nav class="sidebar" id="sidebar">
  <a class="sb-home" href="https://emontes07.github.io/Learning/">← Back to Index</a>
  <div class="sb-title">IT Demo</div>

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
    <li>Create a structured implementation plan with role-based prompts</li>
    <li>Ground the plan on real product specifications</li>
    <li>Translate the plan into a leadership presentation</li>
  </ul>
</div>

<div class="section" id="sec-prereqs">
  <h2>📋 Demo Setup</h2>
  <p>Required file from the MS-4021 GitHub <a href='https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/tree/master/ResourceFiles' target='_blank'>repository</a>:</p>    <ul class="tips-list">
      <li><a href='https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/raw/master/ResourceFiles/Contoso_CipherGuard_Product_Specification.docx'>Contoso_CipherGuard_Product_Specification.docx</a></li>
    </ul><div class="callout warn"><strong>📝 NOTE:</strong> Allow up to 10 minutes for OneDrive sync after download.</div>
</div>

<div class="part-card" id="part1">
  <div class="part-header-bar blue"></div>
  <div class="part-header" onclick="togglePart('body1', this)">
    <h2>Part 1: Copilot Chat — Build a Project Implementation Plan</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body1">
<div class="callout"><strong>💡 Why This Matters:</strong> Role-based prompts give Copilot context, so the plan reflects how IT actually delivers projects.</div>
    <ol class="steps" start="1">
      <li>Open <a href='https://m365copilot.com' target='_blank'>M365copilot.com</a> in Web mode.</li>
      <li>Use a role-based prompt to seed the plan.</li>
    </ol>
<div class="prompt-box">You are an IT infrastructure manager at Contoso. Your task is to create a detailed project implementation plan for installing a new network security product in your corporate network. Your plan should include key milestones, resource allocation, potential risks, and a timeline to ensure successful deployment and minimal disruption to operations.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <ol class="steps" start="3">
      <li>Refine the plan with additional structured sections.</li>
    </ol>
<div class="prompt-box">Please add the following sections to the existing plan: testing and QA, training, communication, documentation and reporting, stakeholder analysis, project timeline, and risk assessment and mitigation. Ensure these sections provide detailed action steps and align with the existing content. Avoid duplicating any items already included in the original plan.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="prompt-box">Please export the project plan to a Word document.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <ol class="steps" start="4">
      <li>Save as <strong>Project_Implementation_Plan.docx</strong> and copy the shared URL.</li>
    </ol>
    <div class="self-check">
      <h4>✅ Self-Check: Part 1</h4>
      <label><input type="checkbox"> I generated an IT project plan</label>
      <label><input type="checkbox"> I refined it with structured sections</label>
      <label><input type="checkbox"> I exported to Word</label>
    </div>
  </div>
</div>

<div class="part-card" id="part2">
  <div class="part-header-bar navy"></div>
  <div class="part-header" onclick="togglePart('body2', this)">
    <h2>Part 2: Copilot in Word — Ground the Plan on Product Specs</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body2">
<div class="callout"><strong>💡 Why This Matters:</strong> A generic plan won't deploy your product. Grounding on specs gets you a plan tailored to CipherGuard's requirements.</div>
    <ol class="steps" start="1">
      <li>Open <strong>Word</strong>.</li>
      <li>Use <strong>Describe what you'd like to write</strong> with the prompt below.</li>
    </ol>
<div class="prompt-box">Using the Contoso [/CipherGuard Product Specification.docx] and the 'Project Implementation Plan' template provided in [paste in link to Project_Implementation_Plan.docx], draft a comprehensive project implementation plan for deploying Contoso CipherGuard. Ensure the plan aligns with the product specifications and follows the structure outlined in the template.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="callout"><strong>📝 NOTE:</strong> Brackets indicate referenced documents. Reference by shared link or filename in OneDrive.</div>
    <ol class="steps" start="3">
      <li>Save as <strong>Contoso_Project_Plan.docx</strong> and copy the shared URL.</li>
    </ol>
    <div class="self-check">
      <h4>✅ Self-Check: Part 2</h4>
      <label><input type="checkbox"> I produced a grounded project plan</label>
      <label><input type="checkbox"> I saved and shared the document</label>
    </div>
  </div>
</div>

<div class="part-card" id="part3">
  <div class="part-header-bar magenta"></div>
  <div class="part-header" onclick="togglePart('body3', this)">
    <h2>Part 3: Copilot in PowerPoint — Brief Leadership</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body3">
<div class="callout"><strong>💡 Why This Matters:</strong> Leadership wants the headlines, not the runbook. Copilot turns your plan into a clean executive deck.</div>
    <ol class="steps" start="1">
      <li>Open a new presentation at <a href='https://powerpoint.new' target='_blank'>PowerPoint.new</a>.</li>
      <li>Click <strong>Create presentation from file</strong>.</li>
      <li>Paste the <strong>Contoso_Project_Plan.docx</strong> link.</li>
    </ol>
<div class="prompt-box">Create a presentation from [Link to Contoso_Project_Plan.docx].<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="callout"><strong>📝 NOTE:</strong> Slide generation can take up to two minutes.</div>
    <div class="self-check">
      <h4>✅ Self-Check: Part 3</h4>
      <label><input type="checkbox"> I generated a leadership deck from the plan</label>
    </div>
  </div>
</div>

<div class="section" id="sec-takeaways">
  <h2>🔑 Key Takeaways</h2>
  <div class="takeaways-grid">
    <div class="takeaway-card"><div class="icon">🛠️</div><h4>Plan with Context</h4><p>Role-based prompts produce more relevant plans.</p></div>
    <div class="takeaway-card"><div class="icon">📎</div><h4>Ground in Reality</h4><p>Anchor plans on product docs and templates.</p></div>
    <div class="takeaway-card"><div class="icon">🎯</div><h4>Communicate Up</h4><p>Translate technical plans into executive narratives.</p></div>
    <div class="takeaway-card"><div class="icon">✅</div><h4>Always Validate</h4><p>Review every step before deploying to production.</p></div>
  </div>
</div>

</div>
</div>

<footer>
  <p><strong>Microsoft 365 Copilot — IT Demo</strong></p>
  <p>For questions or feedback, reach out to your training facilitator.</p>
</footer>

<button class="sidebar-toggle" id="sidebarToggle" onclick="openSidebar()" aria-label="Open navigation">☰</button>

<script src="../../Allfiles/demo-script.js"></script>
</body>
</html>
