---
demo:
    title: 'Legal Demo'
layout: none
---

<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Copilot Training for Legal | Learning</title>
<link rel="stylesheet" href="../../Allfiles/demo-style.css">
<style>:root { --hero-from: #5C2D91; --hero-via: #7B3FA8; --hero-to: #0078D4; }</style>
</head>
<body>

<div class="back-bar">
  <a href="https://emontes07.github.io/Learning/">← Back to Index</a>
</div>

<div class="hero">
  <div class="hero-inner">
    <h1>Microsoft 365 Copilot Training for Legal</h1>
    <p class="subtitle">Copilot for Legal Professionals — Research, Drafting &amp; Compliance</p>
    <div class="scenario">
      <strong>Scenario:</strong> You're a legal advisor at Contoso, responsible for assessing whether the company's AI Resume Screening Software complies with the EU AI Act. Your goal is to research legal risks, draft an executive summary, and communicate recommendations to leadership.<br><br>
      <em>Sample prompts are provided to help you get started. Feel free to personalize them — if Copilot doesn't deliver the result you want, refine your prompt and try again.</em>
    </div>
    <div class="hero-meta">
      <span>⚖️ Legal Research</span>
      <span>💬 Copilot Chat</span>
      <span>📝 Word</span>
      <span>📧 Outlook</span>
      <span>🎓 Instructor-Led</span>
    </div>
  </div>
</div>

<div class="sidebar-overlay" id="sidebarOverlay" onclick="closeSidebar()"></div>

<div class="layout">

<nav class="sidebar" id="sidebar">
  <a class="sb-home" href="https://emontes07.github.io/Learning/">← Back to Index</a>
  <div class="sb-title">Copilot Training for Legal</div>

  <a href="#sec-objectives" class="section-link">Learning Objectives</a>
  <a href="#sec-prereqs" class="section-link">Demo Setup</a>

  <a href="#part1" class="part-link">Part 1: Copilot Basics</a>
  <a href="#part2" class="part-link">Part 2: Copilot Chat — Research</a>
  <a href="#part3" class="part-link">Part 3: Copilot in Word</a>
  <a href="#part4" class="part-link">Part 4: Copilot in Outlook</a>
  <a href="#part5" class="part-link">Part 5: Additional Prompts</a>

  <a href="#sec-takeaways" class="section-link" style="margin-top:0.5rem;">Key Takeaways</a>
</nav>

<div class="main-content">

<div class="section" id="sec-objectives">
  <h2>🎯 Learning Objectives</h2>
  <ul class="objectives-list">
    <li>Save and reuse legal-specific prompts for daily productivity</li>
    <li>Use Copilot Memory and Custom Instructions to personalize Copilot for legal work</li>
    <li>Research regulations like the EU AI Act using Copilot Chat in Web mode</li>
    <li>Draft an executive summary in Word grounded on Copilot Chat research</li>
    <li>Communicate findings and recommendations to leadership via Copilot in Outlook</li>
    <li>Apply advanced prompting techniques to interpret legal language and run scenario analyses</li>
  </ul>
</div>

<div class="section" id="sec-prereqs">
  <h2>📋 Demo Setup</h2>
  <p>There are no sample documents required for this demo.</p>
  <div class="prereq-grid">
    <div class="prereq-item"><div class="prereq-icon blue">M</div>Microsoft 365 Copilot License</div>
    <div class="prereq-item"><div class="prereq-icon blue">🌐</div>Access to <strong>m365copilot.com</strong></div>
    <div class="prereq-item"><div class="prereq-icon blue">📝</div>Word (Web or Desktop)</div>
    <div class="prereq-item"><div class="prereq-icon purple">📧</div>Outlook (Web or Desktop)</div>
    <div class="prereq-item"><div class="prereq-icon green">☁</div>OneDrive / SharePoint access</div>
  </div>
  <div class="callout">
    <strong>📝 NOTE:</strong> Sample prompts are provided to help you get started. Feel free to personalize them to suit your needs — be creative and explore! Learn more about new features <a href="https://www.microsoft.com/en-us/microsoft-365/roadmap/copilotchat" target="_blank">here</a>.
  </div>
</div>

<div class="part-card" id="part1">
  <div class="part-header-bar basics"></div>
  <div class="part-header" onclick="togglePart('body1', this)">
    <h2>Part 1: Copilot Basics — Save Prompts &amp; Customize Copilot</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body1">

    <div class="callout">
      <strong>💡 Why This Matters:</strong> Legal professionals run similar prompts repeatedly — clause comparisons, regulatory summaries, plain-English translations. Saving prompts and configuring Copilot Memory lets you reuse your best instructions without retyping them and ensures Copilot understands your legal context.
    </div>

    <h3>Practice 1: How to Save Prompts in Copilot</h3>
    <p>Saving prompts helps you quickly reuse instructions or queries without having to rewrite them each time.</p>

    <p><strong>Step 1: Save a Prompt</strong></p>
    <ol class="steps">
      <li>Open a new browser tab and navigate to <strong><a href="https://m365copilot.com" target="_blank">M365copilot.com</a></strong>.</li>
      <li>Start by running a prompt, for example:</li>
    </ol>
    <div class="prompt-box">Copilot, summarize my emails, Teams messages, and channel messages from the last 1 workday. Categorize them as internal activities, external activities, or messages from my team or manager, and prioritize them for my attention. List action items in a dedicated column and suggest follow-ups if possible, in a dedicated column.

The table should look like this:
Type (Mail/Teams/Channel) | Topic | Summarization | Category | Priority | Action Item | Follow-up.

If I have been directly mentioned, make the font of the topic bold.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <ol class="steps" start="3">
      <li>Hover over the prompt.</li>
      <li>Click <strong>Save Prompt</strong>.</li>
      <li>Give it a name for easy reference.</li>
    </ol>
    <p><img src="../Prompts/Media/ADimage6.png" alt="Save prompt screenshot" style="max-width:100%;border-radius:6px;" /></p>
    <ul class="tips-list">
      <li>Use clear names for prompts (e.g., "Weekly Legal Catch-Up", "Contract Clause Review").</li>
      <li>Share the most frequently used prompts with your team to maintain consistency.</li>
      <li>Regularly review and update saved prompts to keep them relevant.</li>
    </ul>

    <p><strong>Step 2: Access your saved Prompts</strong></p>
    <ol class="steps">
      <li>Open Copilot.</li>
      <li>Click <strong>See more</strong>.</li>
      <li>Select <strong>Prompt Gallery</strong>.</li>
      <li>Go to <strong>Your prompts</strong> — from here, you can delete prompts, share them via link, or share them with a team.</li>
    </ol>
    <p><img src="../Prompts/Media/ADimage3.png" alt="Prompt gallery 1" style="max-width:100%;border-radius:6px;" /></p>
    <p><img src="../Prompts/Media/ADimage4.png" alt="Prompt gallery 2" style="max-width:100%;border-radius:6px;" /></p>
    <p><img src="../Prompts/Media/ADimage5.png" alt="Prompt gallery 3" style="max-width:100%;border-radius:6px;" /></p>

    <h3>Practice 2: Memory and Customization of Copilot</h3>
    <p>Copilot Memory offers a more personalized experience based on your previous chats, work profile, custom instructions, and other metadata. Copilot Customization uses this information to create tailored interactions — for example, you can tell Copilot your writing style so AI-generated drafts sound more like you.</p>

    <p><strong>Step 1: Access Copilot</strong></p>
    <p>Open a new browser tab and navigate to <a href="https://m365.cloud.microsoft/chat" target="_blank">Copilot</a> (or use your usual method to access Copilot).</p>

    <p><strong>Step 2: Add instructions</strong></p>
    <ul class="tips-list">
      <li>Click on the settings by selecting <strong>"…"</strong></li>
      <li>Open <strong>Settings</strong> and select <strong>Personalization</strong>.</li>
      <li>Then select <strong>Custom Instructions</strong>.</li>
    </ul>
    <p><img src="../Prompts/Media/ADimage1.png" alt="Personalization settings" style="max-width:100%;border-radius:6px;" /></p>
    <p><img src="../Prompts/Media/ADimage2.png" alt="Custom instructions" style="max-width:100%;border-radius:6px;" /></p>

    <p>You can add your custom instructions in this section. For reference, here's a guide with sample instructions you can add to Copilot:</p>
    <ul class="tips-list">
      <li><a href="https://livesend.microsoft.com/i/rNoOVLzAAYKpEIxHcPLUSSIGNURf0AnaauPLUSSIGNpTT12ioHC1iT2S9v5zfm___ebPPLUSSIGNq8yBBDVxGsPLUSSIGNGevpl4gM20eehkcX55fDwwHvmMnfisgImZ___gDPLUSSIGN7MtPeWjGSVb8I5OJM40FI6OPIj" target="_blank">Copilot Custom Instructions</a></li>
    </ul>

    <div class="self-check">
      <h4>✅ Self-Check: Part 1</h4>
      <label><input type="checkbox"> I saved a prompt to my Prompt Gallery</label>
      <label><input type="checkbox"> I located my saved prompts in the Prompt Gallery</label>
      <label><input type="checkbox"> I configured Custom Instructions for my legal role</label>
    </div>
  </div>
</div>

<div class="part-card" id="part2">
  <div class="part-header-bar chat"></div>
  <div class="part-header" onclick="togglePart('body2', this)">
    <h2>Part 2: Copilot Chat — Research the EU AI Act</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body2">

    <div class="callout">
      <strong>💡 Why This Matters:</strong> Regulations evolve quickly and legal teams must assess compliance impact under tight timelines. Copilot Chat in Web mode can summarize complex regulations, identify compliance obligations, and surface legal risks — accelerating the research phase of any legal assessment.
    </div>

    <p>Let's start by researching the AI Act and its potential impact on Contoso's AI hiring tool.</p>

    <ol class="steps">
      <li>Open a browser and navigate to <strong><a href="https://m365copilot.com" target="_blank">M365copilot.com</a></strong>.</li>
      <li>Ensure <strong>Web Mode</strong> is selected.</li>
    </ol>
    <p><img src="../Prompts/Media/web-mode.png" alt="Web mode tab" style="max-width:100%;border-radius:6px;" /></p>

    <ol class="steps" start="3">
      <li>In the prompt window, type the following:</li>
    </ol>
    <div class="prompt-box">Contoso is launching an AI Resume Screening Software to evaluate job applicants. As a legal advisor, I need to assess whether it complies with the EU Artificial Intelligence Act. Summarize key provisions related to AI in hiring, compliance requirements for high-risk systems, and potential legal risks.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

    <ol class="steps" start="4">
      <li>Review Copilot's response and take notes on relevant legal risks and compliance requirements.</li>
      <li>Now ask Copilot a series of follow-up questions to gather more information:</li>
    </ol>
    <div class="prompt-box">Does the AI Act classify resume screening software as a high-risk AI system?<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <div class="prompt-box">What are the key obligations for high-risk AI systems under the AI Act?<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
    <div class="prompt-box">Are there any exemptions in the AI Act that could apply to Contoso's system?<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

    <ol class="steps" start="6">
      <li>Now ask Copilot to summarize all the information so far:</li>
    </ol>
    <div class="prompt-box">Summarize all the information we've discussed into a structured list, ensuring no key details are missed. Then, export the summary to a Word document.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

    <ol class="steps" start="7">
      <li>Select the hyperlink Copilot provides for the new Word document to open it.</li>
      <li>Once opened, select <strong>Enable Editing</strong> and then turn on <strong>AutoSave</strong>. Select your OneDrive account when prompted.</li>
      <li>Copy the shared URL for use in the next step.</li>
    </ol>
    <p><img src="../Demos/Media/share-menu-with-copy-link-9fd1c60a.png" alt="Share link menu" style="max-width:100%;border-radius:6px;" /></p>

    <div class="self-check">
      <h4>✅ Self-Check: Part 2</h4>
      <label><input type="checkbox"> I researched the EU AI Act using Copilot Chat in Web mode</label>
      <label><input type="checkbox"> I asked follow-up questions to refine the legal analysis</label>
      <label><input type="checkbox"> I exported a structured summary to a Word document</label>
    </div>
  </div>
</div>

<div class="part-card" id="part3">
  <div class="part-header-bar word"></div>
  <div class="part-header" onclick="togglePart('body3', this)">
    <h2>Part 3: Copilot in Word — Executive Summary</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body3">

    <div class="callout purple">
      <strong>💡 Why This Matters:</strong> Executive leadership needs concise, well-structured summaries — not raw research. Copilot in Word can transform your research notes into polished executive-ready documents in seconds, letting you focus on the legal judgment and recommendations.
    </div>

    <p>Now, we'll draft an executive summary outlining legal risks and recommendations for Contoso's leadership.</p>

    <ol class="steps">
      <li>Open a new instance of Word, either in your browser or desktop application.</li>
      <li>In the <strong>"Describe what you'd like to write"</strong> prompt box, type the following:</li>
    </ol>
    <div class="prompt-box">Reference the following document [Link to exported Copilot Chat summary from the first task] and draft an executive summary outlining key legal risks, compliance requirements, and recommendations for Contoso's AI Resume Screening Software.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

    <div class="callout">
      <strong>📝 NOTE:</strong> Attach the document or paste the shared link directly into the prompt to ensure Copilot can access the relevant content.
    </div>

    <ol class="steps" start="3">
      <li>Review Copilot's output. Before selecting <strong>Keep it</strong>, refine the response by asking Copilot:</li>
    </ol>
    <div class="prompt-box">Add a section on the potential business impact of these compliance requirements.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

    <p>Other optional refinements:</p>
    <ul class="tips-list">
      <li>Ask Copilot to reword sections for a more professional tone.</li>
      <li>Request a shorter, more concise version if the summary is too long.</li>
      <li>Expand with additional sections.</li>
    </ul>

    <ol class="steps" start="4">
      <li>After reviewing and finalizing the document, <strong>copy the generated Executive Summary</strong> to your clipboard for use in the next demo.</li>
    </ol>

    <div class="self-check">
      <h4>✅ Self-Check: Part 3</h4>
      <label><input type="checkbox"> I drafted an executive summary in Word using Copilot</label>
      <label><input type="checkbox"> I refined the draft with follow-up prompts</label>
      <label><input type="checkbox"> I copied the finalized summary for the next step</label>
    </div>
  </div>
</div>

<div class="part-card" id="part4">
  <div class="part-header-bar outlook"></div>
  <div class="part-header" onclick="togglePart('body4', this)">
    <h2>Part 4: Copilot in Outlook — Communicate with Leadership</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body4">

    <div class="callout">
      <strong>💡 Why This Matters:</strong> A legal assessment is only useful if the right stakeholders understand it. Copilot in Outlook can package your findings into a clear, professional email — making it easier to align leadership on next steps.
    </div>

    <p>Lastly, we'll draft an email to Contoso's leadership summarizing our findings and next steps.</p>

    <ol class="steps">
      <li>Open <strong>Outlook</strong> (either in your browser or desktop application).</li>
      <li>Select <strong>New Email</strong>.</li>
      <li>Select <strong>Copilot</strong> in the ribbon. From the drop-down menu, choose <strong>Draft with Copilot</strong>.</li>
      <li>In the <strong>"What do you want this email to say?"</strong> prompt window, type:</li>
    </ol>
    <div class="prompt-box">Draft an email to Contoso's executive leadership summarizing our legal assessment of the AI Resume Screening Software under the EU AI Act. Use the following executive summary as a reference.

[paste Executive Summary from the previous task]

Conclude the email with a request for leadership's input on the next steps, including a proposed compliance review meeting.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

    <div class="callout">
      <strong>📝 NOTE:</strong> Paste the Executive Summary contents that you copied from the previous demo.
    </div>

    <ol class="steps" start="5">
      <li>Once the draft is generated, you can use the <strong>Adjust</strong> feature to modify the tone, length, or level of formality.</li>
    </ol>

    <div class="self-check">
      <h4>✅ Self-Check: Part 4</h4>
      <label><input type="checkbox"> I drafted a leadership email using Copilot in Outlook</label>
      <label><input type="checkbox"> I used the Adjust feature to refine tone or length</label>
    </div>
  </div>
</div>

<div class="part-card" id="part5">
  <div class="part-header-bar prompts"></div>
  <div class="part-header" onclick="togglePart('body5', this)">
    <h2>Part 5: Additional Sample Prompts</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body5">

    <div class="callout green">
      <strong>💡 Why This Matters:</strong> Beyond the core demo flow, these prompts show how Copilot can support common legal tasks — translating legalese for non-lawyers and running "what-if" scenario analyses against contract language.
    </div>

    <h3>Lawyer's Second Copilot Prompt: Plain-English Summary</h3>
    <div class="prompt-box">Convert the technical language of Article I, paragraphs 1 (Normal Exercise) and 2 (Acceleration) into a plain-English summary suitable for non-lawyers, while preserving all legal obligations.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

    <h3>Lawyer's Third Copilot Prompt: Scenario Analysis</h3>
    <div class="prompt-box">Scenario: What happens if the optionee voluntarily leaves the company before the second anniversary (i.e., before any shares vest on October 12, 2012)? Explain which shares, if any, remain exercisable and for how long.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

    <div class="callout warn">
      <strong>⚠️ Reminder:</strong> Always validate Copilot's interpretations against the source legal text. AI outputs are a starting point for analysis — final legal judgment remains with the attorney.
    </div>
  </div>
</div>

<div class="section" id="sec-takeaways">
  <h2>🔑 Key Takeaways</h2>
  <div class="takeaways-grid">
    <div class="takeaway-card">
      <div class="icon">⚖️</div>
      <h4>Research Faster</h4>
      <p>Use Copilot Chat in Web mode to summarize regulations and identify compliance obligations in minutes.</p>
    </div>
    <div class="takeaway-card">
      <div class="icon">🔗</div>
      <h4>Chain Your Tools</h4>
      <p>Chat to research → Word to draft → Outlook to communicate. End-to-end legal workflow without context switching.</p>
    </div>
    <div class="takeaway-card">
      <div class="icon">🔄</div>
      <h4>Iterate, Don't Accept First Draft</h4>
      <p>Refine and follow up. Copilot gets better with each iteration — treat it as a conversation, not a one-shot answer.</p>
    </div>
    <div class="takeaway-card">
      <div class="icon">🧠</div>
      <h4>AI Assists, You Decide</h4>
      <p>Copilot accelerates research and drafting, but legal judgment and final review remain with you.</p>
    </div>
  </div>
</div>

</div>
</div>

<footer>
  <p><strong>Microsoft 365 Copilot Training for Legal</strong> — Research, Drafting &amp; Compliance</p>
  <p>For questions or feedback, reach out to your training facilitator.</p>
</footer>

<button class="sidebar-toggle" id="sidebarToggle" onclick="openSidebar()" aria-label="Open navigation">☰</button>

<script src="../../Allfiles/demo-script.js"></script>
</body>
</html>
