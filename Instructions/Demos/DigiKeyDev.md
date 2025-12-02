[Back to Index](https://emontes07.github.io/Learning/)

## Copilot for Developers & IT Teams

Microsoft 365 Copilot is more than a writing aid—it’s a multifaceted
assistant that can help your engineering and IT teams code faster,
summarize complex information, generate documentation, research new
technologies, automate repetitive tasks, and stay organised. In this
workshop you will explore twelve hands‑on scenarios designed
specifically for developers and IT professionals. Each exercise includes
**sample prompts**, **tips**, and a clear **learning outcome** so you
can immediately apply Copilot in your daily workflows.

> **NOTE:** Feel free to adapt the sample prompts to fit your own
> environment, repositories, or documents. If Copilot’s first answer
> isn’t what you expected, refine your prompt and try again—iteration is
> part of the process!

------------------------------------------------------------------------

### Task 1: Write & Review Code with Copilot

Use **Copilot** (via the Copilot web app or the Copilot pane inside
Microsoft 365 apps) to generate and refine code snippets and scripts.
Copilot can create PowerShell or Bash scripts from natural‑language
descriptions, convert code between languages, and suggest improvements.
Microsoft notes that AI tools like Copilot can generate code snippets,
debug errors and even write documentation and test cases. Community
posts also highlight that by describing a task in plain English, Copilot
can generate ready‑to‑run PowerShell scripts and help refine or
troubleshoot them.

**Steps:**

1.  Open **Copilot** by navigating to
    [copilot.microsoft.com](https://copilot.microsoft.com) or by
    selecting the Copilot icon in Microsoft Teams or the Microsoft 365
    app. Sign in with your organizational account.
2.  To generate a script, enter a clear description of what you need.
    For example: “Generate a PowerShell script that lists all installed
    Windows services and stops any services that have a status of
    ‘stopped’.” Copilot will produce the script inline.
3.  Copy the generated code and paste it into your preferred development
    environment or script editor. Run and test the script, then ask
    Copilot to refine it if you encounter errors or need adjustments.
4.  To review existing code, paste your code into Copilot and ask for
    suggestions on performance, security, or readability. For example:
    “Improve this Python function to handle exceptions and log errors.”
5.  To convert code between languages, paste the original code and
    request a translation, such as “Convert this Bash script to a
    PowerShell script.” Copilot will return the code in the new
    language.
6.  Optionally, ask Copilot to create an **Adaptive Card** definition
    for Teams or Outlook by describing the card’s content and layout.
    Copy the resulting JSON into the appropriate application to test
    your card.

**Sample Prompts:**

    Generate a PowerShell script to bulk‑enable multi‑factor authentication for all users in our tenant.
    Review this C# method for performance and suggest improvements.
    Convert this SQL query into a Python function using pandas.

> **Learning Outcome:**  
> You’ll learn how to use Copilot to generate scripts and code snippets,
> review and improve existing code, and convert code between
> languages—all without leaving the Microsoft 365 ecosystem.

------------------------------------------------------------------------

### Task 2: Summarize & Understand Large Documentation Sets

Developers and IT admins often work with lengthy runbooks, architecture
specs, or wiki pages. Copilot can summarize these documents and extract
action items. Microsoft’s adoption guidance notes that Copilot can
search for information, summarize documents, and draft meeting notes.

**Steps:**

1.  Navigate to [M365copilot.com](https://m365copilot.com/) and open
    **Copilot**.
2.  Upload your document(s)—for example, a network architecture spec, a
    SharePoint wiki page, or a PDF runbook. Copilot accepts Word, PDF,
    text, and other common formats.
3.  Ask Copilot to summarize the document in a specific format. For
    example: “Summarize this 50‑page architecture document into 10
    bullet points and highlight dependencies.”
4.  Request a table of key components or steps. For instance: “Create a
    table listing services, dependencies, and failure points from this
    runbook.”
5.  Ask follow‑up questions to extract specific information, such as
    “What are the prerequisites for deployment?” or “List the step that
    configures the load balancer.”
6.  Optionally, have Copilot draft an action plan or checklist based on
    the summarized content—for example, “Create a checklist to deploy
    this application in a staging environment.”

**Sample Prompts:**

    Summarize the incident report and extract root cause, impact, and mitigation steps.
    From this onboarding guide, list the first 5 tasks a new developer must complete.

> **Learning Outcome:**  
> You’ll learn how to transform long technical documents into concise
> summaries and actionable tables, making it easier to grasp complex
> information.

------------------------------------------------------------------------

### Task 3: Research New Technologies with Copilot’s Research Agent

Copilot can search the web and return concise, sourced answers.
Microsoft notes that Copilot provides direct answers and can conduct
research by searching the web. Use this to explore new technologies like
Microsoft Cloud PC (MCP) servers, serverless architectures, or emerging
frameworks.

**Steps:**

1.  Open **Copilot** via the Copilot app or
    [M365copilot.com](https://m365copilot.com/).
2.  In the prompt, clearly define what you want to research. For
    example: “Research Microsoft Cloud PC (MCP) servers and compare them
    to traditional virtual machines.”
3.  Ask Copilot to provide definitions, pros and cons, pricing
    considerations, and usage scenarios. Copilot will search public
    information and cite sources.
4.  Request comparisons or alternatives. For instance: “Compare Azure
    Functions to AWS Lambda and Google Cloud Functions.”
5.  Follow up with “What are the best practices for securing MCP
    servers?” or “List training resources for learning serverless
    architecture.”
6.  Summarize the findings in a table or bullet list for easy
    consumption.

**Sample Prompts:**

    Explain Microsoft Cloud PC and outline typical use cases and pricing models.
    Research the latest features in .NET 8 and their impact on API development.

> **Learning Outcome:**  
> You’ll learn how to use Copilot as a research assistant to gather
> up‑to‑date information from the web, enabling quick technology
> evaluations.

------------------------------------------------------------------------

### Task 4: Accelerate Standups & Sprint Reviews with Loop + Copilot

Copilot inside **Microsoft Loop** helps teams co‑create content, stay
informed, and pick up where others left off. Use it to prepare standup
summaries, sprint retrospectives, or planning docs based on your
meetings and work items.

**Steps:**

1.  In Microsoft Teams, create a **Loop** component or open an existing
    Loop page.
2.  Click the **Copilot** icon to invoke Copilot in Loop. Ask it to
    aggregate updates from your team’s recent commits, pull requests, or
    meeting notes.
3.  Prompt Copilot to draft a standup summary. For example: “Create
    today’s standup summary based on yesterday’s meeting notes, code
    commits, and issue tracker comments.”
4.  Ask for blockers or risks. For instance: “Identify blockers
    mentioned in our sprint and list the owners.”
5.  Request a sprint demo outline or retrospective. For example:
    “Generate a sprint review agenda using the past two weeks of
    updates.”
6.  Share the Loop component in Teams so the team can edit and
    collaborate in real time.

**Sample Prompts:**

    Summarize our daily standup from yesterday’s meeting notes and highlight blockers.
    Draft a sprint retrospective with sections for achievements, challenges, and improvements.

> **Learning Outcome:**  
> You’ll learn how to leverage Loop with Copilot to consolidate team
> updates and produce dynamic standup summaries and sprint reviews.

------------------------------------------------------------------------

### Task 5: Convert Meetings into Actionable Engineering Work

Copilot in **Microsoft Teams** can summarize meetings, capture who said
what, and suggest action items. Turn design reviews, incident calls, or
planning sessions into structured work items.

**Steps:**

1.  Join or schedule a meeting in **Teams** with the Copilot feature
    enabled.
2.  During the meeting, click **Copilot** to generate a real‑time
    summary of discussion points, decisions, and disagreements.
3.  After the meeting, ask Copilot to provide an action plan. For
    example: “Summarize the incident call and extract root cause,
    mitigation steps, and follow‑up tasks.”
4.  Request a table of tasks with owners and due dates. Copilot can
    compile this into a list you can paste into Azure DevOps or Jira.
5.  Ask Copilot to draft follow‑up emails or Teams posts summarizing
    decisions and next steps.
6.  Review the summary and refine as needed; confirm tasks with
    stakeholders before actioning them.

**Sample Prompts:**

    Create a summary of our technical design review, listing decisions, open questions, and actions.
    Convert this incident meeting into Jira tickets with descriptions and acceptance criteria.

> **Learning Outcome:**  
> You’ll learn how to use Copilot in Teams to capture meeting
> discussions and transform them into actionable tasks, keeping your
> projects on track.

------------------------------------------------------------------------

### Task 6: Generate Technical Documentation Automatically

AI tools like Copilot can generate explanations of code blocks and
project documentation using prompts. Use Copilot to create API docs,
onboarding guides, architecture descriptions, and other technical
materials without leaving the Microsoft 365 ecosystem.

**Steps:**

1.  Copy the relevant block of code or describe the component you want
    to document. Navigate to
    [copilot.microsoft.com](https://copilot.microsoft.com) or open the
    Copilot pane within Word or Teams.
2.  Paste the code into Copilot and ask for an explanation. For example:
    “Explain this function and its parameters for API documentation.”
    Copilot will describe the purpose, parameters, and return values.
3.  Ask Copilot to generate a README or architecture overview. For
    instance: “Generate a project overview including installation
    instructions, usage examples, and architecture summary.”
4.  Request inline comments or docstrings following your team’s style
    guidelines. You might ask: “Add detailed docstrings to this Python
    class with parameter descriptions and examples.”
5.  If documenting multiple components, ask Copilot to create a
    high‑level architecture description or sequence diagram summarizing
    interactions between services.
6.  Copy the generated documentation into your documentation platform
    (Word, OneNote, SharePoint, etc.), review it for accuracy, and edit
    as needed before publishing.

**Sample Prompts:**

    Create API documentation for the orders service, including endpoint descriptions, request/response examples, and error codes.
    Generate a project overview and onboarding guide for new developers joining our team.

> **Learning Outcome:**  
> You’ll learn how to leverage Copilot to automatically generate or
> enhance technical documentation, saving time and ensuring consistency.

------------------------------------------------------------------------

### Task 7: Create Automation Scripts for IT Operations

IT administrators often need to automate tasks like account creation,
device configuration, or policy enforcement. Copilot can generate
ready‑to‑run PowerShell or Bash scripts from plain‑language descriptions
and refine or troubleshoot them.

**Steps:**

1.  Open **Copilot** via the Copilot web app or within a Microsoft 365
    app such as Teams.
2.  Describe the administrative task you want to automate. For example:
    “Create a PowerShell script to enable multi‑factor authentication
    for all users.”
3.  Copilot will generate a script with comments. Review the script and
    ask clarifying questions if needed—for example, “Add logging and
    error handling to this script.”
4.  Test the script in a safe environment. If it fails, copy the error
    message into Copilot and ask for troubleshooting assistance.
5.  Request modifications for different platforms—e.g., “Convert this
    PowerShell script to a Bash script for Linux servers.”
6.  Save the final script and document its usage so others can run it.

**Sample Prompts:**

    Generate an Intune configuration profile in JSON to enforce BitLocker encryption on all Windows devices.
    Write a Bash script to monitor /var/log for intrusion patterns and send email alerts.

> **Learning Outcome:**  
> You’ll learn how to quickly generate and refine automation scripts
> using Copilot, reducing repetitive manual work.

------------------------------------------------------------------------

### Task 8: Troubleshoot Systems & Environments with Logs and Errors

When debugging, developers often paste log files or error messages into
Copilot to get precise answers. A Microsoft guidance article advises
referencing specific functions, error messages, or logs when chatting
with Copilot.

**Steps:**

1.  Open **Copilot** and gather the log files or error messages you need
    to analyze. You can copy‑and‑paste logs or upload a text file.
2.  Provide context in your prompt. For example: “Analyze the attached
    server log and identify any database connection errors.”
3.  If there’s a stack trace, ask Copilot to explain the error and
    propose a fix: “Explain this null reference exception and suggest
    how to resolve it.”
4.  Request a summary of the most common errors in the log file and
    potential root causes.
5.  Follow up with clarifications: “What configuration changes could
    prevent this error?” or “Generate a script to monitor for this error
    and alert the team.”
6.  Implement and test the recommended fixes, then rerun the process if
    new errors occur.

**Sample Prompts:**

    Search this log file for fatal errors and summarize them with timestamps.
    Explain the cause of the 500 Internal Server Error appearing in our web server logs.

> **Learning Outcome:**  
> You’ll learn how to use Copilot to analyze logs, explain error
> messages, and recommend fixes, speeding up incident resolution.

------------------------------------------------------------------------

### Task 9: Create Diagrams & Architecture from Text

Copilot can generate diagrams using code—for example, by producing
Mermaid syntax. Copilot can create diagrams, such as Gantt charts, to
visualize data and provides the code needed to render the diagram. This
is useful for architecture diagrams, sequence diagrams, or data flows.

**Steps:**

1.  Open **Copilot** via the web app or within a Microsoft 365 app.
2.  Describe the architecture you want to visualize. For example: “Draw
    a microservices architecture with API Gateway, authentication
    service, product service, Redis cache, and SQL database.”
3.  Ask Copilot to generate a Mermaid diagram. Copilot will output code
    in the `mermaid` syntax along with an explanation.
4.  Copy the code into a Markdown or diagram tool that supports Mermaid
    (such as a Loop page or a markdown editor) to render the diagram.
5.  Ask Copilot to modify the diagram—for example, “Add a message queue
    between the API Gateway and the product service,” or “Convert this
    to a sequence diagram for user authentication.”
6.  Save and share the visual with your team.

**Sample Prompts:**

    Create a sequence diagram showing user authentication using OAuth 2.0 with a mobile app, identity provider, and resource server.
    Generate a data flow diagram for our ETL pipeline ingesting data from IoT devices into a data lake.

> **Learning Outcome:**  
> You’ll learn how to turn textual descriptions into visual diagrams
> using Copilot, enabling clearer communication of system architectures.

------------------------------------------------------------------------

### Task 10: Prepare and Deliver Technical Presentations

Copilot in **PowerPoint** can read through a long presentation and
provide a bulleted summary of key points. Use Copilot to build and
polish decks summarizing projects, incidents, or architecture changes.

**Steps:**

1.  Open your existing PowerPoint deck or start a new one in
    **PowerPoint for the web**. Click the **Copilot** button in the
    ribbon.
2.  Ask Copilot to summarize your presentation in bullets. For example:
    “Summarize this 40‑slide deck into 5 bullets highlighting key
    findings.”
3.  Provide content and ask Copilot to create slides. For instance:
    “Create a slide describing our migration to Kubernetes, including
    benefits and challenges.”
4.  Request visuals or diagrams. You can ask: “Add a slide with a bar
    chart summarizing monthly incident counts.” Copilot will generate
    charts based on your data.
5.  Ask Copilot to rewrite slide text for clarity, or adjust tone for
    executive audiences.
6.  Practice presenting by asking Copilot to generate speaker notes or
    potential questions from stakeholders.

**Sample Prompts:**

    Create a three‑slide executive summary of our Q3 incident trends and recommended actions.
    Improve this slide deck by simplifying the language and adding a concluding call to action.

> **Learning Outcome:**  
> You’ll learn how to leverage Copilot in PowerPoint to create,
> summarize, and refine presentations for technical leadership and
> stakeholders.

------------------------------------------------------------------------

### Task 11: Write or Improve Policies, SOPs, and Governance Docs

Copilot can help you update and improve policies or standard operating
procedures (SOPs). The Microsoft Scenario Library shows an HR use case
where Copilot compares new and old policy documents, makes a table of
differences, drafts FAQs, creates a change management plan, and develops
training materials. The same approach applies to IT policies, access
controls, or change‑management procedures.

**Steps:**

1.  Gather the current and proposed versions of your policy or SOP
    document and open **Copilot** in Word (or use the Copilot web app).
2.  Ask Copilot to compare the two documents and produce a table of key
    differences. For example: “Compare these two security policies and
    list the changes with rationale.”
3.  Request a draft FAQ explaining the policy update and its impact on
    stakeholders.
4.  Have Copilot create a change‑management plan outlining tasks,
    timelines, and communications needed to implement the updated
    policy.
5.  Ask Copilot to generate training materials or slide decks to help
    colleagues understand the policy changes.
6.  Use Copilot in Teams during review meetings to summarize feedback
    and action items to refine the policy.

**Sample Prompts:**

    Compare the existing backup policy with the proposed update and create a table of changes.
    Draft an FAQ addressing common questions about the new access control policy.

> **Learning Outcome:**  
> You’ll learn how Copilot can assist with policy management—identifying
> changes, drafting communications, and planning implementation—ensuring
> governance documents stay current.

------------------------------------------------------------------------

### Task 12: Analyze Large DevOps or Monitoring Data

Copilot can analyze large datasets from CSV or Excel files, producing
charts and summaries. Microsoft notes that Copilot can perform complex
data analysis and generate charts or reports. Use this to explore
metrics from build pipelines, deployment logs, or system monitoring.

**Steps:**

1.  Export your DevOps metrics—such as deployment durations, test pass
    rates, or monitoring logs—to a CSV or Excel file.
2.  Navigate to [M365copilot.com](https://m365copilot.com/) and open
    **Copilot**. Upload the data file.
3.  Ask Copilot to list the types of visualizations it can create based
    on your data. For example: “What charts can you build from this
    deployment metrics file?”
4.  Request specific analyses, like “Create a line chart showing build
    duration over time” or “Generate a heat map of error counts by
    service and month.”
5.  Ask Copilot to calculate aggregates or perform calculations:
    “Calculate the average deployment success rate per month,” or
    “Identify the top five services with the highest error counts.”
6.  Download or copy the generated visuals and metrics into reports or
    dashboards for sharing with your team.

**Sample Prompts:**

    From this CSV file of application logs, create a bar chart of error counts per microservice.
    Calculate the median deployment time and identify outliers.

> **Learning Outcome:**  
> You’ll learn how to use Copilot to analyze structured data, create
> visualizations, and compute metrics, enabling data‑driven decisions
> for your projects.

------------------------------------------------------------------------

### Final Thoughts

These twelve scenarios showcase how Microsoft 365 Copilot can amplify
the productivity of developers and IT professionals. By integrating
Copilot into your coding workflows, documentation practices, research
tasks, meetings, policy updates, and data analyses, you’ll free time for
more creative and strategic work. Continue experimenting with prompts
and exploring Copilot across other M365 apps—every iteration brings new
insights and efficiencies.
