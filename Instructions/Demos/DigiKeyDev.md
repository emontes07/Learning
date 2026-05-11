---
demo:
    title: 'DigiKey — Developer & IT Copilot Training'
layout: none
---

<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>DigiKey — Developer & IT Copilot Training | Learning</title>
<link rel="stylesheet" href="../../Allfiles/demo-style.css">
<style>:root { --hero-from: #1B5E20; --hero-via: #2E7D32; --hero-to: #00ACC1; }</style>
</head>
<body>

<div class="back-bar">
  <a href="https://emontes07.github.io/Learning/">← Back to Index</a>
</div>

<div class="hero">
  <div class="hero-inner">
    <h1>Copilot for Developers & IT Teams</h1>
    <p class="subtitle">Twelve hands-on scenarios for engineering and IT professionals</p>
    <div class="scenario">
      <strong>Overview:</strong> Microsoft 365 Copilot is more than a writing aid — it's a multifaceted assistant that helps engineering and IT teams code faster, summarize complex information, generate documentation, research new technologies, automate repetitive tasks, and stay organized.
    </div>
    <div class="hero-meta">
      <span>💻 Developer</span>
      <span>🛠️ IT Operations</span>
      <span>🤖 Automation</span>
      <span>📚 Documentation</span>
    </div>
  </div>
</div>

<div class="sidebar-overlay" id="sidebarOverlay" onclick="closeSidebar()"></div>

<div class="layout">

<nav class="sidebar" id="sidebar">
  <a class="sb-home" href="https://emontes07.github.io/Learning/">← Back to Index</a>
  <div class="sb-title">Developer & IT Training</div>

  <a href="#sec-intro" class="section-link">Introduction</a>

  <a href="#part1" class="part-link">Task 1: Write & Review Code with Copilot</a>
  <a href="#part2" class="part-link">Task 2: Summarize & Understand Large Documentation Sets</a>
  <a href="#part3" class="part-link">Task 3: Research New Technologies with Copilot’s Research </a>
  <a href="#part4" class="part-link">Task 4: Accelerate Standups & Sprint Reviews with Loop + C</a>
  <a href="#part5" class="part-link">Task 5: Convert Meetings into Actionable Engineering Work</a>
  <a href="#part6" class="part-link">Task 6: Generate Technical Documentation Automatically</a>
  <a href="#part7" class="part-link">Task 7: Create Automation Scripts for IT Operations</a>
  <a href="#part8" class="part-link">Task 8: Troubleshoot Systems & Environments with Logs and </a>
  <a href="#part9" class="part-link">Task 9: Create Diagrams & Architecture from Text</a>
  <a href="#part10" class="part-link">Task 10: Prepare and Deliver Technical Presentations</a>
  <a href="#part11" class="part-link">Task 11: Write or Improve Policies, SOPs, and Governance Do</a>
  <a href="#part12" class="part-link">Task 12: Analyze Large DevOps or Monitoring Data</a>

  <a href="#sec-takeaways" class="section-link" style="margin-top:0.5rem;">Final Thoughts</a>
</nav>

<div class="main-content">

<div class="section" id="sec-intro">
  <h2>📖 Introduction</h2>
  <h3>Copilot for Developers & IT Teams</h3>
    <p>Microsoft 365 Copilot is more than a writing aid—it’s a multifaceted
assistant that can help your engineering and IT teams code faster,
summarize complex information, generate documentation, research new
technologies, automate repetitive tasks, and stay organised. In this
workshop you will explore twelve hands‑on scenarios designed
specifically for developers and IT professionals. Each exercise includes
<strong>sample prompts</strong>, <strong>tips</strong>, and a clear <strong>learning outcome</strong> so you
can immediately apply Copilot in your daily workflows.</p>
    <div class="callout"><strong>NOTE:</strong> Feel free to adapt the sample prompts to fit your own<br>environment, repositories, or documents. If Copilot’s first answer<br>isn’t what you expected, refine your prompt and try again—iteration is<br>part of the process!</div>
</div>

<div class="part-card" id="part1">
  <div class="part-header-bar blue"></div>
  <div class="part-header" onclick="togglePart('body1', this)">
    <h2>Task 1: Write & Review Code with Copilot</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body1">
    <p>Use <strong>Copilot</strong> (via the Copilot web app or the Copilot pane inside
Microsoft 365 apps) to generate and refine code snippets and scripts.
Copilot can create PowerShell or Bash scripts from natural‑language
descriptions, convert code between languages, and suggest improvements.
Microsoft notes that AI tools like Copilot can generate code snippets,
debug errors and even write documentation and test cases. Community
posts also highlight that by describing a task in plain English, Copilot
can generate ready‑to‑run PowerShell scripts and help refine or
troubleshoot them.</p>
    <p><strong>Steps:</strong></p>
    <ol class="steps">
      <li>Open <strong>Copilot</strong> by navigating to
<a href="https://copilot.microsoft.com" target="_blank">copilot.microsoft.com</a> or by
selecting the Copilot icon in Microsoft Teams or the Microsoft 365
app. Sign in with your organizational account.</li>
      <li>To generate a script, enter a clear description of what you need.
For example: “Generate a PowerShell script that lists all installed
Windows services and stops any services that have a status of
‘stopped’.” Copilot will produce the script inline.</li>
      <li>Copy the generated code and paste it into your preferred development
environment or script editor. Run and test the script, then ask
Copilot to refine it if you encounter errors or need adjustments.</li>
      <li>To review existing code, paste your code into Copilot and ask for
suggestions on performance, security, or readability. For example:
“Improve this Python function to handle exceptions and log errors.”</li>
      <li>To convert code between languages, paste the original code and
request a translation, such as “Convert this Bash script to a
PowerShell script.” Copilot will return the code in the new
language.</li>
      <li>Optionally, ask Copilot to create an <strong>Adaptive Card</strong> definition
for Teams or Outlook by describing the card’s content and layout.
Copy the resulting JSON into the appropriate application to test
your card.</li>
    </ol>
    <p><strong>Sample Prompts:</strong></p>
    <div class="prompt-box">Generate a PowerShell script to bulk‑enable multi‑factor authentication for all users in our tenant.
Review this C# method for performance and suggest improvements.
Convert this SQL query into a Python function using pandas.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <div class="callout purple"><strong>Learning Outcome:</strong>  <br>You’ll learn how to use Copilot to generate scripts and code snippets,<br>review and improve existing code, and convert code between<br>languages—all without leaving the Microsoft 365 ecosystem.</div>
  </div>
</div>

<div class="part-card" id="part2">
  <div class="part-header-bar navy"></div>
  <div class="part-header" onclick="togglePart('body2', this)">
    <h2>Task 2: Summarize & Understand Large Documentation Sets</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body2">
    <p>Developers and IT admins often work with lengthy runbooks, architecture
specs, or wiki pages. Copilot can summarize these documents and extract
action items. Microsoft’s adoption guidance notes that Copilot can
search for information, summarize documents, and draft meeting notes.</p>
    <p><strong>Steps:</strong></p>
    <ol class="steps">
      <li>Navigate to <a href="https://m365copilot.com/" target="_blank">M365copilot.com</a> and open
<strong>Copilot</strong>.</li>
      <li>Upload your document(s)—for example, a network architecture spec, a
SharePoint wiki page, or a PDF runbook. Copilot accepts Word, PDF,
text, and other common formats.</li>
      <li>Ask Copilot to summarize the document in a specific format. For
example: “Summarize this 50‑page architecture document into 10
bullet points and highlight dependencies.”</li>
      <li>Request a table of key components or steps. For instance: “Create a
table listing services, dependencies, and failure points from this
runbook.”</li>
      <li>Ask follow‑up questions to extract specific information, such as
“What are the prerequisites for deployment?” or “List the step that
configures the load balancer.”</li>
      <li>Optionally, have Copilot draft an action plan or checklist based on
the summarized content—for example, “Create a checklist to deploy
this application in a staging environment.”</li>
    </ol>
    <p><strong>Sample Prompts:</strong></p>
    <div class="prompt-box">Summarize the incident report and extract root cause, impact, and mitigation steps.
From this onboarding guide, list the first 5 tasks a new developer must complete.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <div class="callout purple"><strong>Learning Outcome:</strong>  <br>You’ll learn how to transform long technical documents into concise<br>summaries and actionable tables, making it easier to grasp complex<br>information.</div>
  </div>
</div>

<div class="part-card" id="part3">
  <div class="part-header-bar purple"></div>
  <div class="part-header" onclick="togglePart('body3', this)">
    <h2>Task 3: Research New Technologies with Copilot’s Research Agent</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body3">
    <p>Copilot can search the web and return concise, sourced answers.
Microsoft notes that Copilot provides direct answers and can conduct
research by searching the web. Use this to explore new technologies like
Microsoft Cloud PC (MCP) servers, serverless architectures, or emerging
frameworks.</p>
    <p><strong>Steps:</strong></p>
    <ol class="steps">
      <li>Open <strong>Copilot</strong> via the Copilot app or
<a href="https://m365copilot.com/" target="_blank">M365copilot.com</a>.</li>
      <li>In the prompt, clearly define what you want to research. For
example: “Research Microsoft Cloud PC (MCP) servers and compare them
to traditional virtual machines.”</li>
      <li>Ask Copilot to provide definitions, pros and cons, pricing
considerations, and usage scenarios. Copilot will search public
information and cite sources.</li>
      <li>Request comparisons or alternatives. For instance: “Compare Azure
Functions to AWS Lambda and Google Cloud Functions.”</li>
      <li>Follow up with “What are the best practices for securing MCP
servers?” or “List training resources for learning serverless
architecture.”</li>
      <li>Summarize the findings in a table or bullet list for easy
consumption.</li>
    </ol>
    <p><strong>Sample Prompts:</strong></p>
    <div class="prompt-box">Explain Microsoft Cloud PC and outline typical use cases and pricing models.
Research the latest features in .NET 8 and their impact on API development.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <div class="callout purple"><strong>Learning Outcome:</strong>  <br>You’ll learn how to use Copilot as a research assistant to gather<br>up‑to‑date information from the web, enabling quick technology<br>evaluations.</div>
  </div>
</div>

<div class="part-card" id="part4">
  <div class="part-header-bar green"></div>
  <div class="part-header" onclick="togglePart('body4', this)">
    <h2>Task 4: Accelerate Standups & Sprint Reviews with Loop + Copilot</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body4">
    <p>Copilot inside <strong>Microsoft Loop</strong> helps teams co‑create content, stay
informed, and pick up where others left off. Use it to prepare standup
summaries, sprint retrospectives, or planning docs based on your
meetings and work items.</p>
    <p><strong>Steps:</strong></p>
    <ol class="steps">
      <li>In Microsoft Teams, create a <strong>Loop</strong> component or open an existing
Loop page.</li>
      <li>Click the <strong>Copilot</strong> icon to invoke Copilot in Loop. Ask it to
aggregate updates from your team’s recent commits, pull requests, or
meeting notes.</li>
      <li>Prompt Copilot to draft a standup summary. For example: “Create
today’s standup summary based on yesterday’s meeting notes, code
commits, and issue tracker comments.”</li>
      <li>Ask for blockers or risks. For instance: “Identify blockers
mentioned in our sprint and list the owners.”</li>
      <li>Request a sprint demo outline or retrospective. For example:
“Generate a sprint review agenda using the past two weeks of
updates.”</li>
      <li>Share the Loop component in Teams so the team can edit and
collaborate in real time.</li>
    </ol>
    <p><strong>Sample Prompts:</strong></p>
    <div class="prompt-box">Summarize our daily standup from yesterday’s meeting notes and highlight blockers.
Draft a sprint retrospective with sections for achievements, challenges, and improvements.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <div class="callout purple"><strong>Learning Outcome:</strong>  <br>You’ll learn how to leverage Loop with Copilot to consolidate team<br>updates and produce dynamic standup summaries and sprint reviews.</div>
  </div>
</div>

<div class="part-card" id="part5">
  <div class="part-header-bar magenta"></div>
  <div class="part-header" onclick="togglePart('body5', this)">
    <h2>Task 5: Convert Meetings into Actionable Engineering Work</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body5">
    <p>Copilot in <strong>Microsoft Teams</strong> can summarize meetings, capture who said
what, and suggest action items. Turn design reviews, incident calls, or
planning sessions into structured work items.</p>
    <p><strong>Steps:</strong></p>
    <ol class="steps">
      <li>Join or schedule a meeting in <strong>Teams</strong> with the Copilot feature
enabled.</li>
      <li>During the meeting, click <strong>Copilot</strong> to generate a real‑time
summary of discussion points, decisions, and disagreements.</li>
      <li>After the meeting, ask Copilot to provide an action plan. For
example: “Summarize the incident call and extract root cause,
mitigation steps, and follow‑up tasks.”</li>
      <li>Request a table of tasks with owners and due dates. Copilot can
compile this into a list you can paste into Azure DevOps or Jira.</li>
      <li>Ask Copilot to draft follow‑up emails or Teams posts summarizing
decisions and next steps.</li>
      <li>Review the summary and refine as needed; confirm tasks with
stakeholders before actioning them.</li>
    </ol>
    <p><strong>Sample Prompts:</strong></p>
    <div class="prompt-box">Create a summary of our technical design review, listing decisions, open questions, and actions.
Convert this incident meeting into Jira tickets with descriptions and acceptance criteria.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <div class="callout purple"><strong>Learning Outcome:</strong>  <br>You’ll learn how to use Copilot in Teams to capture meeting<br>discussions and transform them into actionable tasks, keeping your<br>projects on track.</div>
  </div>
</div>

<div class="part-card" id="part6">
  <div class="part-header-bar orange"></div>
  <div class="part-header" onclick="togglePart('body6', this)">
    <h2>Task 6: Generate Technical Documentation Automatically</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body6">
    <p>AI tools like Copilot can generate explanations of code blocks and
project documentation using prompts. Use Copilot to create API docs,
onboarding guides, architecture descriptions, and other technical
materials without leaving the Microsoft 365 ecosystem.</p>
    <p><strong>Steps:</strong></p>
    <ol class="steps">
      <li>Copy the relevant block of code or describe the component you want
to document. Navigate to
<a href="https://copilot.microsoft.com" target="_blank">copilot.microsoft.com</a> or open the
Copilot pane within Word or Teams.</li>
      <li>Paste the code into Copilot and ask for an explanation. For example:
“Explain this function and its parameters for API documentation.”
Copilot will describe the purpose, parameters, and return values.</li>
      <li>Ask Copilot to generate a README or architecture overview. For
instance: “Generate a project overview including installation
instructions, usage examples, and architecture summary.”</li>
      <li>Request inline comments or docstrings following your team’s style
guidelines. You might ask: “Add detailed docstrings to this Python
class with parameter descriptions and examples.”</li>
      <li>If documenting multiple components, ask Copilot to create a
high‑level architecture description or sequence diagram summarizing
interactions between services.</li>
      <li>Copy the generated documentation into your documentation platform
(Word, OneNote, SharePoint, etc.), review it for accuracy, and edit
as needed before publishing.</li>
    </ol>
    <p><strong>Sample Prompts:</strong></p>
    <div class="prompt-box">Create API documentation for the orders service, including endpoint descriptions, request/response examples, and error codes.
Generate a project overview and onboarding guide for new developers joining our team.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <div class="callout purple"><strong>Learning Outcome:</strong>  <br>You’ll learn how to leverage Copilot to automatically generate or<br>enhance technical documentation, saving time and ensuring consistency.</div>
  </div>
</div>

<div class="part-card" id="part7">
  <div class="part-header-bar teal"></div>
  <div class="part-header" onclick="togglePart('body7', this)">
    <h2>Task 7: Create Automation Scripts for IT Operations</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body7">
    <p>IT administrators often need to automate tasks like account creation,
device configuration, or policy enforcement. Copilot can generate
ready‑to‑run PowerShell or Bash scripts from plain‑language descriptions
and refine or troubleshoot them.</p>
    <p><strong>Steps:</strong></p>
    <ol class="steps">
      <li>Open <strong>Copilot</strong> via the Copilot web app or within a Microsoft 365
app such as Teams.</li>
      <li>Describe the administrative task you want to automate. For example:
“Create a PowerShell script to enable multi‑factor authentication
for all users.”</li>
      <li>Copilot will generate a script with comments. Review the script and
ask clarifying questions if needed—for example, “Add logging and
error handling to this script.”</li>
      <li>Test the script in a safe environment. If it fails, copy the error
message into Copilot and ask for troubleshooting assistance.</li>
      <li>Request modifications for different platforms—e.g., “Convert this
PowerShell script to a Bash script for Linux servers.”</li>
      <li>Save the final script and document its usage so others can run it.</li>
    </ol>
    <p><strong>Sample Prompts:</strong></p>
    <div class="prompt-box">Generate an Intune configuration profile in JSON to enforce BitLocker encryption on all Windows devices.
Write a Bash script to monitor /var/log for intrusion patterns and send email alerts.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <div class="callout purple"><strong>Learning Outcome:</strong>  <br>You’ll learn how to quickly generate and refine automation scripts<br>using Copilot, reducing repetitive manual work.</div>
  </div>
</div>

<div class="part-card" id="part8">
  <div class="part-header-bar blue"></div>
  <div class="part-header" onclick="togglePart('body8', this)">
    <h2>Task 8: Troubleshoot Systems & Environments with Logs and Errors</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body8">
    <p>When debugging, developers often paste log files or error messages into
Copilot to get precise answers. A Microsoft guidance article advises
referencing specific functions, error messages, or logs when chatting
with Copilot.</p>
    <p><strong>Steps:</strong></p>
    <ol class="steps">
      <li>Open <strong>Copilot</strong> and gather the log files or error messages you need
to analyze. You can copy‑and‑paste logs or upload a text file.</li>
      <li>Provide context in your prompt. For example: “Analyze the attached
server log and identify any database connection errors.”</li>
      <li>If there’s a stack trace, ask Copilot to explain the error and
propose a fix: “Explain this null reference exception and suggest
how to resolve it.”</li>
      <li>Request a summary of the most common errors in the log file and
potential root causes.</li>
      <li>Follow up with clarifications: “What configuration changes could
prevent this error?” or “Generate a script to monitor for this error
and alert the team.”</li>
      <li>Implement and test the recommended fixes, then rerun the process if
new errors occur.</li>
    </ol>
    <p><strong>Sample Prompts:</strong></p>
    <div class="prompt-box">Search this log file for fatal errors and summarize them with timestamps.
Explain the cause of the 500 Internal Server Error appearing in our web server logs.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <div class="callout purple"><strong>Learning Outcome:</strong>  <br>You’ll learn how to use Copilot to analyze logs, explain error<br>messages, and recommend fixes, speeding up incident resolution.</div>
  </div>
</div>

<div class="part-card" id="part9">
  <div class="part-header-bar navy"></div>
  <div class="part-header" onclick="togglePart('body9', this)">
    <h2>Task 9: Create Diagrams & Architecture from Text</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body9">
    <p>Copilot can generate diagrams using code—for example, by producing
Mermaid syntax. Copilot can create diagrams, such as Gantt charts, to
visualize data and provides the code needed to render the diagram. This
is useful for architecture diagrams, sequence diagrams, or data flows.</p>
    <p><strong>Steps:</strong></p>
    <ol class="steps">
      <li>Open <strong>Copilot</strong> via the web app or within a Microsoft 365 app.</li>
      <li>Describe the architecture you want to visualize. For example: “Draw
a microservices architecture with API Gateway, authentication
service, product service, Redis cache, and SQL database.”</li>
      <li>Ask Copilot to generate a Mermaid diagram. Copilot will output code
in the <code>mermaid</code> syntax along with an explanation.</li>
      <li>Copy the code into a Markdown or diagram tool that supports Mermaid
(such as a Loop page or a markdown editor) to render the diagram.</li>
      <li>Ask Copilot to modify the diagram—for example, “Add a message queue
between the API Gateway and the product service,” or “Convert this
to a sequence diagram for user authentication.”</li>
      <li>Save and share the visual with your team.</li>
    </ol>
    <p><strong>Sample Prompts:</strong></p>
    <div class="prompt-box">Create a sequence diagram showing user authentication using OAuth 2.0 with a mobile app, identity provider, and resource server.
Generate a data flow diagram for our ETL pipeline ingesting data from IoT devices into a data lake.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <div class="callout purple"><strong>Learning Outcome:</strong>  <br>You’ll learn how to turn textual descriptions into visual diagrams<br>using Copilot, enabling clearer communication of system architectures.</div>
  </div>
</div>

<div class="part-card" id="part10">
  <div class="part-header-bar purple"></div>
  <div class="part-header" onclick="togglePart('body10', this)">
    <h2>Task 10: Prepare and Deliver Technical Presentations</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body10">
    <p>Copilot in <strong>PowerPoint</strong> can read through a long presentation and
provide a bulleted summary of key points. Use Copilot to build and
polish decks summarizing projects, incidents, or architecture changes.</p>
    <p><strong>Steps:</strong></p>
    <ol class="steps">
      <li>Open your existing PowerPoint deck or start a new one in
<strong>PowerPoint for the web</strong>. Click the <strong>Copilot</strong> button in the
ribbon.</li>
      <li>Ask Copilot to summarize your presentation in bullets. For example:
“Summarize this 40‑slide deck into 5 bullets highlighting key
findings.”</li>
      <li>Provide content and ask Copilot to create slides. For instance:
“Create a slide describing our migration to Kubernetes, including
benefits and challenges.”</li>
      <li>Request visuals or diagrams. You can ask: “Add a slide with a bar
chart summarizing monthly incident counts.” Copilot will generate
charts based on your data.</li>
      <li>Ask Copilot to rewrite slide text for clarity, or adjust tone for
executive audiences.</li>
      <li>Practice presenting by asking Copilot to generate speaker notes or
potential questions from stakeholders.</li>
    </ol>
    <p><strong>Sample Prompts:</strong></p>
    <div class="prompt-box">Create a three‑slide executive summary of our Q3 incident trends and recommended actions.
Improve this slide deck by simplifying the language and adding a concluding call to action.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <div class="callout purple"><strong>Learning Outcome:</strong>  <br>You’ll learn how to leverage Copilot in PowerPoint to create,<br>summarize, and refine presentations for technical leadership and<br>stakeholders.</div>
  </div>
</div>

<div class="part-card" id="part11">
  <div class="part-header-bar green"></div>
  <div class="part-header" onclick="togglePart('body11', this)">
    <h2>Task 11: Write or Improve Policies, SOPs, and Governance Docs</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body11">
    <p>Copilot can help you update and improve policies or standard operating
procedures (SOPs). The Microsoft Scenario Library shows an HR use case
where Copilot compares new and old policy documents, makes a table of
differences, drafts FAQs, creates a change management plan, and develops
training materials. The same approach applies to IT policies, access
controls, or change‑management procedures.</p>
    <p><strong>Steps:</strong></p>
    <ol class="steps">
      <li>Gather the current and proposed versions of your policy or SOP
document and open <strong>Copilot</strong> in Word (or use the Copilot web app).</li>
      <li>Ask Copilot to compare the two documents and produce a table of key
differences. For example: “Compare these two security policies and
list the changes with rationale.”</li>
      <li>Request a draft FAQ explaining the policy update and its impact on
stakeholders.</li>
      <li>Have Copilot create a change‑management plan outlining tasks,
timelines, and communications needed to implement the updated
policy.</li>
      <li>Ask Copilot to generate training materials or slide decks to help
colleagues understand the policy changes.</li>
      <li>Use Copilot in Teams during review meetings to summarize feedback
and action items to refine the policy.</li>
    </ol>
    <p><strong>Sample Prompts:</strong></p>
    <div class="prompt-box">Compare the existing backup policy with the proposed update and create a table of changes.
Draft an FAQ addressing common questions about the new access control policy.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <div class="callout purple"><strong>Learning Outcome:</strong>  <br>You’ll learn how Copilot can assist with policy management—identifying<br>changes, drafting communications, and planning implementation—ensuring<br>governance documents stay current.</div>
  </div>
</div>

<div class="part-card" id="part12">
  <div class="part-header-bar magenta"></div>
  <div class="part-header" onclick="togglePart('body12', this)">
    <h2>Task 12: Analyze Large DevOps or Monitoring Data</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body12">
    <p>Copilot can analyze large datasets from CSV or Excel files, producing
charts and summaries. Microsoft notes that Copilot can perform complex
data analysis and generate charts or reports. Use this to explore
metrics from build pipelines, deployment logs, or system monitoring.</p>
    <p><strong>Steps:</strong></p>
    <ol class="steps">
      <li>Export your DevOps metrics—such as deployment durations, test pass
rates, or monitoring logs—to a CSV or Excel file.</li>
      <li>Navigate to <a href="https://m365copilot.com/" target="_blank">M365copilot.com</a> and open
<strong>Copilot</strong>. Upload the data file.</li>
      <li>Ask Copilot to list the types of visualizations it can create based
on your data. For example: “What charts can you build from this
deployment metrics file?”</li>
      <li>Request specific analyses, like “Create a line chart showing build
duration over time” or “Generate a heat map of error counts by
service and month.”</li>
      <li>Ask Copilot to calculate aggregates or perform calculations:
“Calculate the average deployment success rate per month,” or
“Identify the top five services with the highest error counts.”</li>
      <li>Download or copy the generated visuals and metrics into reports or
dashboards for sharing with your team.</li>
    </ol>
    <p><strong>Sample Prompts:</strong></p>
    <div class="prompt-box">From this CSV file of application logs, create a bar chart of error counts per microservice.
Calculate the median deployment time and identify outliers.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <div class="callout purple"><strong>Learning Outcome:</strong>  <br>You’ll learn how to use Copilot to analyze structured data, create<br>visualizations, and compute metrics, enabling data‑driven decisions<br>for your projects.</div>
  </div>
</div>

<div class="section" id="sec-takeaways">
  <h2>🔑 Final Thoughts</h2>
  <div class="takeaways-grid">
    <div class="takeaway-card"><div class="icon">⚡</div><h4>Iterate Prompts</h4><p>Refine prompts to get better results — Copilot improves with every turn.</p></div>
    <div class="takeaway-card"><div class="icon">📎</div><h4>Ground in Reality</h4><p>Attach the right files. Quality grounding produces quality output.</p></div>
    <div class="takeaway-card"><div class="icon">🔁</div><h4>Reuse What Works</h4><p>Save prompts and patterns you'll use again — your future self will thank you.</p></div>
    <div class="takeaway-card"><div class="icon">✅</div><h4>Always Verify</h4><p>Review AI output before acting on it — you remain the pilot.</p></div>
  </div>
</div>

</div>
</div>

<footer>
  <p><strong>Microsoft 365 Copilot — Developer & IT Training</strong></p>
  <p>For questions or feedback, reach out to your training facilitator.</p>
</footer>

<button class="sidebar-toggle" id="sidebarToggle" onclick="openSidebar()" aria-label="Open navigation">☰</button>

<script src="../../Allfiles/demo-script.js"></script>
</body>
</html>
