---
demo:
    title: 'HR Demo'
layout: none
---

<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>HR Demo | Learning</title>
<link rel="stylesheet" href="../../Allfiles/demo-style.css">
<style>:root { --hero-from: #00695C; --hero-via: #00897B; --hero-to: #0078D4; }</style>
</head>
<body>

<div class="back-bar">
  <a href="https://emontes07.github.io/Learning/">← Back to Index</a>
</div>

<div class="hero">
  <div class="hero-inner">
    <h1>Microsoft 365 Copilot for HR</h1>
    <p class="subtitle">Hire faster — from job description to shortlist to outreach</p>
    <div class="scenario">
      <strong>Scenario:</strong> Streamline the hiring process for a team of UX Designers by creating a tailored job description, shortlisting candidates based on their resumes, and drafting a hiring strategy to align the team.
    </div>
    <div class="hero-meta">
      <span>👥 HR</span>
      <span>📝 Word</span>
      <span>💬 Copilot Chat</span>
      <span>📧 Outlook</span>
      <span>🎨 UX Hiring</span>
    </div>
  </div>
</div>

<div class="sidebar-overlay" id="sidebarOverlay" onclick="closeSidebar()"></div>

<div class="layout">

<nav class="sidebar" id="sidebar">
  <a class="sb-home" href="https://emontes07.github.io/Learning/">← Back to Index</a>
  <div class="sb-title">HR Demo</div>

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
    <li>Generate a tailored job description grounded on responsibilities</li>
    <li>Compare candidate resumes against the job description</li>
    <li>Draft leadership-ready hiring communications</li>
  </ul>
</div>

<div class="section" id="sec-prereqs">
  <h2>📋 Demo Setup</h2>
  <p>The sample documents can be found in the MS-4021 GitHub <a href='https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/tree/master/ResourceFiles' target='_blank'>repository</a>:</p>    <ul class="tips-list">
      <li><a href='https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/raw/master/ResourceFiles/Graphic_Design_Institute_Design_Team_Responsibilities.docx'>Design_Team_Responsibilities.docx</a></li>
      <li><a href='https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/raw/master/ResourceFiles/Resume_Patti_Fernandez.docx'>Resume_Patti_Fernandez.docx</a></li>
      <li><a href='https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/raw/master/ResourceFiles/Resume_Nestor_Wilke.docx'>Resume_Nestor_Wilke.docx</a></li>
      <li><a href='https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/raw/master/ResourceFiles/Resume_Holly_Dickson.docx'>Resume_Holly_Dickson.docx</a></li>
      <li><a href='https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/raw/master/ResourceFiles/Resume_Alex_Wilber.docx'>Resume_Alex_Wilber.docx</a></li>
    </ul><div class="callout warn"><strong>📝 NOTE:</strong> Allow up to 10 minutes for these files to sync to your OneDrive. Download in advance to avoid delays during the demo.</div>
</div>

<div class="part-card" id="part1">
  <div class="part-header-bar navy"></div>
  <div class="part-header" onclick="togglePart('body1', this)">
    <h2>Part 1: Copilot in Word — Draft a Job Description</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body1">
<div class="callout"><strong>💡 Why This Matters:</strong> A well-crafted JD attracts the right candidates and sets clear expectations. Copilot writes the first draft grounded on your team's responsibilities.</div>
    <ol class="steps" start="1">
      <li>Open <strong>Word</strong> (web or desktop).</li>
      <li>In <strong>Describe what you'd like to write</strong>, enter the prompt below.</li>
    </ol>
<div class="prompt-box">I'm the HR Manager at the Graphic Design Institute. We've currently started the hiring process for a new Senior Animation Designer. Please review the attached document outlining the job responsibilities for this role and generate a detailed job description based on this information.

[copy link or reference file to Design_Team_Responsibilities.docx]<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="callout"><strong>📝 NOTE:</strong> Attach the Design_Team_Responsibilities.docx file or paste the shared link directly into the prompt so Copilot can access the content.</div>
    <ol class="steps" start="3">
      <li>Save the document as <strong>GDI_Job_Description.docx</strong>.</li>
      <li>Copy the shared URL for use in the next step (enable AutoSave).</li>
    </ol>
    <div class="self-check">
      <h4>✅ Self-Check: Part 1</h4>
      <label><input type="checkbox"> I drafted a JD grounded on responsibilities</label>
      <label><input type="checkbox"> I saved and copied the share link</label>
    </div>
  </div>
</div>

<div class="part-card" id="part2">
  <div class="part-header-bar blue"></div>
  <div class="part-header" onclick="togglePart('body2', this)">
    <h2>Part 2: Copilot Chat — Compare Resumes Against the JD</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body2">
<div class="callout"><strong>💡 Why This Matters:</strong> Copilot can read multiple resumes at once and rank them against your JD — saving hours of manual screening.</div>
    <ol class="steps" start="1">
      <li>Open <a href='https://m365copilot.com' target='_blank'>M365copilot.com</a>.</li>
      <li>Ensure <strong>Work Mode</strong> is selected.</li>
    </ol>
    <p><img src='../Prompts/Media/work-mode.png' alt='Work mode tab' style='max-width:100%;border-radius:6px;' /></p>
<div class="prompt-box">We are hiring for the position of Senior Animation Designer. Please analyze the attached resumes and compare them to the requirements outlined in the job description provided here: [paste link to GDI_Job_Description.docx]. Rank the candidates from most qualified to least qualified, based on their alignment with the role.

[Resume - Patti Fernandez
Resume - Nestor Wilke
Resume - Holly Dickson
Resume - Alex Wilber]<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
<div class="callout"><strong>📝 NOTE:</strong> Attach the resumes directly to the prompt, or reference each file using shared links or filenames in OneDrive.</div>
    <p>Optionally, ask Copilot to export the response to a Word document.</p>
    <div class="self-check">
      <h4>✅ Self-Check: Part 2</h4>
      <label><input type="checkbox"> I ranked candidates with Copilot Chat</label>
      <label><input type="checkbox"> I exported the ranking to Word (optional)</label>
    </div>
  </div>
</div>

<div class="part-card" id="part3">
  <div class="part-header-bar purple"></div>
  <div class="part-header" onclick="togglePart('body3', this)">
    <h2>Part 3: Copilot in Outlook — Email the Hiring Team</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body3">
<div class="callout"><strong>💡 Why This Matters:</strong> Close the loop quickly. Copilot drafts an email that recommends top candidates and proposes next steps.</div>
    <ol class="steps" start="1">
      <li>Open <strong>Outlook</strong> (web or desktop) → <strong>New Email</strong>.</li>
      <li>Click <strong>Copilot</strong> → <strong>Draft with Copilot</strong>.</li>
    </ol>
<div class="prompt-box">Please draft an email to the hiring team to share that Nestor Wilke and Patti Fernandez align best with the Senior Animation Designer role based on their qualifications. Include a recommendation to schedule interviews for these candidates and request feedback on next steps.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <div class="self-check">
      <h4>✅ Self-Check: Part 3</h4>
      <label><input type="checkbox"> I drafted a recommendation email</label>
      <label><input type="checkbox"> I used Adjust to refine tone/length</label>
    </div>
  </div>
</div>

<div class="section" id="sec-takeaways">
  <h2>🔑 Key Takeaways</h2>
  <div class="takeaways-grid">
    <div class="takeaway-card"><div class="icon">📝</div><h4>Better JDs, Faster</h4><p>Generate strong job descriptions grounded on real responsibilities.</p></div>
    <div class="takeaway-card"><div class="icon">⚖️</div><h4>Objective Screening</h4><p>Compare candidates to the JD with clear, defensible logic.</p></div>
    <div class="takeaway-card"><div class="icon">📧</div><h4>Move the Process</h4><p>Communicate next steps clearly to keep momentum.</p></div>
    <div class="takeaway-card"><div class="icon">🧠</div><h4>Human in the Loop</h4><p>Final hiring decisions remain with you — Copilot accelerates the path.</p></div>
  </div>
</div>

</div>
</div>

<footer>
  <p><strong>Microsoft 365 Copilot — HR Demo</strong></p>
  <p>For questions or feedback, reach out to your training facilitator.</p>
</footer>

<button class="sidebar-toggle" id="sidebarToggle" onclick="openSidebar()" aria-label="Open navigation">☰</button>

<script src="../../Allfiles/demo-script.js"></script>
</body>
</html>
