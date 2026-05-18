---
layout: none
---

<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Immersion Experience — Sales | Learning</title>
<link rel="stylesheet" href="../../Allfiles/demo-style.css">
<style>:root { --hero-from: #C73E1D; --hero-via: #E64A19; --hero-to: #FF7043; }</style>
</head>
<body>

<div class="back-bar">
  <a href="https://emontes07.github.io/Learning/">← Back to Index</a>
</div>

<button class="sidebar-toggle" onclick="openSidebar()" aria-label="Open menu">☰ Menu</button>

<div class="hero">
  <div class="hero-inner">
    <h1>📈 Immersion Experience — Sales</h1>
    <p class="subtitle">Research accounts, build proposals, and close deals faster.</p>
    <div class="hero-meta">
      <span>📈 Sales</span>
      <span>💬 Copilot Chat</span>
      <span>📝 Word</span>
      <span>📊 Excel</span>
    </div>
  </div>
</div>

<div class="sidebar-overlay" id="sidebarOverlay" onclick="closeSidebar()"></div>

<div class="layout">

<nav class="sidebar" id="sidebar">
  <a class="sb-home" href="https://emontes07.github.io/Learning/">← Back to Index</a>
  <div class="sb-title">Sales</div>

  <a href="#sec-intro" class="section-link">Overview</a>
  <a href="#part1-task-1-gather-insights" class="part-link">Task 1: Gather Insights</a>
  <a href="#part2-task-2-align-on-action-items" class="part-link">Task 2: Align on Action Items</a>
  <a href="#part3-task-3-prepare-for-a-customer-meeting" class="part-link">Task 3: Prepare for a Customer Meeting</a>
</nav>

<div class="main-content">

<div class="section" id="sec-intro">
<div markdown="1">

Gather insights from recent customer interactions, align on key action items, and prepare for an upcoming customer meeting.

You'll perform three tasks:

- Gather insights using **Microsoft 365 Copilot Chat**
- Align on action items using **Copilot in Outlook**
- Prepare for a customer meeting using **Copilot in Word**

> **NOTE:** Sample prompts are provided to help you get started. Feel free to personalize them to suit your needs—be creative and explore! If Copilot doesn’t deliver the result you want, refine your prompt and try again. Enjoy the process and have fun experimenting!

</div>
</div>

<div class="part-card" id="part1-task-1-gather-insights">
  <div class="part-header-bar blue"></div>
  <div class="part-header" onclick="togglePart('body1', this)">
    <h2>Task 1: Gather Insights</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body1">
<div markdown="1">

Using **Microsoft 365 Copilot Chat** (In teams), Gather and review insights from recent interactions with a customer on project implementation. These insights will help you understand customer concerns, progress, and any new opportunities to address during future engagements.

**Steps**:

- In **Microsoft Teams**, select **Copilot** at the top of the **Chat** pane.  This opens a **Copilot** window.

    ![screenshot showing Copilot Chat within Teams.](../Prompts/Media/Copilot-chat-in-teams.png)

- Ensure the "Work mode" tab is selected in Copilot Chat:

    ![screenshot showing Work mode tab.](../Prompts/Media/work-mode.png)

**Sample Prompt**:

</div>

<div class="prompt-box">Summarize my recent interactions with [/Name of Person] regarding [specific customer / topic / project]. Organize the summary by key points or actions discussed, and include any follow-up items or outstanding questions that may require attention.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

<div markdown="1">

> **NOTE:** Replace [Name of Person] with the person you’re focusing on, and [specific customer / topic / project] with the relevant topic. Use the **/** character (slash) to reference internal contacts for quick access to recent interactions.

</div>
  </div>
</div>

<div class="part-card" id="part2-task-2-align-on-action-items">
  <div class="part-header-bar green"></div>
  <div class="part-header" onclick="togglePart('body2', this)">
    <h2>Task 2: Align on Action Items</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body2">
<div markdown="1">

Using **Copilot in Outlook**, draft a follow-up email based on the insights gathered from Copilot Chat. Include open action items, clarify responsibilities, and provide updates to a colleague or team to ensure alignment and accountability.

**Steps**:

- In **Outlook**, select **New Email** and then  from the ribbon select **Copilot** > **Draft with Copilot**

    ![screenshot showing Copilot in Outlook.](../Prompts/Media/copilot-outlook-desktop.png)

**Sample Prompt**:

</div>

<div class="prompt-box">Using the insights below, draft a follow-up email to [Name of Person] highlighting the key actions and next steps. Also, ask for a follow-up meeting to discuss further.<br><br>[Paste insights from Copilot Chat here]<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
  </div>
</div>

<div class="part-card" id="part3-task-3-prepare-for-a-customer-meeting">
  <div class="part-header-bar purple"></div>
  <div class="part-header" onclick="togglePart('body3', this)">
    <h2>Task 3: Prepare for a Customer Meeting</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body3">
<div markdown="1">

Using **Copilot in Word**, draft talking points for an upcoming customer status update meeting. Ensure the talking points focus on key deliverables, address customer priorities, and provide clarity on next steps

**Steps**:

- Launch Microsoft Word from your browser [word.new](https://word.new) or use the desktop application.
- Enter your prompt where it says **"Describe what you'd like to write"**.

    ![screenshot showing Copilot in Word.](../Prompts/Media/draft-with-copilot.png)

**Sample Prompt**:

</div>

<div class="prompt-box">Using the insights below, draft talking points for an upcoming status update meeting with [Customer Name]. Focus on any challenges and next steps.<br><br>[Paste insights from Copilot Chat here, or add your own insights]<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
  </div>
</div>


</div><!-- /main-content -->
</div><!-- /layout -->

<script src="../../Allfiles/demo-script.js"></script>
</body>
</html>
