---
demo:
    title: 'Copilot for Edgewell Finance — 60-Minute Immersion'
layout: none
---

<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Copilot for Edgewell Finance | Learning</title>
<link rel="stylesheet" href="../../Allfiles/demo-style.css">

<style>
:root { --hero-from: #2C5F8A; --hero-via: #4A90C2; --hero-to: #F08080; }
:root {
  --ew-blue: #4A90C2;
  --ew-blue-soft: #E8F1F9;
  --ew-coral: #F08080;
  --ew-coral-soft: #FDECEC;
  --ew-sun: #F6C667;
  --ew-sun-soft: #FFF6E0;
  --ew-mint: #8DC9B7;
  --ew-mint-soft: #E8F5F0;
  --ew-ink: #2D3748;
  --ew-muted: #718096;
  --ew-line: #E8ECEF;
}
.ew-prompt {
  background: #F8FAFC;
  border-left: 3px solid var(--ew-sun);
  border-radius: 6px;
  padding: .9rem 1.1rem;
  margin: .9rem 0;
  font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
  font-size: .9rem;
  line-height: 1.6;
  white-space: pre-wrap;
  color: #2D3748;
  position: relative;
}
.ew-prompt-label {
  display: block;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  font-weight: 600;
  font-size: .75rem;
  letter-spacing: .6px;
  text-transform: uppercase;
  color: #C28A2D;
  margin-bottom: .45rem;
}
.ew-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: .8rem; margin: 1rem 0; }
.ew-card {
  background: #fff;
  border: 1px solid var(--ew-line);
  border-top: 3px solid var(--ew-blue);
  border-radius: 8px;
  padding: .9rem 1rem;
}
.ew-card h4 { margin: 0 0 .35rem 0; font-size: .98rem; color: var(--ew-ink); }
.ew-card p { margin: 0; font-size: .88rem; color: var(--ew-muted); }
.ew-card.coral { border-top-color: var(--ew-coral); }
.ew-card.sun { border-top-color: var(--ew-sun); }
.ew-card.mint { border-top-color: var(--ew-mint); }
.ew-pillrow { display: flex; flex-wrap: wrap; gap: .35rem; margin: .6rem 0; }
.ew-pill {
  background: var(--ew-blue-soft);
  color: #2C5F8A;
  border-radius: 999px;
  padding: .2rem .65rem;
  font-size: .82rem;
}
.ew-pill.coral { background: var(--ew-coral-soft); color: #B8484A; }
.ew-pill.mint { background: var(--ew-mint-soft); color: #3F7A66; }
</style>

</head>
<body>

<div class="back-bar">
  <a href="https://emontes07.github.io/Learning/">← Back to Index</a>
</div>

<div class="hero">
  <div class="hero-inner">
    <h1>🪒 Copilot for Edgewell Finance</h1>
    <p class="subtitle">A 60-minute immersion — from interface basics to your first AI agent</p>
    <div class="scenario">
      <strong>How to use this guide:</strong> We'll move quickly during the live session. This page is your take-home companion — every prompt, click path, and tip is here so you can replay at your own pace. Look for the prompt boxes for text you can copy directly into Copilot.<br><br>
      <strong>Before you start:</strong> Open <a href="https://m365.cloud.microsoft/chat" target="_blank" style="color:#fff;text-decoration:underline;">m365.cloud.microsoft/chat</a> and sign in with your Edgewell account. Make sure the green <strong>Work</strong> toggle is on — that's how Copilot grounds answers on Edgewell content.
    </div>
    <div class="hero-meta">
      <span>⏱️ 60 minutes</span>
      <span>👥 Finance team</span>
      <span>🎯 Intro level</span>
      <span>🛠️ Hands-on optional</span>
    </div>
  </div>
</div>

<div class="sidebar-overlay" id="sidebarOverlay" onclick="closeSidebar()"></div>

<div class="layout">

<nav class="sidebar" id="sidebar">
  <a class="sb-home" href="https://emontes07.github.io/Learning/">← Back to Index</a>
  <div class="sb-title">Edgewell Finance — 60-Min Immersion</div>

  <a href="#part1" class="part-link">1. Copilot Foundations</a>
  <a href="#part2" class="part-link">2. Outlook — Faster Inbox, Better Replies</a>
  <a href="#part3" class="part-link">3. Teams — Never Miss a Meeting Again</a>
  <a href="#part4" class="part-link">4. Word — Draft a Memo in 30 Seconds</a>
  <a href="#part5" class="part-link">5. Excel — Talk to Your Data</a>
  <a href="#part6" class="part-link">6. PowerPoint — From Memo to Deck in 60 Seconds</a>
  <a href="#part7" class="part-link">7. Loop & Pages — Collaborate, Don't Email</a>
  <a href="#part8" class="part-link">8. Agent Builder — Your First AI Agent</a>
  <a href="#part9" class="part-link">9. Wrap-up & Next Steps</a>
</nav>

<div class="main-content">

<div class="part-card" id="part1">
  <div class="part-header-bar blue"></div>
  <div class="part-header" onclick="togglePart('body1', this)">
    <h2>1. Copilot Foundations</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body1" markdown="1">

Before we touch any app, let's get comfortable with the Copilot home base — the chat experience at [m365.cloud.microsoft/chat](https://m365.cloud.microsoft/chat). Everything you'll see in Outlook, Word, or Excel later is the same brain wearing different hats.

<img width="305" height="157" alt="image" src="https://github.com/user-attachments/assets/f71cc1e2-2715-4a76-82bd-9c2ce2b9d1d9" />


### The interface at a glance

<div class="ew-grid">
  <div class="ew-card">
    <h4>🟢 Work vs. Web</h4>
    <p>Toggle in the top-right. <strong>Work</strong> grounds answers on Edgewell content. <strong>Web</strong> uses the open internet only.</p>
  </div>
  <div class="ew-card coral">
    <h4>📎 Add content</h4>
    <p>Attach a file, paste a SharePoint link, or reference a meeting as your source of truth.</p>
  </div>
  <div class="ew-card sun">
    <h4>🎨 Agents</h4>
    <p>The left rail lists agents you can chat with — including ones we'll build today.</p>
  </div>
  <div class="ew-card mint">
    <h4>🧠 Memory</h4>
    <p>Copilot remembers facts about you across conversations — your role, your brands, your preferred format.</p>
  </div>
</div>

### Memory — teach Copilot who you are

Memory lets Copilot remember things between chats so you don't have to re-explain yourself every morning.

1. In Copilot Chat, click your **profile picture** (top right) → **Settings** → **Memory & personalization**.
1. Turn **Memory** on if it isn't already.
1. Add a few facts manually, or just chat — Copilot will offer to remember things as they come up.

<div class="ew-prompt">
<span class="ew-prompt-label">💬 Try this prompt</span>
Please remember the following about me so you can tailor future answers:

- I'm on the Edgewell Personal Care Finance team.
- I focus on Brand P&L for Schick and Banana Boat, plus retailer profitability for Walmart, Target, and Amazon.
- When I ask for analysis, default to a concise executive summary first, then a bullet list of the three most material drivers, then a short table.
- Round dollar figures to the nearest hundred thousand and always show variance vs. prior year and vs. plan.
</div>

> **TIP:** One-time investment, every future answer gets sharper. Memory works in Copilot Chat *and* inside Word, Excel, Outlook, and Teams.

### Saved Prompts — your personal prompt library

If you find yourself typing the same kind of prompt every Monday, save it once.

1. Type a prompt in Copilot Chat.
1. Click the **save icon** (bookmark) next to the send button — give it a name and an optional description.
1. Reuse it any time from the **Prompts** gallery on the right rail.

<div class="ew-prompt">
<span class="ew-prompt-label">💬 Saved prompt: "Weekly Brand P&L Pulse"</span>
Summarize the most recent emails, Teams messages, and shared files I've received this week related to Schick or Banana Boat brand performance. Group findings by:

1. Volume / shipment trends
2. Trade spend or promotion activity
3. Margin or pricing signals
4. Anything flagged as risk or opportunity

Keep each section to 3 bullets max. End with the top 3 follow-ups I should action this week.
</div>

<img width="1564" height="561" alt="image" src="https://github.com/user-attachments/assets/ed8d89e9-adae-437b-8b22-9bf20599666e" />



  </div>
</div>

<div class="part-card" id="part2">
  <div class="part-header-bar teal"></div>
  <div class="part-header" onclick="togglePart('body2', this)">
    <h2>2. Outlook — Faster Inbox, Better Replies</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body2" markdown="1">

Finance inboxes are noisy: retailer chargebacks, accruals questions, AR follow-ups, leadership requests. Copilot in Outlook does two things really well — **summarize long threads** and **draft replies in your voice**.

### Summarize a long thread

Open any thread in Outlook → click **Summary by Copilot** at the top of the message.

> **TIP:** Imagine a 14-message thread with the Walmart account team about a $1.2M deduction dispute on Banana Boat SPF 50. Click Summary by Copilot and you'll get the dispute history, current ask, and the open question — in 30 seconds.

### Draft a reply that sounds like you

In any email, click **Draft with Copilot** in the reply box.

<div class="ew-prompt">
<span class="ew-prompt-label">💬 Try this prompt</span>
Draft a reply to the Target account team confirming we'll honor the Q2 promotional allowance on the Schick Hydro 5 line at the agreed 8% off-invoice rate, but flag that the $340K incremental display fee they're requesting is outside our trade calendar and needs Brand approval before we can commit. Keep it warm but firm. Sign off with my name.
</div>

> **IMPORTANT:** After Copilot drafts, click **Adjust → Make it shorter / more formal / more casual**. You can also paste in 2–3 of your past emails and ask Copilot to "match my voice" — it picks up on phrasing fast.

### Catch up after PTO

<div class="ew-prompt">
<span class="ew-prompt-label">💬 Try this prompt</span>
I was out Thursday and Friday last week. Summarize the most important emails I received during those two days. Group them by:

1. Things needing my decision or approval
2. FYIs from leadership
3. Retailer or vendor updates I should track

Flag anything that mentions Schick, Banana Boat, Walmart, Target, or Amazon as high priority.
</div>


  </div>
</div>

<div class="part-card" id="part3">
  <div class="part-header-bar purple"></div>
  <div class="part-header" onclick="togglePart('body3', this)">
    <h2>3. Teams — Never Miss a Meeting Again</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body3" markdown="1">

If a meeting was recorded or transcribed, Copilot can recap it in seconds — even ones you didn't attend.

### Recap a meeting you missed

1. Open the meeting from your Teams calendar (or chat).
1. Click the **Recap** tab.
1. Use the Copilot panel on the right — it's pre-loaded with the transcript.

<div class="ew-prompt">
<span class="ew-prompt-label">💬 Try this prompt</span>
I missed today's S&OP review. Give me:

- A 4-sentence executive summary
- Decisions made (with who owns each)
- Open questions that didn't get resolved
- Anything specifically said about Schick razor inventory or Banana Boat seasonal build for summer

Then list any action items assigned to Finance.
</div>

### Catch up on a busy chat

In a chat or channel, click the **Copilot icon** at the top.

<div class="ew-prompt">
<span class="ew-prompt-label">💬 Try this prompt</span>
Summarize what's been discussed in this channel over the past 7 days. Highlight anything related to month-end close, retailer deductions, or trade spend variance. List unanswered questions at the bottom.
</div>

> **IMPORTANT:** Recap requires transcription. If a meeting wasn't recorded or transcribed, Copilot can't recap it. Encourage organizers to enable transcription for finance reviews.


  </div>
</div>

<div class="part-card" id="part4">
  <div class="part-header-bar orange"></div>
  <div class="part-header" onclick="togglePart('body4', this)">
    <h2>4. Word — Draft a Memo in 30 Seconds</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body4" markdown="1">

Finance writing is often structured: situation → analysis → recommendation. Copilot in Word is great at giving you a strong first draft you can polish.

### Draft from a blank doc

In Word, start a new document → click **Draft with Copilot**.

<div class="ew-prompt">
<span class="ew-prompt-label">💬 Try this prompt</span>
Draft a 1-page Finance memo to the Edgewell North America leadership team on the following topic:

"Q1 Banana Boat margin compression — drivers and proposed actions"

Use this structure:

1. Executive Summary (3 sentences)
2. What happened (bullet list with illustrative numbers — gross margin down 220 bps vs. plan, driven by SPF aerosol propellant cost +18% YoY and unfavorable mix toward club channel)
3. Root causes (3 bullets)
4. Recommended actions (3 bullets, each with an owner placeholder)
5. Asks of leadership

Tone: confident, data-driven, no jargon. Length: under 400 words.
</div>

<img width="929" height="466" alt="image" src="https://github.com/user-attachments/assets/cae47bc3-adc3-448d-b34d-d5487d016b20" />


### Reference your own files

Type **/** in the Copilot box and reference an existing file — Copilot will ground the draft on it.

<div class="ew-prompt">
<span class="ew-prompt-label">💬 Try this prompt</span>
/ [reference: "FY26 Banana Boat Brand Plan.pptx"]

Draft a finance commentary memo summarizing the FY26 plan for Banana Boat. Pull the brand's revenue, gross margin, and trade spend targets directly from the deck. Add a section on the top three financial risks and how we'll monitor them.
</div>


  </div>
</div>

<div class="part-card" id="part5">
  <div class="part-header-bar magenta"></div>
  <div class="part-header" onclick="togglePart('body5', this)">
    <h2>5. Excel — Talk to Your Data</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body5" markdown="1">

This is the section your team will reach for daily. Copilot in Excel can analyze, summarize, suggest formulas, and build charts — all in plain English.

> **TIP:** Copilot works best when your data is in a **formatted Excel Table** (Ctrl+T or Insert → Table). Header row, no merged cells, no blank rows. Two minutes of cleanup unlocks 10× better answers.

### Our illustrative dataset

Imagine an Excel workbook called **Edgewell_Brand_Retailer_P&L.xlsx** with this data:

| Brand | Retailer | Net Sales | COGS | Trade Spend | Gross Margin % |
|---|---|---|---|---|---|
| Schick | Walmart | $48.2M | $22.4M | $6.1M | 41.5% |
| Schick | Target | $22.7M | $10.8M | $3.4M | 40.1% |
| Schick | Amazon | $31.4M | $15.9M | $2.2M | 42.7% |
| Banana Boat | Walmart | $54.6M | $28.9M | $8.3M | 32.0% |
| Banana Boat | Target | $19.8M | $10.2M | $3.1M | 33.8% |
| Banana Boat | Amazon | $26.5M | $13.8M | $1.6M | 41.5% |

> **TIP:** Want to follow along? Type these numbers into a fresh sheet, format as a table, then keep this guide open beside Excel.

### Prompt 1 — Quick analytical summary

<div class="ew-prompt">
<span class="ew-prompt-label">💬 Try this prompt</span>
Looking at this brand-by-retailer P&L, give me:

1. The top 3 takeaways an executive should know
2. Which brand-retailer combination has the highest gross margin %, and which has the lowest
3. A theory on why Banana Boat margins at Amazon are so much higher than at Walmart
4. Two follow-up questions I should investigate
</div>

### Prompt 2 — Add a calculated column

<div class="ew-prompt">
<span class="ew-prompt-label">💬 Try this prompt</span>
Add a new column called "Net Contribution" calculated as Net Sales – COGS – Trade Spend. Show me the formula you used so I can verify it.
</div>

### Prompt 3 — Build a chart

<div class="ew-prompt">
<span class="ew-prompt-label">💬 Try this prompt</span>
Create a clustered column chart comparing Net Sales and Trade Spend for each Brand-Retailer combination. Title it "Brand-Retailer Net Sales vs. Trade Spend". Use a Schick razor red and a Banana Boat orange so it's easy to read.
</div>

### Prompt 4 — Highlight outliers

<div class="ew-prompt">
<span class="ew-prompt-label">💬 Try this prompt</span>
Conditionally format the Gross Margin % column so anything below 35% is highlighted red, 35–40% is amber, and above 40% is green.
</div>

### Prompt 5 — Insight, not just numbers

<div class="ew-prompt">
<span class="ew-prompt-label">💬 Try this prompt</span>
If I want to lift Banana Boat's overall gross margin by 200 basis points next year, which retailer should I focus on first based on this data, and what specifically would you investigate to build the case? Walk me through your reasoning.
</div>

> **IMPORTANT:** Always verify formulas. Copilot is a brilliant assistant, not an auditor. For anything that touches the actuals, double-check formulas before pasting into a real model.


  </div>
</div>

<div class="part-card" id="part6">
  <div class="part-header-bar green"></div>
  <div class="part-header" onclick="togglePart('body6', this)">
    <h2>6. PowerPoint — From Memo to Deck in 60 Seconds</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body6" markdown="1">

Take that Word memo from Section 4 and turn it into a leadership-ready deck.

### Generate a deck from a Word doc

1. Open PowerPoint → **New blank presentation**.
1. Click the Copilot icon → **Create presentation from file**.
1. Pick the Word memo we drafted earlier.

<div class="ew-prompt">
<span class="ew-prompt-label">💬 Try this prompt</span>
Create a 6-slide executive presentation from this Word memo on Q1 Banana Boat margin compression. Include:

- Title slide with the topic and "Edgewell Finance | Q1 Review"
- Executive summary slide (3 takeaways)
- A slide showing margin walk drivers with a placeholder for a chart
- A slide on root causes
- A slide on recommended actions with owners
- A closing "Asks of leadership" slide

Keep text minimal — at most 4 bullets per slide.
</div>

### Refine slide by slide

<div class="ew-prompt">
<span class="ew-prompt-label">💬 Try this prompt</span>
For slide 3, replace the placeholder with a column chart showing margin drivers in this order: Propellant cost (+220 bps drag), Channel mix (+90 bps drag), Pricing actions (-110 bps benefit), Net change (-220 bps).
</div>

> **TIP:** Apply your team's PowerPoint template *before* generating slides — Copilot will respect your fonts, colors, and slide masters.


  </div>
</div>

<div class="part-card" id="part7">
  <div class="part-header-bar navy"></div>
  <div class="part-header" onclick="togglePart('body7', this)">
    <h2>7. Loop & Pages — Collaborate, Don't Email</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body7" markdown="1">

Copilot **Pages** (in Copilot Chat) and **Loop** (in Teams) let multiple people co-author with Copilot in real time. Perfect for finance reviews where you're working through numbers together.

### Pages — promote a great answer into a working doc

After Copilot gives you a useful response in chat, click **Edit in Pages** at the bottom of the response.

<div class="ew-prompt">
<span class="ew-prompt-label">💬 Try this prompt</span>
Build a Page titled "Schick vs. Banana Boat — Retailer Margin Comparison".

Include:

1. A short executive summary
2. A side-by-side table of gross margin % by retailer for both brands
3. A "What we know" section and a "What we need to investigate" section
4. A list of follow-ups with placeholders for owner and due date

Make it ready for me to share with the brand finance leads.
</div>

### Loop — for the live review meeting

In Teams, paste a Loop component (table, task list, or paragraph) into a chat. Everyone edits at once, and Copilot lives right inside it.

> **TIP:** During a brand finance review, share a Loop table with the action items. As the meeting progresses, owners and due dates get filled in by the team in real time — no follow-up email needed.


  </div>
</div>

<div class="part-card" id="part8">
  <div class="part-header-bar blue"></div>
  <div class="part-header" onclick="togglePart('body8', this)">
    <h2>8. Agent Builder — Your First AI Agent</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body8" markdown="1">

This is the finale. We're going to build a **Finance Policy Q&A agent** — a private assistant trained on your finance policies (T&E, approvals, close calendar, capital request thresholds) that anyone on the team can ask questions of.

> **TIP:** Policy Q&A is the single highest-ROI, lowest-risk first agent for a Finance team. It deflects the same 20 repeat questions ("what's the T&E limit for client meals?" / "who approves a $50K capex?") and frees the team for real analysis.

### What we'll build

<div class="ew-grid">
  <div class="ew-card">
    <h4>📥 Inputs</h4>
    <p>A SharePoint folder with your finance policy PDFs and SOPs.</p>
  </div>
  <div class="ew-card coral">
    <h4>🧠 Brain</h4>
    <p>Copilot grounded on those documents, with a clear persona and guardrails.</p>
  </div>
  <div class="ew-card sun">
    <h4>📤 Output</h4>
    <p>A chat agent your team can pin in Copilot Chat or share via a link.</p>
  </div>
</div>

![Screenshot placeholder — Agent Builder home, "Create new agent" highlighted](./media/agent-create.png)

### Step-by-step build

1. In Copilot Chat, open the **Agents** rail on the left → **+ Create agent**.
1. Click **Skip and go to configure** (we'll fill in the structured form ourselves).
1. Fill in **Name**, **Description**, and **Instructions** (see prompts below).
1. Under **Knowledge**, add the SharePoint site or folder containing your finance policies.
1. Add **Starter prompts** — the example questions users see when they open the agent.
1. **Test** in the right-side preview panel.
1. **Create** → share with selected colleagues, or with the whole Finance team.

![Screenshot placeholder — Agent Builder configure pane](./media/agent-configure.png)

### Field 1 — Name & Description

<div class="ew-prompt">
<span class="ew-prompt-label">💬 Name</span>
Edgewell Finance Policy Buddy
</div>

<div class="ew-prompt">
<span class="ew-prompt-label">💬 Description</span>
Answers questions about Edgewell finance policies — travel & expense, approval thresholds, the close calendar, capex requests, and procurement guidelines. Always cites the source policy and section.
</div>

### Field 2 — Instructions (the system prompt)

<div class="ew-prompt">
<span class="ew-prompt-label">💬 Instructions</span>
You are the Edgewell Finance Policy Buddy — a friendly, precise assistant for the Edgewell Personal Care Finance team.

YOUR JOB
- Answer policy and process questions using ONLY the documents in your knowledge source.
- Always cite the specific policy name and section number you used.
- If a question is not covered in your knowledge, say so clearly and suggest who the user should contact (e.g., "This isn't covered in the policies I have access to — please reach out to the Controller's office.").

STYLE
- Direct, plain-language, no jargon.
- Lead with the answer in 1–2 sentences, then the supporting detail.
- Use bullet points when listing thresholds or steps.

GUARDRAILS
- Never invent policy details, dollar amounts, or approval flows.
- Never give tax, legal, or audit opinions — direct those to the relevant function.
- If a user asks about confidential financial results, decline politely and remind them this agent is for policy questions only.

TONE
- Helpful, calm, occasionally warm. Think "the Finance colleague everyone wants to sit next to."
</div>

### Field 3 — Starter prompts

<div class="ew-prompt">
<span class="ew-prompt-label">💬 Starter prompts to add</span>
1. What's the T&E limit for client meals in North America?
2. Who approves a capital request between $50K and $250K?
3. When does the FY26 close calendar lock the GL for month-end?
4. What's our policy on accepting gifts from suppliers?
5. How do I submit a vendor onboarding request?
</div>

### Field 4 — Knowledge sources

> **TIP:** Start narrow. Point the agent at one well-curated SharePoint folder of approved finance policies. Don't dump the whole Finance site in there on day one — quality of sources directly drives quality of answers.

Suggested sources to add:

<div class="ew-pillrow">
  <span class="ew-pill">📁 SharePoint: /Finance/Policies/T&E</span>
  <span class="ew-pill">📁 SharePoint: /Finance/Policies/Approvals</span>
  <span class="ew-pill">📁 SharePoint: /Finance/Close/CloseCalendar.xlsx</span>
  <span class="ew-pill">📁 SharePoint: /Finance/Policies/Procurement</span>
</div>

### Test it before you ship

In the preview pane on the right, try the starter prompts plus a few edge cases:

<div class="ew-prompt">
<span class="ew-prompt-label">💬 Test cases to run</span>
1. A clear, in-scope question:
   "What's the daily T&E limit for client dinners in the US?"

2. A question on the edge of policy:
   "If I take a $400K project to my VP, do I still need CFO approval?"

3. An out-of-scope question (should politely decline):
   "What was Schick's gross margin last quarter?"

4. A trick question (should not invent an answer):
   "What's the policy on accepting NFTs as supplier gifts?"
</div>

> **IMPORTANT:** Pilot before broadcasting. Share with 3–5 colleagues for a week. Collect their feedback inside the agent's chat history. Refine the instructions and knowledge sources before opening it up to the whole team.

### Where this can go next

<div class="ew-grid">
  <div class="ew-card">
    <h4>🧾 Variance Commentary Helper</h4>
    <p>Drafts month-end variance narratives in your team's voice and format.</p>
  </div>
  <div class="ew-card coral">
    <h4>📋 Retailer Deduction Triage</h4>
    <p>Classifies incoming retailer deductions and routes to the right analyst.</p>
  </div>
  <div class="ew-card mint">
    <h4>📅 Close Calendar Concierge</h4>
    <p>Knows every deadline, every owner, every dependency in your monthly close.</p>
  </div>
</div>


  </div>
</div>

<div class="part-card" id="part9">
  <div class="part-header-bar teal"></div>
  <div class="part-header" onclick="togglePart('body9', this)">
    <h2>9. Wrap-up & Next Steps</h2>
    <span class="toggle-icon">▾</span>
  </div>
  <div class="part-body collapsed" id="body9" markdown="1">

### Three things to do this week

1. **Set up Memory.** 5 minutes. Pays back forever. Use the prompt in Section 1.
1. **Save 2 prompts** you'll reuse — one for inbox triage, one for Excel analysis.
1. **Pilot the Finance Policy Buddy agent** with 3 colleagues before sharing broadly.

### What's coming in the deeper sessions

<div class="ew-pillrow">
  <span class="ew-pill">📊 Variance analysis deep-dive</span>
  <span class="ew-pill coral">🏷️ Trade spend & promo ROI</span>
  <span class="ew-pill mint">🤖 Building your second & third agents</span>
  <span class="ew-pill">🔐 Governance & responsible AI</span>
</div>

### Resources

- 🎓 [Microsoft Copilot Learning Hub](https://adoption.microsoft.com/en-us/copilot/)
- 📚 [Prompt Library — official starter prompts](https://copilot.cloud.microsoft/en-us/prompts)
- 🛠️ [Agent Builder docs](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/copilot-studio-agent-builder)
- 📝 Erik's prior demo guides:
    - [10 — Copilot Basics (Legal)](https://emontes07.github.io/Learning/Instructions/Demos/10-Legal-Demo.html)
    - [11 — Finance / Excel](https://emontes07.github.io/Learning/Instructions/Demos/11-Finance-Demo.html)
    - [12 — Researcher & Analyst Agents](https://emontes07.github.io/Learning/Instructions/Demos/12-Researcher-Analyst-Demo.html)
    - [Executive Agents — Agent Builder](https://emontes07.github.io/Learning/Instructions/Prompts/Exec-Agents.html)


[Back to Index](https://emontes07.github.io/Learning/)

  </div>
</div>

</div>
</div>

<footer>
  <p><strong>Copilot for Edgewell Finance — 60-Minute Immersion</strong></p>
  <p>For questions or feedback, reach out to your training facilitator.</p>
</footer>

<button class="sidebar-toggle" id="sidebarToggle" onclick="openSidebar()" aria-label="Open navigation">☰</button>

<script src="../../Allfiles/demo-script.js"></script>
</body>
</html>
