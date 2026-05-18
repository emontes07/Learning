---
layout: none
---

<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Immersion Experience — HR | Learning</title>
<link rel="stylesheet" href="../../Allfiles/demo-style.css">
<style>:root { --hero-from: #00695C; --hero-via: #00897B; --hero-to: #26A69A; }</style>
</head>
<body>

<div class="back-bar">
  <a href="https://emontes07.github.io/Learning/">← Back to Index</a>
</div>

<button class="sidebar-toggle" onclick="openSidebar()" aria-label="Open menu">☰ Menu</button>

<div class="hero">
  <div class="hero-inner">
    <h1>👥 Immersion Experience — HR</h1>
    <p class="subtitle">Streamline recruiting with research, role templates, and interview guides.</p>
    <div class="hero-meta">
      <span>👥 HR</span>
      <span>💬 Copilot Chat</span>
      <span>📝 Word</span>
    </div>
  </div>
</div>

<div class="sidebar-overlay" id="sidebarOverlay" onclick="closeSidebar()"></div>

<div class="layout">

<nav class="sidebar" id="sidebar">
  <a class="sb-home" href="https://emontes07.github.io/Learning/">← Back to Index</a>
  <div class="sb-title">HR</div>

  <a href="#sec-intro" class="section-link">Overview</a>
  <a href="#part1-task-1-research-market-trends" class="part-link">Task 1: Research market trends</a>
  <a href="#part2-task-2-create-a-role-templateoutline" class="part-link">Task 2: Create a role template/outline</a>
  <a href="#part3-task-3-design-an-interview-guide" class="part-link">Task 3: Design an interview guide</a>
</nav>

<div class="main-content">

<div class="section" id="sec-intro">
<div markdown="1">

Streamline your recruiting process by researching industry trends, creating a standardized role template, and designing a reusable interview guide to attract and evaluate top talent.

You'll perform three tasks:

- Research market trends using  **Copilot Chat**
- Create a role template/outline using **Copilot Chat**
- Design an interview guide using **Copilot in Word**

> **NOTE:** Sample prompts are provided to help you get started. Feel free to personalize them to suit your needs—be creative and explore! If Copilot doesn’t deliver the result you want, refine your prompt and try again. Enjoy the process and have fun experimenting!

</div>
</div>

<div class="part-card" id="part1-task-1-research-market-trends">
  <div class="part-header-bar blue"></div>
  <div class="part-header" onclick="togglePart('body1', this)">
    <h2>Task 1: Research market trends</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body1">
<div markdown="1">

Using **Copilot Chat**, research the latest trends and data on competitive job descriptions for your chosen role. Focus on identifying key skills, qualifications, and industry-specific needs to ensure your hiring process aligns with current market demands.

**Steps**:

- Open a new browser tab and navigate to [M365copilot.com](https://m365copilot.com/)
- Ensure the "web mode" tab is selected in Copilot Chat:

    ![screenshot showing web mode tab.](../Prompts/Media/web-mode.png)

**Sample Prompt**:

</div>

<div class="prompt-box">Generate a table of key skills and experience required for [software engineers] at a large enterprise technology company based on market trends and leading technology companies.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

<div markdown="1">

> **NOTE:** Replace [software engineers] with the specific role you're focusing on.

</div>
  </div>
</div>

<div class="part-card" id="part2-task-2-create-a-role-templateoutline">
  <div class="part-header-bar green"></div>
  <div class="part-header" onclick="togglePart('body2', this)">
    <h2>Task 2: Create a role template/outline</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body2">
<div markdown="1">

Using **Copilot Chat**, create a standardized job description template for the role based on the insights from Task 1. This template should include key sections like responsibilities, qualifications, and company values, ensuring consistency and efficiency in future hiring efforts.

**Sample Prompt**:

</div>

<div class="prompt-box">Using the insights from Task 1, create a job description template for [software engineers]. Include sections for responsibilities, qualifications, and a description of the company’s mission and culture.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

<div markdown="1">

> **NOTE:** Replace [software engineers] with the role you're focusing on. This template will serve as a reusable framework for future job postings.

> **TIP**  
>
> - Ask Copilot to export the response to a Word document to save the template for future use. Save the document to your OneDrive and copy the shared URL.
> - To copy the link, open the saved Word document and select **Share** > **Copy Link**, as shown below:  
> ![Share link.](../Demos/Media/share-menu-with-copy-link-9fd1c60a.png)

</div>
  </div>
</div>

<div class="part-card" id="part3-task-3-design-an-interview-guide">
  <div class="part-header-bar purple"></div>
  <div class="part-header" onclick="togglePart('body3', this)">
    <h2>Task 3: Design an interview guide</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body3">
<div markdown="1">

Using **Copilot in Word**, develop a reusable interview guide tailored to the role. Include structured questions to evaluate technical and behavioral competencies, as well as a scoring rubric to ensure consistent assessments across candidates.

**Steps**:

- Launch Microsoft Word from your browser ([word.new](https://word.new)) or use the desktop application.
- Enter your prompt where it says **"Describe what you'd like to write"**.

    ![screenshot showing Copilot in Word.](../Prompts/Media/draft-with-copilot.png)

**Sample Prompt**:

</div>

<div class="prompt-box">Create an interview guide for [software engineers] that includes technical and behavioral questions, plus a scoring rubric to evaluate candidates consistently.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

<div markdown="1">

> **NOTE:** Replace [software engineers] with the role you're focusing on. This guide will help streamline the candidate evaluation process and ensure fairness.

> **TIP** Paste the shared document link you saved in Task 2 into your prompt to ensure it aligns with the role template. Alternatively, type "/" in Copilot to quickly reference and insert relevant files from OneDrive.

</div>
  </div>
</div>


</div><!-- /main-content -->
</div><!-- /layout -->

<script src="../../Allfiles/demo-script.js"></script>
</body>
</html>
