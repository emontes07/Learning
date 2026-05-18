---
layout: none
---

<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Immersion Experience — IT | Learning</title>
<link rel="stylesheet" href="../../Allfiles/demo-style.css">
<style>:root { --hero-from: #01579B; --hero-via: #0277BD; --hero-to: #0288D1; }</style>
</head>
<body>

<div class="back-bar">
  <a href="https://emontes07.github.io/Learning/">← Back to Index</a>
</div>

<button class="sidebar-toggle" onclick="openSidebar()" aria-label="Open menu">☰ Menu</button>

<div class="hero">
  <div class="hero-inner">
    <h1>💻 Immersion Experience — IT</h1>
    <p class="subtitle">Speed up tickets, docs, and infrastructure planning with Copilot.</p>
    <div class="hero-meta">
      <span>💻 IT</span>
      <span>💬 Copilot Chat</span>
      <span>📝 Word</span>
    </div>
  </div>
</div>

<div class="sidebar-overlay" id="sidebarOverlay" onclick="closeSidebar()"></div>

<div class="layout">

<nav class="sidebar" id="sidebar">
  <a class="sb-home" href="https://emontes07.github.io/Learning/">← Back to Index</a>
  <div class="sb-title">IT</div>

  <a href="#sec-intro" class="section-link">Overview</a>
  <a href="#part1-task-1-research-upcoming-features" class="part-link">Task 1: Research upcoming features</a>
  <a href="#part2-task-2-draft-an-announcement" class="part-link">Task 2: Draft an announcement</a>
  <a href="#part3-task-3-create-a-survey" class="part-link">Task 3: Create a survey</a>
</nav>

<div class="main-content">

<div class="section" id="sec-intro">
<div markdown="1">

Drive tech engagement and user satisfaction by researching upcoming product or service features, sharing updates, and collecting feedback.  

You'll perform three tasks:  

- Research upcoming features using **Microsoft 365 Copilot Chat**.  
- Draft an announcement using **Copilot in Word**.  
- Create a survey using **Copilot in Forms**.  

> **NOTE:** Sample prompts are provided to help you get started. Feel free to personalize them to suit your needs—be creative and explore! If Copilot doesn’t deliver the result you want, refine your prompt and try again. Enjoy the process and have fun experimenting!

</div>
</div>

<div class="part-card" id="part1-task-1-research-upcoming-features">
  <div class="part-header-bar blue"></div>
  <div class="part-header" onclick="togglePart('body1', this)">
    <h2>Task 1: Research upcoming features</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body1">
<div markdown="1">

Using **Microsoft 365 Copilot Chat**, research the upcoming features of a product or service of your choice. Focus on identifying updates that align with your organization’s goals and address key business needs.  

**Steps**:

- Open a new browser tab and navigate to [M365copilot.com](https://m365copilot.com/)
- Ensure the "web mode" tab is selected in Copilot Chat:

    ![screenshot showing web mode tab.](../Prompts/Media/web-mode.png)

**Sample Prompt**:

</div>

<div class="prompt-box">Pull a list of [Microsoft 365] features releasing in the next 90 days<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

<div markdown="1">

> **NOTE:** Replace [Microsoft 365] with the product or service you're focusing on.

</div>
  </div>
</div>

<div class="part-card" id="part2-task-2-draft-an-announcement">
  <div class="part-header-bar green"></div>
  <div class="part-header" onclick="togglePart('body2', this)">
    <h2>Task 2: Draft an announcement</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body2">
<div markdown="1">

Using **Copilot in Word**, draft an engaging announcement for end users about new features in the product or service of your choice. Highlight the key benefits, practical uses, and how these features may simplify everyday tasks.  

**Steps**:

- Launch Microsoft Word from your browser ([word.new](https://word.new)) or use the desktop application.
- Enter your prompt where it says **"Describe what you'd like to write"**.

    ![screenshot showing Copilot in Word.](../Prompts/Media/draft-with-copilot.png)

**Sample Prompt**:

</div>

<div class="prompt-box">Draft a post about the upcoming features in [Microsoft 365: (list of features)]. Describe the benefits to help drive adoption. <button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

<div markdown="1">

> **NOTE:** Replace [Microsoft 365: (list of features)] with the specific product & features you're focusing on.

</div>
  </div>
</div>

<div class="part-card" id="part3-task-3-create-a-survey">
  <div class="part-header-bar purple"></div>
  <div class="part-header" onclick="togglePart('body3', this)">
    <h2>Task 3: Create a survey</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body3">
<div markdown="1">

Using **Copilot in Forms**, create a survey to collect user feedback about their experiences with the product or service. Include questions about satisfaction, usability, and any potential pain points.  

**Steps**:

- Open a new browser tab and navigate to [forms.office.com]https://forms.office.com/
- Select **New form** in the top left hand corner of the screen.

**Sample Prompt**:

</div>

<div class="prompt-box">Create a survey to capture feedback from users in my organization to understand their experience and satisfaction with [Microsoft 365] products and services.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

<div markdown="1">

> **NOTE:** Replace [Microsoft 365] with the product or service you're focusing on.

</div>
  </div>
</div>


</div><!-- /main-content -->
</div><!-- /layout -->

<script src="../../Allfiles/demo-script.js"></script>
</body>
</html>
