---
layout: none
---

<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Immersion Experience — Executive Assistant | Learning</title>
<link rel="stylesheet" href="../../Allfiles/demo-style.css">
<style>:root { --hero-from: #4A148C; --hero-via: #6A1B9A; --hero-to: #8E24AA; }</style>
</head>
<body>

<div class="back-bar">
  <a href="https://emontes07.github.io/Learning/">← Back to Index</a>
</div>

<button class="sidebar-toggle" onclick="openSidebar()" aria-label="Open menu">☰ Menu</button>

<div class="hero">
  <div class="hero-inner">
    <h1>📅 Immersion Experience — Executive Assistant</h1>
    <p class="subtitle">Manage calendars, communications, and executive priorities with ease.</p>
    <div class="hero-meta">
      <span>📅 EA</span>
      <span>💬 Copilot Chat</span>
      <span>📧 Outlook</span>
    </div>
  </div>
</div>

<div class="sidebar-overlay" id="sidebarOverlay" onclick="closeSidebar()"></div>

<div class="layout">

<nav class="sidebar" id="sidebar">
  <a class="sb-home" href="https://emontes07.github.io/Learning/">← Back to Index</a>
  <div class="sb-title">Executive Assistant</div>

  <a href="#sec-intro" class="section-link">Overview</a>
  <a href="#part1-task-1-summarize-communications" class="part-link">Task 1: Summarize communications</a>
  <a href="#part2-task-2-prepare-for-your-day" class="part-link">Task 2: Prepare for your day</a>
  <a href="#part3-task-3-draft-a-follow-up-email" class="part-link">Task 3: Draft a follow-up email</a>
</nav>

<div class="main-content">

<div class="section" id="sec-intro">
<div markdown="1">

Optimize daily tasks by summarizing communications, preparing for your day, and sending a follow-up email.  

You'll perform three tasks:  

- Summarize communications using **Microsoft 365 Copilot Chat**.  
- Plan your day using **Microsoft 365 Copilot Chat**.  
- Draft a follow-up email using **Copilot in Outlook**.  

> **NOTE:** Sample prompts are provided to help you get started. Feel free to personalize them to suit your needs—be creative and explore! If Copilot doesn’t deliver the result you want, refine your prompt and try again. Enjoy the process and have fun experimenting!

</div>
</div>

<div class="part-card" id="part1-task-1-summarize-communications">
  <div class="part-header-bar blue"></div>
  <div class="part-header" onclick="togglePart('body1', this)">
    <h2>Task 1: Summarize communications</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body1">
<div markdown="1">

Using **Microsoft 365 Copilot Chat**, catch up on emails, chats, and meetings from specific leaders and stakeholders. Focus on identifying key discussions, action items, and updates to ensure you're fully informed and ready to respond.  

**Steps**:

- Open a new browser tab and navigate to [M365copilot.com](https://m365copilot.com/).
- Ensure the "Work mode" tab is selected in Copilot Chat:

    ![screenshot showing Work mode tab.](../Prompts/Media/work-mode.png)

**Sample Prompt**:

</div>

<div class="prompt-box">Summarize all email, meetings and chats from [/name of person] over the last 7 days and list any action items I may have from these interactions.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

<div markdown="1">

> **NOTE:** Replace [Name of Person] with the person you’re focusing on. Use the **/** character (slash) to reference internal contacts for quick access to recent interactions.

</div>
  </div>
</div>

<div class="part-card" id="part2-task-2-prepare-for-your-day">
  <div class="part-header-bar green"></div>
  <div class="part-header" onclick="togglePart('body2', this)">
    <h2>Task 2: Prepare for your day</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body2">
<div markdown="1">

Using **Microsoft 365 Copilot Chat**, plan your day and review upcoming meetings. Create a to-do list or categorize your meetings to ensure they align with your priorities. Focus on organizing your schedule to stay prepared and productive.  

**Sample Prompt**:

</div>

<div class="prompt-box">Help me plan for my day and any upcoming meetings I may have today. <button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
  </div>
</div>

<div class="part-card" id="part3-task-3-draft-a-follow-up-email">
  <div class="part-header-bar purple"></div>
  <div class="part-header" onclick="togglePart('body3', this)">
    <h2>Task 3: Draft a follow-up email</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body3">
<div markdown="1">

Using Copilot in Outlook, draft an email requesting updates or additional information on a recent topic or discussion. Provide any context needed to ensure clarity and alignment.

**Steps**:

- In **Outlook**, select **New Email** and then  from the ribbon select **Copilot** > **Draft with Copilot**

    ![screenshot showing Copilot in Outlook.](../Prompts/Media/copilot-outlook-desktop.png)

**Sample Prompt**:

</div>

<div class="prompt-box">Draft an email to [Name of Person] requesting an update on [specific topic or project]. Include a brief summary of the context:  <br><br>[Insert a one- to two-sentence summary or details here.]<br><button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
  </div>
</div>


</div><!-- /main-content -->
</div><!-- /layout -->

<script src="../../Allfiles/demo-script.js"></script>
</body>
</html>
