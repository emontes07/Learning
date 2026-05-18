---
layout: none
---

<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Immersion Experience — Finance | Learning</title>
<link rel="stylesheet" href="../../Allfiles/demo-style.css">
<style>:root { --hero-from: #1B5E20; --hero-via: #2E7D32; --hero-to: #43A047; }</style>
</head>
<body>

<div class="back-bar">
  <a href="https://emontes07.github.io/Learning/">← Back to Index</a>
</div>

<button class="sidebar-toggle" onclick="openSidebar()" aria-label="Open menu">☰ Menu</button>

<div class="hero">
  <div class="hero-inner">
    <h1>💰 Immersion Experience — Finance</h1>
    <p class="subtitle">Collect data, evaluate trends, and draft financial analyses.</p>
    <div class="hero-meta">
      <span>💰 Finance</span>
      <span>💬 Copilot Chat</span>
      <span>📊 Excel</span>
      <span>📝 Word</span>
    </div>
  </div>
</div>

<div class="sidebar-overlay" id="sidebarOverlay" onclick="closeSidebar()"></div>

<div class="layout">

<nav class="sidebar" id="sidebar">
  <a class="sb-home" href="https://emontes07.github.io/Learning/">← Back to Index</a>
  <div class="sb-title">Finance</div>

  <a href="#sec-intro" class="section-link">Overview</a>
  <a href="#part1-task-1-collect-financial-data" class="part-link">Task 1: Collect Financial Data</a>
  <a href="#part2-task-2-evaluate-financial-impacts-and-trends" class="part-link">Task 2: Evaluate Financial Impacts and Trends</a>
  <a href="#part3-task-3-draft-a-financial-analysis-document" class="part-link">Task 3: Draft a Financial Analysis Document</a>
</nav>

<div class="main-content">

<div class="section" id="sec-intro">
<div markdown="1">

Improve financial decision-making by using Microsoft 365 Copilot to collect, analyze, and document key financial insights.

You'll perform three tasks:  

- Collect financial data using **Copilot Chat**.  
- Evaluate financial impacts and trends using **Copilot Chat**.  
- Draft a financial analysis document using **Copilot in Word**.  

> **NOTE:** Sample prompts are provided to help you get started. Feel free to personalize them to suit your needs—be creative and explore! If Copilot doesn’t deliver the result you want, refine your prompt and try again. Enjoy the process and have fun experimenting!

</div>
</div>

<div class="part-card" id="part1-task-1-collect-financial-data">
  <div class="part-header-bar blue"></div>
  <div class="part-header" onclick="togglePart('body1', this)">
    <h2>Task 1: Collect Financial Data</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body1">
<div markdown="1">

Using **Microsoft 365 Copilot Chat**, gather relevant financial data, including market trends, revenue insights, and cost structures for a company or industry of your choice. This information helps establish a solid foundation for financial analysis, ensuring you have accurate data points to assess business performance.

**Steps**:

- Open a new browser tab and navigate to [M365copilot.com](https://m365copilot.com/).
- Ensure the **"Web mode"** tab is selected in **Copilot Chat**:

    ![screenshot showing Work mode tab.](../Prompts/Media/web-mode.png)

**Sample Prompt**:

</div>

<div class="prompt-box">Summarize key financial indicators for [company/industry] over the last year, including revenue growth, cost trends, and market conditions.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

<div markdown="1">

> **NOTE:** Replace [company/industry] with a specific entity you want to analyze. Use the **/** character (slash) to reference internal company data where applicable.

</div>
  </div>
</div>

<div class="part-card" id="part2-task-2-evaluate-financial-impacts-and-trends">
  <div class="part-header-bar green"></div>
  <div class="part-header" onclick="togglePart('body2', this)">
    <h2>Task 2: Evaluate Financial Impacts and Trends</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body2">
<div markdown="1">

Using **Microsoft 365 Copilot Chat**, evaluate the financial data you’ve collected to identify trends, risks, and opportunities. Analyze cost fluctuations, revenue growth patterns, and other key indicators to extract meaningful insights that can inform decision-making.

**Sample Prompt**:

</div>

<div class="prompt-box">Based on recent financial performance, identify key trends, risks, and opportunities for [company/industry]. Provide insights on cost fluctuations and revenue projections.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

<div markdown="1">

> **TIP 1:** If you need a deeper analysis, ask Copilot to compare trends across multiple periods or companies.

> **TIP 2:**  
>
> - Ask Copilot to export the response to a Word document to save for the next task. Save the document to your OneDrive and copy the shared URL.
> - To copy the link, open the saved Word document and select **Share** > **Copy Link**, as shown below:  
> ![Share link.](../Demos/Media/share-menu-with-copy-link-9fd1c60a.png)

</div>
  </div>
</div>

<div class="part-card" id="part3-task-3-draft-a-financial-analysis-document">
  <div class="part-header-bar purple"></div>
  <div class="part-header" onclick="togglePart('body3', this)">
    <h2>Task 3: Draft a Financial Analysis Document</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body3">
<div markdown="1">

Using **Copilot in Word**, create a structured financial analysis document that summarizes your key findings, trends, and strategic recommendations. Ensure the document presents clear takeaways, helping stakeholders quickly understand the financial outlook and implications.

**Steps**:

- Launch Microsoft Word from your browser ([word.new](https://word.new)) or use the desktop application.
- Enter your prompt where it says **"Describe what you'd like to write"**.

    ![screenshot showing Copilot in Word.](../Prompts/Media/draft-with-copilot.png)

**Sample Prompt**:

</div>

<div class="prompt-box">Draft a financial analysis report on [company/industry], summarizing key revenue trends, cost analysis, profitability insights, and future financial projections. Use the insights from the linked document to structure the report logically.<br><br>[Paste link to shared Word document from Task 2 here]<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

<div markdown="1">

> **Tip:** Before selecting **Keep it**, ask Copilot to refine your document by expanding on a topic or adjusting the tone for clarity.

</div>
  </div>
</div>


</div><!-- /main-content -->
</div><!-- /layout -->

<script src="../../Allfiles/demo-script.js"></script>
</body>
</html>
