---
layout: none
---

<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Immersion Experience — Business Manager | Learning</title>
<link rel="stylesheet" href="../../Allfiles/demo-style.css">
<style>:root { --hero-from: #1A237E; --hero-via: #283593; --hero-to: #3949AB; }</style>
</head>
<body>

<div class="back-bar">
  <a href="https://emontes07.github.io/Learning/">← Back to Index</a>
</div>

<button class="sidebar-toggle" onclick="openSidebar()" aria-label="Open menu">☰ Menu</button>

<div class="hero">
  <div class="hero-inner">
    <h1>📊 Immersion Experience — Business Manager</h1>
    <p class="subtitle">Plan, track, and lead teams with AI-powered insight.</p>
    <div class="hero-meta">
      <span>📊 Business Manager</span>
      <span>💬 Copilot Chat</span>
      <span>📝 Word</span>
    </div>
  </div>
</div>

<div class="sidebar-overlay" id="sidebarOverlay" onclick="closeSidebar()"></div>

<div class="layout">

<nav class="sidebar" id="sidebar">
  <a class="sb-home" href="https://emontes07.github.io/Learning/">← Back to Index</a>
  <div class="sb-title">Business Manager</div>

  <a href="#sec-intro" class="section-link">Overview</a>
  <a href="#part1-task-1-review-communications" class="part-link">Task 1: Review communications</a>
  <a href="#part2-task-2-prepare-for-a-meeting" class="part-link">Task 2: Prepare for a meeting</a>
  <a href="#part3-task-3-send-a-follow-up-email" class="part-link">Task 3: Send a follow-up email</a>
</nav>

<div class="main-content">

<div class="section" id="sec-intro">
<div markdown="1">

Optimize daily tasks by reviewing communications, sending an email, and preparing for an upcoming meeting.  

You'll perform three tasks:  

- Review communications using **Microsoft 365 Copilot Chat**.  
- Prepare meeting talking points using **Copilot in Pages**.
- Draft a follow-up email using **Copilot in Outlook**.  

> **NOTE:** Sample prompts are provided to help you get started. Feel free to personalize them to suit your needs—be creative and explore! If Copilot doesn’t deliver the result you want, refine your prompt and try again. Enjoy the process and have fun experimenting!

</div>
</div>

<div class="part-card" id="part1-task-1-review-communications">
  <div class="part-header-bar blue"></div>
  <div class="part-header" onclick="togglePart('body1', this)">
    <h2>Task 1: Review communications</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body1">
<div markdown="1">

Using **Microsoft 365 Copilot Chat**, gather insights from recent interactions with a specific person about a particular topic or project. Focus on identifying key points, action items, and any outstanding questions. This ensures you stay up-to-date on team projects and can keep stakeholders informed of progress, challenges, and outcomes.  

**Steps**:

- Open a new browser tab and navigate to [M365copilot.com](https://m365copilot.com/).
- Ensure the "Work mode" tab is selected in Copilot Chat:

    ![screenshot showing Work mode tab.](../Prompts/Media/work-mode.png)

**Sample Prompt**:

</div>

<div class="prompt-box">Summarize my recent interactions with [/Name of Person] regarding [specific topic or project]. Organize the summary by key points or actions discussed, and include any follow-up items or outstanding questions that may require attention.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

<div markdown="1">

> **NOTE:** Replace [Name of Person] with the person you’re focusing on, and [specific topic or project] with the relevant topic. Use the **/** character (slash) to reference internal contacts for quick access to recent interactions.

</div>
  </div>
</div>

<div class="part-card" id="part2-task-2-prepare-for-a-meeting">
  <div class="part-header-bar green"></div>
  <div class="part-header" onclick="togglePart('body2', this)">
    <h2>Task 2: Prepare for a meeting</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body2">
<div markdown="1">

Using **Copilot in Pages**, create talking points for an upcoming stakeholder meeting based on the insights gathered in Microsoft 365 Copilot Chat. Focus on progress updates, key dates, challenges or risks, and actionable next steps to ensure a productive discussion.

**Steps**:

1. Under **Copilot Chat's response** from the previous task, select **Edit in Pages**:  
   ![screenshot showing Copilot in Pages.](../Prompts/Media/edit_in_pages.png)

2. In the new Pages screen that opens, select **View all Pages**:  
   ![screenshot showing Copilot in Pages.](../Prompts/Media/view-all-pages.png)

3. In the new Pages window, interact with Copilot by selecting the **Copilot Icon** on the right-hand side of the document.

**Sample Prompt**:

</div>

<div class="prompt-box">Using these insights, draft talking points for an upcoming stakeholder meeting. Focus on progress updates, key dates, challenges and next steps. <button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

<div markdown="1">

> **Tip:**  
> - Pages can be used as a collaborative space to work with your colleagues in real-time. Share the page by typing the "@" symbol followed by a colleague’s name.
> - After adding your colleague, click on their name to give them access. They will receive an email notification with a link to collaborate on the page.

</div>
  </div>
</div>

<div class="part-card" id="part3-task-3-send-a-follow-up-email">
  <div class="part-header-bar purple"></div>
  <div class="part-header" onclick="togglePart('body3', this)">
    <h2>Task 3: Send a follow-up email</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body3">
<div markdown="1">

Using **Copilot in Outlook**, draft a follow-up email based on the insights gathered in Microsoft 365 Copilot Chat. Include details such as progress updates, pending actions, next steps, and a request for a follow-up meeting to discuss further.

**Steps**:

- In **Outlook**, select **New Email** and then  from the ribbon select **Copilot** > **Draft with Copilot**

    ![screenshot showing Copilot in Outlook.](../Prompts/Media/copilot-outlook-desktop.png)

**Sample Prompt**:

</div>

<div class="prompt-box">Using the insights below, draft a follow-up email to [Name of Person] requesting an update on progress and next steps. Also, ask for a follow-up meeting to discuss further on the project deadline. <br><br>[Paste insights from Copilot Chat here, or add your own insights]<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
  </div>
</div>


</div><!-- /main-content -->
</div><!-- /layout -->

<script src="../../Allfiles/demo-script.js"></script>
</body>
</html>
