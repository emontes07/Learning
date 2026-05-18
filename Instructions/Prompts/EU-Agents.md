---
layout: none
---

<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Immersion Experience — Agents (Business Users) | Learning</title>
<link rel="stylesheet" href="../../Allfiles/demo-style.css">
<style>:root { --hero-from: #0D47A1; --hero-via: #1976D2; --hero-to: #42A5F5; }</style>
</head>
<body>

<div class="back-bar">
  <a href="https://emontes07.github.io/Learning/">← Back to Index</a>
</div>

<button class="sidebar-toggle" onclick="openSidebar()" aria-label="Open menu">☰ Menu</button>

<div class="hero">
  <div class="hero-inner">
    <h1>🤖 Immersion Experience — Agents (Business Users)</h1>
    <p class="subtitle">Design a simple retrieval-based agent with Copilot Studio.</p>
    <div class="hero-meta">
      <span>🤖 Agents</span>
      <span>💬 Copilot Chat</span>
      <span>🛠️ Copilot Studio</span>
    </div>
  </div>
</div>

<div class="sidebar-overlay" id="sidebarOverlay" onclick="closeSidebar()"></div>

<div class="layout">

<nav class="sidebar" id="sidebar">
  <a class="sb-home" href="https://emontes07.github.io/Learning/">← Back to Index</a>
  <div class="sb-title">Agents (Business Users)</div>

  <a href="#sec-intro" class="section-link">Overview</a>
  <a href="#part1-task-1-identify-a-productivity-challenge" class="part-link">Task 1: Identify a Productivity Challenge</a>
  <a href="#part2-task-2-explore-ai-solution-ideas-with-researcher" class="part-link">Task 2: Explore AI Solution Ideas with Researcher</a>
  <a href="#part3-task-3-build-and-test-your-agent" class="part-link">Task 3: Build and Test Your Agent</a>
</nav>

<div class="main-content">

<div class="section" id="sec-intro">
<div markdown="1">

Discover how Microsoft 365 Copilot and Copilot Studio can help you solve everyday productivity challenges by designing a simple **retrieval-based agent**. This streamlined exercise will walk you through identifying a common issue, exploring how AI could help, and then creating a simple agent to test.  

You'll perform three tasks:

- Identify a productivity pain point  
- Explore how AI could help with retrieval and organization  
- Build and test a simple agent in **Copilot Studio**  

> **NOTE:** Sample prompts are provided to help you get started—feel free to personalize them to fit your situation.  
>
> If you’d like help generating or refining prompts, try the <a href="https://appsource.microsoft.com/en-us/product/office/WA200007578" target="_blank">Prompt Coach agent</a>, which can suggest, improve, and evaluate prompts so you get better results with Copilot.

</div>
</div>

<div class="part-card" id="part1-task-1-identify-a-productivity-challenge">
  <div class="part-header-bar blue"></div>
  <div class="part-header" onclick="togglePart('body1', this)">
    <h2>Task 1: Identify a Productivity Challenge</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body1">
<div markdown="1">

Think about a common issue in your day-to-day work—something that slows you down or makes it harder to find or organize information. You can reflect individually, or use **Copilot Chat** as a partner to help generate ideas and surface common pain points.

Examples:

- Finding the latest version of a document  
- Gathering updates from multiple emails or chats  
- Remembering details from past projects or meetings  

**Steps:**  

- Open a new browser tab and navigate to [m365.cloud.microsoft/chat](https://m365.cloud.microsoft/chat). 

- Ensure the **Work mode** tab is selected in **Copilot Chat**.  

   ![Screenshot showing Work mode tab in Copilot Chat.](../Prompts/Media/work-mode.png)  

    **Sample Prompt:**

</div>

<div class="prompt-box">    Summarize the top challenges I face in my daily work, based on recent emails, chats, and documents. Show results in a simple list with: <br>    <br>    - Title (short label for the issue) <br>    - Description (1–2 sentences) <button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
  </div>
</div>

<div class="part-card" id="part2-task-2-explore-ai-solution-ideas-with-researcher">
  <div class="part-header-bar green"></div>
  <div class="part-header" onclick="togglePart('body2', this)">
    <h2>Task 2: Explore AI Solution Ideas with Researcher</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body2">
<div markdown="1">

Use the **Researcher Agent** to explore how Copilot or agents might help with your chosen challenge.

**Steps:**  

- In the Copilot Chat menu, expand **Agents** and select **Researcher**.  

   ![Screenshot showing Researcher selected in M365 Copilot menu.](../Prompts/Media/researcher.png)  

- Try a sample prompt like this:

</div>

<div class="prompt-box">   Explore possible AI solutions to help with [insert productivity issue]. Focus on retrieval-based approaches using Microsoft Copilot or Copilot Studio agents. Summarize two or three ways an agent could help me find, organize, or summarize information more efficiently.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

<div markdown="1">

> **TIP:** Keep the focus on practical, everyday use cases—like quickly surfacing a doc or pulling updates from multiple sources.
  
    > **NOTE:** Researcher may take 5–10 minutes to complete, depending on your request. Its responses are highly detailed, so while it’s working, try running the same prompt in Copilot Chat. Comparing the two outputs is a great way to see how each tool approaches the task.

</div>
  </div>
</div>

<div class="part-card" id="part3-task-3-build-and-test-your-agent">
  <div class="part-header-bar purple"></div>
  <div class="part-header" onclick="togglePart('body3', this)">
    <h2>Task 3: Build and Test Your Agent</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body3">
<div markdown="1">

Now, create a simple retrieval agent in **Copilot Studio** to address your challenge.  

**Steps:**  

1. In the **Copilot Chat** menu, select **Create agent**.

   ![Screenshot showing create an agent link.](../Prompts/Media/create-agent.png)  

1. In the **Describe** tab, draft your agent’s role. For example:

</div>

<div class="prompt-box">   You’re a virtual assistant that helps me with [key task]. Be concise and always reference my recent files or resources when possible.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

<div markdown="1">

![Screenshot showing describe agent with sample prompt filled in.](../Prompts/Media/create-agent-through-describe.png)  

1. Select the **Configure** Tab and add one knowledge source (e.g., **My Emails** or **My Teams chats and meetings**).

    ![Screenshot showing knowledge sources section in agent builder.](../Prompts/Media/knowledge-sources.png)

1. Test your agent using the **Test** pane and refine as needed.  
1. Select **Create** to publish your agent and start using it.  

> **TIP:** Even a very simple agent—like one that helps you find recent project files—can show the power of retrieval in your daily work.

</div>
  </div>
</div>


</div><!-- /main-content -->
</div><!-- /layout -->

<script src="../../Allfiles/demo-script.js"></script>
</body>
</html>
