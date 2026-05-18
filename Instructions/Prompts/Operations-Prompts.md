---
layout: none
---

<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Immersion Experience — Operations | Learning</title>
<link rel="stylesheet" href="../../Allfiles/demo-style.css">
<style>:root { --hero-from: #004D40; --hero-via: #00695C; --hero-to: #00796B; }</style>
</head>
<body>

<div class="back-bar">
  <a href="https://emontes07.github.io/Learning/">← Back to Index</a>
</div>

<button class="sidebar-toggle" onclick="openSidebar()" aria-label="Open menu">☰ Menu</button>

<div class="hero">
  <div class="hero-inner">
    <h1>⚙️ Immersion Experience — Operations</h1>
    <p class="subtitle">Analyze processes, improve efficiency, and document procedures.</p>
    <div class="hero-meta">
      <span>⚙️ Operations</span>
      <span>💬 Copilot Chat</span>
      <span>📊 Excel</span>
    </div>
  </div>
</div>

<div class="sidebar-overlay" id="sidebarOverlay" onclick="closeSidebar()"></div>

<div class="layout">

<nav class="sidebar" id="sidebar">
  <a class="sb-home" href="https://emontes07.github.io/Learning/">← Back to Index</a>
  <div class="sb-title">Operations</div>

  <a href="#sec-intro" class="section-link">Overview</a>
  <a href="#part1-task-1-research-supplier-options" class="part-link">Task 1: Research supplier options</a>
  <a href="#part2-task-2-develop-a-supplier-transition-plan" class="part-link">Task 2: Develop a supplier transition plan</a>
  <a href="#part3-task-3-communicate-the-supplier-change" class="part-link">Task 3: Communicate the supplier change</a>
</nav>

<div class="main-content">

<div class="section" id="sec-intro">
<div markdown="1">

Draft a supplier transition plan by assessing potential vendors and outlining the transition process.

You'll perform three tasks:  

- Research supplier options using **Microsoft 365 Copilot Chat**.  
- Develop a supplier transition plan using **Copilot in Word**.  
- Communicate the supplier change using **Copilot in Outlook**.  

> **NOTE:** Sample prompts are provided to help you get started. Feel free to personalize them to suit your needs—be creative and explore! If Copilot doesn’t deliver the result you want, refine your prompt and try again. Enjoy the process and have fun experimenting!

</div>
</div>

<div class="part-card" id="part1-task-1-research-supplier-options">
  <div class="part-header-bar blue"></div>
  <div class="part-header" onclick="togglePart('body1', this)">
    <h2>Task 1: Research supplier options</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body1">
<div markdown="1">

Using **Microsoft 365 Copilot Chat**, research and compare potential suppliers for a specific product or service. Identify key decision factors such as cost, reliability, service level agreements (SLAs), and scalability.  

**Steps**:

- Open a new browser tab and navigate to [M365copilot.com](https://m365copilot.com/).
- Ensure the "web mode" tab is selected in Copilot Chat:

    ![screenshot showing web mode tab.](../Prompts/Media/web-mode.png)

**Sample Prompt**:

</div>

<div class="prompt-box">Compare three leading suppliers for [product/service] in [select your industry]. Provide a summary of pricing, contract flexibility, service reliability, and customer support quality.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

<div markdown="1">

> **NOTE:** Replace [product/service] with the item or service you are evaluating for your supplier transition. Replace [select your industry] with the relevant industry, such as healthcare, manufacturing, or retail.  

> **TIP**  
>
> - Ask Copilot to export the response to a Word document to save for the next task. Save the document to your OneDrive and copy the shared URL.
> - To copy the link, open the saved Word document and select **Share** > **Copy Link**, as shown below:  
> ![Share link.](../Demos/Media/share-menu-with-copy-link-9fd1c60a.png)

</div>
  </div>
</div>

<div class="part-card" id="part2-task-2-develop-a-supplier-transition-plan">
  <div class="part-header-bar green"></div>
  <div class="part-header" onclick="togglePart('body2', this)">
    <h2>Task 2: Develop a supplier transition plan</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body2">
<div markdown="1">

Using **Copilot in Word**, draft a structured plan outlining the supplier transition process, expected benefits, and key risks. Ensure the plan includes justifications for the switch, a transition timeline, and stakeholder considerations.  

- Launch Microsoft Word from your browser ([word.new](https://word.new)) or use the desktop application.
- Enter your prompt where it says **"Describe what you'd like to write"**.

    ![screenshot showing Copilot in Word.](../Prompts/Media/draft-with-copilot.png)

**Sample Prompt**:

</div>

<div class="prompt-box">Based on the supplier research from [Paste in shared Word document link from Task 1], draft a Supplier Transition Plan outlining why [Company] is switching to [Supplier X]. Include key benefits, a transition timeline, and potential risks.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

<div markdown="1">

> **NOTE:** Replace [Company] with your organization and [Supplier X] with the selected supplier. Adjust the details to fit the business need.

> **TIP** Ask Copilot in Word to summarize the transition plan into 3-4 key points for use in an email update.

</div>
  </div>
</div>

<div class="part-card" id="part3-task-3-communicate-the-supplier-change">
  <div class="part-header-bar purple"></div>
  <div class="part-header" onclick="togglePart('body3', this)">
    <h2>Task 3: Communicate the supplier change</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body3">
<div markdown="1">

Using **Copilot in Outlook**, draft an email announcing the proposed supplier transition to your team. Clearly explain the reasoning, expected benefits, and any action steps needed for a smooth transition.  

**Steps**:

- In **Outlook**, select **New Email** and then  from the ribbon select **Copilot** > **Draft with Copilot**

    ![screenshot showing Copilot in Outlook.](../Prompts/Media/copilot-outlook-desktop.png)

**Sample Prompt**:

</div>

<div class="prompt-box">Write an internal email to my team announcing a potential supplier transition to [Supplier X] using the key points below:<br><br>[Summarized key points from the Supplier Transition Plan]<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

<div markdown="1">

> **NOTE:** Replace [Supplier X] with the chosen supplier and tailor the message for your internal audience.

</div>
  </div>
</div>


</div><!-- /main-content -->
</div><!-- /layout -->

<script src="../../Allfiles/demo-script.js"></script>
</body>
</html>
