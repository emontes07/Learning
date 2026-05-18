---
layout: none
---

<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Immersion Experience — Agents (Executives) | Learning</title>
<link rel="stylesheet" href="../../Allfiles/demo-style.css">
<style>:root { --hero-from: #311B92; --hero-via: #4527A0; --hero-to: #5E35B1; }</style>
</head>
<body>

<div class="back-bar">
  <a href="https://emontes07.github.io/Learning/">← Back to Index</a>
</div>

<button class="sidebar-toggle" onclick="openSidebar()" aria-label="Open menu">☰ Menu</button>

<div class="hero">
  <div class="hero-inner">
    <h1>🤖 Immersion Experience — Agents (Executives)</h1>
    <p class="subtitle">Design an executive-level retrieval agent in Copilot Studio.</p>
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
  <div class="sb-title">Agents (Executives)</div>

  <a href="#sec-intro" class="section-link">Overview</a>
  <a href="#part1-task-1-identify-a-work-related-challenge" class="part-link">Task 1: Identify a Work-Related Challenge</a>
  <a href="#part2-task-2-break-down-the-problem" class="part-link">Task 2: Break Down the Problem</a>
  <a href="#part3-task-3-explore-ai-solution-ideas-with-researcher" class="part-link">Task 3: Explore AI Solution Ideas with Researcher</a>
  <a href="#part4-task-4-conceptualize-your-agent" class="part-link">Task 4: Conceptualize Your Agent</a>
</nav>

<div class="main-content">

<div class="section" id="sec-intro">
<div markdown="1">

Explore how Microsoft 365 Copilot and Copilot Studio can help you address a real work-related challenge by designing a simple **retrieval-based agent**. This exercise will walk you through identifying an issue, breaking it down, exploring where AI might help, and then creating a conceptual agent to solve it.  

You'll perform four tasks:

- Identify a work-related issue  
- Break down the problem and explore where AI could help  
- Use **Researcher** to uncover insights and solution ideas  
- Conceptualize and mock up a retrieval-based agent in **Copilot Studio**  

> **NOTE:** Sample prompts are provided to help you get started—feel free to personalize them to fit your situation. 
>
> If you’d like help generating or refining prompts, try the <a href="https://appsource.microsoft.com/en-us/product/office/WA200007578" target="_blank">Prompt Coach agent</a><br>, which can suggest, improve, and evaluate prompts so you get better results with Copilot.

</div>
</div>

<div class="part-card" id="part1-task-1-identify-a-work-related-challenge">
  <div class="part-header-bar blue"></div>
  <div class="part-header" onclick="togglePart('body1', this)">
    <h2>Task 1: Identify a Work-Related Challenge</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body1">
<div markdown="1">

Start by thinking about a real issue you encounter in your role—something that slows you down or makes information harder to access. You can reflect individually, or use **Copilot Chat** as a partner to help generate ideas and identify a challenge where retrieving and organizing knowledge would make a difference.  

To guide your thinking, consider:  

- **What’s working well today**  
- **What’s not working well**  
- **Where AI *might* be able to help**  

**Steps:**  

- Open a new browser tab and navigate to [m365.cloud.microsoft/chat](https://m365.cloud.microsoft/chat).  
- Ensure the **Work mode** tab is selected in **Copilot Chat**:  

   ![Screenshot showing Work mode tab in Copilot Chat.](../Prompts/Media/work-mode.png)  

    **Sample Prompt:**

</div>

<div class="prompt-box">   I’m researching common day-to-day issues I face at work, such as processes, collaboration, or time management. Look at recent conversations from [Teams chats, Outlook emails, or other collaboration tools] related to [your role focus]. Summarize the key issues or pain points mentioned in the last 6 months. Show the results in a table with:  <br><br>    - Title: Short label for the issue  <br>    - Description: Brief summary of the challenge  <br>    - Frequency: How often it comes up (e.g., number of mentions)<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
  </div>
</div>

<div class="part-card" id="part2-task-2-break-down-the-problem">
  <div class="part-header-bar green"></div>
  <div class="part-header" onclick="togglePart('body2', this)">
    <h2>Task 2: Break Down the Problem</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body2">
<div markdown="1">

Using **Copilot Chat**, take the challenge you identified in Task 1 and break it into smaller parts:

- What makes this issue difficult?  
- Where does information get stuck or lost?  
- Who is impacted most?  

    **Sample Prompt (Copilot Chat – Work Mode):**

</div>

<div class="prompt-box">    Break down the problem of [insert challenge]. Identify root causes, pain points, and which areas of work are most affected.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

<div markdown="1">

> **TIP:** Think about where retrieval of knowledge would save you time or help your team make faster decisions.

</div>
  </div>
</div>

<div class="part-card" id="part3-task-3-explore-ai-solution-ideas-with-researcher">
  <div class="part-header-bar purple"></div>
  <div class="part-header" onclick="togglePart('body3', this)">
    <h2>Task 3: Explore AI Solution Ideas with Researcher</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body3">
<div markdown="1">

Use the **Researcher Agent** to see how Copilot and agents could help. Focus on solutions that retrieve, organize, or summarize knowledge—not automate tasks. 

**Steps:**

- Open a new browser tab and navigate to [m365.cloud.microsoft/chat](https://m365.cloud.microsoft/chat).
- In the Copilot Chat menu, expand **Agents** and select **Researcher**  

    ![Screenshot showing Researcher selected in M365 Copilot menu.](../Prompts/Media/researcher.png)  

    **Sample Prompt (Researcher Agent):**

</div>

<div class="prompt-box">    Explore possible AI solutions to address [insert problem]. Focus on retrieval-based approaches using Microsoft Copilot, Copilot Studio agents, or connected knowledge sources. Summarize three possible solution approaches, their benefits, and limitations.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

<div markdown="1">

> **TIP:** Look for opportunities where an agent could make knowledge easier to find, reuse, or share.

    > **NOTE:** Researcher may take 5–10 minutes to complete, depending on your request. Its responses are highly detailed, so while it’s working, try running the same prompt in Copilot Chat. Comparing the two outputs is a great way to see how each tool approaches the task.

</div>
  </div>
</div>

<div class="part-card" id="part4-task-4-conceptualize-your-agent">
  <div class="part-header-bar orange"></div>
  <div class="part-header" onclick="togglePart('body4', this)">
    <h2>Task 4: Conceptualize Your Agent</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body4">
<div markdown="1">

Now, take your insights and create a simple mock agent in **Copilot Studio**. Keep the focus on retrieval—your agent should help surface, organize, or summarize information.

**Steps:**

- **Start in Copilot Studio**

    1. Open your browser and navigate to [m365.cloud.microsoft/chat](https://m365.cloud.microsoft/chat).
    1. Select **Create agent** in the right-hand rail to launch **Copilot Studio**.

        ![Screenshot showing create an agent link.](../Prompts/Media/create-agent.png)

- **Define your Agent (Describe tab or Configure tab)**

    1. Choose the **Describe** tab and use this sample prompt (or write your own):

</div>

<div class="prompt-box">        You’re a virtual assistant for our [project/team name]. Your role is to help with [key tasks]. Be concise, stay on-brand, and reference our shared resources when possible.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

<div markdown="1">

![Screenshot showing describe agent with sample prompt filled in.](../Prompts/Media/create-agent-through-describe.png)

        > **NOTE:** You can start from scratch or base your agent on a template, which pre-populates settings and instructions you can later customize.

    1. If **Describe** isn’t available, switch to the **Configure** tab and enter the same details manually: name, description, and agent instructions.

        ![Screenshot showing configure agent.](../Prompts/Media/name-describe-agent.png)

- **Customize your Agent**

    In the **Configure** tab, explore these options:

    1. Add at least one knowledge source (e.g., a document saved to OneDrive/SharePoint or Your emails).

        ![Screenshot showing knowledge sources section in agent builder.](../Prompts/Media/knowledge-sources.png)

    1. Define starter prompts to help others get started with your agent

        ![Screenshot showing starter prompts section in agent builder.](../Prompts/Media/starter-prompts.png)

        > **TIP:** Starter prompts help guide users on how to interact with your agent.

- **Test and Create**

    1. Use the **Test** feature (available in the right pane throughout the agent-building process) to try out your draft agent and refine any issues.
    2. Once satisfied, select **Create** to publish the agent.
    3. Share your agent with others or open it for immediate use.  

> **TIP:** The goal isn’t to build a perfect agent today—it’s to explore how retrieval-focused agents can make knowledge easier to access in your daily work.

</div>
  </div>
</div>


</div><!-- /main-content -->
</div><!-- /layout -->

<script src="../../Allfiles/demo-script.js"></script>
</body>
</html>
